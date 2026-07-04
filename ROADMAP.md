# pydepgate roadmap

This document describes the forward trajectory of pydepgate. For what has
already shipped, see [CHANGELOG.md](CHANGELOG.md).

The version numbers below are targets, not commitments. Some items
depend on others being completed first. Beyond that, the project has a
demonstrated pattern of shipping work earlier than planned. Treat this
roadmap as the general shape of where the project is going, not as a
schedule.

## Current Version: 0.7.0

## About this rewrite

This is the third major revision of the roadmap.

The first version was written before any code existed. It described a
five-version build plan with phase boundaries and acceptance criteria.
Execution outpaced it within weeks.

The second version caught up to reality on scope but used patch-level
bumps for several core capability releases, which produced a versioning
calibration problem that compounded over a stretch of releases.

A third internal draft sequenced the work as foundation-first: evidence
database, then citation and validation, then policy, then comparison,
then Burn Notice, then dependency resolution and the visible products
that depend on it. That draft was also outpaced before being committed
to the repository. Dependency resolution shipped at v0.4.7, which was
the v0.10.0 slot in the third draft. The API surface refactor surfaced
as a near-term priority through real prototyping work and was committed
to publicly before this revision was written.

This version of the roadmap reflects what has actually shipped and the
current planning order, including the doctor and preflight release that
ships before the daemon, the reframed SIEM story as a generic emit
mechanism on the daemon, and the explicit MUST SHIP pins on three
items that are not deferrable beyond their slot.

The pattern of roadmaps being outpaced by execution is likely to
continue. Future revisions of this document should be expected.

## State at v0.4.7 (at the time of the creation of this new ROADMAP)

The static analysis pipeline handles wheels, sdists, installed packages,
loose source files, and package-like trees. It performs recursive
payload decoding, payload peek, deep mode, JSON output, human output,
SARIF 2.1.0, and process-pool parallelism.

The analyzer stack covers density signals, dynamic execution detection,
encoding-abuse detection, suspicious stdlib usage, string and
obfuscation analysis, enrichment, and a safe partial resolver.

The reporting stack includes human output, JSON, SARIF, decoded tree
reports, IOC material, and explanatory output.

The CVE database subsystem downloads and imports OSV PyPI vulnerability
data into a local SQLite database. The `cvescan` command scans a
wheel's package identity against that database using metadata
extraction, PEP 440 range evaluation, and unevaluated-range evidence.

Dependency resolution is available as infrastructure, exposing direct,
first-level, and transitive dependencies. The resolver is not yet wired
into the scan command surface. Wiring it is part of the work block
described below.

## Versioning policy

Patch releases are for bug fixes, doc polish, rule tuning, and narrow
compatibility changes. Minor releases are for new scanner subsystems,
new commands, new schemas, new storage layers, new policy surfaces, or
new engine-level behavior.

Pre-1.0 versions reserve the right to make breaking changes to the
public API surface (CLI flags, JSON schema, SARIF schema, exit codes,
rule schema) within minor version bumps. After 1.0, breaking changes
go through a formal deprecation cycle.

Released tags from v0.4.1 onward are immutable. When released behavior
needs to change, the change ships as a new version with a changelog
explaining what happened.

## Already shipped

This section catalogs what has landed, with parentheticals on items
that shipped at a version different from any prior planned slot.

### v0.3.0 and earlier

- [x] Static analysis pipeline for wheels, sdists, installed packages,
      and loose source files
- [x] Four production analyzers: `encoding_abuse`, `dynamic_execution`,
      `string_ops`, `suspicious_stdlib`
- [x] Rules engine with TOML and JSON support, predicate operators,
      typo suggestions, severity rewriting, suppression behavior
- [x] Safe partial evaluator for string and expression resolution
      without executing user code
- [x] Three output formats: human-readable terminal, JSON, SARIF
      (initial stub)
- [x] Recursive payload decoder with multi-layer chain reconstruction
      (not in any prior roadmap)
- [x] Density analyzer with 32 rules covering DENS001-051 (not in any
      prior roadmap)
- [x] Encrypted archive output for decoded payloads
- [x] Pre-commit hook configuration
- [x] IOC sidecar format
- [x] Artifact-level and file-level provenance hashes (SHA256, SHA512)
- [x] Tristate `--decode-iocs` flag
- [x] PEM and DER classification (shipped v0.3.2, not in any prior
      roadmap)

### v0.4.0

