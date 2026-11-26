# M6.2 — Testing strategy and acceptance traceability

Status: proposed review material; no tests executed by this document | 2026-11-26 ET
Task #104 (M6.2.a), parent PBI #71 as recorded in issue. M2.3 and M5.3 approval prerequisites remain open. Review preparation only. [PRD](../product/product-requirements.md), [acceptance criteria](acceptance-criteria.md), [conversion contract](../architecture/conversion-specification.md), [threat model](../architecture/security-and-privacy.md).

## Test layers and evidence ownership

| Layer | Scope | Proposed execution |
|---|---|---|
| L1 Domain unit | Source locators, ordered identities, rule precedence, profile validation, mapping, eligibility, revisions | Every change; deterministic in-process tests |
| L2 Import/conversion integration | Actual parser and renderer, independent inventory oracle, assets, final safe output, rejection paths | Every relevant PR; synthetic fixtures, exact dependency versions |
| L3 Local application browser | Import, preview, warnings, keyboard, copy success/failure, cancellation, stale state, offline and network inspection | Agreed baseline browsers; local harness only |
| L4 Manual destination | Actual LinkedIn Article paste, native media insertion, corrections, save/reopen | Human tester; exact browser/profile/route; no editor automation or publication |
| L5 Performance and product outcome | Reference-device latency and responsiveness; paired active preparation effort | Controlled run protocol; report raw observations and limitations |
| L6 Delivery/security | Dependency/license review, build provenance, headers, deployment smoke and rollback | M6 controls and M7/M8 release verification |

Prefer fast domain and integration feedback; browser checks cover real platform boundaries. Test doubles can exercise failure branches but do not prove real clipboard permission, browser behavior or destination persistence. L4 cannot be replaced by a screenshot of preview or automated LinkedIn activity. Frameworks and CI execution details remain pending stack and delivery approval.

## Requirement-to-acceptance-to-test traceability

| Requirement | Acceptance | Primary layers | Expected evidence |
|---|---|---|---|
| FR-01 import | AC-01 | L1/L2/L3 | All agreed input types; invalid/oversized input explicitly rejected |
| FR-02 inventory | AC-01 | L1/L2 | Independent authored inventory, ordered occurrence coverage and unsupported records |
| FR-03 normalization/provenance | AC-01 | L1/L2 | Valid source locators, immutable source, canonical mapping |
| FR-04 destination conversion | AC-02/03 | L1/L2/L4 | Versioned rules, final mapping, scoped actual target observations |
| FR-05 preview/report | AC-02/05 | L2/L3 | Counts reconcile; location/reason/recovery; simulation labeled |
| FR-06 alternatives and warnings | AC-02/05 | L1/L3 | Reviewed safe alternatives, invalidated stale acknowledgement, blocked unsafe/unaccounted output |
| FR-07 media extraction | AC-04 | L2/L3/L4 | Asset identity, repeated ordered occurrences, missing-reference recovery |
| FR-08 clipboard | AC-03/06 | L3/L4 | HTML/plain representations, real paste, denial and explicit fallback |
| FR-09 title/body/media handoff | AC-04/06 | L3/L4 | Separate title and cover, ordered manual placements and reopened draft |
| FR-10 profile and limits | AC-05 | L1/L3/L4 | Exact version/date, unknown distinct from unsupported, no false verification |
| FR-11 basic preview editing (P1) | Proposed additional check if selected | L1/L3 | User edits separate from adapter changes; original retained |
| FR-12 recovery package (P1) | Proposed additional check if selected | L2/L3 | Local export includes recoverable assets/report; no hidden data transfer |
| NFR-01 local first | AC-07 | L2/L3/L6 | Offline after load, zero document upload |
| NFR-02 safety | AC-07 | L1/L2/L3 | Abuse cases S01–S08 and final output safety |
| NFR-03 determinism | AC-08 | L1/L2 | Repeated normalized outputs, mappings and reports equivalent |
| NFR-04 accessibility | AC-09 | L3 | Keyboard-only core journey; readable status/errors, visible focus |
| NFR-05 progress/performance | AC-10 | L3/L5 | Reference-device p95, cancellation, responsiveness |
| NFR-06 extensibility | AC-11 | L1/L2 | Synthetic second adapter, no importer changes |
| NFR-07 telemetry/privacy | AC-07 | L3/L6 | Network/storage/log inspection, no hidden document telemetry |
| Product effort reduction | AC-12 | L4/L5 | Equivalent paired manual/ScribeRelay results, failures disclosed |

