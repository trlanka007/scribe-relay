# M5.1 — Solution architecture review preparation

Status: provisional review material, not M5 acceptance | 2026-11-25 ET
Task #99 (M5.1.a), parent PBI #66 as recorded in issue. M3.6 and M4.3 approvals remain outstanding; this document prepares the review of existing hypotheses, not formal execution of the blocked architecture gate. No stack or deployment selection.

## Candidate system boundary

The existing [C4 views](c4/README.md) remain the baseline. ScribeRelay receives user-selected files or explicitly pasted content, processes locally, presents a reconciled preview/report, and prepares separate title/body/media handoff. The author alone operates LinkedIn. No mandatory backend, AI, account, server-side conversion, private API or automated editor integration. This is a candidate consistent with NFR-01/02/06/07, not a validated deployment.

## Evidence-to-boundary review

| C4 level | Existing view | Proposed refinement for review | Evidence and uncertainty |
|---|---|---|---|
| Context | [5,000 feet](c4/01-context.md) | Keep author as sole bridge to destination; distinguish documented native controls from observed paste | M3.1 official documentation; actual editor fidelity unknown |
| Containers | [2,000 feet](c4/02-containers.md) | Evaluate local browser execution with static code delivery; worker as optional execution boundary, not a new service | F08 and device performance unverified |
| Components | [1,000 feet](c4/03-components.md) | Distinguish independent source inventory from semantic extraction and ordered reconciliation; separate asset identity from occurrence | M3.4 synthetic evidence, pinned rerun #151 outstanding |
| Contracts | [Ground level](c4/04-detail.md) | Bind review and handoff eligibility to source/output/profile revisions; separate local clipboard result and author-reported destination checks | M4 draft workflows, not accepted interaction design |

These refinements are review proposals only; existing C4 files are not promoted to approved architecture. Detailed canonical model and adapter contracts belong to M5.2/M5.3 after prerequisites.

## Deployment alternatives

| Alternative | Advantages | Tradeoffs / required evidence |
|---|---|---|
| Static browser application with local processing | Minimal operations and no mandatory document transfer; aligns with user-controlled clipboard | Browser memory/worker constraints, parser availability/licensing, secure context, offline after load and clipboard validation |
| Installed desktop application with local processing | Potential native file/clipboard integration, offline distribution | Packaging, signing, updates, cross-platform maintenance and larger operational scope; native clipboard does not guarantee LinkedIn fidelity |
| Local companion plus browser interface | Can isolate parsing in local process where browser constraints are material | Installation and local IPC security, version coordination, support overhead; investigate only if browser-only limitations warrant it |
| Remote conversion service | May enable server-side library ecosystem and resource scaling | Conflicts with mandatory local-first conversion unless separately optional and approved; document transfer/privacy/operations cost; not a candidate for required MVP conversion |

Recommendation for review: prioritize evaluating browser-local execution; retain desktop/companion alternatives if measurable constraints justify them. No hosting provider, framework, language, parser or distribution model selected. Python synthetic probes do not establish browser deployability.

## Proposed responsibility refinements

- Input safety checks precede unsafe parsing or resource expansion; semantic extraction and independent inventory provide distinct evidence, not two labels on the same parser result.
- Canonical document and provenance remain source-oriented. Destination adapters never mutate the original and do not call the external editor.
- Reconciliation verifies ordered occurrence coverage, source-to-output mapping and explicit recovery. Byte coverage alone does not prove semantic preservation.
- Safe rendering/export is a separate boundary. Acknowledgement cannot override unsafe output or unaccounted content.
- Session coordinator distinguishes current revision, stale results, copy success/failure and author-reported verification; clipboard success does not mean publication success.
- Local asset inventory keeps repeated placements even when bytes are deduplicated; missing references remain visible and no implicit network fetch occurs.

## Review dependencies and decision packet

| Decision | Evidence required | Gate / task |
|---|---|---|
| Supported clipboard/media route | Edge/Chrome and manual paste/reopen F01–08; explicit fallback | M3.2/3.3, #94/#95 |
| Parser and source boundary | #151 pinned regression, unsupported-content policy, deployment-environment comparison | M3.4 / M5.2 |
| Interaction and acknowledgement | Reviewed M4.1–4.3 scenarios and relevant M3 results | #96–98 |
| Deployment/runtime boundary | Evidence for resource limits, offline/no-fetch and supported browser route; compare alternatives | #99 |
| Canonical model and adapter contracts | Approved upstream boundaries and provenance/reconciliation examples | #100/#101 |
| Stack and ADRs | Evidence-based library/runtime/licensing comparison, explicit owner approval | #102 |
| Production readiness | Security, test strategy and delivery gates | M6 |

Use the [interim feasibility gate review](../research/feasibility-gate-review.md) as the outstanding evidence register. Review material does not resolve #151 or any M3/M4 gate. No production implementation, dependency changes, task closure or hierarchy changes. Formal M5 review and acceptance remain blocked until prerequisites are satisfied or explicitly revised by owner.
