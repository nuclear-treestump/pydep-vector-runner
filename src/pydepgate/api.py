"""pydepgate.api

The public API is intentionally small. It uses the same internal scanner runner
that the CLI uses, so import callers do not need to fake argparse namespaces.

Normal API objects do not expose raw payload material. Native scanner objects and
DecodedTree are available only through explicit UNSAFE tokens because those
objects may retain payload-bearing analyzer context.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
import io
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

from pydepgate.cli._archive import write_encrypted_zip
from pydepgate.reporters.decoded_tree import (
    iocs as tree_iocs,
    sources as tree_sources,
    text as tree_text,
)
from pydepgate.reporters import sarif
from pydepgate.reporters.scan_result import human as scan_human
from pydepgate.reporters.scan_result import json as scan_json

from pydepgate.enrichers.payload_peek import (
    DEFAULT_MAX_BUDGET,
    DEFAULT_MAX_DEPTH,
    DEFAULT_MIN_LENGTH,
    PayloadPeek,
)
from pydepgate.events import (
    EventEmitter,
    EventSink,
    JsonlEventSink,
    MemoryEventSink,
    mintsgt,
)
from pydepgate.rules.defaults import DEFAULT_RULES
from pydepgate.rules.loader import load_user_rules
from pydepgate.engines.base import ScanResult, Severity
from pydepgate.scanning import (
    ScanTargetRef,
    StaticDecodeOptions,
    StaticScanOutcome,
    StaticScanRequest,
    execute_static_scan,
)

_SDIST_SUFFIXES = (".tar.gz", ".tgz", ".tar.bz2", ".tar.xz", ".tar")
_ARCHIVE_SUFFIXES = (".whl", ".zip", ".tar.gz", ".tgz", ".tar.bz2", ".tar.xz", ".tar")
_DECODE_IOCS_CHOICES = ("off", "hashes", "full")
_OUTPUT_FORMAT_CHOICES = ("text", "human", "json", "sarif")
_BLOCKED_CONTEXT_KEYS = {
    "_full_value",
    "_full_value_truncated",
}
_DECODED_BLOCK_SAFE_KEYS = {
    "chain",
    "layers_count",
    "final_kind",
    "final_bytes_size",
    "unwrap_status",
    "preview_hex",
    "preview_text",
    "preview_truncated",
    "indicators",
    "pickle_warning",
    "continues_as",
    "der",
}


class PyDepGateApiError(RuntimeError):
    """Raised when the public API cannot satisfy a request."""


class _UnsafeToken:
    """Capability token for dangerous public API operations."""

    __slots__ = ("name",)

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"UNSAFE.{self.name}"


class _UnsafeNamespace:
    """Explicit opt-in tokens for operations that can expose payload material."""

    ALLOW_NATIVE_RESULT = _UnsafeToken("ALLOW_NATIVE_RESULT")
    ALLOW_DECODED_TREE = _UnsafeToken("ALLOW_DECODED_TREE")
    ALLOW_PAYLOAD_ARCHIVE_EXPORT = _UnsafeToken("ALLOW_PAYLOAD_ARCHIVE_EXPORT")


UNSAFE = _UnsafeNamespace()


@dataclass(frozen=True, slots=True)
class ScanFinding:
    """Payload-safe finding record for public API consumers."""

    signal_id: str
    analyzer: str
    severity: str
    internal_path: str
    line: int
    column: int
    description: str
    file_kind: str
    triage_reason: str
    file_sha256: str | None = None
    file_sha512: str | None = None
    context: Mapping[str, object] = field(default_factory=dict)

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-safe representation of this finding."""
        return {
            "signal_id": self.signal_id,
            "analyzer": self.analyzer,
            "severity": self.severity,
            "internal_path": self.internal_path,
            "line": self.line,
            "column": self.column,
            "description": self.description,
            "file_kind": self.file_kind,
            "triage_reason": self.triage_reason,
            "file_sha256": self.file_sha256,
            "file_sha512": self.file_sha512,
            "context": dict(self.context),
        }


