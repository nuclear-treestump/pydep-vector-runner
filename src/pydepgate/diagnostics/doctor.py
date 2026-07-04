"""pydepgate.diagnostics.doctor

Local pydepgate diagnostic checks.

pydepgate doctor is a readiness and support surface for the local
installation. It observes state, explains what it finds, and suggests fixes.
It does not initialize databases, download vulnerability feeds, rewrite config,
or repair user state.
"""

from __future__ import annotations

import importlib
import importlib.metadata
import os
import platform
import sqlite3
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import pydepgate
from pydepgate.dbs.cvedb import constants as cvedb_constants
from pydepgate.dbs.cvedb import schema as cvedb_schema
from pydepgate.dbs.pdgdb import schema as pdgdb_schema
from pydepgate.diagnostics.model import (
    DOCTOR_SCHEMA_VERSION,
    STATUS_FAIL,
    STATUS_PASS,
    STATUS_SKIP,
    STATUS_WARN,
    DoctorCheck,
    DoctorReport,
)
from pydepgate.pdgplatform import paths as platform_paths
from pydepgate.rules.defaults import DEFAULT_RULES
from pydepgate.rules.loader import ENV_RULES_FILE, GateFileError, load_user_rules


@dataclass(frozen=True, slots=True)
class DoctorOptions:
    """Options for local diagnostics.

    Attributes:
        rules_file: Optional explicit rules file path, mirroring the CLI's
            ``--rules-file`` behavior.
        include_event_smoke: When true, writes one event to a temporary JSONL
            file and memory sink to verify local serialization plumbing.
    """

    rules_file: str | Path | None = None
    include_event_smoke: bool = True


def run_doctor(options: DoctorOptions | None = None) -> DoctorReport:
    """Run local diagnostic checks and return a structured report."""
    options = options or DoctorOptions()
    checks: list[DoctorCheck] = []

    for family in (
        _check_runtime,
        _check_install_metadata,
        _check_paths,
        _check_environment,
        _check_cvedb,
        _check_pdgdb,
        lambda: _check_rules(options),
        _check_policies_placeholder,
        _check_daemon_placeholder,
    ):
        checks.extend(_guard_check_family(family))

    if options.include_event_smoke:
        checks.extend(_guard_check_family(_check_event_smoke))
    else:
        checks.append(
            DoctorCheck(
                check_id="PDG-DOC-EVENTS-000",
                component="events",
                status=STATUS_SKIP,
                title="event smoke test skipped",
                detail="The caller disabled the temporary event JSONL serialization check.",
            )
        )

    return DoctorReport(
        schema_version=DOCTOR_SCHEMA_VERSION,
        pydepgate_version=pydepgate.__version__,
        generated_at=datetime.now(timezone.utc).isoformat(),
        checks=tuple(checks),
    )


def _guard_check_family(factory: Callable[[], list[DoctorCheck]]) -> list[DoctorCheck]:
    try:
        return factory()
    except Exception as exc:
        return [
            DoctorCheck(
                check_id="PDG-DOC-INTERNAL-001",
                component="runtime",
                status=STATUS_FAIL,
                title="diagnostic family crashed",
                detail=f"{type(exc).__name__}: {exc}",
                remediation="file an issue with the pydepgate doctor JSON output attached",
            )
        ]


def _check_runtime() -> list[DoctorCheck]:
    version = sys.version_info
    version_text = platform.python_version()
    if version >= (3, 11):
        status = STATUS_PASS
        title = "Python version supported"
        remediation = None
    else:
        status = STATUS_FAIL
        title = "Python version unsupported"
        remediation = "run pydepgate with Python 3.11 or newer"

    return [
        DoctorCheck(
            check_id="PDG-DOC-RUNTIME-001",
            component="runtime",
            status=status,
            title=title,
            detail=(
                f"Python {version_text}\n"
                f"Executable: {sys.executable}\n"
                f"Platform: {platform.platform()}"
            ),
            remediation=remediation,
            data={
                "python_version": version_text,
                "executable": sys.executable,
                "platform": platform.platform(),
            },
        )
    ]


