# Changelog

All notable changes to pydepgate are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Pre-1.0 versions reserve the right to make breaking changes to the
public API surface (CLI flags, JSON schema, exit codes) within minor
version bumps. After 1.0, the contracts in [CONTRIBUTING.md](CONTRIBUTING.md)
become binding stability promises with formal deprecation cycles.

## [Unreleased]

(no changes yet)

## [0.7.0] - 2026-07-03

### Added

- Added `pydepgate doctor` command

### Changed

- Updated API to expose doctor commands
- Updated CLI to use doctor commands


## [0.6.1] - 2026-06-20

### Added

- Wired CVE scanning to use SGTs
- Added event log support to CVE scanning

### Changed

- Added `scan_mode`, `target_kind`, `target_identity`, `target_ref`, and
  `result_kind` metadata to relevant internal scanner events to support
  downstream evidence correlation and future combined reporting.

## [0.6.0] - 2026-06-14

### Added

- **Evented scan execution.** Static scan runs now produce a structured
  event lifecycle in addition to normal report output. The scan path
  emits grant, engine, scan, decode, evidence, completion, and failure
  events as immutable envelopes with run identifiers, correlation
  identifiers, optional parent event identifiers, ticket identifiers,
  severity, payload schema labels, and stable payload digests. This
  turns a scan from a one-shot report into a machine-readable lifecycle
  that downstream tools can inspect, correlate, and archive.

- **`--event-log PATH` for `pydepgate scan`.** Static scans can now
  append JSONL event envelopes to a caller-selected path. The event log
  is separate from human, JSON, SARIF, decoded-payload, and IOC sidecar
  output. It records scan lifecycle metadata, not payload bytes or
  decoded malware material.

- **`PYDEPGATE_EVENT_LOG` environment variable.** Provides an
  environment-driven default event-log path for scan invocations. The
  CLI flag takes precedence over the environment variable, matching the
  existing configuration convention used by other scan features.

- **`pydepgate.events` package.** New event infrastructure for
  immutable event telemetry. The package includes deep-freezing helpers,
  JSON-safe serialization helpers, `EventEnvelope`, `EventEmitter`, and
  sink implementations for memory, JSONL files, tee fanout, and null
  output. Event payloads are validated as JSON-safe data and rejected
  when they contain unsafe or non-deterministic values such as raw
  bytes, NaN, infinity, cyclic structures, or non-string mapping keys.

- **Scan Granting Tickets.** New `ScanGrantingTicket` model for
  grant-bound scan execution. Tickets carry run and correlation IDs,
  issuer and actor metadata, target identity, target kind, scan mode,
  allowed actions, issue and expiry timestamps, ruleset and policy
  fingerprints, budgets, local invocation evidence, and a stable ticket
  digest. The first implementation is local and unsigned; it exists to
  establish the execution contract that future daemon, policy, and
  warehouse work can harden further.

- **Evented static runner.** Static scan execution now has a reusable
  runner layer separate from CLI rendering. The runner creates the
  engine, dispatches wheel, sdist, installed-package, loose-file, and
  auto-detected targets, performs optional recursive decode, emits
  lifecycle events, and returns a structured outcome to callers. The
  CLI now acts as an adapter over this runner instead of owning the
  scan execution path directly.

- **Public Python API.** New `pydepgate.api` module with a contextless
  `scan()` entry point for static scans. API consumers can scan wheels,
  source distributions, installed packages, and loose files without
  shelling out to the CLI. The API returns a safe `ScanApiResult` with
  summary properties, safe finding records, hash-only IOC records,
  event access, report rendering, report writing, and IOC sidecar
  export.

- **Safe API result surface.** Public API results now block direct
  access to native scanner internals by default. `result.result`,
  `result.outcome`, and `result.decoded_tree` raise API errors instead
  of exposing the native `ScanResult`, runner outcome, or decoded tree
  object graph. Advanced callers must use explicit `UNSAFE` capability
  tokens to access native internals.

- **`pydepgate.api.UNSAFE` capability tokens.** Added explicit unsafe
  access tokens for native result access, decoded tree access, and
  payload archive export. The API does not accept casual boolean
  opt-ins for unsafe material. Callers must pass the exact capability
  token for the unsafe operation they are requesting.

- **Safe public finding records.** API consumers now receive sanitized
  `ScanFinding` records instead of native finding objects. Safe finding
  contexts preserve bounded payload peek and peek-chain preview data
  when requested, but strip full payload values and payload-bearing
  internals such as `_full_value`, `_full_value_truncated`,
  `decoded_source`, raw payload fields, and full DER material.

- **Hash-only IOC records in the API.** API results expose `result.iocs`
  as structured `ScanIOC` records. These include source location,
  signal IDs, severity, decode chain, terminal kind, terminal size,
  indicators, containing-file hashes, original payload hashes, decoded
  payload hashes, and extraction timestamp when available. They do not
  expose decoded source or raw payload bytes.

- **API report rendering and writing.** `ScanApiResult.render()` and
  `ScanApiResult.write_report()` reuse the existing pydepgate reporter
  stack for text/human, JSON, and SARIF output. `human` is accepted as
  an alias for `text`. API output does not maintain a separate renderer
  implementation.

- **API IOC sidecar export.** `ScanApiResult.write_iocs()` writes the
  same hash-oriented IOC sidecar format used by the CLI decode path,
  allowing API consumers to export decoded-payload hash evidence without
  reaching into decoded-tree internals.

- **Unsafe payload archive export for API full mode.** API consumers
  can export the encrypted decoded-payload archive only when the scan
  was run with `decode_iocs="full"` and the caller provides
  `UNSAFE.ALLOW_PAYLOAD_ARCHIVE_EXPORT`. Hashes mode cannot export
  payload archives.

- **API guardrails for archive targets.** The public API rejects
  `single=True` for archive artifacts such as `.whl`, `.zip`, `.tar`,
  `.tar.gz`, `.tgz`, `.tar.bz2`, and `.tar.xz`. Archive artifacts must
  be scanned as artifacts, not as loose source files. The static runner
  also enforces target/ticket consistency as defense in depth.

- **API summary helper.** `ScanApiResult.to_summary()` returns a compact
  JSON-safe summary containing scan mode, target, artifact kind,
  artifact hashes, finding and diagnostic counts, skipped count,
  suppressed count, IOC count, event count, ruleset fingerprint, and
  scan statistics.

- **Event and API documentation.** Added documentation for event logs,
  event envelopes, event lifecycle semantics, event safety boundaries,
  public API usage, safe result surfaces, IOC access, output rendering,
  unsafe capability tokens, and API guardrails.

- **Adversarial event-handling tests.** Added tests for event payload
  safety, immutability, deterministic serialization, sink failure
  behavior, strict versus non-strict sink modes, scan failure event
  emission, decode failure event emission, parent-event chains, ticket
  correlation, and JSONL integrity.

