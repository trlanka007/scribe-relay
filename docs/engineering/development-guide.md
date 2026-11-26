# M6.3 — Development guide review

Status: proposed conventions, not approved or implemented | 2026-11-26 ET
Task #105 (M6.3.a), parent PBI #72 as recorded in issue. M5.4 stack approval remains outstanding. Review preparation only. See [spec-driven workflow](spec-driven-workflow.md), [test strategy](../testing/test-strategy.md), [security review](../architecture/security-and-privacy.md), [deployment strategy](deployment-strategy.md) and repository AGENTS.md.

## Entry and repository organization

Production work starts only after explicit M2/M5 approvals and M6 readiness. M3 disposable experiments remain isolated under spikes/m3 and require approved scope. Do not promote experiments or their dependencies into production by default.

Candidate logical source layout (paths and runtime-specific project structure subject to accepted ADRs):
- src/domain: canonical semantics, invariants and provenance; no UI, destination or network dependency.
- src/import: source-specific importers and independent inventory; no destination policy.
- src/conversion: deterministic orchestration, rule application and reconciliation.
- src/destinations: data-only profiles and mapping implementations; no authenticated editor integration.
- src/safety: bounded input, asset and final representation validation; applied across boundaries.
- src/application: workflow/revision coordinator and explicit handoff ports.
- src/ui: import, preview, report, recovery and accessible controls.
- tests: domain, integration, local browser, synthetic fixtures and independently reviewed expected inventories.
- docs and specs: requirements, decisions, plans, tasks and evidence.

These are conceptual modules, not mandated folders, package boundaries or a framework choice. Keep dependencies directed toward stable domain contracts; UI and infrastructure adapt ports, domain does not import UI or platform APIs. Prefer simple modules over premature separate deployables. No folders or source files created by this guide.

## Development conventions

Use accepted runtime strict type checking where available, explicit validation of untrusted boundary data, stable error codes and actionable safe diagnostics. Preserve immutable source and revision identity; make effects explicit. Avoid global mutable conversion state, hidden I/O, automatic fetching or destination-specific assumptions in importers. Cancellation must prevent stale output from becoming eligible. Tests verify final output, not just mapping claims.

Use consistent formatter, linter, naming and test conventions appropriate to selected stack. Pin supported toolchain and dependency graph; document reproducible setup and commands after ADR acceptance. No fabricated commands or version pins here. Review licenses, advisories, transitive dependencies and browser/runtime compatibility. Keep research environments separate from production toolchain.

## Spec-driven delivery and pull request review

Follow constitution -> specify -> clarify -> plan -> tasks -> analyze -> implement -> verify. Refine M7 tasks into independently testable slices only after prerequisites. No unlinked issues: maintain native Epic/Feature/PBI/Task hierarchy and verify parent links. Use feature branches from current main; no direct main changes or force pushes. Owner approves merge.

Every PR includes objective, stable task ID and linked GitHub issue, scope, prerequisites, requirement/test references, changes, actual verification evidence, limitations, risk and recovery. Distinguish primary task from related dependency and completion from progress. Native PR-to-task linkage is preferred; textual cross-reference is supplemental, and connector limitations must be disclosed. Do not auto-close partial tasks; closing keywords require accepted completion evidence. A review merge is not gate approval.

Proposed merge checklist:
- Scope and task linkage verified; spec/plan/task alignment reviewed.
- Relevant format/lint/type/build/unit/integration/local-browser checks succeed; report actual commands/results or explicit not-run.
- Independent inventory and negative regression cases cover changed content paths.
- No unsafe/unaccounted output, private fixtures, secret, hidden network request or false target support claim.
- Dependencies and license/security changes reviewed; docs/evidence updated.
- Owner review and applicable branch protection checks satisfied.

A future task-link validation check can require valid existing issue references and verify native association if supported by approved GitHub APIs. Do not assert current branch rules enforce this or that the connector creates native links. No ruleset or CI change in this PR.

## Proposed CI stages

| Stage | Intent | Blocking condition after approval |
|---|---|---|
| Source hygiene | Format, lint, type checks and secret scan | Relevant check failure |
| Reproducible install/build | Approved toolchain, lockfile, build and artifact identity | Drift, build failure or unreviewed dependency |
| Domain/integration | Unit/fixture/negative tests and final reconciliation | Test failure, unsafe/unaccounted regression |
| Local browser | Core flow, clipboard/local harness, keyboard and network controls | Agreed baseline failure |
| Dependency and artifact review | License/advisory review, provenance and safe evidence | Unresolved critical risk or unauthorized dependency |
| Manual review | Actual destination evidence when impacted; task and owner review | Required evidence missing |

CI runs on synthetic data only; never automate LinkedIn or use account credentials. Use least-privilege job permissions, reviewed/pinned third-party actions, isolated runners for untrusted changes, no secrets in untrusted PR contexts, bounded retention and sanitized logs. No deployment credentials in ordinary validation jobs. Exact workflows, check names and branch rules require owner approval and actual setup verification.

Definition of done: acceptance criteria satisfied with evidence, no undisclosed content loss, security controls verified as applicable, documentation and native hierarchy consistent, owner approval recorded. Do not equate planned test coverage with execution or use coverage percentage alone as a release gate.

No production code, tooling setup, CI workflows, branch policy changes, task closure or approved engineering standard in this iteration.
