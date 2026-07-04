"""pydepgate.cli.main

pydepgate CLI entry point.

Sets up argparse with global flags, registers all subcommands,
handles environment-variable defaults, and dispatches to the
selected subcommand. Returns the subcommand's exit code.
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass

from pydepgate.cli import exit_codes
from pydepgate.cli.subcommands import (
    completion,
    exec_stub,
    preflight,
    scan,
    version,
    explain,
    cvedb,
    cvescan,
    db,
    doctor,
)
from pydepgate.cli.subcommands.version import get_version

from pydepgate.cli.command_handlers.peek_args import (
    add_peek_arguments,
    build_peek_enricher,
    peek_chain_enabled,
    validate_peek_args,
)
from pydepgate.cli.command_handlers.decode_args import (
    add_decode_arguments,
    decode_enabled,
    validate_decode_args,
)

from pydepgate.cli.command_handlers.sarif_args import (
    add_sarif_arguments,
    validate_sarif_args,
)

# Color mode constants. Used as the values of args.color and as the
# argparse choices. Exposed at module level so tests and the reporter
# can refer to them without retyping string literals.
COLOR_AUTO = "auto"
COLOR_ALWAYS = "always"
COLOR_NEVER = "never"
COLOR_CHOICES = (COLOR_AUTO, COLOR_ALWAYS, COLOR_NEVER)


# Default engine parallel-threshold value, also referenced by the
# scan and preflight subcommands when constructing StaticEngine.
DEFAULT_PARALLEL_THRESHOLD = 1000

# Thrashing multipliers. workers > 2x available CPUs warns;
# workers > 4x warns more sternly; workers > 8x refuses outright.
THRASH_WARN_MULTIPLIER = 2
THRASH_SEVERE_MULTIPLIER = 4
THRASH_REFUSE_MULTIPLIER = 8


@dataclass(frozen=True)
class WorkersSpec:
    """Result of parsing a single --workers value.

    Carries both the resolved integer worker count and whether the
    user wrote 'auto'. The resolver needs the latter to decide
    whether to emit the single-CPU stderr note (Case 6 in the
    conflict matrix).
    """

    value: int | None  # None for serial (current behavior preserved)
    was_auto: bool


def _available_cpus() -> int:
    """Return the number of CPUs this process can actually use.

    Prefers os.sched_getaffinity (Linux) which respects cgroup CPU
    limits typical in CI containers. Falls back to os.cpu_count()
    on platforms that do not expose affinity (macOS, Windows). Always
    returns at least 1.
    """
    try:
        return max(1, len(os.sched_getaffinity(0)))
    except AttributeError:
        return max(1, os.cpu_count() or 1)


def _parse_workers(value: str) -> WorkersSpec:
    """Parse a --workers value into a WorkersSpec.

    Accepts:
      'serial' -> WorkersSpec(value=None, was_auto=False)
      'auto'   -> WorkersSpec(value=_available_cpus(), was_auto=True)
      integer string >= 1 -> WorkersSpec(value=int, was_auto=False)

    Anything else raises argparse.ArgumentTypeError, which argparse
    converts into a clean usage error at parse time.
    """
    if value == "serial":
        return WorkersSpec(value=None, was_auto=False)
    if value == "auto":
        return WorkersSpec(value=_available_cpus(), was_auto=True)
    try:
        n = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"--workers must be an integer, 'serial', or 'auto'; " f"got {value!r}"
        )
    if n < 1:
        raise argparse.ArgumentTypeError(f"--workers must be >= 1, got {n}")
    return WorkersSpec(value=n, was_auto=False)


def _resolve_workers_config(
    args: argparse.Namespace,
    stderr,
) -> tuple[int | None, int, list[str]]:
    """Translate parsed CLI args into engine configuration.

    Returns (workers, parallel_threshold, cli_diagnostics):

      workers              The integer worker count (or None for
                           serial) to pass to StaticEngine.
      parallel_threshold   The threshold value to pass to
                           StaticEngine. 0 when --force-parallel
                           is active and the configuration is
                           actually parallel-capable.
      cli_diagnostics      A list of human-readable diagnostic
                           strings that ALSO went to stderr.
                           Delivery 3.1 will thread these into
                           ScanResult.diagnostics; for now they
                           sit on args for subcommands to consume.

    Calls sys.exit(TOOL_ERROR) on the 8x refuse case (Case 4
    extended). Emits warnings to stderr (and records them in the
    returned list) for Cases 1, 2a, 3, 5, 6, and the new 4x severe
    thrashing case.
    """
    spec: WorkersSpec | None = getattr(args, "workers", None)
    force_parallel: bool = bool(getattr(args, "force_parallel", False))

    workers: int | None = spec.value if spec is not None else None
    was_auto: bool = spec.was_auto if spec is not None else False
    threshold: int = DEFAULT_PARALLEL_THRESHOLD
    cli_diagnostics: list[str] = []

    cpus = _available_cpus()

    # --- 8x refuse (Case 4 ramped up) ------------------------------------
    # Hard limit. No override, no env-var escape hatch. If a user
    # genuinely needs to exceed this, they can patch the constant.
    if workers is not None and workers > THRASH_REFUSE_MULTIPLIER * cpus:
        msg = (
            f"error: --workers {workers} exceeds "
            f"{THRASH_REFUSE_MULTIPLIER}x available CPUs ({cpus}); "
            f"refusing to run (this would severely impact system stability)"
        )
        print(msg, file=stderr)
        sys.exit(exit_codes.TOOL_ERROR)

    # --- Cases 1, 2a, 5: force-parallel with non-parallel workers --------
    # All three collapse to "you asked to force parallel but your
    # workers configuration cannot actually run parallel."
    if force_parallel and (workers is None or workers < 2):
        if workers is None:
            phrasing = "is serial (no --workers given or --workers serial)"
        else:
            phrasing = f"is {workers} (--workers must be >= 2 to parallelize)"
        msg = (
            f"warning: --force-parallel has no effect when workers config "
            f"{phrasing}; running serial"
        )
        print(msg, file=stderr)
        cli_diagnostics.append(msg.removeprefix("warning: "))
        # threshold stays at default; force-parallel is a no-op here.
    elif force_parallel:
        # Force-parallel actually applies. Drop the threshold to 0
        # so the engine engages parallel regardless of file count.
        threshold = 0

    # --- Case 6: auto resolved to 1 on a single-CPU machine --------------
    # Informational note. Auto did what was asked; the environment
    # is the constraint.
    if was_auto and workers == 1:
        msg = (
            "note: --workers auto resolved to 1 (running serial); "
            "no additional CPUs available to this process"
        )
        print(msg, file=stderr)
        cli_diagnostics.append(msg.removeprefix("note: "))

    # --- Case 3: thrashing warnings --------------------------------------
    # Tiered: > 2x warns, > 4x warns more sternly. > 8x already
    # exited above.
    if workers is not None and workers > THRASH_SEVERE_MULTIPLIER * cpus:
        msg = (
            f"warning: --workers {workers} exceeds "
            f"{THRASH_SEVERE_MULTIPLIER}x available CPUs ({cpus}); "
            f"severe CPU thrashing expected, throughput will degrade"
        )
        print(msg, file=stderr)
        cli_diagnostics.append(msg.removeprefix("warning: "))
    elif workers is not None and workers > THRASH_WARN_MULTIPLIER * cpus:
        msg = (
            f"warning: --workers {workers} exceeds "
            f"{THRASH_WARN_MULTIPLIER}x available CPUs ({cpus}); "
            f"expect CPU contention, not linear speedup"
        )
        print(msg, file=stderr)
        cli_diagnostics.append(msg.removeprefix("warning: "))

    return workers, threshold, cli_diagnostics


def _env_bool(name: str) -> bool:
    """Read a boolean environment variable.

    Truthy values: 1, true, yes, on (case-insensitive).
    Anything else (including unset) is False.
    """
    val = os.environ.get(name, "").lower()
    return val in ("1", "true", "yes", "on")


def _env_str(name: str, default: str | None = None) -> str | None:
    """Read a string environment variable, returning default if unset."""
    return os.environ.get(name, default)


def _color_default_from_env() -> str:
    """Compute the default value for --color from the environment.

    Precedence:
      1. PYDEPGATE_COLOR if set to one of auto/always/never.
      2. NO_COLOR or PYDEPGATE_NO_COLOR env vars (any value) map
         to "never" per the no-color.org convention.
      3. Otherwise "auto", which defers to TTY detection at render
         time.

    A bogus PYDEPGATE_COLOR value (e.g. "PYDEPGATE_COLOR=foo") is
    ignored and treated as if unset, falling through to the
    NO_COLOR check. We deliberately do not warn about this here
    because argparse runs before stderr-routing decisions are made;
    a typo'd env var falling back to a sane default is the least
    surprising behavior.
    """
    explicit = os.environ.get("PYDEPGATE_COLOR", "").strip().lower()
    if explicit in COLOR_CHOICES:
        return explicit

    if os.environ.get("NO_COLOR") or os.environ.get("PYDEPGATE_NO_COLOR"):
        return COLOR_NEVER

    return COLOR_AUTO


def _workers_default_from_env() -> WorkersSpec | None:
    """Compute the default value for --workers from the environment.

    Reads PYDEPGATE_WORKERS and runs it through _parse_workers,
    returning the resulting WorkersSpec on success or None when the
    env var is unset, empty, or contains an invalid value.

    Silently swallowing parse failures matches the convention from
    _color_default_from_env: a bogus env value (typo, leftover
    fragment from a misformatted assignment, etc.) falls back to
    "as if unset" rather than crashing argparse before parse can
    surface a useful error. The user's actual CLI invocation gets
    the chance to override it, and the absence of an applied env
    default does not surprise anyone.

    Accepted env values match the CLI grammar exactly:
      PYDEPGATE_WORKERS=serial   -> WorkersSpec(value=None, was_auto=False)
      PYDEPGATE_WORKERS=auto     -> WorkersSpec(value=<cpus>, was_auto=True)
      PYDEPGATE_WORKERS=<int>    -> WorkersSpec(value=int, was_auto=False)

    Anything else (negative integers, zero, non-numeric strings,
    floating point) is silently ignored.
    """
    value = os.environ.get("PYDEPGATE_WORKERS", "").strip()
    if not value:
        return None
    try:
        return _parse_workers(value)
    except argparse.ArgumentTypeError:
        return None


def _add_global_flags(
    parser: argparse.ArgumentParser,
    is_subparser: bool = False,
) -> None:
    """Add the pydepgate global flags to a parser.

    Called both on the top-level parser AND on each subcommand parser
    so flags work in either position. When called on a subparser, the
    defaults are SUPPRESS so that omitted flags do not clobber values
    captured by the top-level parser.
    """
    # Use argparse.SUPPRESS as default for subparsers so omitted flags
    # don't overwrite values set at the top level. For the top-level
    # parser, use the env-var-derived defaults normally.
    if is_subparser:
        ci_default = argparse.SUPPRESS
        format_default = argparse.SUPPRESS
        color_default = argparse.SUPPRESS
        min_severity_default = argparse.SUPPRESS
        strict_exit_default = argparse.SUPPRESS
    else:
        ci_default = _env_bool("PYDEPGATE_CI")
        format_default = _env_str("PYDEPGATE_FORMAT")
        color_default = _color_default_from_env()
        min_severity_default = _env_str("PYDEPGATE_MIN_SEVERITY")
        strict_exit_default = _env_bool("PYDEPGATE_STRICT_EXIT")

    parser.add_argument(
        "--ci",
        action="store_true",
        default=ci_default,
        help=(
            "CI mode: compact output, no color, JSON default format, "
            "diagnostics to stderr. Env: PYDEPGATE_CI"
        ),
    )
    parser.add_argument(
        "--format",
        choices=("human", "json", "sarif"),
        default=format_default,
        help=(
            "Output format. Default: human (json under --ci). " "Env: PYDEPGATE_FORMAT"
        ),
    )

    # --color is the canonical control. It takes one of three values:
    #   auto    Use color when stdout is a TTY and no NO_COLOR-style
    #           env var is set (the historical default behavior).
    #   always  Force color, even when stdout is not a TTY. Useful for
    #           piping to less -R or capturing colored output to a file
    #           that will later be rendered by a terminal-aware viewer.
    #   never   Disable color unconditionally.
    #
    # --no-color is kept as a backwards-compatible alias for
    # --color=never. Both write to args.color so the rest of the CLI
    # only has one attribute to consult. Old invocations and old CI
    # configs that pass --no-color continue to work without changes.
    parser.add_argument(
        "--color",
        choices=COLOR_CHOICES,
        default=color_default,
        metavar="WHEN",
        help=(
            "Control ANSI color output. 'auto' (default) emits color "
            "when stdout is a TTY; 'always' forces color even when "
            "piped or redirected; 'never' disables color entirely. "
            "Env: PYDEPGATE_COLOR. NO_COLOR and PYDEPGATE_NO_COLOR "
            "env vars (any value) imply --color=never."
        ),
    )
    parser.add_argument(
        "--no-color",
        action="store_const",
        const=COLOR_NEVER,
        dest="color",
        default=argparse.SUPPRESS,
        help=(
            "Alias for --color=never. Kept for backwards compatibility. "
            "Env: PYDEPGATE_NO_COLOR or NO_COLOR"
        ),
    )

    parser.add_argument(
        "--min-severity",
        choices=("info", "low", "medium", "high", "critical"),
        default=min_severity_default,
        help=("Suppress findings below this severity. " "Env: PYDEPGATE_MIN_SEVERITY"),
    )
    parser.add_argument(
        "--strict-exit",
        action="store_true",
        default=strict_exit_default,
        help=(
            "Apply --min-severity to display only; compute exit code "
            "from all findings. Env: PYDEPGATE_STRICT_EXIT"
        ),
    )

    parser.add_argument(
        "--rules-file",
        default=(
            argparse.SUPPRESS if is_subparser else _env_str("PYDEPGATE_RULES_FILE")
        ),
        help=(
            "Path to a .gate rules file. Default: discover "
            "pydepgate.gate in cwd or venv. Env: PYDEPGATE_RULES_FILE"
        ),
    )
    parser.add_argument(
        "--no-map",
        action="store_true",
        default=bool(os.environ.get("PYDEPGATE_NO_MAP")),
        help=(
            "Suppress the density map visualization in human output. "
            "Env: PYDEPGATE_NO_MAP"
        ),
    )

    # --workers / --force-parallel: control the engine's parallel pool.
    # Live in _add_global_flags so they work at top-level and per-
    # subcommand position. Validation and stderr warnings happen in
    # _resolve_workers_config after parse.
    parser.add_argument(
        "--workers",
        type=_parse_workers,
        default=(argparse.SUPPRESS if is_subparser else _workers_default_from_env()),
        metavar="WORKERS",
        help=(
            "Number of worker processes for per-file scans. Accepts "
            "an integer >= 1, 'serial' (default), or 'auto' (use "
            "available CPUs, respects CI CPU limits via "
            "sched_getaffinity on Linux). Below the file-count "
            "threshold (1000 files), parallel is downgraded to "
            "serial with a diagnostic in the scan report. "
            "Env: PYDEPGATE_WORKERS"
        ),
    )
    parser.add_argument(
        "--force-parallel",
        action="store_true",
        default=(
            argparse.SUPPRESS if is_subparser else _env_bool("PYDEPGATE_FORCE_PARALLEL")
        ),
        help=(
            "Run parallel regardless of file count (bypasses the "
            "1000-file threshold). No effect without --workers >= 2. "
            "Env: PYDEPGATE_FORCE_PARALLEL"
        ),
    )

    add_peek_arguments(parser, is_subparser=is_subparser)  # Peek args (--peek*)
    add_decode_arguments(parser, is_subparser=is_subparser)  # Decode args (--decode*)
    add_sarif_arguments(parser, is_subparser=is_subparser)  # SARIF args (--sarif*)


def build_parser() -> argparse.ArgumentParser:
    """Construct the argparse parser tree."""
    parser = argparse.ArgumentParser(
        prog="pydepgate",
        description=(
            "A lightweight Python runner that interdicts suspicious "
            "startup behavior. Statically analyzes packages for the "
            "patterns used in supply-chain attacks like LiteLLM 1.82.8."
        ),
        epilog=(
            "Use 'pydepgate <subcommand> --help' for subcommand-specific "
            "help, or 'pydepgate help' for an overview."
        ),
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"pydepgate {get_version()}",
    )

    # Add global flags at the top level so 'pydepgate --format json scan pip' works.
    _add_global_flags(parser)

    # Subcommand registration.
    subparsers = parser.add_subparsers(
        dest="subcommand",
        title="subcommands",
        metavar="<subcommand>",
    )

    # Each subcommand registers its own arguments AND inherits the
    # global flags so 'pydepgate scan pip --format json' also works.
    scan.register(subparsers)
    preflight.register(subparsers)
    exec_stub.register(subparsers)
    version.register(subparsers)
    explain.register(subparsers)
    cvedb.register(subparsers)
    cvescan.register(subparsers)
    db.register(subparsers)
    doctor.register(subparsers)
    # Help subcommand.
    help_parser = subparsers.add_parser(
        "help",
        help="Show help for pydepgate or a specific subcommand",
    )
    help_parser.add_argument(
        "topic",
        nargs="?",
        help="Subcommand to show help for, or omit for top-level help",
    )
    help_parser.set_defaults(func=lambda args: _run_help(parser, args))

    # Add global flags to every subcommand parser.
    for subparser_name in subparsers.choices:
        _add_global_flags(subparsers.choices[subparser_name], is_subparser=True)

    # Completion subcommands. Registered after the global-flags loop
    # so the hidden _complete subcommand does not get the global
    # flags applied: its `words` REMAINDER positional must accept
    # tokens like `--format` as data, not interpret them as flags.
    completion.register(subparsers)

    return parser


def _run_help(parser: argparse.ArgumentParser, args: argparse.Namespace) -> int:
    """Implement the 'help' subcommand by routing to argparse's help."""
    if not args.topic:
        parser.print_help()
        return 0
    # Find the subparser for the given topic and print its help.
    subparsers_actions = [
        action
        for action in parser._actions
        if isinstance(action, argparse._SubParsersAction)
    ]
    for sp_action in subparsers_actions:
        if args.topic in sp_action.choices:
            sp_action.choices[args.topic].print_help()
            return 0
    sys.stderr.write(f"unknown subcommand: {args.topic}\n")
    return exit_codes.TOOL_ERROR


