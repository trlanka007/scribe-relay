# Work-package catalog — 1,000-foot view

Proposed | 2026-11-25. Parent milestones and gates: [execution plan](milestone-execution-plan.md). Each row is an independently reviewable package; detailed tasks live in [backlog](execution-backlog.md). All future packages are proposed, not scheduled.

| ID | Activity / deliverable | Dependency | Completion evidence |
|---|---|---|---|
| M0.1 | Repository, owner controls, agent instructions | — | PRs #1–3 and main protections |
| M1.1 | Vision, audience, problem and boundaries | M0.1 | vision.md; owner acceptance |
| M1.2 | Competitor positioning and test evidence | M1.1 | competitive-analysis.md, competitor-evaluations.md |
| M1.3 | Working brand and clearance risks | M1.1 | brand-analysis.md; public clearance deferred |
| M2.1 | PRD and prioritized requirements | M1.1 | product-requirements.md; owner review |
| M2.2 | MVP boundary and roadmap | M2.1 | mvp-scope.md, roadmap.md |
| M2.3 | Acceptance criteria and measurement | M2.1 | acceptance-criteria.md; agreed metrics |
| M3.1 | Platform/API/policy evidence | M2.1 | feasibility-and-constraints.md; source recheck |
| M3.2 | HTML/clipboard and persistence tests F01–F04,F07–F08 | M3.1 | per-browser runs and matrix |
| M3.3 | Image paste and assisted placement F05–F06 | M3.1 | media fixture and recorded outcomes |
| M3.4 | DOCX/Markdown extraction F09–F10 | M2.1 | parser comparison and supported subset |
| M3.5 | Benchmark protocol/baseline F11 | M3.2 | manual/ToolHa baseline; final result deferred to M7 |
| M3.6 | Feasibility synthesis and gate | M3.2–5 | risk disposition, revised scope/profile if needed |
| M4.1 | Personas, jobs and journey | M2.2 | docs/design/user-workflows.md |
| M4.2 | Import, preview, report and recovery wireframes | M4.1,M3.2 | docs/design/ux-design.md |
| M4.3 | Handoff/media, error and accessibility flows | M4.2,M3.3 | reviewed scenarios and keyboard path |
| M5.1 | Context, containers and deployment alternatives | M3.6,M4.3 | reviewed C4 views and solution-architecture.md |
| M5.2 | Canonical model and provenance | M3.4,M5.1 | canonical-document-model.md, examples |
| M5.3 | Conversion rules and destination contracts | M3.2,M5.2 | conversion-specification.md, destination-adapters.md |
| M5.4 | Stack tradeoffs and ADRs | M5.1–3 | technology-stack.md and accepted ADRs |
| M6.1 | Security/privacy and threat model | M5.1–3 | security-and-privacy.md, mitigations |
| M6.2 | Test strategy and fixture coverage | M2.3,M5.3 | test-strategy.md, traceability |
| M6.3 | Dev conventions, CI/CD and deployment | M5.4 | development-guide.md, deployment-strategy.md |
| M7.1 | Vertical slice: one source to clipboard | M6 gate | tested end-to-end slice, no silent loss |
| M7.2 | Remaining source importers and assets | M7.1 | FR-01–03,07 tests |
| M7.3 | Compatibility engine and destination conversion | M7.1,M7.2 | FR-04–06,10 tests |
| M7.4 | Preview, recovery, clipboard and handoff | M7.3 | FR-05–09 and accessibility tests |
| M7.5 | Regression, security, actual draft and final F11 benchmark | M7.4 | AC-01–12 evidence and defect disposition |
| M8.1 | Private pilot and feedback | M7 gate | pilot findings, consent and support process |
| M8.2 | Release readiness and rollback | M8.1 | release checklist, known limitations, rollback test |
| M8.3 | Owner release decision and roadmap update | M8.2 | release approval; brand clearance if public |

Paths without current files are planned deliverables, not broken links. Review gate definitions in parent plan. M1–M3 existing documentation is linked in [index](../README.md).
