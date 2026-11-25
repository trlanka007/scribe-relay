# Product roadmap

Version 0.1 | Status: Proposed | 2026-11-25

Sequence is milestone-based, not a calendar commitment.

| Milestone | Outputs | Exit gate |
|---|---|---|
| M0 Repository | README, governance, owner review workflow | Complete |
| M1 Discovery | Vision, competitive and brand research | PR #1 merged; explicit status acceptance remains to be recorded |
| M2 Requirements | PRD, MVP scope, roadmap, acceptance criteria | Owner approves requirements and proposed metrics |
| M3 Feasibility | LinkedIn platform evidence, clipboard/media experiments, compatibility matrix | Critical handoff and media risks resolved or scope revised |
| M4 Experience | User workflows, issue resolution, preview/handoff UX | Owner approves interaction model |
| M5 Architecture | Document model, conversion spec, adapters, ADRs, stack tradeoffs | Owner approves architecture |
| M6 Engineering readiness | Security, privacy, testing, development and deployment standards | Release gates and engineering controls agreed |
| M7 Implementation | Vertical slice then remaining P0 capabilities | Acceptance suite and real draft validation pass |
| M8 Release | Private pilot, feedback, operational readiness | Owner approves release; public brand clearance as applicable |

## Post-MVP candidates
Additional destination adapters (personal blogs, WordPress, others based on demand and supported integrations); recovery/export packages; optional editing and AI assistance; optional persistence. Prioritize using measured manual effort, conversion failures, user feedback and platform feasibility rather than feature count.

## Dependencies
LinkedIn editor behavior and platform terms; browser clipboard capabilities; import library fidelity and security; representative sanitized fixtures. Feasibility precedes production stack selection. No production implementation before requirements and architecture approval.

## Risk-driven sequencing
Validate rich-text paste first, then source inventory and images, then unsupported transformations. Compare effort against ToolHa and manual import using identical fixtures. If platform constraints invalidate core value, reassess product scope before investing in infrastructure.

## Execution detail
See the [zoomable milestone execution plan](../engineering/milestone-execution-plan.md) for work packages, task seeds, dependencies and evidence gates. Architecture hypotheses are in the [C4 views](../architecture/c4/README.md). These do not change approved scope or select a stack.
