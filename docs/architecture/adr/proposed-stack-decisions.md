# Proposed architecture decision records — stack review packet

Status: all Proposed, none accepted | 2026-11-26 ET
Task #102; see [technology stack evaluation](../technology-stack.md). Decision IDs are draft local identifiers, not new GitHub issues. No production implementation authorization.

## ADR-P01 — Local execution and deployment boundary

Context: NFR-01/02/07; M3 browser and parser evidence incomplete.
Proposal: evaluate static HTTPS delivery with local browser conversion first.
Alternatives: installed desktop, local companion, .NET WebAssembly browser runtime; mandatory remote conversion excluded under current local-first requirement.
Consequences: minimal required infrastructure; browser constraints and clipboard user activation become material. Static hosting delivers code, not document processing.
Acceptance evidence: offline after load, bounded memory/latency, local-only network trace, viable parser and F08/manual destination route.
Revisit if browser cannot satisfy hard gates or supported device limits. No provider chosen.

## ADR-P02 — Language and UI/runtime

Context: M5 canonical and adapter contracts require deterministic typed boundaries and accessible state management.
Proposal: evaluate TypeScript + browser APIs, React versus lightweight UI, with domain logic isolated from UI framework.
Alternative: .NET WebAssembly with JS interop; desktop if browser-only fails.
Consequences: candidate single-language web implementation, runtime validation still mandatory; framework and worker boundary need verification.
Acceptance evidence: representative import-to-local-clipboard slice in approved disposable experiment scope, keyboard flow, stale revision and cancellation checks, dependency/license review. No language/framework accepted.

## ADR-P03 — Parsing and independent accounting

Context: M3.4 historical probes show why semantic extraction alone is insufficient; #151 open.
Proposal: evaluate source-specific parsing plus independent bounded inventory, explicit provenance and ordered reconciliation. Do not rely on converter HTML as source truth.
Alternatives: single library with independently verified inventory facilities; custom bounded package extraction; reject unsupported inputs when complete accounting impossible.
Consequences: more verification effort, less silent loss; no broad DOCX feature promise.
Acceptance evidence: exact fixture inventory, negative/malformed cases, asset occurrence and story scope, reproducible runtime comparisons, reviewed supported subset. No parser or ZIP library accepted.

## ADR-P04 — Rendering, sanitization and handoff

Context: FR-04–10, NFR-02; LinkedIn paste/reopen unverified.
Proposal: safe structured output, reviewed allowlist/serializer and independent final-output reconciliation; user-activated clipboard and separate media plan.
Alternatives: vetted sanitizer, native safe DOM construction, tested rendered-selection fallback; plain-text recovery only. No automated LinkedIn interaction.
Consequences: preview is local simulation; unsupported/unknown features remain explicit; sanitize without silent loss.
Acceptance evidence: no execution/implicit fetch, unsafe link and resource tests, final output mapping, actual manual F01–F08 evidence and approved warning policy.
Revisit if safe rich handoff cannot satisfy core scope.

## ADR-P05 — Test and delivery tooling

Context: AC-01–12 and future M6 engineering readiness.
Proposal: layered deterministic domain/fixture tests, local browser tests and human destination validation; immutable build artifact and rollback review.
Alternatives: runtime-appropriate unit/browser harnesses and distribution methods.
Consequences: real destination checks stay manual; CI cannot certify external editor behavior from a local preview.
Acceptance evidence: approved M6 test strategy, security controls, exact dependency/lockfile and license review, reproducible build, release/rollback proof. No workflow, hosting or test framework accepted.

## Acceptance register

For each ADR record exact selected alternative/version, evidence references, reviewer, decision date, consequences and supersession conditions when accepted. Until then every entry remains Proposed. M5.1–3 prerequisites, M3 evidence and owner approval remain outstanding; no task closure, scope waiver or production dependency.