def _check_install_metadata() -> list[DoctorCheck]:
    imported = pydepgate.__version__
    try:
        installed = importlib.metadata.version("pydepgate")
    except importlib.metadata.PackageNotFoundError:
        return [
            DoctorCheck(
                check_id="PDG-DOC-INSTALL-001",
                component="install",
                status=STATUS_WARN,
                title="installed package metadata not found",
                detail=(
                    f"Imported pydepgate version: {imported}\n"
                    "This usually means pydepgate is running from a source checkout "
                    "or an editable environment."
                ),
                remediation="install the package into the environment if this is not intentional",
                data={"imported_version": imported, "installed_version": None},
            )
        ]

    if installed == imported:
        return [
            DoctorCheck(
                check_id="PDG-DOC-INSTALL-001",
                component="install",
                status=STATUS_PASS,
                title="installed package metadata matches imported version",
                detail=f"pydepgate {imported}",
                data={"imported_version": imported, "installed_version": installed},
            )
        ]

    return [
        DoctorCheck(
            check_id="PDG-DOC-INSTALL-001",
            component="install",
            status=STATUS_WARN,
            title="installed package metadata differs from imported version",
            detail=(
                f"Imported version: {imported}\n"
                f"Installed metadata version: {installed}"
            ),
            remediation="reinstall pydepgate or verify that the editable checkout is intentional",
            data={"imported_version": imported, "installed_version": installed},
        )
    ]


def _check_paths() -> list[DoctorCheck]:
    specs = (
        ("PDG-DOC-PATHS-001", "cache directory", platform_paths.pydepgate_cache_dir()),
        (
            "PDG-DOC-PATHS-002",
            "config directory",
            platform_paths.pydepgate_config_dir(),
        ),
        ("PDG-DOC-PATHS-003", "data directory", platform_paths.pydepgate_data_dir()),
    )
    checks = []
    for check_id, label, path in specs:
        checks.append(_check_directory_path(check_id, label, path))
    return checks


def _check_directory_path(check_id: str, label: str, path: Path) -> DoctorCheck:
    data = {"path": str(path), "exists": path.exists()}
    if path.exists() and not path.is_dir():
        return DoctorCheck(
            check_id=check_id,
            component="paths",
            status=STATUS_FAIL,
            title=f"{label} path is not a directory",
            detail=str(path),
            remediation="move or remove the file blocking pydepgate's state directory",
            data=data,
        )
    if path.exists():
        if os.access(path, os.W_OK):
            return DoctorCheck(
                check_id=check_id,
                component="paths",
                status=STATUS_PASS,
                title=f"{label} exists and is writable",
                detail=str(path),
                data={**data, "writable": True},
            )
        return DoctorCheck(
            check_id=check_id,
            component="paths",
            status=STATUS_FAIL,
            title=f"{label} exists but is not writable",
            detail=str(path),
            remediation="fix directory permissions or point XDG paths at a writable location",
            data={**data, "writable": False},
        )

    ancestor = _nearest_existing_ancestor(path)
    ancestor_writable = os.access(ancestor, os.W_OK)
    if ancestor_writable:
        return DoctorCheck(
            check_id=check_id,
            component="paths",
            status=STATUS_WARN,
            title=f"{label} does not exist yet",
            detail=f"{path}\nNearest existing parent is writable: {ancestor}",
            remediation="no action required unless a command later fails to create it",
            data={
                **data,
                "nearest_existing_parent": str(ancestor),
                "parent_writable": True,
            },
        )
    return DoctorCheck(
        check_id=check_id,
        component="paths",
        status=STATUS_FAIL,
        title=f"{label} does not exist and no writable parent was found",
        detail=f"{path}\nNearest existing parent: {ancestor}",
        remediation="create the parent directory or set the corresponding XDG environment variable",
        data={
            **data,
            "nearest_existing_parent": str(ancestor),
            "parent_writable": False,
        },
    )