def _apply_ci_defaults(args: argparse.Namespace) -> None:
    """Apply --ci behavioral cluster: implies several other flags.

    CI mode forces JSON format (unless explicitly set) and disables
    color (unless the user explicitly opted in via --color=always).
    The latter is unusual but legitimate: a CI runner with a colored
    log viewer wants the escape codes preserved even under --ci.
    """
    if not args.ci:
        return
    if not args.format:
        args.format = "json"
    # Only auto-flip color to "never" when the user hasn't explicitly
    # asked for "always". An explicit --color=always paired with --ci
    # is a deliberate choice and we respect it.
    if args.color == COLOR_AUTO:
        args.color = COLOR_NEVER


def main(argv: list[str] | None = None) -> int:
    """Top-level entry point. Returns an exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    validate_peek_args(args)
    validate_decode_args(args)
    validate_sarif_args(args)

    # Resolve --workers and --force-parallel into engine config.
    # Stashes results on args so subcommands can pick them up when
    # constructing StaticEngine (wired in Delivery 3.1). Emits stderr
    # warnings here regardless; the cli_diagnostics list will land
    # in ScanResult.diagnostics once the subcommand wiring ships.
    workers, parallel_threshold, cli_diags = _resolve_workers_config(
        args,
        sys.stderr,
    )
    args._workers_count = workers
    args._workers_threshold = parallel_threshold
    args._workers_diagnostics = tuple(cli_diags)

    if not args.subcommand:
        parser.print_help()
        return 0

    _apply_ci_defaults(args)

    # Default format if still unset.
    if not args.format:
        args.format = "human"

    if not hasattr(args, "func"):
        parser.print_help()
        return exit_codes.TOOL_ERROR

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
