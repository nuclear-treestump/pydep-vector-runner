"""pydepgate.diagnostics.model

Structured diagnostic report models for pydepgate.

The diagnostics package is intentionally library-first. CLI commands,
public API wrappers, and future daemon health endpoints should all consume
these objects rather than scraping human output.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

DOCTOR_SCHEMA_VERSION = 1

STATUS_PASS = "pass"
STATUS_WARN = "warn"
STATUS_FAIL = "fail"
STATUS_SKIP = "skip"
STATUS_VALUES = (STATUS_PASS, STATUS_WARN, STATUS_FAIL, STATUS_SKIP)


@dataclass(frozen=True, slots=True)
class DoctorCheck:
    """One local diagnostic check produced by ``pydepgate doctor``."""

    check_id: str
    component: str
    status: str
    title: str
    detail: str
    remediation: str | None = None
    data: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.status not in STATUS_VALUES:
            raise ValueError(f"unknown doctor status: {self.status!r}")

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-safe representation of this check."""
        return {
            "check_id": self.check_id,
            "component": self.component,
            "status": self.status,
            "title": self.title,
            "detail": self.detail,
            "remediation": self.remediation,
            "data": _json_safe_mapping(self.data),
        }


@dataclass(frozen=True, slots=True)
class DoctorReport:
    """Structured report for local pydepgate diagnostics."""

    schema_version: int
    pydepgate_version: str
    generated_at: str
    checks: tuple[DoctorCheck, ...]

    @property
    def summary(self) -> dict[str, int]:
        """Return check counts keyed by status."""
        counts = {status: 0 for status in STATUS_VALUES}
        for check in self.checks:
            counts[check.status] = counts.get(check.status, 0) + 1
        return counts

    @property
    def failed(self) -> bool:
        """True when at least one diagnostic check failed."""
        return any(check.status == STATUS_FAIL for check in self.checks)

    @property
    def warned(self) -> bool:
        """True when at least one diagnostic check emitted a warning."""
        return any(check.status == STATUS_WARN for check in self.checks)

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-safe representation of this report."""
        return {
            "schema_version": self.schema_version,
            "pydepgate_version": self.pydepgate_version,
            "generated_at": self.generated_at,
            "summary": self.summary,
            "checks": [check.to_dict() for check in self.checks],
        }


def _json_safe_mapping(mapping: Mapping[str, Any]) -> dict[str, object]:
    return {str(key): _json_safe(value) for key, value in mapping.items()}


def _json_safe(value: Any) -> object:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Mapping):
        return _json_safe_mapping(value)
    if isinstance(value, (tuple, list, set, frozenset)):
        return [_json_safe(item) for item in value]
    return str(value)