- **Public API tests.** Added unittest coverage for API validation,
  unsafe access gates, result repr safety, safe finding sanitization,
  hash-only IOC exposure, renderer integration, report writing, archive
  guardrails, and payload archive export restrictions.

### Changed

- **Static scan execution is now grant-bound and evented.** The static
  scan path mints a local scan granting ticket, validates scan
  authorization, builds an event emitter, executes through the static
  runner, and emits lifecycle events while preserving existing CLI
  output behavior.

- **CLI scan execution now uses the shared static runner.** The CLI
  remains responsible for argument parsing, rendering, decode side-file
  writing, evidence database writes, and exit-code behavior, but scanner
  execution itself is now reusable by the public API and future daemon
  work.

- **Recursive decode IOC modes are stricter.** `decode_iocs="hashes"`
  computes and exposes hash IOC material without retaining decoded
  source text in the decoded tree. Decoded source retention is reserved
  for `decode_iocs="full"` and unsafe/full-mode export paths.

- **Decode completion events include IOC metadata.** Decode completion
  payloads now report whether a decoded tree was available, the root
  node count, total decoded node count, IOC count, and decode IOC mode.
  Event consumers can tell whether decoded IOC material exists without
  parsing native result objects.

- **Public API output is content-safe by default.** The API preserves
  bounded payload peek previews when explicitly requested, but no longer
  exposes native scanner internals, decoded source, raw payload bytes,
  or full payload values through normal public result access.

- **Result representations are compact.** `ScanApiResult` and
  `StaticScanOutcome` use compact repr behavior so printing a result
  does not dump the full native scan result, decoded tree, event stream,
  or payload-bearing internals.

- **Event sink failures are configurable.** API and runner callers can
  choose strict event sink behavior, where sink errors abort the scan,
  or non-strict behavior, where sink errors are captured as warnings
  and scan execution continues.

### Fixed

- **Archive-as-loose-file API footgun.** The public API no longer allows
  `.whl` and other archive artifacts to be scanned with `single=True`,
  preventing artifact bytes from being misclassified as loose source
  input and producing meaningless density findings.

- **API result object bloat.** Printing API scan results no longer
  expands the entire native result graph, decoded tree, and event list.

- **Payload material leakage through API internals.** Normal public API
  access no longer exposes decoded tree internals or decoded source
  material. Hash IOC mode no longer retains decoded source in the
  decoded tree.

- **Parser robustness for arbitrary random bytes.** The Python source
  parser now treats CPython tokenizer and parser `SystemError` failures
  on malformed byte streams as parse failures rather than tool crashes.
  This closes a rare crash path where `tokenize.tokenize()` on random
  bytes containing NULs could surface an internal `SystemError` after a
  `SyntaxError` had already been set. The parser now returns a
  structured syntax-error result for that input class. Tests were
  changed from nondeterministic `os.urandom()` fuzzing to deterministic
  adversarial byte corpora plus targeted monkeypatch tests for
  `tokenize.detect_encoding`, `tokenize.tokenize`, and `ast.parse`.

- **Event failure path coverage.** Added adversarial tests that force
  scan dispatch failures and verify `internal.scanner.scan_failed` is
  emitted with the correct parent event, severity, exception type, and
  message before the original exception is re-raised.

### Security

No security advisories in this release.

This release hardens pydepgate's own output boundaries. Event logs,
public API summaries, safe finding records, JSON/SARIF render paths,
and hash IOC records are designed to avoid re-publishing payload bytes,
decoded malware source, command lines, URLs, secrets, or native scanner
internals by default. Payload peek continues to provide bounded previews
when explicitly enabled, but full decoded payload material requires
`decode_iocs="full"` and an explicit unsafe export capability.

The new event system validates payloads as JSON-safe data before
emission, rejects non-deterministic and raw-byte payload shapes, freezes
event payloads against mutation, and computes stable payload digests.
These properties make event logs suitable for downstream evidence
handling without turning them into a second payload transport.

The scan granting ticket model is local and unsigned in this release.
It is an execution contract and provenance primitive, not yet a remote
trust boundary. Future daemon, warehouse, and policy work may strengthen
that model with signature, delegation, or remote identity semantics.

The parser robustness fix is a defensive hardening change for hostile
artifact input. It prevents malformed random byte streams from escaping
as interpreter-internal tokenizer exceptions during source parsing and
keeps parser behavior aligned with pydepgate's scan-safety contract:
untrusted content can fail to parse, but it should not crash the tool.



## [0.5.0] - 2026-05-30

### Added

- **Local evidence database (`pdgdb` subsystem).** New persistent
  memory layer for pydepgate scan history. The evidence database
  stores scan runs, scanned artifacts, file identities, static
  findings, decoded payload tree nodes, and CVE findings in a
  local SQLite database under `$XDG_DATA_HOME/pydepgate/pdgdb/evidence.db`.
  The database is distinct from the CVE database managed by
  `pydepgate cvedb`: the CVE database is a derived cache that can
  be rebuilt from upstream OSV data at any time; the evidence
  database contains user-generated scan history and lives under
  the XDG data directory rather than the cache directory to
  reflect that difference in semantics.

- **`pydepgate db` subcommand.** Seven actions for creating,
  inspecting, and querying the evidence database. `db init`
  creates the database at the default XDG path, or reports its
  path and last-modified timestamp if it already exists. `db path`
  prints the database path without requiring the database to
  exist, matching the `cvedb path` convention and enabling
  scripting patterns like `sqlite3 "$(pydepgate db path)"
  ".tables"`. `db status` shows record counts (scan runs,
  scanned artifacts, static findings, decoded nodes, CVE
  findings), schema version, creating pydepgate version, creation
  timestamp, and last-modified timestamp. `db list-runs` lists
  scan runs newest-first with separate static and CVE finding
  counts per run so `scan` and `cvescan` runs are immediately
  distinguishable. `db query --package NAME` queries artifact
  records by package name with optional `--version` filtering;
  name matching is case-insensitive and normalizes hyphens to
  underscores. `db query --artifact-sha512 SHA512` queries by
  artifact content hash. `db explain --run-id UUID` reconstructs
  the full record for a single run including all static findings
  sorted by path and line, decoded nodes with their child findings,
  and CVE findings; `--format json` emits the same data as a
  structured JSON document.

- **`pydepgate scan --save-to-db` flag.** Persists the result of
  a static scan to the evidence database. Writes a scan run
  record, a scanned artifact record with SHA-256, SHA-512, and
  resolved package name and version, a file identity record for
  each distinct file that produced a finding, and a static
  finding record for each active finding. Suppressed findings are
  not stored. When `--decode-payload-depth` is also active,
  decoded payload tree nodes and their child findings are written
  in a second independent transaction after static findings commit;
  a failure writing decoded nodes does not roll back the static
  findings record. DB write failures emit a warning to stderr and
  do not affect the scan exit code, output format, or report
  content.