P1 checks are conditional proposals, not new accepted P0 criteria. Acceptance criteria remain authoritative.

## Fixture coverage and independent oracles

| Fixture family | Available evidence / source | Planned coverage |
|---|---|---|
| Rich HTML baseline | [Static fixture](../../tests/fixtures/linkedin-rich-text.html) and [manual sheet](manual-linkedin-article-run-sheet.md) | E01–E11, Unicode, headings, links, lists, quote, divider, table, code |
| Markdown | Existing M3 parser spike fixtures and malformed-source probes | Dialect, exact byte spans/CRLF, reference links, unsafe/raw HTML, malformed syntax, missing image |
| DOCX | Existing generated-package and OPC probes | Ordered text/table cells, styles/numbering, auxiliary stories, relationship scope, repeated/missing assets, unsupported structures |
| Media | [Synthetic media run sheet](manual-linkedin-media-run-sheet.md) | Body vs cover, direct paste vs native upload, placement/caption/alt/reopen |
| Security | [S01–S14 catalog](../architecture/security-and-privacy.md) | Small bounded abuse cases, no execution or implicit fetch, safe rejection, stale revision, retention |
| Representative article | Planned sanitized certification-style fixture | End-to-end realistic composition; synthetic by default; private material requires separate permission |
| Performance | Planned size-bucket synthetic fixtures | Agreed small/typical/upper-bound inputs, repeatable size and asset counts |

Existing spike artifacts are not production regression fixtures by default. The fixture README is an initial baseline; review inventory and identities before promoting additional fixtures. Human-reviewed expected inventory must be authored independently of the parser under test, with explicit order, multiplicity, semantics and source locators. Use exact fixture identity and safe expected output; do not regenerate expected results merely to make failing tests pass. Record fixture generator/version when applicable. No private documents, real account data or private draft URLs in CI.

## Negative and mutation checks

- Remove, duplicate or reorder an authored occurrence while maintaining aggregate text counts; independent reconciliation must detect the mismatch.
- Drop a final output node after sanitization or insert unmapped authored text; block handoff.
- Change profile or source revision after review; invalidate stale acknowledgement and copy result.
- Deny rich clipboard write; require explicit fallback and distinguish it from rich success.
- Use unmatched browser/route or unknown capability; never promote Unknown to supported.
- Run bounded security cases from M6.1; inspect attempts at network requests before offline tests. Test both successful offline operation and absence of unauthorized transfer when network is available.

## Evidence protocol and metrics

Record test ID, FR/NFR/AC, source revision, fixture identity, expected/actual result, runtime/dependency versions, browser/OS, profile/route, date, sanitized evidence and defect reference. Status: Not run, Pass, Fail, Blocked, or Not applicable with reason; Unknown target observation is never Pass. Historical spike records remain scoped; #151 pinned regression is unresolved. No fabricated test counts.

For AC-08 compare ordered normalized semantics, output, media plan, mapping and diagnostics; exclude only agreed incidental metadata. For AC-10 agree reference device, size units, timing start/end, cold/warm conditions and run count before measurement; proposed p95 <= 3 seconds applies to agreed local conversion fixtures, not network loading or human paste. Report individual timings, sample size, percentile method, failures and responsiveness; do not discard failed runs. Resource safety limits are separate from benchmark sizes.

For AC-12 use [F11 benchmark protocol](../research/preparation-effort-benchmark.md): at least three equivalent paired A/C runs per fixture, counterbalanced order, same target quality and verified reopened draft. Proposed >=50% median active effort reduction; record edits, clicks, media, failures and unavailable arms. A/B is baseline research, not proof of A/C improvement. No numeric baseline established.

## Proposed quality gates

| Gate | Required review/evidence |
|---|---|
| M6 readiness | Approved M2/M5, reviewed threat controls and test plan, agreed fixture/device/browser/profile boundaries, selected tooling and delivery controls |
| M7 PR | Relevant automated checks pass, changed behavior has traceable tests, security and accounting regressions block merge; no unverified target support claims |
| M7 MVP | All P0 AC evidence including manual actual paste/reopen and agreed performance/effort targets; unresolved failures explicitly reviewed, no unsafe or unaccounted output waiver |
| M8 release | Pilot feedback, known limitations, dependency/security review, release smoke/rollback and explicit owner authorization |

No production implementation or CI workflow added. Proposed tests have not run, actual browser/device baseline and thresholds remain pending, and no approval or issue closure is implied. Review with M6.1 and M6.3 before readiness acceptance.
