# Specification-driven delivery workflow

Proposed | 2026-11-25 | ScribeRelay-owned process, inspired by [GitHub Spec Kit](https://github.github.com/spec-kit/quickstart.html) and its [spec-of-specs guidance](https://github.github.com/spec-kit/how-to/spec-of-specs.html). No AIS-owned tooling, third-party agent scripts or actual Spec Kit initialization is included.

## Abstraction and work item model
| Level | Work item | Definition |
|---|---|---|
| 5,000 / 2,000 ft | Epic | One M0–M8 milestone outcome and gate |
| 1,000 ft | Feature | One independently reviewable work package, stable Mx.y ID |
| Ground level | PBI | User/owner outcome with acceptance scenarios; USn under feature |
| Ground level | Task | Concrete activity or verification, stable Mx.y.a ID; future seeds refined before work |

For research and documentation, PBI means an evidence or decision outcome, not an artificial end-user feature. For implementation, PBIs are independently testable user outcomes. Split a PBI when it cannot be delivered or verified independently; keep stable IDs and link new issues. See [issue index](github-backlog-index.md).

## Spec-driven lifecycle
1. Constitution: review [project principles](../../specs/constitution.md) and AGENTS.md.
2. Specify: define outcome, story priority, scenarios, functional scope, measurable success, exclusions and ambiguity in spec.md; owner reviews.
3. Clarify: resolve evidence gaps and scope choices; do not assume unknown target support.
4. Plan: define approved technical approach, contracts, dependencies, file paths, safety and test strategy in plan.md. M3 research may precede plan; M5/M6 approval is mandatory before production.
5. Tasks: create ordered, testable tasks.md checkboxes referencing issue IDs, PBIs, prerequisites and paths; use [P] only where parallel work is demonstrably safe.
6. Analyze: check constitution, spec/plan/tasks consistency, requirements/AC coverage, issue links and dependency gates.
7. Implement: owner-approved scope only; use feature branch and PR; tests and evidence accompany code.
8. Verify/converge: actual target-editor tests and reconciliation; update specs and evidence when discoveries change assumptions; close issues only after acceptance.

This adapts the upstream workflow; it does not claim official Spec Kit commands are installed. The existing PRD and acceptance criteria are the master scope; feature specs are narrower derivations.

## Labels
- type:epic, type:feature, type:pbi, type:task — exactly one per backlog item.
- milestone:M0 through milestone:M8 — planning alignment, not native GitHub milestone assignment.
- area:core-implementation — P0 M7 delivery and verification only; includes the M7 epic, features, PBIs and tasks.
- area:optional-enhancement — conditional P1 items, not core MVP.
- area:governance/product/research/design/architecture/engineering/release/documentation — distinguish supporting work.
- status:review/ready/blocked/done/deferred — readiness snapshot; ready means eligible for refinement, not that all dependencies or spike permissions have been cleared. Reconcile labels and issue state as gates change.
- priority:P0/P1 — production scope where assigned; kind:validation for explicit verification seeds.

## Operational rules
No direct main writes; owner approval for merges. M2/M5 explicit approvals and M6 readiness block M7. Isolated spikes need owner-approved scope; no LinkedIn automation. No task estimates, assignees, dates or production stack chosen here. Keep GitHub issues operational; link rather than duplicate requirement details. Use issue checkboxes for tasks and update spec task references when scope changes. Native GitHub sub-issue relationships are mandatory; see the hierarchy rules below. Native milestone assignment remains unconfigured; milestone labels provide planning alignment.

## Native issue hierarchy (verified 2026-11-25)
Use GitHub native sub-issues for Epic → Feature → PBI → Task. Epics are roots. Every non-epic must have exactly one parent of the preceding type, including documentation debt and conditional P1 work. Do not use a textual parent header as a substitute for the relationship; redundant parent headers may be removed after native verification. Documentation index links remain useful for navigation and stable-ID traceability.

For each newly created or moved issue, establish and verify the native relationship before declaring backlog setup complete. Check parent identity, type, milestone alignment, and absence of cycles; do not silently reparent. When the GitHub connector cannot write relationships, use owner-controlled authenticated GitHub CLI or another approved native GitHub mechanism. Report any unlinked issue explicitly; do not claim native hierarchy completion on the basis of Markdown links. Native links do not establish execution dependencies or authorize production coding.

Baseline: 128 issues, 119 expected native links; all 119 verified on 2026-11-25. Direct child counts matched the mapping; no orphan or incorrect parent was observed. Description cleanup is cosmetic and not a gate.

## Existing debt
Issues #5 and #7 map to M2.2; #6 maps to M2.1. Original documentation, pr-review and tech-debt labels retained. They are not core implementation. M0 historical issues closed with existing governance evidence; M1/M2 remain in review despite merged PRs.