- **`pydepgate cvescan --save-to-db` flag.** Persists the result
  of a CVE scan to the evidence database. Writes a scan run
  record, a scanned artifact record, a CVE scan run record, and
  a CVE finding record for each matched vulnerability. Artifact
  hashes are computed from the wheel file at write time. Zero-
  finding runs still write the scan run and CVE scan run records
  so the absence of findings is itself a recorded fact. DB write
  failures are non-fatal on the same terms as the static scan
  path.

- **`pydepgate.dbs.pdgdb` package.** Three modules forming the
  pdgdb subsystem. `schema.py` defines the full DDL for ten
  tables (`db_metadata`, `schema_migrations`, `scan_runs`,
  `scanned_artifacts`, `file_identities`, `static_findings`,
  `decoded_nodes`, `decoded_child_findings`, `cve_scan_runs`,
  `cve_findings`) with appropriate indexes and foreign keys,
  plus a connection helper that configures WAL journal mode,
  foreign key enforcement, busy timeout, and the pdgdb
  application ID (`0x70646764`, distinct from the cvedb
  application ID `0x70646763`). `writer.py` provides
  `write_scan_result`, `write_decoded_tree`, and
  `write_cve_scan_result` as the public write API. `reader.py`
  provides `get_db_status`, `list_runs`, `query_by_package`,
  `query_by_artifact_sha512`, and `explain_run` as the public
  read API, with typed row dataclasses for all query results.

- **Schema migration framework.** The evidence database uses an
  in-place migration framework rather than the hard-reject-and-
  rebuild pattern used by the CVE database, because the evidence
  database contains user-generated history that cannot be
  reproduced from upstream data. A `schema_migrations` table
  records applied migration IDs and timestamps. The MIGRATIONS
  registry in `schema.py` is an ordered tuple of
  `(migration_id, sql)` pairs applied inside individual
  transactions on the first write after an upgrade. For schema
  version 1 (this release) the migrations tuple is empty; the
  framework is present so databases created under v0.5.0 can be
  upgraded in place when future versions introduce schema changes.

- **`METADATA_KEY_LAST_MODIFIED` in pdgdb metadata.** The evidence
  database records a `last_modified` ISO 8601 UTC timestamp in
  `db_metadata` that is updated after every successful write.
  `db status` and `db init` both surface this timestamp so
  operators can tell at a glance when the database was last
  touched without querying individual run records.

- **`db` CLI documentation.** New `docs/cli/db.md` covering all
  seven actions, output formats, the evidence database location
  and XDG override, schema versioning and migration behavior,
  and the relationship between `db`, `scan --save-to-db`, and
  `cvescan --save-to-db`.

- **`--save-to-db` documentation additions.** The `scan` and
  `cvescan` CLI reference pages each gain a `--save-to-db` flag
  section describing what is stored, the non-fatal failure
  behavior, and how to inspect stored results with `pydepgate db`.

### Changed

- **`pydepgate db list-runs` shows separate STATIC and CVE
  finding columns.** Rather than a single FINDINGS column that
  would show 0 for `cvescan` runs and 0 CVE findings for `scan`
  runs, the table distinguishes the two finding types. This makes
  runs immediately readable without needing to correlate the CMD
  column against the count.

- **`pydepgate db query` output shows separate static and CVE
  finding counts per artifact row.** Same motivation as the
  `list-runs` change: a cvescan artifact row would otherwise
  appear to have zero findings.

- **`pydepgate db explain` output gains a CVE findings section.**
  For `cvescan` runs, the explain output now shows a CVE findings
  block with severity, canonical ID, match kind, and summary for
  each stored finding. The JSON format includes a `cve_findings`
  array alongside the existing `findings` and `decoded_nodes`
  arrays.

- Moved `src/pydepgate/package_tools/cvedb/*` to `src/pydepgate/dbs/cvedb/*`.

- Deleted no longer relevant information from changelog regarding features from old roadmap.

### Security

No security advisories in this release. The evidence database
processes only pydepgate's own scan output and never executes or
evaluates user-provided content. Payload bytes from decoded trees
are explicitly not written to the database; only structural
metadata (chain, indicators, hashes, stop reason) is stored.
The `METADATA_KEY_LAST_MODIFIED` timestamp and schema migration
framework do not affect the static analysis threat model or the
CVE lookup behavior.

## [0.4.7] - 2026-05-24

### Added

- Added dependency resolution support for package artifacts.
- Added first-level dependency discovery.
- Added transitive dependency discovery, enabling pydepgate to reason over dependency closure rather than only the directly inspected package.

### Changed

- Migrated internal run/correlation identifiers from UUID4 to a stdlib UUID7 implementation, improving temporal ordering and traceability of generated identifiers.

### Security

No security advisories in this release.

This release lays groundwork for future SBOM emission and CVE scanner prestaging. With dependency resolution now available, pydepgate can begin mapping artifacts to their broader dependency graph before deeper vulnerability and policy analysis.

## [0.4.6] - 2026-05-22

### Added

- **Package metadata extraction for artifacts.** New
  `pydepgate.package_tools.metadata` module for reading package
  identity and artifact-level metadata from Python wheels. The
  reader prefers root `.dist-info/METADATA` `Name` and `Version`
  fields, records `.dist-info/WHEEL` values when present, parses
  `direct_url.json` as artifact-declared provenance evidence, and
  falls back to wheel filename identity only when core metadata is
  missing or incomplete. The result objects are frozen and
  pickle-safe so future package-level scanners can reuse the same
  metadata layer without reopening or reinterpreting artifacts.

- **CVE database lookup layer.** New
  `pydepgate.package_tools.cvedb.lookup` module for querying the
  local OSV PyPI SQLite database by package name and version. The
  lookup layer supports exact affected-version rows, the
  importer's `ALL` sentinel, normalized package-name matching, and
  evaluated `ECOSYSTEM` advisory ranges. It returns immutable
  `LookupResult`, `VulnerabilityMatch`, and `UnevaluatedRange`
  records instead of CLI-specific output so scanner, report, and
  future policy code can consume the same query primitive.

- **Private PEP 440 version helper.** New private
  `pydepgate.package_tools.cvedb._pepver` helper for conservative,
  stdlib-only package version comparison. It handles the supported
  PEP 440 shapes needed by OSV ecosystem ranges, including release
  segments, epochs, pre-releases, post releases, dev releases, and
  local versions. Unsupported or unparseable comparisons return
  unknown instead of falling back to string comparison, which avoids
  silent false negatives in range evaluation.

- **Package-level CVE scanner package.** New
  `pydepgate.package_tools.cvescanner` package for scanning a
  package identity against the local CVE database. The scanner
  exposes artifact, metadata, and direct identity entrypoints,
  preserves metadata warnings, returns package-level
  `CveFinding` records, and keeps unevaluated advisory ranges as
  separate evidence rather than pretending they are findings. An
  optional `applied_policy_result` value is accepted and preserved
  on scan results so future policy ingestion can influence the CVE
  scanner without changing the public call shape.