- [x] SARIF 2.1.0 output with full rules catalog (planned v1.0.0 in
      first roadmap, shipped v0.4.0)
- [x] Decoded-payload codeFlows in SARIF
- [x] `--sarif-srcroot` flag and `PYDEPGATE_SARIF_SRCROOT` environment
      variable
- [x] Content-blind SARIF emission
- [x] SARIF validation CI workflow against the Microsoft SARIF
      Multitool

### v0.4.2

- [x] OSV PyPI CVE database subsystem with download, streaming parse,
      atomic SQLite writes (not in any prior roadmap)
- [x] `pydepgate cvedb` command surface (`update`, `status`, `path`)
- [x] OSV ranges as first-class data with state machine parsing
- [x] Structural ALL-versions detection with sentinel fast-path
- [x] Run UUID tracking in cvedb metadata
- [x] Three-phase import progress bars (read, parse, write)

### v0.4.5

- [x] Engine parallelism with process-pool execution
- [x] `--workers` and `--force-parallel` CLI flags
- [x] `ScanResult.scan_id` field with cross-report correlation
- [x] Picklability contract tests
- [x] DENS051 emission gated by docstring content classification
- [x] Density analyzer signal weight calibration against 137-package
      real-world corpus

### v0.4.6

- [x] Package metadata extraction module for wheels (not in any prior
      roadmap)
- [x] CVE database lookup layer with normalized package-name matching
- [x] Private PEP 440 version helper (stdlib-only, conservative
      comparison)
- [x] Package-level CVE scanner package
- [x] `pydepgate cvescan` CLI command
- [x] OSV `ECOSYSTEM` range evaluation for CVE scanning

### v0.4.7

- [x] Dependency resolution including first-level and transitive
      discovery (planned v0.10.0 in third roadmap draft, shipped
      v0.4.7)
- [x] UUIDv7 migration from UUID4 for run and correlation identifiers
      (stdlib-only implementation)
- [x] `pydepgate.run_context` module with thread-safe lazy generation
      and daemon-mode reset support

### v0.5.0: Local evidence database

Memory layer for findings, scans, decoded trees, and CVE results.
Foundation for citation, validation, false-positive memory, daemon,
and runtime miss reports.

- [x] Local pydepgate SQLite database, separate from the OSV CVE DB
- [x] Schema versioning with migration framework
- [x] Storage tables for scan runs, scanned artifacts, file identities
      and internal paths, static findings, decoded tree nodes, and CVE
      scan runs and findings
- ~~[ ] Stable finding fingerprint v1 specification document~~ - Moved to v0.7.0
- [x] `pydepgate scan --save-to-db` and `pydepgate cvescan --save-to-db`
- [x] `pydepgate db path`, `db status`, `db list-runs`,
      `db query --package`, `db query --artifact-sha512`,
      `db explain --run-id`
- [x] Producer ID field on every stored finding (for daemon
      forensics later)
- [x] Tests covering schema creation, schema mismatch, stored findings,
      stored CVE findings, decoded nodes, and DB explain behavior

### v0.6.0

Evented scan execution, public API foundation, safe result surfaces,
and adversarial hardening discovered while preparing the next work
block. This release changed the scan path from a CLI-owned report
operation into an authorized, correlated, evented execution lifecycle
that can be reused by API consumers and future daemon/policy work.

- [x] `pydepgate.events` package with immutable `EventEnvelope`,
      JSON-safe serialization, deep-freezing helpers, stable payload
      digests, and strict event-type prefix validation
- [x] `EventEmitter` and memory, JSONL, tee, and null event sinks
- [x] `ScanGrantingTicket` model for local grant-bound scan execution,
      including run/correlation IDs, ticket IDs, ticket digests,
      target identity, allowed actions, budgets, ruleset fingerprints,
      and local invocation evidence
- [x] CLI `--event-log` flag and `PYDEPGATE_EVENT_LOG` environment
      variable for scan lifecycle JSONL output
- [x] Static scan runner split from CLI rendering so the CLI, public
      API, and future daemon paths can execute the same scanner path
      without shelling out or reaching into argparse internals
- [x] Contextless public `pydepgate.api.scan()` entry point for static
      scans over wheels, sdists, installed packages, and loose files
- [x] Safe `ScanApiResult` surface with compact summaries, blocked
      native internals, safe finding records, hash-only IOC records,
      event access, reporter reuse, report writing, and IOC sidecar
      export
- [x] `pydepgate.api.UNSAFE` capability tokens for deliberate native
      result access, decoded-tree access, and full payload archive
      export
