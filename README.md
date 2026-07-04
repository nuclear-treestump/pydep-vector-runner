# pydepgate

pydepgate statically scans Python package artifacts for suspicious install-time and startup behavior, and includes a built-in CVE scanner for known vulnerable package versions.

It supports wheels, source distributions, installed packages, package-like directories, and loose Python files. It does not import, install, execute, compile, or deserialize package code.

The scanner looks for risky packaging patterns such as .pth startup hooks, suspicious setup.py behavior, encoded payloads, decode-then-execute chains, obfuscated execution primitives, suspicious standard-library usage, and rule-defined indicators.

pydepgate is designed to work in restricted environments. CVE database updates are separate from cvescan execution, so teams can update the database through an approved path and run scans later in high-side or air-gapped environments.

[PyPI package](https://pypi.org/project/pydepgate/) · [Documentation](https://nuclear-treestump.github.io/pydepgate/) · [Funding](FUNDING.md)

<details>
<summary>Build, package, and release status</summary>

Statistics are provided by PyPI and pepy.tech.

[![PyPI](https://img.shields.io/pypi/v/pydepgate.svg)](https://pypi.org/project/pydepgate/)
[![Downloads](https://pepy.tech/badge/pydepgate)](https://pepy.tech/project/pydepgate)

Tests are performed against Python 3.11, 3.12, and 3.13.

[![Unit tests](https://github.com/nuclear-treestump/pydepgate/actions/workflows/do_unittests.yml/badge.svg)](https://github.com/nuclear-treestump/pydepgate/actions/workflows/do_unittests.yml)
[![SARIF validation](https://github.com/nuclear-treestump/pydepgate/actions/workflows/do_sarif_validation.yml/badge.svg)](https://github.com/nuclear-treestump/pydepgate/actions/workflows/do_sarif_validation.yml)
[![CodeQL Advanced](https://github.com/nuclear-treestump/pydepgate/actions/workflows/codeql.yml/badge.svg)](https://github.com/nuclear-treestump/pydepgate/actions/workflows/codeql.yml)
[![CodeQL](https://github.com/nuclear-treestump/pydepgate/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/nuclear-treestump/pydepgate/actions/workflows/github-code-scanning/codeql)

From 0.5.0 onward, container releases are signed by digest and GitHub-attested. Builds include BuildKit provenance and SBOM attestations, use verified PyPI wheel inputs, and are reproducible for supported platforms.

[![docker-publish](https://github.com/nuclear-treestump/pydepgate/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/nuclear-treestump/pydepgate/actions/workflows/docker-publish.yml)
[![docker-repro-check](https://github.com/nuclear-treestump/pydepgate/actions/workflows/docker-repro.yml/badge.svg)](https://github.com/nuclear-treestump/pydepgate/actions/workflows/docker-repro.yml)

</details>

## What's New

0.7.0 - Added `pydepgate doctor` command, will be required for policies and future daemon diagnostics

## Why this exists

Python can execute package-provided code before the user's script does anything.

`.pth` files in `site-packages` can run import lines during interpreter initialization. `sitecustomize.py` and `usercustomize.py` are imported automatically when present. Source distributions can execute `setup.py` during installation. Packages can run top-level `__init__.py` code when imported. Console-script entry points are generated during installation and executed later as normal commands.

These are normal Python features. They are also useful supply-chain attack surfaces.

The March 2026 LiteLLM supply-chain compromise used this class of startup behavior and is catalogued as [MITRE ATT&CK T1546.018](https://attack.mitre.org/techniques/T1546/018/). The `.pth` vector has also been acknowledged as a security gap in [CPython issue #113659](https://github.com/python/cpython/issues/113659).

Existing tools answer related but different questions. `pip-audit` and Safety check whether a known package version has known vulnerabilities. Bandit checks a source tree for risky Python patterns. pydepgate asks a package-artifact question:

> Does this artifact contain suspicious behavior that could run during installation, interpreter startup, import-time initialization, or generated entry-point execution?

See [THREAT_MODEL.md](THREAT_MODEL.md) for a detailed breakdown of pydepgate's expected threat model.

## Install

```bash
pip install pydepgate
```

Requires Python 3.11 or later. pydepgate has no third-party runtime dependencies.

## Quick start

```bash
pydepgate scan some-package-1.0.0-py3-none-any.whl
pydepgate scan some-package-1.0.0.tar.gz
pydepgate scan litellm
pydepgate scan --single suspicious_module.py
pydepgate explain DENS010
```

The first two commands scan package artifacts from disk. The third resolves an installed package from the active environment. `--single` scans one file directly. `explain` prints the meaning of a signal or rule.

Exit code `0` means no blocking findings. Exit code `2` means at least one HIGH or CRITICAL finding. The full exit code contract is documented in [docs/reference/exit-codes.md](https://nuclear-treestump.github.io/pydepgate/reference/exit-codes).

## A larger scan

```bash
pydepgate scan --deep suspicious-package.whl \
    --peek \
    --peek-chain \
    --decode-payload-depth=5 \
    --decode-iocs=hashes \
    --format sarif \
    --event-log scan.events.jsonl \
    --min-severity high > findings.sarif
```

That run enables the heavier scan path. It scans ordinary library files, peeks into bounded encoded payloads, and re-scans decoded payloads up to the requested depth.

It writes SARIF to stdout, records scan events as JSONL, emits hash-only IOC records, and exits with code `2` if HIGH or CRITICAL findings are present.

pydepgate does not import, install, execute, compile, or deserialize the package.

## What pydepgate detects

The current scanner has five main analyzer families. Analyzers emit raw signals. The rules engine turns those signals into severity-rated findings based on file kind and context.

### Encoding abuse: ENC001, ENC002

pydepgate detects patterns where encoded content is decoded and executed in one chain, such as:

```python
exec(base64.b64decode(payload))
```

It handles base64, hex, codec-based, zlib, bz2, lzma, and gzip variants. With `--peek`, pydepgate can partially unwrap encoded literals within configured limits. ENC002 fires when the unwrap chain is nested or reaches the configured depth.

### Dynamic execution: DYN001-DYN007

pydepgate flags direct calls to `exec`, `eval`, `compile`, and `__import__`. It also looks for indirect access through `getattr`, `globals()`, `locals()`, `vars()`, `__builtins__`, compile-then-exec patterns, and simple aliases such as:

```python
e = exec
e(payload)
```

### String obfuscation: STR001-STR004

The string analyzer uses a partial evaluator to resolve simple obfuscated strings without running user code. It handles concatenation, character codes, slicing, `str.join`, `bytes.fromhex(...).decode()`, f-string assembly, and single-assignment variables.

The goal is to catch cases where code hides names such as `eval`, `exec`, or dangerous standard-library calls behind string construction.

### Suspicious standard-library usage: STDLIB001-STDLIB003

pydepgate flags standard-library calls that are unusual in startup vectors:

* process spawn through `os.system`, `subprocess.Popen`, `subprocess.run`, or `os.exec*`;
* network access through `urllib.request.urlopen`, `socket.socket`, or `http.client`;
* native code loading through `ctypes.CDLL` or `ctypes.WinDLL`.

The default rules promote these findings heavily when they appear in `setup.py` or `.pth` files.

### Code density: DENS001-DENS051

The density layer looks for patterns common in obfuscated or generated payloads: high-entropy strings, base64-looking literals, machine-generated identifiers, invisible Unicode characters, homoglyphs, disproportionate AST depth, deeply nested lambdas, byte-range integer arrays, high-entropy docstrings, and dynamic `__doc__` references passed to callables.

These signals are calibrated by file kind. A high-entropy base64 literal in a `.pth` file is much more suspicious than the same literal in an ordinary library file.

Complete signal details are in [docs/reference/signals.md](https://nuclear-treestump.github.io/pydepgate/reference/signals).

## Layered detection example

The LiteLLM 1.82.8 `.pth` attack shape can be reduced to a single line:

```python
import base64; exec(base64.b64decode('cHJpbnQoMSkK'))
```

A grep for `exec` catches that example. A grep for `base64.b64decode` catches it too. But single-pattern detection is brittle, so pydepgate fires several independent signals on the same line:

```text
ENC001   decode-then-execute pattern
DYN002   exec() with non-literal argument at module scope
DENS001  token-dense single line
DENS010  high-entropy string literal
DENS011  base64-alphabet string literal
```

The rule layer promotes those findings because the file is a `.pth`.

pydepgate is not evasion-proof, and any tool that claims it is would be lying. The goal is to make simple evasions less useful by layering independent signals around startup behavior.

## What pydepgate does not do

pydepgate is a static triage tool. It does not prove that a package is safe.

It does not execute packages in a sandbox, emulate install-time behavior, prove intent, or replace manual review for high-risk packages. It also does not fully replace `pip-audit`, Safety, Bandit, Semgrep, SBOM tooling, or sandbox detonation. 

Findings should be treated as review signals, CI gates, or evidence for escalation.

## Safe output model

pydepgate is built around a simple constraint: hostile package artifacts should be treated as data, not as code to run.

Package code is not imported, installed, executed, compiled, or deserialized. Payload peek emits bounded previews instead of full payload values. Pickle data is detected but not deserialized. Decompression is bounded by byte budgets. SARIF messages do not include payload bytes. Event logs record scan lifecycle metadata, not decoded payload material. Hash-only IOC mode emits hashes instead of payload contents.

Full decoded payload export is available only through explicit full-mode decode options. The Python API also blocks native scanner internals and decoded trees unless the caller passes explicit unsafe capability tokens.

## Outputs

pydepgate can write human-readable terminal output, JSON, SARIF 2.1.0, hash-only IOC sidecars, JSONL event logs, and local SQLite evidence records.

SARIF output is intended for GitHub Code Scanning and other SARIF consumers. JSON is for automation. Event logs record scan lifecycle events. SQLite evidence storage keeps scan results available after the terminal session is gone.

```bash
pydepgate scan some-package.whl --format sarif > findings.sarif
pydepgate scan some-package.whl --event-log scan.events.jsonl
pydepgate scan some-package.whl --save-to-db
```

Reference docs:

* [Output formats](https://nuclear-treestump.github.io/pydepgate/reference/output-formats)
* [Event log format](https://nuclear-treestump.github.io/pydepgate/reference/event-log)
* [SARIF integration](https://nuclear-treestump.github.io/pydepgate/guides/sarif-integration)

## Database

pydepgate can save scan and CVE results to a local SQLite database.

The database stores scan runs, scanned artifacts, static findings, decoded-payload trees, and CVE findings. It is populated by `pydepgate scan --save-to-db` and `pydepgate cvescan --save-to-db`.

Deleting the database removes saved scan history and evidence records.

```bash
pydepgate db init
pydepgate scan someartifact.tar.gz --save-to-db
pydepgate db query --package someartifact
pydepgate db list-runs
pydepgate db explain --run-id 00000000-0000-0000-0000-000000000
```

`--save-to-db` creates the database if it does not already exist. `db query` searches saved runs by package name. `db explain` prints the findings for a saved run.

See the [Database CLI reference](https://nuclear-treestump.github.io/pydepgate/cli/db) for command details.


## Recursive decode and IOC output

`--decode-payload-depth=N` re-scans decoded payloads. This catches multi-layer shapes where an outer encoded payload decodes to source that contains another encoded payload.

```bash
pydepgate scan --deep some-package.whl --peek \
    --decode-payload-depth=3 \
    --decode-iocs=hashes \
    --decode-location ./forensics
```

With `--decode-iocs=hashes`, pydepgate writes hash-only IOC records. With `--decode-iocs=full`, it writes an encrypted archive of decoded payload material plus a plaintext IOC sidecar.

The default archive password is `infected`, following malware-research convention.

Full reference: [docs/guides/decode-payloads.md](https://nuclear-treestump.github.io/pydepgate/guides/decode-payloads).

## Rules

Analyzers emit signals. Rules decide what those signals mean.

Default rules are built into pydepgate. Users can override or add rules with a `pydepgate.gate` file in TOML or JSON. Auto-discovery checks the project root and the active virtual environment root unless `--rules-file` is provided.

```bash
pydepgate scan some-package.whl --rules-file company-rules.gate
```

Example rule:

```toml
[[rule]]
id = "litellm-pth-stdlib"
signal_id = "STDLIB001"
file_kind = "pth"
action = "set_severity"
severity = "critical"
explain = "subprocess calls in .pth files have no legitimate use case."
```

Supported actions are `set_severity`, `suppress`, and `set_description`. User rules take precedence over default rules. Suppressed findings are tracked separately so users can see what would have fired.

```bash
pydepgate explain STDLIB001
pydepgate explain DENS010
pydepgate explain --rule default_stdlib001_in_pth
pydepgate explain --list
```

Full reference:

* [Rules file reference](https://nuclear-treestump.github.io/pydepgate/reference/rules-file)
* [Custom rules guide](https://nuclear-treestump.github.io/pydepgate/guides/custom-rules)

## Known-vulnerability scan (`cvescan`)

`pydepgate scan` looks for suspicious behavior in the artifact itself. `pydepgate cvescan` checks package identity against a local OSV-backed CVE database.

```bash
pydepgate cvedb update
pydepgate cvescan some-package.whl
pydepgate cvescan --save-to-db some-package.whl
pydepgate cvedb path
```
`cvedb update` refreshes the local OSV-backed database. `cvescan` checks the artifact against that database. `--save-to-db` saves the result to pydepgate's local evidence database.

Use `pydepgate scan` and `pydepgate cvescan` when you want behavior-based scanning and known-vulnerability coverage.

pydepgate's `cvedb` command respects `XDG_CACHE_HOME` and follows the XDG Base Directory Specification.

Further reading:

* [`cvedb` Command](https://nuclear-treestump.github.io/pydepgate/cli/cvedb)
* [`cvescan` Command](https://nuclear-treestump.github.io/pydepgate/cli/cvescan)

## Python API

pydepgate can be used as a local Python library for package-intake tooling, CI helpers, and custom scanners.

```python
import pydepgate.api as pydepgate

result = pydepgate.scan(
    "suspicious-package.whl",
    mode="static",
    deep=True,
    peek=True,
    peek_chain=True,
    decode=True,
    decode_payload_depth=5,
    decode_iocs="hashes",
    event_log="scan.events.jsonl",
    output_format="json",
)

print(result.finding_count)
print(result.iocs)
print([event.event_type for event in result.events])

sarif = result.render(format="sarif")
result.write_iocs("iocs.txt")
result.write_report("findings.json", format="json")
```

The public API exposes summaries, finding records, hash-only IOC records, event data, and rendered reports. It blocks native scanner internals, decoded trees, and payload material unless explicit unsafe capability tokens are used.

```python
native = result.get_native_result(
    unsafe=pydepgate.UNSAFE.ALLOW_NATIVE_RESULT,
)
```

Archive artifacts cannot be scanned as loose files through the public API. For example, `single=True` with a `.whl`, `.zip`, `.tar.gz`, `.tgz`, `.tar.bz2`, or `.tar.xz` target is rejected before scan execution just as it would with the CLI.

API docs:

* [Python API overview](https://nuclear-treestump.github.io/pydepgate/api/)
* [API scan reference](https://nuclear-treestump.github.io/pydepgate/api/scan)
* [API result objects](https://nuclear-treestump.github.io/pydepgate/api/result)
* [API safety model](https://nuclear-treestump.github.io/pydepgate/api/safety)

## Docker

```bash
docker pull ghcr.io/nuclear-treestump/pydepgate:latest
docker pull ghcr.io/nuclear-treestump/pydepgate:0.X.Y
docker pull ghcr.io/nuclear-treestump/pydepgate:0.X
```

The official image is published for `linux/amd64` and `linux/arm64`. For CI and package-intake workflows, pin by digest instead of relying on a mutable tag.

From 0.5.0 onward, container releases are signed by digest and GitHub-attested. Builds include BuildKit provenance and SBOM attestations, use verified PyPI wheel inputs, and are reproducible for supported platforms.

Container tags, digests, verification commands, runtime properties, and local invocation patterns are documented in the [Docker image guide](https://nuclear-treestump.github.io/pydepgate/guides/docker-image).

## Where pydepgate fits

| Tool type           | Main question                                        | pydepgate's role                                                                                     |
| ------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `pip-audit`, Safety | Is this known version vulnerable?                    | pydepgate looks for suspicious behavior in the artifact itself.                                      |
| Bandit              | Does this source tree contain risky Python patterns? | pydepgate focuses on package startup vectors, encoded payloads, and adversarial artifact shapes.     |
| Semgrep             | Does code match configured rules?                    | pydepgate ships package-aware analyzers, a rule layer, decoded-payload scanning, and report outputs. |
| Sandbox detonation  | What happens if this runs?                           | pydepgate is static and does not execute package code.                                               |

## Current status

The static scanner is usable today. It scans wheels, sdists, installed packages, package-like trees, and loose files. The current analyzer set covers encoding abuse, dynamic execution, string obfuscation, suspicious standard-library usage, and code-density signals.

The CLI supports human-readable output, JSON, SARIF 2.1.0, custom rules, recursive decoded-payload scanning, payload peek, IOC sidecars, event logs, SQLite evidence storage, pre-commit hooks, shell completion, and Docker images.

The Python API supports local static scans with guarded access to native internals and decoded payload material. 

## In progress

ROADMAP.md is the best place to look for project direction.

The next major work block is the policy engine. Longer-term work includes guarded install flows, repository policy files, runtime interdiction, and the planned `workplan` and `warehouse` components.

Future API work will add a Context object for callers that need more control over scan configuration and policy state.

## Design constraints

pydepgate has no third-party runtime dependencies. 

Parsers and analyzers do not execute, compile, deserialize, or import input content. The partial evaluator reimplements only the operations it needs on values it produced itself.

Normal output paths avoid payload material. Bounded previews are allowed when requested. Full decoded payload values require explicit full-mode export.

Scan execution can emit JSONL event records for scan start, completion, failure, decode work, and evidence writes. Event payloads are JSON-safe and reject raw bytes, cyclic structures, NaN, infinity, and non-string mapping keys before emission. More events will be added as the API develops.

Static scans run under local scan tickets that record run identity, correlation identity, target identity, allowed actions, budgets, fingerprints, and invocation evidence. These tickets are local and unsigned today. 

Container releases should be verified by digest rather than by mutable tag alone. From 0.5.0 onward, the Docker container publishing workflow has been significantly hardened. See [Docker Image: Release Integrity](https://nuclear-treestump.github.io/pydepgate/guides/docker-image.html#release-integrity) for further details.

## Architecture

pydepgate is organized as a layered static-analysis pipeline. It breaks package artifacts into structured inputs, analyzes the parts in context, and turns raw signals into findings.

Parsers turn package contents into structured representations. Artifact enumeration decides which files are in scope. Analyzers walk parsed representations and emit `Signal` objects. The rules engine turns signals into `Finding` objects. Reporters render findings as human text, JSON, or SARIF.

Analyzers do not see raw bytes directly. They operate on parser output and shared AST utilities. The `_resolver.py` module is used by analyzers that need partial expression evaluation. It returns structured `ResolutionResult` objects with success/failure status, operation counts, partial values, and resolved fragments.

The static engine exposes three main single-file entry points. `scan_file(path)` reads bytes and routes by filename. `scan_bytes(content, internal_path, ...)` is used by wheel, sdist, and installed-package enumeration. `scan_loose_file_as(path, file_kind)` forces a file kind and is used by `pydepgate scan --single`.

The event-handling path adds a shared scanner runner, local scan tickets, structured event envelopes, memory and JSONL event sinks, and the public Python API.

## Development

```bash
git clone https://github.com/nuclear-treestump/pydepgate
cd pydepgate
pip install -e .
python -m unittest discover tests -v
```

The test suite has grown to roughly 1800 tests. Coverage includes analyzer behavior, evasion cases, false-positive cases, adversarial parser inputs, synthetic wheels and sdists, CLI subprocess tests, event-system tests, API-safety tests, runner-contract tests, random-byte parser hardening, and reporter leakage tests.

To regenerate the binary `.pth` fixtures after editing them:

```bash
python scripts/generate_fixtures.py
```

Contributors should read [CONTRIBUTING.md](CONTRIBUTING.md) before opening large PRs.

## Safety notes

The test fixtures in `tests/fixtures/` and the synthetic samples used in integration tests model the structure of known attacks, including LiteLLM 1.82.8 and Trojan Source CVE-2021-42574. They contain inert payloads only. No actual malicious code is present in this repository.

For regression testing against real malicious samples, use disposable VMs or containers. Do not commit malicious samples to this repository.

Possible datasets:

* [OSSF malicious-packages](https://github.com/ossf/malicious-packages)
* [Datadog malicious-software-packages-dataset](https://github.com/DataDog/malicious-software-packages-dataset)
* [lxyeternal/pypi_malregistry](https://github.com/lxyeternal/pypi_malregistry)

## Known limitations

pydepgate is static analysis. It has known gaps.

Current analysis gaps include function return tracking, `__builtins__` as a Name subscript, tuple unpacking, augmented assignment, conditional assignments in resolver variable tracking, lambda scope precision, and aliased standard-library imports such as:

```python
from subprocess import Popen as P
```

Some density-layer signals can fire on legitimate generated code. `DENS020` and `DENS040` can appear in Cython output, parser tables, and generated configuration. `DENS031` can fire on legitimate non-English variable names in non-Latin codebases. These are intentionally lower severity outside startup vectors so they can act as contributing signals instead of standalone alerts.

Scan tickets are local and unsigned in the current release. They provide execution structure and provenance, not remote trust.

The policy engine has not shipped yet. Event logs and API results can support policy decisions, but they do not currently enforce allow, warn, quarantine, or reject decisions.

## Documentation

Start here:

* [Getting started](https://nuclear-treestump.github.io/pydepgate/index)
* [CLI reference](https://nuclear-treestump.github.io/pydepgate/cli/index)
* [Python API](https://nuclear-treestump.github.io/pydepgate/api/)
* [Signals reference](https://nuclear-treestump.github.io/pydepgate/reference/signals)
* [Rules file reference](https://nuclear-treestump.github.io/pydepgate/reference/rules-file)
* [CI integration guide](https://nuclear-treestump.github.io/pydepgate/guides/ci-integration)
* [Decode payloads guide](https://nuclear-treestump.github.io/pydepgate/guides/decode-payloads)
* [Docker image guide](https://nuclear-treestump.github.io/pydepgate/guides/docker-image)

## Project independence

pydepgate is maintained as an independent public defensive tool. It is not controlled by a vendor, employer, or private customer roadmap. This project will not be sold, transferred to a corporation, or made part of any employment or work agreement that could capture or stifle it. 

If a time comes when development by the current maintainer is no longer possible, the maintainer commits to finding a successor who will be held to the same conditions. If no such successor can be found, the project will be archived rather than placed under corporate control.

Long-form funding and independence notes are in [FUNDING.md](FUNDING.md).

## Author

Ikari ([@0xIkari](https://github.com/0xIkari))

Security engineering contact: [ikari@nuclear-treestump.com](mailto:ikari@nuclear-treestump.com)

## License

Apache 2.0. See [LICENSE](LICENSE).
