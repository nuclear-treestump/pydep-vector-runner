"""pydepgate.diagnostics.render

Renderers for pydepgate diagnostic reports."""

from __future__ import annotations

import json
from collections import OrderedDict

from pydepgate.diagnostics.model import DoctorReport

_COMPONENT_TITLES = {
    "runtime": "Runtime",
    "install": "Install",
    "paths": "Paths",
    "environment": "Environment",
    "cvedb": "CVE database",
    "pdgdb": "Evidence database",
    "rules": "Rules",
    "policies": "Policies",
    "daemon": "Daemon",
    "events": "Events",
}


_COMPONENT_ORDER = (
    "runtime",
    "install",
    "paths",
    "environment",
    "cvedb",
    "pdgdb",
    "rules",
    "policies",
    "daemon",
    "events",
)


def render_json(report: DoctorReport) -> str:
    """Render a diagnostic report as stable, pretty JSON."""
    return json.dumps(report.to_dict(), indent=2, sort_keys=True)


def render_human(report: DoctorReport) -> str:
    """Render a diagnostic report for terminal use."""
    grouped: OrderedDict[str, list] = OrderedDict(
        (name, []) for name in _COMPONENT_ORDER
    )
    for check in report.checks:
        grouped.setdefault(check.component, []).append(check)

    lines: list[str] = ["pydepgate doctor", ""]

    for component, checks in grouped.items():
        if not checks:
            continue
        title = _COMPONENT_TITLES.get(component, component.replace("_", " ").title())
        lines.append(title)
        for check in checks:
            lines.append(f"  {check.status.upper():<4} {check.title}")
            for detail_line in check.detail.splitlines():
                if detail_line:
                    lines.append(f"       {detail_line}")
            if check.remediation:
                lines.append(f"       Fix: {check.remediation}")
        lines.append("")

    summary = report.summary
    lines.append(
        "Summary: "
        f"{summary.get('pass', 0)} pass, "
        f"{summary.get('warn', 0)} warn, "
        f"{summary.get('fail', 0)} fail, "
        f"{summary.get('skip', 0)} skip"
    )
    return "\n".join(lines)