- [x] Hashes/full IOC mode boundary: `decode_iocs="hashes"` exposes
      hash IOC evidence without retaining decoded source, while full
      payload material remains gated behind `decode_iocs="full"` and
      explicit unsafe export
- [x] Archive-as-single guardrails preventing `.whl`, `.zip`, `.tar`,
      `.tar.gz`, `.tgz`, `.tar.bz2`, and `.tar.xz` artifacts from
      being scanned through the loose-file API path
- [x] API rendering through the existing human/text, JSON, and SARIF
      reporters instead of an API-specific renderer stack
- [x] Decode completion events with tree availability, root node
      count, total node count, IOC count, and IOC mode
- [x] Adversarial event tests for payload safety, immutability,
      deterministic serialization, sink failures, parent-event chains,
      scan failure events, decode failure events, and ticket
      correlation
- [x] Public API tests for validation, unsafe access gates, result repr
      safety, safe finding sanitization, hash-only IOC exposure,
      renderer integration, report writing, archive guardrails, and
      payload archive restrictions
- [x] Parser hardening for arbitrary hostile byte streams, including
      CPython tokenizer/parser `SystemError` handling and deterministic
      random-byte regression coverage

### v0.7.0
- [x] `pydepgate doctor` command with checks for installation
      integrity, configuration validity, CVE database status, schema
      version, and rule-set consistency
- [x] Structured output suitable for support bundles and CI gates
- [x] Tests for each diagnostic check

## New Identified Work

The items below were not part of the original version ladder. They were
heavy-lift work discovered during implementation that had to land before
the next major work group could be safely built on top of pydepgate.

- Static scan execution had to be split out of the CLI before the API,
  daemon, policy layer, and future warehouse paths could share one scan
  implementation.
- Scan lifecycle events had to exist before daemon emission, evidence
  correlation, policy verdicts, and downstream consumers could reason
  about what happened during a run.
- Local Scan Granting Tickets had to exist before policy, daemon, and
  future tool delegation could be expressed as authorized work instead
  of loose function calls.
- The public Python API had to exist before pydepgate could be treated
  as a library by package-intake tooling and later context/workplan
  surfaces.
- Public API result safety had to be designed before decoded payloads,
  IOCs, native results, and reporter output could be exposed without
  turning pydepgate into a payload vending machine.
- Payload IOC mode semantics had to be tightened so hash mode produces
  hash evidence only and full decoded source stays behind explicit full
  mode plus unsafe export.
- Archive-as-single guardrails had to be added after API testing showed
  that a wheel could otherwise be misclassified as a loose source file.
- Event handling needed adversarial tests for immutability, JSON safety,
  sink failure, failure-event emission, and parent-chain correctness
  before it could become trusted release infrastructure.
- API renderer reuse had to be wired through the existing reporter stack
  so CLI and API consumers do not drift into separate output dialects.
- Parser random-byte hardening had to be added after fuzz-style tests
  exposed CPython tokenizer/parser `SystemError` paths on hostile byte
  streams.

# Current work block

The remaining items below describe the visible planning horizon. The
order reflects dependency relationships and priority commitments. Three
items are marked MUST SHIP, meaning they are priority pins within the
work block and should land as early as the dependency order allows.

The v0.6.0 event/API foundation shipped earlier than the policy engine
slot it displaced. The policy layer now starts the remaining work block
because the evented runner and safe API surface give it a cleaner place
to attach.

### v0.8.0: Policy engine

Internal policy layer that severity-rewrites findings, applies rule
precedence, detects conflicts with the builtin baseline, and surfaces
`AppliedPolicyResult` to consumers. This is the engine. The repo-side
policy file (`PYDEPPOLICY.md`) ships separately at v0.16.0.

- [ ] `AppliedPolicyResult` data model
- [ ] Severity rewriting pipeline with rule precedence
- [ ] Builtin baseline conflict detection
- [ ] Wiring into static scan and CVE scan result paths
- [ ] Tests for policy parsing, invalid policy, baseline conflict, and
      policy-result serialization

This was the original v0.6.0 slot. It moves here because v0.6.0
shipped the evented scan and public API foundation that policy depends
on.

### v0.9.0: Cite and validate-finding

Citation generation and finding validation against the evidence
database. Findings become portable artifacts that can be filed in
issues, security advisories, and CI failures.