- **`pydepgate cvescan` CLI command.** New standalone CLI command
  for scanning wheel artifacts against the local CVE database. The
  command reads package identity from wheel metadata, queries the
  `cvedb` database, and emits human or JSON output. It supports
  `--db-path`, `--ignore-missing-db`, `--format human|json`,
  `--min-severity`, and `--strict-exit`. The normal
  `pydepgate scan` command is unchanged; `cvescan` is intentionally
  package-level while `scan` remains file and startup-vector
  focused.

- **CVE scanner documentation.** New CLI documentation page for
  `pydepgate cvescan`, covering setup with `pydepgate cvedb
  update`, supported artifacts, human and JSON output, match types,
  unevaluated ranges, flags, exit codes, database behavior, and the
  relationship between `scan` and `cvescan`.

### Changed

- **OSV range rows are now evaluated for CVE scanning.**
  `ECOSYSTEM` rows from the `affected_ranges` table are evaluated
  using the private PEP 440 helper. Supported range outcomes are
  surfaced as `range-fixed`, `range-last-affected`, or `range-open`
  matches. Non-ecosystem ranges such as `GIT` ranges are preserved
  as unevaluated advisory evidence with an explicit reason instead
  of being compared against Python package versions.

- **`cvedb` package exports lookup shims.** The
  `pydepgate.package_tools.cvedb` package now exposes
  `lookup_package()` and `lookup_package_in_db()` as public shims
  over the storage-focused lookup module. This gives callers a
  stable import point without moving scanner policy or CLI behavior
  into the database package.

### Security

No security advisories in this release.

This release adds a package-level known-vulnerability scanner. It
does not change the existing static file-analysis threat model or
make `pydepgate scan` perform CVE lookups implicitly. CVE data is
read from the local OSV-derived SQLite database and processed as
data only. Unsupported advisory range types, including Git commit
ranges, are not coerced into Python version comparisons.

The new scanner was exercised against 200 random packages chosen
from affected entries in the OSV DB and correctly reports 
exact-version malware records, fixed-bound vulnerability ranges,
 and last-affected malicious package ranges from the OSV PyPI dataset.

## [0.4.5] - 2026-05-17
 
### Added
 
- **Engine parallelism.** The static engine now supports running
  per-file analysis in a process pool. The `StaticEngine`
  constructor accepts a `workers` parameter (positive integer
  or `None` for serial) and a `parallel_threshold` parameter
  (file count below which parallel is suppressed even when
  workers is greater than one, default 1000). The pool primitive
  is `ProcessPoolExecutor` with a worker initializer that pickles
  the engine once per worker rather than once per task. The
  picklability contract documented in CONTRIBUTING.md is
  preserved; `FileScanInput`, `FileScanOutput`, and all default
  analyzers continue to round-trip through pickle cleanly.
  Default behavior is unchanged: serial execution when workers
  is None, automatic fallback to serial when the in-scope file
  count is below the threshold. Parallelism pays off when
  per-file work is large enough to amortize the
  ProcessPoolExecutor startup cost (roughly 200 to 400
  milliseconds per pool). In benchmark runs across 137 real
  PyPI packages with warm caches, non-deep mode is fastest in
  serial at 29.7 seconds; parallel with workers=4 ran 31.9
  seconds with the threshold gate engaged and 37.9 seconds with
  `--force-parallel` enabled, because pool startup dominates the
  small-file workload typical of non-deep scans. Deep mode is
  the opposite story: workers=4 on a 4-core runner ran 59.5
  seconds versus 79.4 seconds serial, a 25 percent improvement,
  and the gate is the right default for most operators because
  it preserves the serial speed advantage on small inputs while
  unlocking parallel speedup on large ones.
- **`--workers` CLI flag and `PYDEPGATE_WORKERS` environment
  variable.** Accepts an integer worker count or
  the string `auto`. The auto path uses
  `os.sched_getaffinity(0)` on Linux for cgroup awareness,
  falling back to `os.cpu_count()` elsewhere. When the resolved
  count exceeds 2x the available CPU count, the CLI emits a
  thrashing warning to stderr and surfaces it as a diagnostic
  in `ScanResult.diagnostics`. Beyond 4x the warning is severe.
  Beyond 8x the run is refused with exit code 3 (TOOL_ERROR)
  and a clear message rather than silently over-subscribing the
  system. The multiplier tiers live as named constants in
  `cli.main` and are not currently configurable from the
  command line.
- **`--force-parallel` CLI flag and `PYDEPGATE_FORCE_PARALLEL`
  environment variable.** Maps to `parallel_threshold=0`,
  bypassing the file-count gate. Useful when an operator knows
  parallel is the right choice for the workload despite a small
  file count, or for testing the parallel path in CI without
  needing a large fixture.
- **`ScanResult.scan_id` field.** Every scan now carries a UUID4
  generated at scan start, threaded through `ScanResult` and
  emitted by all reporters (JSON, text, IOC sidecar, SARIF,
  decoded payload tree). This is the same shape and intent as
  the `METADATA_KEY_LAST_IMPORT_RUN_UUID` introduced for the
  `cvedb` subsystem in 0.4.2: every invocation produces a
  unique identifier that downstream consumers can use for
  cross-report correlation, audit trails, and answering the
  "which invocation produced this output" question without
  relying on timestamp guessing.
- **`initial_diagnostics` parameter on `StaticEngine`.**
  CLI-level diagnostics (workers thrashing warnings, threshold
  fallback notices, configuration soft warnings) are passed into
  the engine at construction and threaded through every
  `ScanResult` construction site. A warning that appears on the
  terminal is now also visible to JSON consumers and SARIF
  ingest, which makes it possible to audit the configuration
  of a scan after the fact rather than only at run time.
- **Picklability contract tests.** New `tests/test_pickle_contract.py`
  module with 20 tests asserting that `FileScanInput`,
  `FileScanOutput`, every default analyzer, the engine instance,
  and the `PayloadPeek` enricher all round-trip through pickle
  without loss. The default-rules construction inside the
  engine is exercised specifically as a load-bearing test for
  cross-process behavior. These tests are infrastructure for the
  parallelism work and run on every CI invocation as a
  regression guard against future analyzer changes that
  accidentally break the picklability contract.
### Changed
 
- **DENS051 emission gated by docstring content.** The signal
  previously fired on any `__doc__` reference passed to a
  callable, on the threat-model premise that payloads can be
  hidden in docstring text and executed via that pattern. It
  now resolves the target docstring statically (handling bare
  `__doc__` per Python's runtime semantics, where a class body
  resolves to the class docstring and a function body or module
  top level resolves to the module docstring, and
  `<obj>.__doc__` where obj is a top-level name in the same
  file) and consults `_magic.detect_format()` on the resolved
  content. When the content classifies as terminal `ascii_text`,
  the finding is suppressed. For any other classification (any
  encoding shape, Python source, pickle, binary), the finding
  emits as before. Unresolvable references emit conservatively.
  The motivating false positive set was libraries using
  sphinx-style docformat patterns; scipy alone accounted for 38
  such false positives in the stress test corpus before this
  change. The threat-model coverage is preserved: payload-bearing
  docstrings (base64, hex, embedded Python source, pickle)
  classify as non-`ascii_text` and continue to emit.