def _check_environment() -> list[DoctorCheck]:
    names = (
        "PYDEPGATE_CI",
        "PYDEPGATE_FORMAT",
        "PYDEPGATE_COLOR",
        "PYDEPGATE_NO_COLOR",
        "PYDEPGATE_MIN_SEVERITY",
        "PYDEPGATE_STRICT_EXIT",
        "PYDEPGATE_RULES_FILE",
        "PYDEPGATE_NO_MAP",
        "PYDEPGATE_WORKERS",
        "PYDEPGATE_FORCE_PARALLEL",
        "PYDEPGATE_SARIF_SRCROOT",
        "XDG_CACHE_HOME",
        "XDG_CONFIG_HOME",
        "XDG_DATA_HOME",
        "NO_COLOR",
    )
    present = {name: os.environ[name] for name in names if name in os.environ}
    warnings = _environment_warnings(present)
    if warnings:
        return [
            DoctorCheck(
                check_id="PDG-DOC-ENV-001",
                component="environment",
                status=STATUS_WARN,
                title="environment variables need attention",
                detail="\n".join(warnings),
                remediation="fix or unset the unexpected environment variable values",
                data={"set": present, "warnings": warnings},
            )
        ]
    if present:
        detail = "Set variables: " + ", ".join(sorted(present))
    else:
        detail = "No pydepgate or XDG environment overrides are set."
    return [
        DoctorCheck(
            check_id="PDG-DOC-ENV-001",
            component="environment",
            status=STATUS_PASS,
            title="environment variable scan completed",
            detail=detail,
            data={"set": present},
        )
    ]


def _environment_warnings(present: dict[str, str]) -> list[str]:
    warnings: list[str] = []
    if present.get("PYDEPGATE_FORMAT") not in (None, "human", "json", "sarif"):
        warnings.append("PYDEPGATE_FORMAT should be one of: human, json, sarif")
    if present.get("PYDEPGATE_COLOR") not in (None, "auto", "always", "never"):
        warnings.append("PYDEPGATE_COLOR should be one of: auto, always, never")
    if present.get("PYDEPGATE_MIN_SEVERITY") not in (
        None,
        "info",
        "low",
        "medium",
        "high",
        "critical",
    ):
        warnings.append(
            "PYDEPGATE_MIN_SEVERITY should be one of: info, low, medium, high, critical"
        )
    workers = present.get("PYDEPGATE_WORKERS")
    if workers not in (None, "auto", "serial"):
        try:
            if int(workers) < 1:
                warnings.append(
                    "PYDEPGATE_WORKERS must be auto, serial, or an integer >= 1"
                )
        except ValueError:
            warnings.append(
                "PYDEPGATE_WORKERS must be auto, serial, or an integer >= 1"
            )
    rules_file = present.get("PYDEPGATE_RULES_FILE")
    if rules_file:
        path = Path(rules_file)
        if path.suffix != ".gate":
            warnings.append("PYDEPGATE_RULES_FILE should point to a .gate file")
        elif not path.is_file():
            warnings.append("PYDEPGATE_RULES_FILE points to a missing file")
    return warnings


