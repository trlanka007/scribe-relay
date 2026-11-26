# Documentation index

Status: Discovery, requirements and feasibility documentation merged; experiments pending | 2026-11-25

## Discovery (PR #1)
- [Vision](product/vision.md)
- [Competitive analysis](product/competitive-analysis.md)
- [Brand research](research/brand-analysis.md)
- [Competitor evaluations](research/competitor-evaluations.md)

## Requirements (PR #4)
- [PRD](product/product-requirements.md)
- [MVP scope](product/mvp-scope.md)
- [Roadmap](product/roadmap.md)
- [Acceptance criteria](testing/acceptance-criteria.md)

## Feasibility (current review)
- [Platform constraints](architecture/feasibility-and-constraints.md)
- [Dated official platform evidence recheck (M3.1)](research/official-platform-evidence-2026-11-25.md)
- [Manual Article paste/reopen run sheet (M3.2)](testing/manual-linkedin-article-run-sheet.md)
- [Interim parser feasibility synthesis (M3.4)](research/parser-feasibility-synthesis.md)
- [Manual media run sheet (M3.3)](testing/manual-linkedin-media-run-sheet.md)
- [Preparation effort benchmark (M3.5)](research/preparation-effort-benchmark.md)
- [Interim feasibility gate review (M3.6)](research/feasibility-gate-review.md)
- [Experiment protocol](research/platform-compatibility.md)
- [Compatibility matrix](testing/formatting-compatibility-matrix.md)
- [Synthetic fixtures](../tests/fixtures/README.md)

## Experience design (proposed)
- [Author personas, jobs and journeys (M4.1)](design/user-workflows.md)
- [Import, preview and report wireframes (M4.2)](design/ux-design.md)
- [Handoff, media recovery and accessibility (M4.3)](design/handoff-and-recovery.md)

## Zoomable planning and architecture (proposed)
- [Milestone execution plan: 5,000 to ground level](engineering/milestone-execution-plan.md)
- [Work-package catalog](engineering/work-packages.md)
- [Execution backlog](engineering/execution-backlog.md)
- [C4-inspired architecture views](architecture/c4/README.md)
- [Solution architecture review preparation (M5.1)](architecture/solution-architecture.md)
- [Canonical model and provenance review (M5.2)](architecture/canonical-document-model.md)
- [Conversion specification review (M5.3)](architecture/conversion-specification.md)
- [Destination adapter and profile review (M5.3)](architecture/destination-adapters.md)
- [Technology stack evaluation (M5.4)](architecture/technology-stack.md)
- [Proposed stack ADRs (M5.4)](architecture/adr/proposed-stack-decisions.md)

## Engineering readiness (proposed)
- [Security and privacy threat model review (M6.1)](architecture/security-and-privacy.md)
- [Testing strategy and acceptance traceability (M6.2)](testing/test-strategy.md)
- [Development guide review (M6.3)](engineering/development-guide.md)
- [Deployment strategy review (M6.3)](engineering/deployment-strategy.md)

## Specification-driven backlog (proposed)
- [GitHub epic / feature / PBI / task index](engineering/github-backlog-index.md)
- [Spec-driven delivery workflow](engineering/spec-driven-workflow.md)
- [Feature specification seeds](../specs/README.md)

## Planned reviews
1. Discovery and requirements: merged baselines; explicit document acceptance labels remain to be recorded.
2. Feasibility: platform constraints, evidence and technical risks.
3. Experience design: user workflows and UX.
4. Architecture: canonical document model, conversion specification, destination adapters and ADRs.
5. Engineering readiness: security, privacy, testing, deployment and development standards.

## Governance
- **Proposed:** awaits owner review.
- **Accepted:** explicitly agreed by the owner.
- **Validated:** supported by recorded experiments, with scope and limitations.
- **Deferred:** deliberately outside the current scope.
- Unknown or undocumented is not equivalent to unsupported.

GitHub is the source of truth. Use branches and pull requests; merge only with owner approval. Record decisions, evidence, assumptions and unresolved questions separately. Do not treat roadmap features as implemented or select a production technology stack before evaluating requirements. No production implementation before requirements and architecture reviews. Disposable feasibility spikes require owner-approved scope, synthetic data, isolation from production code and documented results.
