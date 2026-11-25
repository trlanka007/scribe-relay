# Execution backlog — granular view

Proposed | 2026-11-25. This is a task-level seed, not a claim of issue creation or completion. See [work packages](work-packages.md).

## Current priority: M3

All experiments pending unless evidence says otherwise. Use [protocol](../research/platform-compatibility.md), [matrix](../testing/formatting-compatibility-matrix.md) and [fixture](../../tests/fixtures/README.md).

| Task | Action | Prerequisite | Done when / evidence |
|---|---|---|---|
| M3.1.a | Recheck official platform and clipboard documentation | — | dated source notes; native/API distinction |
| M3.2.a | Record Windows/Edge version, fixture hash and expected inventory | approved scope | reproducible run header |
| M3.2.b | Copy rendered HTML and paste into fresh draft | M3.2.a | F01–04,F07 per-element observations |
| M3.2.c | Reopen autosaved draft and compare | M3.2.b | persistence observations, link targets checked manually |
| M3.2.d | Repeat in Chrome | M3.2.a | independent run and browser differences |
| M3.2.e | Prepare isolated user-triggered HTML/plain clipboard spike | owner-approved scope | local-only spike with no LinkedIn automation |
| M3.2.f | Repeat rich paste, reopen and permission/fallback tests | M3.2.e | F08 evidence, profile candidates |
| M3.3.a | Create synthetic local image and placement fixture | approved scope | asset hash, anchors and expected inventory |
| M3.3.b | Test rendered inline image copy/paste | M3.3.a | F05 recorded; no silent assumption |
| M3.3.c | Test native upload/cover and ordered placement | M3.3.a | F06 steps, time, reopen |
| M3.4.a | Create synthetic DOCX/Markdown inventories and edge cases | approved scope | reviewed expected elements |
| M3.4.b | Compare candidate parsers in disposable spikes | M3.4.a | F09/F10 fidelity, error and security notes |
| M3.5.a | Gather manual and ToolHa preparation baseline | M3.2.b | paired fixture timing protocol and baseline |
| M3.6.a | Reconcile results into compatibility matrix | M3.2–5 | supported/unknown/fallback states with evidence |
| M3.6.b | Review critical risks and scope changes | M3.6.a | owner decision; no unsupported claims |

For each run record date, browser/OS, fixture hash, copy method, expected and actual on paste/reopen, outcome, manual action, duration and sanitized evidence. User performs authenticated editor interactions. No publishing.

## Later milestones — provisional task seeds

| Task | Action | Completion artifact / criterion |
|---|---|---|
| M4.1.a | Describe primary author and secondary rich-text user | reviewed persona/jobs and journey |
| M4.2.a | Sketch import/preview/report screen states | wireframes for success, warnings, rejection |
| M4.3.a | Design media placement and export acknowledgement | user-controlled handoff and keyboard flow |
| M5.1.a | Refine C4 views using M3 evidence | owner-approved boundaries and deployment alternatives |
| M5.2.a | Specify node identity, source spans and asset references | model invariants and representative examples |
| M5.3.a | Define adapter/profile and reconciliation contracts | deterministic mapping rules and failure cases |
| M5.4.a | Compare candidate stack and write ADRs | evidence-backed decision, alternatives and consequences |
| M6.1.a | Threat-model untrusted files, HTML, assets and clipboard | mitigations and abuse fixtures |
| M6.2.a | Map FR/NFR/AC to test layers | test plan and release gates |
| M6.3.a | Define CI, lint/build/test, review and rollback conventions | approved engineering/deployment guides |
| M7.1.a | Build smallest approved end-to-end slice | one source → inventory → preview → copy |
| M7.2.a | Add approved importers and asset inventory | FR-01–03,07 reconciliation tests |
| M7.3.a | Implement profile-aware transformation/report | FR-04–06,10 and deterministic tests |
| M7.4.a | Integrate handoff and accessible issue recovery | FR-05–09 scenarios pass |
| M7.5.a | Execute full AC suite and final F11 comparison | actual draft evidence and measured metrics |
| M8.1.a | Conduct owner-approved private pilot | feedback and prioritized defects |
| M8.2.a | Validate release/rollback and support documentation | checklist completed |
| M8.3.a | Obtain release approval and revise roadmap | owner decision and release record |

Expand tasks at their parent gate; do not infer approved stack, hosting, estimates, or class designs from these seeds. Link each eventual GitHub issue/PR to its task ID. Owner is approval authority; task assignees remain unset.