def _check_cvedb() -> list[DoctorCheck]:
    db_path = _cvedb_path()
    if not db_path.exists():
        return [
            DoctorCheck(
                check_id="PDG-DOC-CVEDB-001",
                component="cvedb",
                status=STATUS_WARN,
                title="CVE database not found",
                detail=str(db_path),
                remediation="run 'pydepgate cvedb update' to download and import OSV data",
                data={"path": str(db_path), "exists": False},
            )
        ]
    if not db_path.is_file():
        return [
            DoctorCheck(
                check_id="PDG-DOC-CVEDB-001",
                component="cvedb",
                status=STATUS_FAIL,
                title="CVE database path is not a file",
                detail=str(db_path),
                remediation="remove the blocking path and run 'pydepgate cvedb update'",
                data={"path": str(db_path), "exists": True, "is_file": False},
            )
        ]

    conn = None
    try:
        conn = _open_sqlite_readonly(db_path)
        cvedb_schema.check_schema_compatibility(conn)
        metadata = cvedb_schema.read_all_metadata(conn)
        range_count = _safe_count(conn, "affected_ranges")
    except cvedb_schema.SchemaVersionMismatch as exc:
        return [
            DoctorCheck(
                check_id="PDG-DOC-CVEDB-002",
                component="cvedb",
                status=STATUS_FAIL,
                title="CVE database schema is incompatible",
                detail=str(exc),
                remediation="run 'pydepgate cvedb update --force' to rebuild the local CVE database",
                data={"path": str(db_path), "error": str(exc)},
            )
        ]
    except sqlite3.Error as exc:
        return [
            DoctorCheck(
                check_id="PDG-DOC-CVEDB-003",
                component="cvedb",
                status=STATUS_FAIL,
                title="CVE database could not be opened read-only",
                detail=f"{db_path}\n{type(exc).__name__}: {exc}",
                remediation="rebuild the local CVE database with 'pydepgate cvedb update --force'",
                data={"path": str(db_path), "error": str(exc)},
            )
        ]
    finally:
        if conn is not None:
            conn.close()

    detail_parts = [
        str(db_path),
        f"Schema version: {metadata.get(cvedb_schema.METADATA_KEY_SCHEMA_VERSION, 'unknown')}",
        f"Records imported: {metadata.get(cvedb_schema.METADATA_KEY_RECORDS_IMPORTED, 'unknown')}",
        f"Range rows: {range_count if range_count is not None else 'unknown'}",
        f"Last update: {metadata.get(cvedb_schema.METADATA_KEY_LAST_FULL_UPDATE, 'never')}",
    ]
    snapshot = metadata.get(cvedb_schema.METADATA_KEY_LAST_SNAPSHOT_SHA256)
    if snapshot:
        detail_parts.append(f"Snapshot SHA256: {snapshot[:16]}...")
    return [
        DoctorCheck(
            check_id="PDG-DOC-CVEDB-001",
            component="cvedb",
            status=STATUS_PASS,
            title="CVE database schema is compatible",
            detail="\n".join(detail_parts),
            data={
                "path": str(db_path),
                "metadata": metadata,
                "range_count": range_count,
            },
        )
    ]


