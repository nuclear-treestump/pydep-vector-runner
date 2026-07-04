"""pydepgate.cli.subcommands.doctor

The ``doctor`` subcommand diagnoses local pydepgate installation state.
It is intentionally a renderer around ``pydepgate.diagnostics`` so the
public API and future daemons can use the same diagnostic core.
"""

from __future__ import annotations

import argparse
import sys

from pydepgate.cli import exit_codes
from pydepgate.diagnostics.doctor import DoctorOptions, run_doctor
from pydepgate.diagnostics.render import render_human, render_json


def register(subparsers) -> None:
    """Register the doctor subcommand."""
    parser = subparsers.add_parser(
        "doctor",
        help="Diagnose local pydepgate installation and state",
        description=(
            "Diagnose local pydepgate installation state, storage paths, "
            "database readiness, rules discovery, environment variables, "
            "event serialization, and reserved policy/daemon diagnostic surfaces."
        ),
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        default=False,
        help="Return a non-zero exit code when warnings are present",
    )
    parser.add_argument(
        "--no-event-smoke",
        action="store_true",
        default=False,
        help="Skip the temporary event serialization smoke test",
    )
    parser.set_defaults(func=run)


def run(args: argparse.Namespace) -> int:
    """Run local diagnostics and render the requested output format."""
    report = run_doctor(
        DoctorOptions(
            rules_file=getattr(args, "rules_file", None),
            include_event_smoke=not bool(getattr(args, "no_event_smoke", False)),
        )
    )

    output_format = getattr(args, "format", None) or "human"
    if output_format == "json":
        sys.stdout.write(render_json(report))
        sys.stdout.write("\n")
    elif output_format == "human":
        sys.stdout.write(render_human(report))
        sys.stdout.write("\n")
    else:
        sys.stderr.write("error: doctor supports --format human or --format json\n")
        return exit_codes.TOOL_ERROR

    if report.failed:
        return exit_codes.TOOL_ERROR
    if getattr(args, "strict", False) and report.warned:
        return exit_codes.TOOL_ERROR
    return exit_codes.CLEAN
