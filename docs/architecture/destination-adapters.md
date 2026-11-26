# M5.3 — Destination adapters and compatibility profiles

Status: provisional contract proposal; not approved or implemented | 2026-11-25 ET
Task #101 (M5.3.a), parent PBI #68 as recorded in issue. See [conversion specification](conversion-specification.md), [canonical model](canonical-document-model.md), [compatibility matrix](../testing/formatting-compatibility-matrix.md). Formal prerequisites M3.2/M5.2 outstanding.

## Boundary and extension model

Source importers produce canonical semantics plus source inventory/provenance; adapters consume that contract, never source-format parser internals. A destination adapter is a local policy/mapping boundary, not an authenticated integration. The conversion engine owns generic orchestration and independent reconciliation; adapter mapping claims are checked against final safe output. Handoff is a separate user-triggered boundary. Adding an adapter should not require changes to existing importers unless a genuine canonical/source capability changes (NFR-06, AC-11).

| Contract operation | Input | Output / constraints |
|---|---|---|
| Describe destination | Adapter identity/version | Human-readable destination and available routes; no network |
| Resolve profile | Destination and explicit environment/route | Exact immutable profile or explicit unknown/unavailable; no automatic support extrapolation |
| Validate options | Canonical revision, profile, choices | Validated options or actionable diagnostics |
| Map semantics | Canonical nodes/occurrences, local asset references, profile, validated options | Structured output, rule IDs, provenance mapping, candidate diagnostics and ordered media plan |
| Prepare representation | Mapped output and selected route | Candidate safe HTML/plain text or other explicitly approved representation; final safety/reconciliation outside adapter claims |
| Describe handoff | Eligible final representation, report and media plan | Manual instructions and capability limitations, no clipboard write or destination call |

These are logical operations, not executable interfaces, package APIs, plugin loading or network services. Exact type system, error transport and serialization remain M5.4/M7 decisions. Profiles are data, not executable arbitrary scripts. Reject unknown profile schema or unrecognized rule identifiers.

## Profile contract (proposed)

| Field group | Required information |
|---|---|
| Identity | Destination ID, profile ID, immutable profile version, schema version, compatible adapter/rule versions |
| Applicability | Editor surface, OS/browser/build range if established, route (rich clipboard, rendered selection, native media), feature and context |
| Evidence | Source type (documentation/local test/actual target test), run reference, date, observed paste/reopen results, limitations, review state |
| Capability | Per-feature status; native capability distinct from paste and reopen |
| Mapping | Stable rule ID/version, applicability and precedence, proposed representation, disclosed transformation/recovery |
| Lifecycle | Proposed/accepted/superseded, review owner/date, re-test triggers, superseding profile reference |

Never widen an observed browser or route result without review. A native upload documented in help is evidence of a native control, not proof of clipboard image support. Local clipboard success is not actual editor evidence. Unknown feature or unmatched context remains Unknown; explicit safe fallback may be proposed but is not a verified support designation. An unsupported state must have scoped negative evidence; an absent observation is not unsupported. A profile may be stale or superseded; surface that fact and require the agreed eligibility policy rather than silently upgrading.

## Initial LinkedIn candidate

| Profile dimension | Proposed value / evidence |
|---|---|
| Destination | LinkedIn Articles (not feed posts, newsletters or automated publishing) |
| Baseline context | Desktop Edge/Chrome candidates on Windows; exact versions pending |
| Body route | User-activated HTML and plain-text clipboard representations; rendered selection fallback candidate |
| Media route | Separate local asset and placement guidance; author uses native controls |
| Title/cover | Separate slots and author confirmation; no inferred upload success |
| Native capability | Documented controls per M3.1 |
| Actual paste/reopen | Unknown for F01–F08 pending recorded manual runs |
| Lifecycle | Proposed; not an approved supported browser profile |

No native article draft creation endpoint is established in reviewed public documentation; no private endpoint or automated DOM interaction. Adapter cannot access LinkedIn credentials, draft URLs or actual editor content. Author manually saves and verifies draft. Other publishing destinations remain future work.

## Extension and verification scenarios

- Add a synthetic second destination with different heading/table/media policy: existing Markdown/DOCX/rich-text importer contracts remain unchanged; same canonical snapshot drives distinct outputs and reports.
- Select a different browser or copy route without evidence: show Unknown, never reuse unsupported applicability silently.
- Profile version or rule changes: deterministic re-conversion from original canonical source; stale acknowledgement and copy result invalidated.
- Conflicting or malformed profile: fail explicitly before producing eligible output.
- Adapter emits an unsafe URL or unmapped text: independent safety and reconciliation reject it despite adapter claims.
- Destination changes editor behavior: record new scoped manual evidence, review new profile version, retain historical evidence and do not mutate prior profiles.

M6/M7 must execute these as applicable test scenarios; they are not results. No dependency, deployment, plugin infrastructure, stack choice, compatibility matrix modification, issue closure or gate acceptance. Formal M5.3 review waits for upstream evidence and owner approval.