- **`_magic.looks_like_python()` requires syntactic position.**
  Python token detection now requires the token to appear at
  the start of a line (after optional leading whitespace)
  rather than anywhere in the first 2KB of text. The previous
  substring containment fired on prose using Python keywords
  as English words; phrases like "the multivariate class for"
  or "import duties were levied" both classified as
  `python_source` under the old heuristic. Line-anchored
  matching distinguishes prose from source correctly because
  Python statements appear at statement boundaries and prose
  embeds keywords mid-sentence. Indented code inside docstrings
  or examples continues to classify correctly because each line
  is lstripped before the prefix check. The narrow tradeoff is
  that single-line Python embedded mid-sentence in prose (the
  shape `"Run this: import os; os.system('ls')"`) no longer
  classifies as Python, which is not a meaningful attack
  pattern.
- **Density analyzer signal weights.** Several signal confidences
  in the code-density analyzer were adjusted based on stress
  testing across a 137-package real-world corpus that surfaced
  noisier-than-intended emission tiers at the previous
  calibration. The threat-model signal IDs and their emission
  conditions are unchanged; the weights determine how
  aggressively each signal propagates to blocking severity in
  default rule sets. The exact deltas are in the analyzer
  source, and the post-calibration stress run on the same
  corpus produces 11 findings across 4 packages (down from
  hundreds across 20 packages), each of which is a correct
  detection of high-entropy content that operators may choose
  to suppress at the rule layer for their own workloads (test
  fixtures, embedded shell scripts, Unicode data tables, known
  distribution `.pth` files).
- **`StaticEngine._aggregate_outputs` signature.** Accepts an
  `extra_diagnostics` parameter for diagnostics produced after
  engine construction (parallel fallback notices, etc.) so they
  can appear alongside the initial diagnostics in
  `ScanResult.diagnostics`. The signature change is internal;
  no public-API consumers are affected.
### Security
 
No security advisories in this release. The DENS051 and
`_magic.looks_like_python` calibrations are false positive
reductions: the underlying detection of payload-bearing
docstring patterns (encoded content, embedded Python source,
pickle data) is unchanged, the unwrap loop is unaffected, and
the threat-model coverage of the canonical LiteLLM 1.82.8
attack pattern was re-verified after the calibration work.
The engine parallelism work preserves the picklability
contract for the per-file scan path; analyzer behavior is
identical whether the engine runs serial or parallel, and
the picklability tests guard against accidental divergence.

## [0.4.2] - 2026-05-15

### Added

- **OSV PyPI CVE database (`cvedb` subsystem).** New subsystem
  for managing the local CVE database built from OSV PyPI
  snapshots. Implements the full ingestion pipeline: download
  with SHA256 verification, streaming JSON parse with
  ThreadPoolExecutor, multi-contributor deduplication by
  canonical CVE ID (CVE/GHSA/PYSEC precedence), and atomic
  SQLite writes. `pydepgate cvedb update` fetches the latest
  snapshot and imports ~16,500 distinct vulnerabilities in
  under 10 seconds. The `cvedb` subcommand exposes three
  actions: `update` (download and import), `status` (show
  record counts and metadata), and `path` (print DB location).
  Database is cached in `$XDG_CACHE_HOME/pydepgate/cvedb/`
  following the XDG Base Directory spec.

- **OSV ranges as first-class data.** The `affected_ranges`
  table captures version constraints from OSV range events
  (introduced, fixed, last_affected) as parsed (range_type,
  introduced, fixed, last_affected) tuples. Ranges are walked
  as a state machine: `introduced` opens a range, `fixed` or
  `last_affected` closes it, and a dangling `introduced` at
  end-of-events emits as open-ended. Range-only records (no
  explicit version list) now contribute data instead of
  warnings. A real OSV import yields 7,000-15,000 range rows
  alongside 500,000+ exact version rows, making the full
  constraint space queryable by the PEP 440 evaluator.

- **Structural ALL-versions detection with sentinel fast-path.**
  When a range has `introduced=0` with no fixed/last_affected
  closer, it qualifies as "every version affected". The importer
  flags the package and emits a sentinel row `(canonical_id,
  package, "ALL")` in `affected_versions`. Depscan queries
  become `WHERE version = ? OR version = 'ALL'`, handling both
  exact-match and universal-coverage CVEs in one disjunction
  without invoking the PEP 440 evaluator. This is the structural
  fast-path; semantic ALL detection (creative ways of expressing
  universal coverage) is deferred to the range evaluator.

- **Run UUID tracking in cvedb metadata.** Each import writes a
  universally unique run ID (`METADATA_KEY_LAST_IMPORT_RUN_UUID`)
  to the database metadata block. This UUID is foundational for
  SARIF `automationDetails.id` correlation, audit trails, and
  the "which invocation produced this DB" question. Defaults to
  `uuid.uuid4()` unless explicitly overridden; the run_context
  module manages generation with thread-safe double-checked
  locking.

- **Three-phase import progress bars (read, parse, write).**
  The importer exposes a `ProgressCallbacks` dataclass bundling
  update and finish callbacks for read, parse, and write phases.
  The CLI displays four bars total: Downloading (from fetcher),
  then Reading (zip entries), Parsing (JSON records),
  and Writing (DB inserts). Finish callbacks add newlines so
  each bar completes cleanly before the next starts. Write-phase
  progress fires after each batch of 1,000 rows, yielding ~560
  updates during a real 560k-row import for a smooth bar without
  per-row overhead.