- [ ] Stable finding fingerprint v1 specification document
- [ ] `pydepgate validate-finding ARTIFACT FINDING` supporting static
      finding fingerprints, CVE finding fingerprints, and decoded node
      fingerprints
- [ ] `pydepgate cite` with modes for maintainer issues, false-positive
      submissions, security advisory evidence, and CI failures
- [ ] Tests that validation remains stable across renderer changes

### ~~v0.9.0~~: pydepgate doctor - Shipped in v0.7.0 

Diagnostic command for pydepgate installation, configuration, CVE
database state, and any other tool-state surface that operators need
to verify before relying on scan output. Doctor answers the question
"is pydepgate set up to do its job correctly." It does not scan
packages or inspect the running interpreter.

- [x] `pydepgate doctor` command with checks for installation
      integrity, configuration validity, CVE database status, schema
      version, and rule-set consistency
- [x] Structured output suitable for support bundles and CI gates
- [x] Tests for each diagnostic check

### v0.10.0: pydepgate preflight

Live-system scanner for the running Python environment. Preflight
inspects the active interpreter, installed packages, `sitecustomize`,
`usercustomize`, `.pth` files in `site-packages`, and the other
startup-vector surfaces present on the system to confirm the
environment has not been compromised. Where `pydepgate scan` operates
on artifacts before they enter the environment, preflight operates on
the environment after entry. Both share the analyzer set; the entry
point and target enumeration differ.

- [ ] `pydepgate preflight` command for environment-walking scan
- [ ] Enumeration of the active interpreter's site-packages,
      sitecustomize, usercustomize, and `.pth` files
- [ ] Read-only handling of system surfaces with explicit
      non-modification guarantees
- [ ] Output formats matching `pydepgate scan` (human, JSON, SARIF)
- [ ] Exit-code semantics matching `pydepgate scan`
- [ ] Tests for clean and compromised fixture environments

### v0.11.0: Daemon (pydepgate-d) with --emit

Mirror and intake gate, with a generic emission mechanism for
forwarding events to external consumers. The emit mechanism replaces
the original vendor-specific SIEM integration plan. Vendor-specific
integrations can be added later if demand warrants them; in the
meantime, ndjson or json over a configured endpoint is sufficient for
any SIEM-shaped consumer to ingest pydepgate output.

- [ ] Intake directory watcher or configurable artifact source
- [ ] Scan, CVE scan, policy application, and evidence write for
      every new artifact
- [ ] `--emit ndjson|json` flag with configurable endpoint target
- [ ] Allow, warn, quarantine, and reject actions
- [ ] Health and status output
- [ ] Worker parallelism
- [ ] Container image
- [ ] Tests for intake, quarantine, event output, and policy behavior

### v0.12.0: Shape skeleton **MUST SHIP**

Structural skeleton analyzer for adversarial-shape detection. Lives
in `pydepgate/analyzers/closet/`. Detects behavioral skeletons
(call-and-constant patterns, AST-shape fingerprints) that match
across surface-different malware samples.

- [ ] Skeleton extraction primitive
- [ ] Comparison primitive for matching candidate skeletons against
      known-bad shapes
- [ ] Tests against curated malware corpus

### v0.13.0: Credential-exfil detection **MUST SHIP**

Detection of credential-harvesting attack patterns. Covers sensitive
directory enumeration, credential-format regex compilation, SSL
verification disabled, external config fetch, and value truncation
before exfiltration. Cluster-pattern correlation across the new
signals so individually-low-confidence signals stack into
high-confidence findings. This does not use regex alone, regex is utilized against AST output.

- [ ] Sensitive-directory enumeration detection
- [ ] Credential-pattern regex detection (label-based and
      content-based)
- [ ] SSL verification disabled detection
- [ ] External config-fetch pattern detection
- [ ] Value-truncation-before-network-send detection
- [ ] Cluster correlation across credential-exfil signals
- [ ] Tests against TrapDoor campaign samples and similar shapes

### v0.14.0: False positive detection and downgrade

Known false-positive table with hash-bound records, distributed as a
signed artifact. Reviewed findings are downgraded to LOW with
provenance rather than suppressed.

- [ ] False-positive table schema and storage
- [ ] Immutable, hash-bound FP records with sequence numbers and
      sortable IDs
- [ ] Strong-match (artifact plus file) downgrade to LOW
- [ ] Weak-match (file plus name plus version) annotation without
      severity change
- [ ] FP intake process documentation
- [ ] Tests for FP application, weak-match annotation, and signature
      validation

