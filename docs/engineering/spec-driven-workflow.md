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

This adapts the upstream workflow; it does not claim official Spec Kit commands or GitHub native hierarchy are installed. The existing PRD and acceptance criteria are the master scope; feature specs are narrower derivations.

## Labels
- type:epic, type:feature, type:pbi, type:task — exactly one per backlog item.
- milestone:M0 through milestone:M8 — planning alignment, not native GitHub milestone assignment.
- area:core-implementation — P0 M7 delivery and verification only; includes the M7 epic, features, PBIs and tasks.
- area:optional-enhancement — conditional P1 items, not core MVP.
- area:governance/product/research/design/architecture/engineering/release/documentation — distinguish supporting work.
- status:review/ready/blocked/done/deferred — readiness snapshot; ready means eligible for refinement, not that all dependencies or spike permissions have been cleared. Reconcile labels and issue state as gates change.
- priority:P0/P1 — production scope where assigned; kind:validation for explicit verification seeds.

## Operational rules
No direct main writes; owner approval for merges. M2/M5 explicit approvals and M6 readiness block M7. Isolated spikes need owner-approved scope; no LinkedIn automation. No task estimates, assignees, dates or production stack chosen here. Keep GitHub issues operational; link rather than duplicate requirement details. Use issue checkboxes for tasks and update spec task references when scope changes. Native sub-issues and milestone API writes were not exposed by the current connector; Markdown relationships and labels are the supported baseline.

## Existing debt
Issues #5 and #7 map to M2.2; #6 maps to M2.1. Original documentation, pr-review and tech-debt labels retained. They are not core implementation. M0 historical issues closed with existing governance evidence; M1/M2 remain in review despite merged PRs.