- **New `cvedb` CLI summary format with totals.** The import
  summary now reports exact version rows, range rows, aliases,
  parse errors (each on its own line), and a Total summing all
  four. Example: `Exact version rows: 528447 / Range rows: 7842
  / Aliases: 25934 / Parse errors: 0 / Total: 562223`. The format
  makes it easy to spot coverage gaps (nonzero parse errors means
  some records weren't ingested) and track import growth over time.

### Changed

- **`pydepgate cvedb status` output gains range counts and run
  UUID.** The status display now shows a live query count of
  `affected_ranges` rows (not cached in metadata, so it reflects
  the actual table state) and the last import run's UUID if
  available. The "Skipped (no vers)" line is removed since
  range-only records are no longer skipped; they now appear as
  range rows. Schema version is included for future migrations.

- **CVE database schema version 2.** The `affected_ranges` table
  is new; the PRIMARY KEY strategy uses empty strings for absent
  `fixed` and `last_affected` fields (never NULL) so the key
  remains composite and deduplication works cleanly. Old v1
  databases are rejected with a hard error and a directive to
  re-run `cvedb update`; no in-place migration is offered.
  Future schema versions will follow the same hard-reject
  pattern to avoid migration complexity.

- **Importer API shape.** The `import_from_zip` function
  replaces the single `progress_callback` argument with a
  `progress: ProgressCallbacks | None` parameter. Tests
  typically pass `None` (silent import); the CLI constructs the
  bundle with all six callbacks. The `ImportResult` dataclass
  drops `records_skipped_no_versions` and adds
  `records_with_no_usable_data` (for CVEs with PyPI mentions
  but neither versions nor ranges; rare/never in practice) and
  `affected_range_rows` (count of range table inserts).

- **`cvedb update` download vs. import bars separated.** The
  download phase (checking and fetching the OSV snapshot) is now
  visually distinct from the import phase (reading, parsing,
  writing), making it easy to diagnose where time is spent. The
  download bar covers the HEAD check and full transfer; import
  bars cover unpacking and database operations.

### Security

No security advisories in this release. The cvedb subsystem
processes untrusted OSV JSON without executing user-provided
content (parsing is read-only and validation-strict). The run
UUID provides forensic trails for audit; databases can be
reproduced from the recorded snapshot SHA256 and run ID.

## [0.4.1] - 2026-05-12

### Added
- No new code, this is just to complete the link rename after the repo was renamed so that the URLs are correct and valid.

### Changed
- Updated `pyproject.toml` URLs
- Changed lifecycle from Alpha to Beta
- Added "supply-chain" topic

### Security
- No changes
- No security advisories in this release

#### Full Changelog: [v0.4.0...v0.4.1](https://github.com/nuclear-treestump/pydepgate/compare/v0.4.0...v0.4.1)

## [0.4.0] - 2026-05-10

### Added

- **SARIF 2.1.0 output.** `--format sarif` now emits real
  SARIF 2.1.0 documents instead of the under-development stub
  that shipped through 0.3.x. Each scan run produces a single
  document with the full rules catalog under
  `tool.driver.rules`, per-finding results with severity-mapped
  levels (critical/high to `error`, medium to `warning`, low/info
  to `note`), GitHub-compatible `security-severity` numeric
  scores, 24-character partial fingerprints for cross-run alert
  deduplication, and `automationDetails.id` of the form
  `pydepgate/{artifact_kind}/` for cross-run grouping. Deep
  scans suffix `_deep` to the artifact kind so deep and non-deep
  runs of the same artifact group separately. Compatible with
  GitHub Code Scanning, Azure DevOps, and any consumer that
  follows the OASIS SARIF 2.1.0 spec.
- **Decoded-payload codeFlows.** Findings reached through the
  recursive decode pipeline are surfaced as SARIF results with
  `codeFlows` describing the decode chain. Each `threadFlow`
  walks from the outer high-entropy literal through each decode
  layer to the innermost detection, surfacing the attack path
  in consumer UI like GitHub's "Show paths". Multi-layer
  payloads (the LiteLLM 1.82.8 attack pattern) produce nested
  threadFlow encoding with `nestingLevel` reflecting decode
  depth.
- **`--sarif-srcroot PATH` flag and `PYDEPGATE_SARIF_SRCROOT`
  environment variable.** Populates
  `originalUriBaseIds.PROJECTROOT` in the emitted document and
  tags on-disk artifact locations with `uriBaseId: "PROJECTROOT"`
  so SARIF consumers resolve paths against a known source root.
  Required when ingesting into GitHub Code Scanning for in-repo
  source navigation. The flag has CLI-over-env precedence
  matching the existing flag conventions, treats empty string
  as unset, and emits a soft warning to stderr when set without
  `--format sarif`.
- **Content-blind SARIF emission.** The document describes what
  was called (`subprocess.run()`, `urllib.request.urlopen()`)
  without including arguments, URLs, or literal payload bytes.
  This is by design: SARIF documents flow into CI logs, code
  scanning UIs, and artifact downloads, and embedding payload
  content there would replicate the exact threat the analyzer
  is detecting. A defender can publish a SARIF document
  publicly without re-leaking the underlying attack content.
  Verified against a real LiteLLM 1.82.8 sample before release.
- **`pydepgate.reporters.sarif` package.** New reporter package
  with submodules for severity mapping, URI scheme decisions,
  partial fingerprints, rule descriptor catalog generation,
  per-finding result construction, and full document assembly.
  The package is imported automatically when `--format sarif`
  is selected and is not part of the public API surface.
- **`pydepgate.cli.sarif_args` module.** Argparse helpers and
  validation for the new SARIF flag family, mirroring the
  `decode_args` and `peek_args` patterns. Exposes
  `add_sarif_arguments`, `sarif_srcroot` query helper, and
  `validate_sarif_args` soft-warning function.
- **`scripts/build_sarif_fixtures.py`.** Stdlib-only fixture
  builder that produces three benign wheels for SARIF
  validation: a clean package, a package with high-entropy
  literals that trigger DENS010/DENS011, and a package with a
  2-layer base64 chain whose innermost layer contains a
  benign `subprocess.run(['echo', 'hello-from-fixture'], ...)`
  call. The fixtures pattern-match as suspicious to the
  analyzer but contain no real malicious behavior, keeping CI
  artifacts safe to share and reproducible from a reviewable
  Python script. No binary fixtures committed to the
  repository.
- **`scripts/validate_sarif.sh`.** Local equivalent of the CI
  validation workflow. Builds the fixtures, scans each, runs
  `sarif validate` on the output. Useful for catching SARIF
  regressions on a developer machine before pushing to CI.
  Requires .NET SDK 8.0 or later for the Microsoft SARIF
  Multitool. Accepts an optional target argument to scan a
  specific file instead of the synthesized fixtures.
- **`.github/workflows/do_sarif_validation.yml`.** New CI
  workflow that validates pydepgate's SARIF emission against
  the Microsoft SARIF Multitool on every PR to main. The
  Multitool is the authoritative SARIF 2.1.0 validator and is
  what GitHub Code Scanning's ingestion uses internally.
  Validation hard-fails on warnings and errors. Accepts a
  `workflow_dispatch` `target` input for manual validation
  against arbitrary artifacts. Uploads emitted SARIF documents
  as a 7-day artifact regardless of pass/fail for debugging.

### Changed

- **`--format sarif` exit code semantics.** Previously returned
  exit code 3 (TOOL_ERROR) regardless of findings, signaling
  the under-development stub. Now computes the same exit code
  as the JSON and human formats: 0 for clean, 1 for findings
  below blocking severity, 2 for HIGH or CRITICAL findings, 3
  only for actual tool errors. CI that relied on the always-
  error behavior to detect "SARIF is not implemented yet" needs
  updating; that detection mechanism was never documented as a
  contract.
- **CLI scan flow restructured for SARIF and decode
  integration.** When `--format sarif` and
  `--decode-payload-depth` are both set, the decoded tree is
  now computed before the format dispatch and threaded into
  the SARIF renderer so codeFlows appear in the output. The
  same tree is then reused by the file-writing decode pass
  instead of running the decode driver twice. Users running
  both SARIF and decode in the same scan now get all expected
  outputs (SARIF document plus text/JSON report, IOC sidecar,
  optional encrypted archive) from one decode pass. Previously,
  SARIF format suppressed the file-writing decode pass; users
  who wanted both outputs had to run two scans.
- **Documentation.** README updated with a new SARIF output
  section under Usage, a Recently Added entry leading the
  section, and additions to the flag and environment-variable
  tables. The Status section now lists SARIF under "What works
  today" with the codeFlow encoding, severity mapping, and
  content-blindness properties called out. CHANGELOG, this
  document, gets the present entry.

### Security

The SARIF emission was audited against a real LiteLLM 1.82.8
sample before release. The document describes findings
behaviorally without including arguments to dangerous calls,
URLs, command lines, or literal payload bytes. This property
is structural rather than incidental: the per-finding message
text is constructed from analyzer signal IDs and rule
descriptions, not from the matched content. A future change
that introduced content into the message text would violate
this design constraint and is the kind of regression the CI
validation catches.

No security advisories in this release.

### Coming in 0.5.0

The following are planned for the next minor release. Tracking
issues will land in [ROADMAP.md](ROADMAP.md):

- **SIEM emission layer.** First-class HEC integration for
  Splunk, with CIM-compliant data models so findings populate
  Enterprise Security correctly rather than appearing as raw
  JSON. Elastic, Datadog and Sentinel emission planned
  alongside. Carried forward from the 0.3.0 changelog's
  "Coming in 0.4.0" list; SARIF was the headline item that
  landed in 0.4.0.
- **Engine parallelism.** The picklability contract documented
  in CONTRIBUTING.md is preserved through 0.4.0; 0.5.0 will
  enable a process pool for the per-file scan phase, targeting
  meaningful speedups on multi-megabyte wheels with thousands
  of files. Carried forward from the 0.3.0 list.

## [0.3.3] - 2026-05-05

### Changed

- **Reporters refactor.** Improved reporter module organization and structure for enhanced maintainability.
- **Location field added to all source files.** Every file in `src/pydepgate` now includes location metadata in the docstring. Example: `pydepgate.cli.subcommands.scan`.

## [0.3.2] - 2026-05-02

### Added

- **Tests for PEM detection and DER classification.** Comprehensive test coverage for PEM format recognition and DER structure classification to ensure robust certificate and payload analysis.

### Changed

- **Code structure refactoring.** Improved code organization and readability across core modules for better maintainability and clearer responsibility boundaries.

## [0.3.1] - 2026-05-01

### Fixed

- **JSON output patch.** Resolved issues with JSON output formatting and serialization to ensure consistent and valid JSON emission across all report modes.

## [0.3.0] - 2026-04-30

### Added

- **Artifact-level provenance hashes.** Scan results now include
  SHA256 and SHA512 of the scanned artifact (the wheel, sdist, or
  loose file). These appear in the JSON output's top-level
  `artifact` block as nullable `sha256` and `sha512` fields, in the
  decoded-payload tree's `artifact_sha256`/`artifact_sha512` fields,
  and in the IOC sidecar header. Installed-package scans report
  null because there is no single-file representation. The full
  forensic chain from artifact to decoded payload is now captured.
- **File-level hashes per finding.** Each finding in the JSON
  output gains nullable top-level `file_sha256` and `file_sha512`
  fields, sourced from the file's `ScanContext`. These let
  consumers correlate a finding to the specific file inside an
  artifact, which matters for wheels with hundreds of internal
  files where multiple findings might fire across different ones.
- **Containing-file hashes in decoded payload tree.** Each
  `DecodedNode` carries `containing_file_sha256` and
  `containing_file_sha512` fields when populated. The
  `render_iocs` and `render_sources` outputs include a "containing
  file" line per IOC block when the file hash differs from the
  artifact hash. For loose-file `--single` scans where the
  artifact and the file are the same bytes, the redundant line is
  suppressed.
- **Tristate `--decode-iocs` flag.** Three modes: `off` (single
  plaintext report file, default), `hashes` (plaintext report plus
  plaintext `.iocs.txt` sidecar with hash records), `full`
  (encrypted ZIP archive containing report.txt, sources.txt, and
  iocs.txt, plus a plaintext `.iocs.txt` sidecar next to the
  archive). The `full` mode always produces output, including a
  NOFINDINGS stub archive when nothing is found, so downstream
  tooling can rely on archive presence as a signal.
- **Encrypted archive output for `--decode-iocs=full`.** ZipCrypto-
  encrypted ZIP files using the malware-research convention
  password "infected" by default (configurable via
  `--decode-archive-password`). UTC timestamp in filename. Status
  prefix (`FINDINGS_` or `NOFINDINGS_`) makes downstream filtering
  trivial. Compression mode selectable via
  `--decode-archive-compression` (deflated by default; STORED
  available for forensic-grade preservation).
- **`--decode-location` flag.** Specifies where decode output
  should land. Accepts a directory path; the actual filename is
  generated from the artifact identity, timestamp, and status.
- **`--decode-payload-depth` flag.** Maximum recursion depth for
  the decoded-payload pass. Defaults to 0 (decoding off); set to a
  positive integer to enable.
- **Min-severity filter for decoded trees.** When
  `--min-severity` is set on a scan that runs the decode pass, the
  filter applies to the decoded tree as a presentation step.
  Decoding itself runs over every payload-bearing finding
  regardless of severity, so a low-severity outer finding that
  decodes to a critical inner one is still captured. The filter
  preserves chain context: a low-severity ancestor with a
  high-severity descendant is kept so the chain remains visible.
- **Engine `_hashes.py` module.** New helper module with a single
  `hash_pair(content) -> (sha256, sha512)` function. Centralizes
  hash computation across the engine, enumerators, and decode
  driver to ensure consistent format (lowercase hex, no
  separators) for downstream consumers.
- **Pre-commit hook configuration.** Two hook IDs exposed via
  `.pre-commit-hooks.yaml`: `pydepgate` (runs against staged `.py`
  files with `--min-severity high` to avoid blocking commits on
  low-severity informational signals) and `pydepgate-pth` (runs
  against staged `.pth` files at the strictest threshold since
  `.pth` files have no legitimate use case for the patterns
  pydepgate detects). Both honor `PYDEPGATE_*` environment
  variables for CI configuration.
- **`PYDEPGATE_DECODE_*` environment variables.** Five new vars
  for configuring decode behavior without changing the command
  line: `PYDEPGATE_DECODE_PAYLOAD_DEPTH`, `PYDEPGATE_DECODE_IOCS`,
  `PYDEPGATE_DECODE_LOCATION`, `PYDEPGATE_DECODE_ARCHIVE_PASSWORD`,
  `PYDEPGATE_DECODE_ARCHIVE_COMPRESSION`. CLI flags take
  precedence when both are set.

### Changed

- **JSON schema_version bumped from 2 to 3.** The change is purely
  additive: the top-level `artifact` block gains nullable `sha256`
  and `sha512` fields, and each entry in `findings` gains nullable
  top-level `file_sha256` and `file_sha512` fields. Consumers
  built against schema_version 2 continue to work without
  modification because their unknown-field handling treats the
  new keys as ignorable. Consumers should branch on the
  `schema_version` field as the canonical signal rather than
  testing for field presence.
- **Decoded-tree JSON output gains a `schema_version` field.**
  The output of `render_json` in `enrichers.decode_payloads` now
  includes `schema_version: 1`. Earlier versions emitted the same
  shape without a version field; consumers built against the
  schema-versionless output continue to work because the new
  field is additive and existing keys are unchanged. Future
  changes to this schema will bump the version.
- **`.pth` file dispatch now tries Python source path first.**
  When a `.pth` file's content is valid Python (the common case
  for malicious `.pth` payloads, where the entire file is a
  single-line `import...exec()` expression), the engine routes it
  through the standard Python source analysis path. This gives
  these files full enricher integration (peek, decode, and
  others) where previously they routed through the `.pth`-
  specific path that did not integrate with enrichers. The
  `.pth`-specific path remains the fallback for legitimately
  mixed-format files containing path-addition lines that aren't
  valid Python.