### v0.15.0: Install gate and SBOM emission **MUST SHIP**

Inspect-before-install command that uses the dependency resolver from
v0.4.7 to download artifacts, scan them, apply policy, and only hand
off to pip when policy permits. SBOM emission lands here as a
byproduct of the resolution graph. Both CycloneDX and SPDX formats.

- [ ] Wire dependency resolver into scan pipeline
- [ ] Guarded install command
- [ ] Artifact download into a controlled wheelhouse
- [ ] Resolution, then scan of every resolved artifact, then CVE scan
      of every resolved artifact
- [ ] Policy application across the resolved set
- [ ] CycloneDX SBOM emission
- [ ] SPDX SBOM emission
- [ ] Stop condition on blocking findings
- [ ] Hand-off to pip only after policy permits it
- [ ] Tests for block, warn, report-only, and clean install paths

### v0.16.0: Repo policy layer (PYDEPPOLICY.md)

Repository-side policy declaration file. Human-readable Markdown with
an armored machine-readable section. Consumed by the policy engine
from v0.7.0.

- [ ] `PYDEPPOLICY.md` parser
- [ ] `pydepgate.findings-policy.v1` schema definition
- [ ] Support for package identity expectations, canonical repository
      expectations, startup-vector expectations, SBOM expectations,
      and known false-positive references
- [ ] `pydepgate policy inspect PYDEPPOLICY.md`
- [ ] Tests for policy parsing, invalid policy, and baseline conflict

### v0.17.0: Repo comparison

Artifact-versus-repository claim comparison. Detects contradiction
clusters where multiple low-confidence signals (name similarity,
owner similarity, non-fork status, metadata disagreement, startup
vector presence) stack into a clear typosquat or impersonation
signal.

- [ ] `pydepgate compare ARTIFACT --github URL`
- [ ] Wheel metadata to repository metadata comparison
- [ ] License expression versus LICENSE file comparison
- [ ] Source layout versus artifact layout comparison
- [ ] Requirements files versus build metadata comparison
- [ ] Critical-path package registry with visual-similarity and
      edit-distance checks
- [ ] Fork-status checks via GitHub metadata
- [ ] Cluster correlation findings that escalate severity when
      multiple signals point the same direction
- [ ] Tests for benign mismatch, typosquat-style mismatch, and
      critical-path impersonation

### v0.18.0: Full API refactor and stability

Full refactor of the library and CLI boundary. The library serves the
CLI, not the other way around. Downstream consumers can integrate
against a stable API surface without reaching into CLI modules. The
v0.6.0 release shipped the static scan slice early; this slot completes
that direction across the remaining scan families and long-lived
consumer contracts.

- [x] Static scan execution boundary clarified: the CLI and public API
      now share the static runner instead of the CLI owning scan
      execution
- [x] Contextless static scan public API documented and tested
- [x] API safety contracts and unsafe capability gates documented and
      tested for the static scan slice
- [ ] CVE scan, evidence write, policy application, daemon, and future
      tool execution boundaries clarified through the same API layer
- [ ] Public API versioning and deprecation policy for pre-1.0
      consumers
- [ ] Full API stability tests across all exposed scan families

### After v0.18.0: Roadmap refresh

The current work block is reassessed. Items that shipped early or
slipped, items that emerged from real usage and were not anticipated,
and items from the next work block (below) get reconciled into the
plan that follows.

## Next work block

These items are planned but not dated. They sit past the current
visible planning horizon and will be slotted into versions during the
roadmap refresh that follows v0.18.0.

- **Burn Notice.** Signed dead-data emergency intelligence feed for
  burning known malicious artifacts, files, decoded payloads,
  structural skeletons, transform chains, or package-and-version
  pairs while a permanent detector is being prepared in code. Canonical
  command `pydepgate burnnotice update` with `lightning` and `maldex`
  as accepted aliases. Burn Notices expire by next minor version
  unless explicitly extended, and become incorporated as code-level
  detections in the release that succeeds them.
- **Runtime tripwire.** Behavior monitoring with isolated execution,
  audit hooks, policy interdiction, and runtime miss reporting. Every
  miss feeds back into the static layer as a future detection.
- **Explorer.** Bulk observation layer for turning many local scan
  runs into threat intelligence. NDJSON and SQLite snapshot exports.
  No telemetry by default.
- **npm and other ecosystems.** Cross-ecosystem expansion. Python
  stays primary until the current work block lands solidly, after
  which the stdlib-only principle gets a per-ecosystem interpretation
  and the rule taxonomy gets a cross-ecosystem mapping.