def _check_pdgdb() -> list[DoctorCheck]:
    db_path = _pdgdb_path()
    if not db_path.exists():
        return [
            DoctorCheck(
                check_id="PDG-DOC-PDGDB-001",
                component="pdgdb",
                status=STATUS_WARN,
                title="evidence database not found",
                detail=str(db_path),
                remediation="run 'pydepgate db init' or run a scan with '--save-to-db'",
                data={"path": str(db_path), "exists": False},
            )
        ]
    if not db_path.is_file():
        return [
            DoctorCheck(
                check_id="PDG-DOC-PDGDB-001",
                component="pdgdb",
                status=STATUS_FAIL,
                title="evidence database path is not a file",
                detail=str(db_path),
                remediation="remove the blocking path and run 'pydepgate db init'",
                data={"path": str(db_path), "exists": True, "is_file": False},
            )
        ]

    conn = None
    try:
        conn = _open_sqlite_readonly(db_path)
        pdgdb_schema.check_schema_compatibility(conn)
        metadata = pdgdb_schema.read_all_metadata(conn)
        counts = {
            "scan_runs": _safe_count(conn, "scan_runs"),
            "scanned_artifacts": _safe_count(conn, "scanned_artifacts"),
            "static_findings": _safe_count(conn, "static_findings"),
            "decoded_nodes": _safe_count(conn, "decoded_nodes"),
            "cve_findings": _safe_count(conn, "cve_findings"),
        }
    except pdgdb_schema.SchemaVersionMismatch as exc:
        return [
            DoctorCheck(
                check_id="PDG-DOC-PDGDB-002",
                component="pdgdb",
                status=STATUS_FAIL,
                title="evidence database schema is incompatible",
                detail=str(exc),
                remediation="run the appropriate pydepgate db migration for this release",
                data={"path": str(db_path), "error": str(exc)},
            )
        ]
    except sqlite3.Error as exc:
        return [
            DoctorCheck(
                check_id="PDG-DOC-PDGDB-003",
                component="pdgdb",
                status=STATUS_FAIL,
                title="evidence database could not be opened read-only",
                detail=f"{db_path}\n{type(exc).__name__}: {exc}",
                remediation="move the corrupt database aside and run 'pydepgate db init' if needed",
                data={"path": str(db_path), "error": str(exc)},
            )
        ]
    finally:
        if conn is not None:
            conn.close()

    detail = [
        str(db_path),
        f"Schema version: {metadata.get(pdgdb_schema.METADATA_KEY_SCHEMA_VERSION, 'unknown')}",
        f"Created at: {metadata.get(pdgdb_schema.METADATA_KEY_CREATED_AT, 'unknown')}",
        f"Last modified: {metadata.get(pdgdb_schema.METADATA_KEY_LAST_MODIFIED, 'unknown')}",
        f"Scan runs: {counts['scan_runs']}",
        f"Artifacts: {counts['scanned_artifacts']}",
        f"Static findings: {counts['static_findings']}",
        f"Decoded nodes: {counts['decoded_nodes']}",
        f"CVE findings: {counts['cve_findings']}",
    ]
    return [
        DoctorCheck(
            check_id="PDG-DOC-PDGDB-001",
            component="pdgdb",
            status=STATUS_PASS,
            title="evidence database schema is compatible",
            detail="\n".join(detail),
            data={"path": str(db_path), "metadata": metadata, "counts": counts},
        )
    ]


def _check_rules(options: DoctorOptions) -> list[DoctorCheck]:
    explicit = str(options.rules_file) if options.rules_file is not None else None
    try:
        loaded = load_user_rules(explicit_path=explicit)
    except GateFileError as exc:
        return [
            DoctorCheck(
                check_id="PDG-DOC-RULES-001",
                component="rules",
                status=STATUS_FAIL,
                title="user rules file failed to load",
                detail=str(exc),
                remediation="fix the .gate file or unset PYDEPGATE_RULES_FILE",
                data={"rules_file": explicit or os.environ.get(ENV_RULES_FILE)},
            )
        ]

    default_count = len(DEFAULT_RULES)
    user_count = len(loaded.rules)
    if loaded.source_path is None:
        return [
            DoctorCheck(
                check_id="PDG-DOC-RULES-001",
                component="rules",
                status=STATUS_PASS,
                title="no user rules file discovered",
                detail=f"Built-in rules available: {default_count}",
                data={
                    "source_path": None,
                    "default_rule_count": default_count,
                    "user_rule_count": 0,
                    "also_found": [],
                    "warnings": [],
                },
            )
        ]

    detail = [
        str(loaded.source_path),
        f"Built-in rules: {default_count}",
        f"User rules: {user_count}",
    ]
    if loaded.also_found:
        detail.append("Also found but not loaded:")
        detail.extend(f"- {path}" for path in loaded.also_found)
    if loaded.warnings:
        detail.append("Warnings:")
        detail.extend(f"- {warning}" for warning in loaded.warnings)

    return [
        DoctorCheck(
            check_id="PDG-DOC-RULES-001",
            component="rules",
            status=STATUS_WARN if loaded.warnings else STATUS_PASS,
            title=(
                "user rules loaded with warnings"
                if loaded.warnings
                else "user rules loaded successfully"
            ),
            detail="\n".join(detail),
            remediation="review the rules-file warnings" if loaded.warnings else None,
            data={
                "source_path": str(loaded.source_path),
                "default_rule_count": default_count,
                "user_rule_count": user_count,
                "also_found": [str(path) for path in loaded.also_found],
                "warnings": list(loaded.warnings),
            },
        )
    ]