@dataclass(frozen=True, slots=True)
class ScanIOC:
    """Hash-only IOC record extracted from a decoded payload."""

    source: str
    signal_ids: tuple[str, ...]
    severity: str
    chain: tuple[str, ...]
    final_kind: str
    final_size: int
    indicators: tuple[str, ...]
    file_sha256: str | None = None
    file_sha512: str | None = None
    original_sha256: str | None = None
    original_sha512: str | None = None
    decoded_sha256: str | None = None
    decoded_sha512: str | None = None
    extracted_at: str | None = None

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-safe representation of this IOC record."""
        return {
            "source": self.source,
            "signal_ids": list(self.signal_ids),
            "severity": self.severity,
            "chain": list(self.chain),
            "final_kind": self.final_kind,
            "final_size": self.final_size,
            "indicators": list(self.indicators),
            "file_sha256": self.file_sha256,
            "file_sha512": self.file_sha512,
            "original_sha256": self.original_sha256,
            "original_sha512": self.original_sha512,
            "decoded_sha256": self.decoded_sha256,
            "decoded_sha512": self.decoded_sha512,
            "extracted_at": self.extracted_at,
        }


@dataclass(frozen=True, slots=True)
class ScanApiResult:
    """Result returned by pydepgate.api.scan.

    The default public surface is hash-only and metadata-only. Native scanner
    results and decoded trees are gated because they can contain payload-bearing
    analyzer context or decoded source material.
    """

    mode: str
    target: str
    ruleset_fingerprint: str
    decode_iocs: str
    _ticket: object = field(repr=False)
    _outcome: StaticScanOutcome = field(repr=False)
    _events: tuple[object, ...] = field(repr=False)
    _min_severity: str | None = field(default=None, repr=False)
    _output_format: str = field(default="text", repr=False)

    def __repr__(self) -> str:
        return (
            "ScanApiResult("
            f"mode={self.mode!r}, "
            f"target={self.target!r}, "
            f"artifact_kind={self.artifact_kind!r}, "
            f"finding_count={self.finding_count}, "
            f"diagnostic_count={self.diagnostic_count}, "
            f"ioc_count={len(self.iocs)}, "
            f"event_count={len(self.events)}, "
            f"output_format={self._output_format!r}, "
            f"ruleset_fingerprint={self.ruleset_fingerprint!r}"
            ")"
        )

    @property
    def ticket(self):
        """Return the scan granting ticket for this API run."""
        return self._ticket

    @property
    def events(self) -> tuple[object, ...]:
        """Return event envelopes emitted during this API run."""
        return self._events

    @property
    def outcome(self):
        """Block direct access to the native static outcome."""
        raise PyDepGateApiError(
            "native StaticScanOutcome may expose payload-bearing internals; "
            "use get_static_outcome(unsafe=UNSAFE.ALLOW_NATIVE_RESULT)"
        )

    @property
    def result(self):
        """Block direct access to the native ScanResult."""
        raise PyDepGateApiError(
            "native ScanResult may contain payload-bearing analyzer context; "
            "use get_native_result(unsafe=UNSAFE.ALLOW_NATIVE_RESULT)"
        )

    @property
    def decoded_tree(self):
        """Block direct access to the internal decoded-payload tree."""
        raise PyDepGateApiError(
            "DecodedTree is an internal payload-analysis object; use result.iocs "
            "for hash-only records or get_decoded_tree(unsafe=UNSAFE.ALLOW_DECODED_TREE)"
        )

    def get_static_outcome(self, *, unsafe: object):
        """Return the native StaticScanOutcome after explicit unsafe opt-in."""
        _require_unsafe(unsafe, UNSAFE.ALLOW_NATIVE_RESULT, "native static outcome")
        return self._outcome

    def get_native_result(self, *, unsafe: object):
        """Return the native ScanResult after explicit unsafe opt-in."""
        _require_unsafe(unsafe, UNSAFE.ALLOW_NATIVE_RESULT, "native scan result")
        return self._outcome.result

    def get_decoded_tree(self, *, unsafe: object):
        """Return the internal DecodedTree after explicit unsafe opt-in."""
        _require_unsafe(unsafe, UNSAFE.ALLOW_DECODED_TREE, "decoded tree")
        return self._outcome.decoded_tree

    @property
    def artifact_kind(self) -> str:
        """Return the scanned artifact kind."""
        return self._outcome.result.artifact_kind.value

    @property
    def artifact_sha256(self) -> str | None:
        """Return the artifact SHA-256 when available."""
        return self._outcome.result.artifact_sha256

    @property
    def artifact_sha512(self) -> str | None:
        """Return the artifact SHA-512 when available."""
        return self._outcome.result.artifact_sha512

    @property
    def finding_count(self) -> int:
        """Return the number of findings in the native result."""
        return len(self._outcome.result.findings)

    @property
    def diagnostic_count(self) -> int:
        """Return the number of diagnostics in the native result."""
        return len(self._outcome.result.diagnostics)

    @property
    def findings(self) -> tuple[ScanFinding, ...]:
        """Return payload-safe finding summaries."""
        return tuple(
            _safe_finding(finding) for finding in self._outcome.result.findings
        )

    @property
    def iocs(self) -> tuple[ScanIOC, ...]:
        """Return hash-only decoded-payload IOC records."""
        return _collect_iocs(self._outcome.decoded_tree)

    def to_summary(self) -> dict[str, object]:
        """Return a compact JSON-safe summary for API consumers."""
        stats = self._outcome.result.statistics
        return {
            "mode": self.mode,
            "target": self.target,
            "artifact_identity": self._outcome.result.artifact_identity,
            "artifact_kind": self.artifact_kind,
            "artifact_sha256": self.artifact_sha256,
            "artifact_sha512": self.artifact_sha512,
            "finding_count": self.finding_count,
            "diagnostic_count": self.diagnostic_count,
            "suppressed_finding_count": len(self._outcome.result.suppressed_findings),
            "skipped_count": len(self._outcome.result.skipped),
            "ioc_count": len(self.iocs),
            "event_count": len(self.events),
            "ruleset_fingerprint": self.ruleset_fingerprint,
            "decode_iocs": self.decode_iocs,
            "statistics": {
                "files_total": stats.files_total,
                "files_scanned": stats.files_scanned,
                "files_skipped": stats.files_skipped,
                "files_failed_to_parse": stats.files_failed_to_parse,
                "signals_emitted": stats.signals_emitted,
                "analyzers_run": stats.analyzers_run,
                "enrichers_run": stats.enrichers_run,
                "duration_seconds": stats.duration_seconds,
            },
        }

    def render(
        self,
        *,
        format: str | None = None,
        color: str = "never",
        ci_mode: bool = False,
        peek_chain: bool | None = None,
        sarif_srcroot: str | None = None,
        sarif_scan_mode: str | None = None,
    ) -> str:
        """Render this result using pydepgate's existing reporters.

        format accepts "text", "human", "json", or "sarif". The "human"
        spelling aliases to "text". Text and JSON render the filtered scan
        result using the same reporters as the CLI. SARIF receives the decoded
        tree so decoded child findings can be represented in SARIF without
        exposing the tree as a normal public API attribute.
        """
        normalized = _normalize_output_format(format or self._output_format)
        stream = io.StringIO()
        filtered = _filtered_result(self._outcome.result, self._min_severity)
        if peek_chain is None:
            peek_chain = bool(self._ticket.budget.get("peek_chain", False))

        if normalized == "json":
            scan_json.render(filtered, stream)
        elif normalized == "sarif":
            sarif.render(
                filtered,
                self._outcome.decoded_tree,
                stream,
                srcroot=sarif_srcroot,
                scan_mode=sarif_scan_mode or _default_sarif_scan_mode(self._ticket),
            )
        else:
            scan_human.render(
                filtered,
                stream,
                color=color,
                ci_mode=ci_mode,
                peek_chain=peek_chain,
            )
        return stream.getvalue()

    def write_report(
        self,
        path: str | Path,
        *,
        format: str | None = None,
        color: str = "never",
        ci_mode: bool = False,
        peek_chain: bool | None = None,
        sarif_srcroot: str | None = None,
        sarif_scan_mode: str | None = None,
    ) -> Path:
        """Write a rendered scan report using an existing reporter."""
        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            self.render(
                format=format,
                color=color,
                ci_mode=ci_mode,
                peek_chain=peek_chain,
                sarif_srcroot=sarif_srcroot,
                sarif_scan_mode=sarif_scan_mode,
            ),
            encoding="utf-8",
        )
        return output_path

    def write_iocs(self, path: str | Path) -> Path:
        """Write decoded-payload IOC hashes using the CLI sidecar format."""
        tree = self._outcome.decoded_tree
        if tree is None:
            raise PyDepGateApiError("no decoded-payload tree is available")
        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(tree_iocs.render(tree), encoding="utf-8")
        return output_path

    def write_payload_archive(
        self,
        path: str | Path,
        *,
        unsafe: object,
        password: str = "infected",
        compression: str = "deflate",
        write_sidecar: bool = True,
    ) -> Path:
        """Write an encrypted decoded-payload archive after explicit opt-in.

        This is allowed only when scan(..., decode_iocs="full") was used.
        The archive contains report.txt, sources.txt, and iocs.txt using the
        same renderer family as the CLI full mode. The sidecar, when enabled,
        contains hash-only IOCs and is safe to hand to automation.
        """
        _require_unsafe(
            unsafe,
            UNSAFE.ALLOW_PAYLOAD_ARCHIVE_EXPORT,
            "payload archive export",
        )
        if self.decode_iocs != "full":
            raise PyDepGateApiError(
                "payload archive export requires scan(..., decode_iocs='full')"
            )
        tree = self._outcome.decoded_tree
        if tree is None:
            raise PyDepGateApiError("no decoded-payload tree is available")

        archive_path = Path(path)
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        target_safe = _sanitize_target_for_filename(
            Path(self._outcome.result.artifact_identity).name
        )
        inner_dir = (target_safe or "decoded").replace(".", "_")[:50]
        report_text = tree_text.render(tree, include_iocs=False)
        sources_text = tree_sources.render(tree)
        iocs_text = tree_iocs.render(tree)
        entries = [
            (f"{inner_dir}/report.txt", report_text.encode("utf-8")),
            (f"{inner_dir}/sources.txt", sources_text.encode("utf-8")),
            (f"{inner_dir}/iocs.txt", iocs_text.encode("utf-8")),
        ]
        tmp_archive = archive_path.with_name(archive_path.name + ".tmp")
        write_encrypted_zip(
            tmp_archive,
            entries,
            password=password,
            compression=compression,
        )
        tmp_archive.replace(archive_path)
        if write_sidecar:
            archive_path.with_suffix(archive_path.suffix + ".iocs.txt").write_text(
                iocs_text,
                encoding="utf-8",
            )
        return archive_path


def doctor(
    *,
    include_event_smoke: bool = True,
    rules_file: str | Path | None = None,
):
    """Run local pydepgate diagnostics and return a structured report.

    The report is the same object used by ``pydepgate doctor``. It is
    payload-safe and intended for support tooling, CI checks, and future
    daemon health surfaces.
    """
    from pydepgate.diagnostics.doctor import DoctorOptions, run_doctor

    return run_doctor(
        DoctorOptions(
            include_event_smoke=include_event_smoke,
            rules_file=rules_file,
        )
    )


def scan(
    target: str | Path,
    *,
    mode: str = "static",
    deep: bool = False,
    single: bool = False,
    as_kind: str | None = None,
    peek: bool = False,
    peek_chain: bool = False,
    peek_depth: int = DEFAULT_MAX_DEPTH,
    peek_budget: int = DEFAULT_MAX_BUDGET,
    peek_min_length: int = DEFAULT_MIN_LENGTH,
    decode: bool = False,
    decode_payload_depth: int = 3,
    decode_iocs: str = "off",
    min_severity: str | None = None,
    output_format: str | None = None,
    rules_file: str | Path | None = None,
    event_log: str | Path | None = None,
    event_sinks: Sequence[EventSink] = (),
    workers: int | None = None,
    parallel_threshold: int = 1000,
) -> ScanApiResult:
    """Run a contextless scan through pydepgate's internal scan API.

    Only mode="static" is supported in this first public facade. URL targets are
    reserved for a future context or intake layer that can materialize remote
    artifacts under policy.
    """
    if mode != "static":
        raise PyDepGateApiError("only mode='static' is supported by this API")
    normalized_output_format = _normalize_output_format(output_format or "text")

    target_text = str(target)
    if decode_iocs not in _DECODE_IOCS_CHOICES:
        raise PyDepGateApiError("decode_iocs must be one of 'off', 'hashes', or 'full'")
    if decode_iocs != "off" and not decode:
        raise PyDepGateApiError("decode_iocs requires decode=True")
    if _looks_like_url(target_text):
        raise PyDepGateApiError(
            "URL targets require an intake/context layer and are not supported yet"
        )
    if single and deep:
        raise PyDepGateApiError("single=True and deep=True are incompatible")
    if single and _looks_like_archive_target(target_text):
        raise PyDepGateApiError(
            "single=True cannot be used with archive artifacts such as "
            ".whl, .zip, .tar.gz, .tgz, .tar.bz2, or .tar.xz"
        )
    if as_kind is not None and not single:
        raise PyDepGateApiError("as_kind only applies when single=True")
    if decode:
        peek = True

    loaded = load_user_rules(explicit_path=rules_file)
    all_rules = tuple(DEFAULT_RULES) + tuple(loaded.rules)
    ruleset_fingerprint = _ruleset_fingerprint(all_rules)

    target_kind = "loose_file" if single else _target_kind_for_static(target_text)
    target_ref = ScanTargetRef(
        kind="loose_file" if single else target_kind,
        identity=target_text,
        location=target_text,
        metadata={"api_mode": mode},
    )

    actions = ["scan"]
    if decode:
        actions.append("decode")

    budget = {
        "workers": workers,
        "parallel_threshold": parallel_threshold,
        "deep": bool(deep),
        "single": bool(single),
        "peek": bool(peek),
        "peek_chain": bool(peek_chain),
        "decode_enabled": bool(decode),
        "decode_payload_depth": decode_payload_depth,
        "decode_iocs": decode_iocs,
    }

    ticket = mintsgt(
        target_kind=target_kind,
        target_identity=target_text,
        scan_mode=(
            "static.single"
            if single
            else ("static.deep" if deep else "static.artifact")
        ),
        allowed_actions=tuple(actions),
        ruleset_fingerprint=ruleset_fingerprint,
        budget=budget,
        metadata={
            "api": "pydepgate.api.scan",
            "mode": mode,
            "rules_file": str(rules_file) if rules_file else None,
            "loaded_rules_path": (
                str(loaded.source_path) if loaded.source_path else None
            ),
            "default_rule_count": len(DEFAULT_RULES),
            "user_rule_count": len(loaded.rules),
            "combined_rule_count": len(all_rules),
        },
        issuer="pydepgate.api",
        actor="api-user",
        require_cli_stack=False,
    )

    memory_sink = MemoryEventSink()
    sinks: list[EventSink] = [memory_sink]
    sinks.extend(tuple(event_sinks))
    if event_log is not None:
        sinks.append(JsonlEventSink(event_log))

    emitter = EventEmitter(
        producer="pydepgate.api",
        sinks=tuple(sinks),
        run_id=ticket.run_id,
        correlation_id=ticket.correlation_id,
    )
    grant_event = emitter.emit(
        "internal.scanner.scan_grant_issued",
        _ticket_event_payload(ticket),
        ticket_id=ticket.ticket_id,
    )

    enrichers = []
    if peek:
        enrichers.append(
            PayloadPeek(
                min_length=peek_min_length,
                max_depth=peek_depth,
                max_budget=peek_budget,
            )
        )

    request = StaticScanRequest(
        ticket=ticket,
        target_ref=target_ref,
        rules=all_rules,
        emitter=emitter,
        ruleset_fingerprint=ruleset_fingerprint,
        enrichers=tuple(enrichers),
        as_kind=as_kind,
        grant_event_id=grant_event.event_id,
        decode_options=StaticDecodeOptions(
            peek_min_length=peek_min_length,
            peek_depth=peek_depth,
            peek_budget=peek_budget,
            min_severity=min_severity,
        ),
        strict_event_sinks=True,
    )
    outcome = execute_static_scan(request)

    emitter.emit(
        "internal.scanner.run_completed",
        {
            "artifact_identity": outcome.result.artifact_identity,
            "artifact_kind": outcome.result.artifact_kind.value,
            "finding_count": len(outcome.result.findings),
            "diagnostic_count": len(outcome.result.diagnostics),
        },
        ticket_id=ticket.ticket_id,
        parent_event_id=(
            outcome.decode_completed_event_id or outcome.scan_completed_event_id
        ),
    )

    return ScanApiResult(
        mode=mode,
        target=target_text,
        ruleset_fingerprint=ruleset_fingerprint,
        decode_iocs=decode_iocs,
        _ticket=ticket,
        _outcome=outcome,
        _events=memory_sink.events,
        _min_severity=min_severity,
        _output_format=normalized_output_format,
    )


def _require_unsafe(actual: object, expected: object, operation: str) -> None:
    if actual is not expected:
        raise PyDepGateApiError(
            f"{operation} requires explicit unsafe token {expected!r}"
        )


def _safe_finding(finding) -> ScanFinding:
    signal = finding.signal
    context = finding.context
    return ScanFinding(
        signal_id=signal.signal_id,
        analyzer=signal.analyzer,
        severity=finding.severity.value,
        internal_path=context.internal_path,
        line=signal.location.line,
        column=signal.location.column,
        description=signal.description,
        file_kind=context.file_kind.value,
        triage_reason=context.triage_reason,
        file_sha256=context.file_sha256,
        file_sha512=context.file_sha512,
        context=_sanitize_mapping(signal.context),
    )


def _sanitize_mapping(mapping: Mapping[str, Any]) -> dict[str, object]:
    clean: dict[str, object] = {}
    for key, value in mapping.items():
        text_key = str(key)
        if text_key in _BLOCKED_CONTEXT_KEYS or text_key.startswith("_"):
            continue
        if text_key == "decoded" and isinstance(value, Mapping):
            clean[text_key] = _sanitize_decoded_block(value)
            continue
        clean[text_key] = _json_safe(value)
    return clean


def _json_safe(value: Any) -> object:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Mapping):
        return _sanitize_mapping(value)
    if isinstance(value, (tuple, list, set, frozenset)):
        return [_json_safe(item) for item in value]
    return repr(value)


def _sanitize_decoded_block(decoded: Mapping[str, Any]) -> dict[str, object]:
    clean: dict[str, object] = {}
    for key, value in decoded.items():
        text_key = str(key)
        if text_key not in _DECODED_BLOCK_SAFE_KEYS:
            continue
        clean[text_key] = _json_safe(value)
    return clean


def _normalize_output_format(format_name: str) -> str:
    normalized = format_name.lower().strip()
    if normalized == "human":
        normalized = "text"
    if normalized not in ("text", "json", "sarif"):
        raise PyDepGateApiError(
            "output format must be one of 'text', 'human', 'json', or 'sarif'"
        )
    return normalized


def _filtered_result(result: ScanResult, min_severity: str | None) -> ScanResult:
    threshold = _parse_severity(min_severity)
    display_findings = tuple(
        finding
        for finding in result.findings
        if _severity_meets_threshold(finding.severity, threshold)
    )
    return result.__class__(
        artifact_identity=result.artifact_identity,
        artifact_kind=result.artifact_kind,
        findings=display_findings,
        skipped=result.skipped,
        statistics=result.statistics,
        diagnostics=result.diagnostics,
        artifact_sha256=result.artifact_sha256,
        artifact_sha512=result.artifact_sha512,
        suppressed_findings=result.suppressed_findings,
        scan_id=result.scan_id,
        per_file_statistics=result.per_file_statistics,
    )


def _parse_severity(severity_str: str | None) -> Severity:
    if not severity_str:
        return Severity.INFO
    mapping = {severity.value: severity for severity in Severity}
    try:
        return mapping[severity_str.lower()]
    except KeyError as exc:
        raise PyDepGateApiError(f"unknown severity threshold: {severity_str}") from exc


def _severity_meets_threshold(severity: Severity, threshold: Severity) -> bool:
    rank = {
        Severity.INFO: 0,
        Severity.LOW: 1,
        Severity.MEDIUM: 2,
        Severity.HIGH: 3,
        Severity.CRITICAL: 4,
    }
    return rank[severity] >= rank[threshold]


def _default_sarif_scan_mode(ticket) -> str | None:
    if ticket.scan_mode == "static.deep":
        return f"{ticket.target_kind}_deep"
    return None


def _looks_like_archive_target(target: str) -> bool:
    lowered = target.lower()
    return lowered.endswith(_ARCHIVE_SUFFIXES)


def _collect_iocs(decoded_tree) -> tuple[ScanIOC, ...]:
    if decoded_tree is None:
        return ()

    records: list[ScanIOC] = []

    def visit(node) -> None:
        ioc = getattr(node, "ioc_data", None)
        if ioc is not None:
            signal_ids = [node.outer_signal_id]
            for signal_id in getattr(node, "triggered_by", ()):  # child trigger signals
                if signal_id not in signal_ids:
                    signal_ids.append(signal_id)
            records.append(
                ScanIOC(
                    source=node.outer_location,
                    signal_ids=tuple(signal_ids),
                    severity=node.outer_severity,
                    chain=tuple(node.chain),
                    final_kind=node.final_kind,
                    final_size=node.final_size,
                    indicators=tuple(node.indicators),
                    file_sha256=node.containing_file_sha256,
                    file_sha512=node.containing_file_sha512,
                    original_sha256=ioc.original_sha256,
                    original_sha512=ioc.original_sha512,
                    decoded_sha256=ioc.decoded_sha256,
                    decoded_sha512=ioc.decoded_sha512,
                    extracted_at=ioc.extract_timestamp,
                )
            )
        for child in getattr(node, "children", ()):  # recursive decoded layers
            visit(child)

    for root in getattr(decoded_tree, "nodes", ()):  # tolerate older tree-like objects
        visit(root)
    return tuple(records)


def _target_kind_for_static(target: str) -> str:
    lowered = target.lower()
    if lowered.endswith(".whl"):
        return "wheel"
    for suffix in _SDIST_SUFFIXES:
        if lowered.endswith(suffix):
            return "sdist"
    return "installed_package"


def _ruleset_fingerprint(rules) -> str:
    import hashlib

    digest = hashlib.sha256()
    for rule in rules:
        digest.update(repr(rule).encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def _ticket_event_payload(ticket) -> dict:
    payload = ticket.to_dict()
    payload.pop("ticket_nonce", None)
    return payload


def _looks_like_url(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith("http://") or lowered.startswith("https://")


def _sanitize_target_for_filename(target: str) -> str:
    safe = []
    for ch in target:
        if ch.isalnum() or ch in ("-", "_", "."):
            safe.append(ch)
        else:
            safe.append("_")
    return "".join(safe).strip("._")


__all__ = [
    "PyDepGateApiError",
    "ScanApiResult",
    "ScanFinding",
    "ScanIOC",
    "UNSAFE",
    "doctor",
    "scan",
]