- **`decode_payloads` module moved.** Relocated from
  `pydepgate.cli.decode_payloads` to
  `pydepgate.enrichers.decode_payloads`. The module operates on
  findings as a post-scan enricher, not as CLI plumbing, and the
  new location reflects that. External callers importing from the
  old path need to update imports. No CLI behavior changes.
- **Inner archive directory uses underscores instead of dots.**
  When the decode pass produces an encrypted archive containing
  report.txt/sources.txt/iocs.txt under a target-named
  subdirectory, the subdirectory name now has dots replaced with
  underscores (`litellm_init_pth/` instead of `litellm_init.pth/`).
  Windows treats folders with file extensions inconsistently;
  Explorer may attempt to open such a folder as a file, and some
  unzip utilities refuse to create the directory. The archive
  filename itself keeps the extension since it's a real `.zip`
  file. The IOC sidecar file path is unaffected.
- **IOC sidecar format gains an artifact-identity header.** The
  plaintext `.iocs.txt` sidecar (and the `iocs.txt` inside the
  encrypted archive) now begin with an artifact-identity header
  block when artifact hashes are populated. The header uses the
  same two-token shape as existing hash lines
  (`artifact_sha256 <hex>`), so `grep '^artifact_sha256'` works
  unchanged for the new field. Existing consumers that grep for
  `decoded_sha256` or `original_sha256` continue to work because
  those lines are unchanged.