def _check_policies_placeholder() -> list[DoctorCheck]:
    try:
        importlib.import_module("pydepgate.policies")
        detail = "Policy package scaffold is importable; policy diagnostics are not implemented yet."
    except Exception as exc:
        detail = (
            f"Policy package scaffold is not importable: {type(exc).__name__}: {exc}"
        )
    return [
        DoctorCheck(
            check_id="PDG-DOC-POLICIES-000",
            component="policies",
            status=STATUS_SKIP,
            title="policy diagnostics reserved for a future release",
            detail=detail,
            data={"available": False},
        )
    ]


def _check_daemon_placeholder() -> list[DoctorCheck]:
    present = []
    for name in (
        "pydepgate.daemons",
        "pydepgate.daemons.auditd",
        "pydepgate.daemons.evidenced",
        "pydepgate.daemons.intaked",
        "pydepgate.daemons.policyd",
        "pydepgate.daemons.scannerd",
    ):
        try:
            importlib.import_module(name)
            present.append(name.rsplit(".", 1)[-1])
        except Exception:
            continue
    detail = (
        "Daemon package scaffolds detected: " + ", ".join(present)
        if present
        else "No daemon package scaffolds are importable yet."
    )
    detail += "\nRuntime daemon health checks are not implemented yet."
    return [
        DoctorCheck(
            check_id="PDG-DOC-DAEMON-000",
            component="daemon",
            status=STATUS_SKIP,
            title="daemon diagnostics reserved for a future release",
            detail=detail,
            data={"detected_modules": present, "available": False},
        )
    ]


def _check_event_smoke() -> list[DoctorCheck]:
    from pydepgate.events import EventEmitter, JsonlEventSink, MemoryEventSink

    with tempfile.TemporaryDirectory() as tmp:
        jsonl_path = Path(tmp) / "events.jsonl"
        memory = MemoryEventSink()
        jsonl = JsonlEventSink(jsonl_path, append=False)
        emitter = EventEmitter(
            producer="pydepgate.doctor",
            sinks=(memory, jsonl),
        )
        event = emitter.emit(
            "internal.system.doctor_smoke_test",
            {"purpose": "diagnostic event serialization smoke test"},
        )
        lines = jsonl_path.read_text(encoding="utf-8").splitlines()
        if len(memory.events) == 1 and len(lines) == 1 and event.event_id in lines[0]:
            return [
                DoctorCheck(
                    check_id="PDG-DOC-EVENTS-001",
                    component="events",
                    status=STATUS_PASS,
                    title="event JSONL serialization smoke test succeeded",
                    detail="Temporary memory and JSONL sinks accepted one diagnostic event.",
                    data={"event_id": event.event_id},
                )
            ]
    return [
        DoctorCheck(
            check_id="PDG-DOC-EVENTS-001",
            component="events",
            status=STATUS_FAIL,
            title="event JSONL serialization smoke test failed",
            detail="The temporary event sinks did not receive the expected diagnostic event.",
            remediation="file an issue with the pydepgate doctor JSON output attached",
        )
    ]


def _open_sqlite_readonly(path: Path) -> sqlite3.Connection:
    uri = path.resolve().as_uri() + "?mode=ro"
    return sqlite3.connect(uri, uri=True)


def _safe_count(conn: sqlite3.Connection, table: str) -> int | None:
    try:
        row = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
    except sqlite3.OperationalError:
        return None
    return int(row[0]) if row else 0


def _cvedb_path() -> Path:
    return (
        platform_paths.pydepgate_cache_dir() / "cvedb" / cvedb_constants.CVE_DB_FILENAME
    )


def _pdgdb_path() -> Path:
    return platform_paths.pydepgate_data_dir() / "pdgdb" / "evidence.db"


def _nearest_existing_ancestor(path: Path) -> Path:
    current = path.parent
    while not current.exists() and current != current.parent:
        current = current.parent
    return current