- **pyc triage layer.** Compiled-bytecode inspection using `dis` and
  `marshal` from stdlib. Header parsing, magic and version
  identification, code object traversal, constant string extraction,
  import and name extraction, suspicious opcode families, and nested
  code object traversal. Full decompilation back to source is not
  in scope; structural triage is.

## Deferred or reframed

- **Vendor-specific SIEM integrations.** The original plan included
  first-class Splunk, Elastic, Datadog, and Sentinel emission with
  vendor-specific data models. This is replaced by the generic
  `--emit ndjson|json` mechanism on the daemon. The generic emit
  mechanism covers the same functional ground without per-vendor
  integration work and is sufficient for any SIEM-shaped consumer to
  ingest pydepgate output. Vendor-specific integrations can be added
  later if demand warrants the scope.
- **Full pyc decompilation.** A multi-month time sink. The pyc triage
  layer in the next work block covers the high-value subset using
  stdlib primitives. Decompilation back to source is not on the
  near-term roadmap.

## v1.0.0: Stable contracts

1.0.0 is the point where the core public contracts become stable
enough for other tools, repositories, maintainers, and users to depend
on them. The version is reserved for that inflection point. The
specific minor version that precedes 1.0.0 is determined by the
roadmap refresh that follows v0.18.0, not by this document.

What has to be true before 1.0:

- Stable CLI contract for core commands
- Stable JSON schema for static scan output
- Stable JSON schema for CVE scan output
- Stable finding fingerprint schema
- Stable DB schema migration policy
- Stable Burn Notice schema if Burn Notice has landed
- Stable `PYDEPPOLICY.md` schema
- Stable false-positive record format
- Stable exit-code policy
- Stable SARIF behavior for the 1.x line
- Complete rule catalog and signal ID documentation
- Threat model and architecture documentation
- Consumer guide for downstream tools

Acceptance criterion: a downstream tool or maintainer process can
consume pydepgate output, cite findings, validate findings, and apply
policy without chasing schema drift release to release.

## Principles

These are the constraints decisions get measured against.

**Standard library only at runtime.** Every runtime dependency would
become part of pydepgate's own supply chain, which is the thing
pydepgate exists to defend against. Build, test, and CI tooling are
free to use whatever fits. Runtime is not.

**Never execute, import, compile, or deserialize untrusted content.**
The parsers, the partial evaluator, the payload-peek loop, and the
decoder all read content, they do not run it. Pickle is detected,
never loaded. The bounded resolver models a small fixed set of
operations using only Python builtins on values it produced itself.
Anything outside that set is unresolved, never run.

**Content-blind public output.** Reports describe behavior without
re-leaking secrets, URLs, command lines, payload bytes, or decoded
malware into CI logs and public issue trackers. Detailed evidence is
hash-bound, so a defender can publish a report without publishing the
attack content.

**Evidence over claims.** Findings carry enough evidence to be
validated independent of the report's prose: artifact hash, file
hash, signal ID, decoded payload hash when relevant, finding
fingerprint, and a validation path. If a finding cannot be cited,
disputed, or independently checked, the design is incomplete.

**Reviewed false positives are downgraded, not erased.** A finding
that was looked at and accepted is qualitatively different from a
finding nobody has seen. Erasure removes useful memory and creates
blind spots. LOW with a known-FP annotation preserves the history.

**Remote intelligence is dead data.** Burn Notices and imported feeds
add known-bad evidence, never executable behavior. They can make
pydepgate stricter. They cannot suppress, downgrade, or allowlist
builtin detections. No remote Python, no remote plugins, no remote
suppression rules, ever.

**Local first.** Normal scanning works without a service account, a
SaaS backend, or any network dependency. Network features are
explicit: CVE DB update, Burn Notice update, custom feed import,
guarded install downloads, or future contribution paths.

**Performance is measured, not asserted.** Large packages and CI
budgets are real constraints. Parallelism, caching, bounded decoding,
and per-mode performance budgets are part of the design, not
afterthoughts. Performance claims need benchmarks behind them.

**Structural detection over rule count.** A feature that catches more
attacks at the cost of being easier to evade is a net loss. The
preferred direction is structural: startup vectors, transform chains,
decoded payload trees, call and constant skeletons, metadata
contradictions, and policy conflicts. The harder an attacker has to
work to hide a pattern, the stronger the signal when the pattern is
visible.
