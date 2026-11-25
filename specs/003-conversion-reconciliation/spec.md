# Feature specification: Conversion and reconciliation

Status: Proposed; blocked | Feature #44 | PBI #75 | M7.3

## User story US1 (P0)
As an author, I can understand exactly how my source content will be transformed for LinkedIn.

## Acceptance scenarios
- Given the same source, options and versioned profile, when converting repeatedly, then normalized output and report are equivalent and all source IDs are accounted for.
- Given an unknown or unsupported feature, when previewing, then it is not represented as preserved; reason and recovery are explicit.

## Requirements and success criteria
FR-04–06,10; AC-02,03,05,08. See [PRD](../../docs/product/product-requirements.md) and [acceptance criteria](../../docs/testing/acceptance-criteria.md); agreed targets apply, candidate targets are not measured results.

## Scope and exclusions
Only approved LinkedIn Articles MVP; no publishing automation, mandatory upload or AI. P1 and future destinations excluded. See [MVP scope](../../docs/product/mvp-scope.md).

## Dependencies and open questions
M7.1, M7.2; approved profile and adapter contract. Clarify exact supported subset, profile, fixtures and applicable owner decisions before plan approval. No code-level design chosen.

## Next
[Plan](plan.md) | [Tasks](tasks.md)