### Fixed

- **Decode pass on `.pth` files now produces real output.**
  Previously, scanning a single-line malicious `.pth` file with
  `--decode-iocs=full` produced a NOFINDINGS stub archive even
  when the file clearly contained an encoded payload (the
  LiteLLM 1.82.8 attack pattern). Root cause was a multi-layer
  interaction: the `.pth` analysis path did not integrate with
  the peek enricher, peek's unwrap loop classified subprocess-
  wrapped Python source as a terminal kind with no transforms,
  and the decode driver gated recursion on peek producing a
  decoded block. The fix combines three changes: `.pth` files
  with valid Python content now route through the Python source
  path (which integrates with peek), peek now emits decoded
  blocks for `python_source` terminals so the decode driver can
  recurse into the embedded source to find inner payloads, and
  the decode driver's recursion logic correctly handles the
  multi-layer chain. The full forensic chain from outer Python
  source to inner base64 payload to decoded malicious code is
  now captured. This corrects a major detection gap for the
  `subprocess.Popen([..., 'python', '-c', '<huge>'])` malware
  pattern that wraps base64-encoded Python inside a Popen call.
- **`--decode-format=json` no longer crashes with TypeError.**
  Previously, the JSON output path raised
  `TypeError: report_render_json() missing 1 required positional
  argument: 'stream'` due to a function naming collision between
  the main scan output renderer (`report_render_json` in
  `cli.reporter`, signature `(result, stream)`) and the
  decode-tree renderer (`render_json` in
  `enrichers.decode_payloads`, signature `(tree)`). The decode
  pass now correctly calls `render_json` with the
  `DecodedTree` argument.
- **Pre-commit hook integration confirmed working.** Multiple
  test runs of `pre-commit try-repo` against the public
  pydep-vector-runner repo confirm hooks initialize, the Python
  environment installs pydepgate from PyPI, both hook IDs
  register, and they correctly skip when no matching files are
  staged. (This was never broken in code; the previous
  uncertainty was a misreading of `try-repo` output where
  "no files to check" was correctly the result of running
  against an empty target directory rather than a hook failure.)
- **Filter preserves new hash fields when rebuilding tree.**
  `filter_tree_by_severity` now correctly propagates
  `artifact_sha256`, `artifact_sha512`, `containing_file_sha256`,
  and `containing_file_sha512` through to the filtered tree.
  Previously these were silently dropped because the filter
  rebuilt nodes without copying through new fields.
- **`SyntaxWarning` from `ast.parse` no longer pollutes stderr.**
  Decoded payloads frequently contain Python source with invalid
  escape sequences and useless `is` comparisons that Python 3.12
  raises as `SyntaxWarning`. The Python source parser now
  suppresses these warnings inside a tightly-scoped
  `warnings.catch_warnings()` block during the parse call.
  Surrounding code's warning behavior is unaffected; only
  `SyntaxWarning` from this specific parse is silenced. Other
  warning categories (`DeprecationWarning`, `RuntimeWarning`)
  pass through unchanged.

### Security

(No security advisories in this release. Detection improvements
documented under "Fixed" above represent enhanced coverage of
existing attack patterns, not vulnerabilities in pydepgate itself.)


[Unreleased]: https://github.com/nuclear-treestump/pydepgate/compare/v0.6.1...HEAD
[0.6.1]: https://github.com/nuclear-treestump/pydepgate/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/nuclear-treestump/pydepgate/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/nuclear-treestump/pydepgate/compare/v0.4.7...v0.5.0
[0.4.7]: https://github.com/nuclear-treestump/pydepgate/compare/v0.4.6...v0.4.7
[0.4.6]: https://github.com/nuclear-treestump/pydepgate/compare/v0.4.5...v0.4.6
[0.4.5]: https://github.com/nuclear-treestump/pydepgate/compare/v0.4.2...v0.4.5
[0.4.2]: https://github.com/nuclear-treestump/pydepgate/compare/v0.4.1...v0.4.2
[0.4.1]: https://github.com/nuclear-treestump/pydepgate/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/nuclear-treestump/pydepgate/compare/v0.3.3...v0.4.0
[0.3.3]: https://github.com/nuclear-treestump/pydepgate/compare/v0.3.2...v0.3.3
[0.3.2]: https://github.com/nuclear-treestump/pydepgate/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/nuclear-treestump/pydepgate/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/nuclear-treestump/pydepgate/releases/tag/v0.3.0
