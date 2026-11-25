# Feature specification: Vertical slice

Status: Proposed; blocked | Feature #42 | PBI #73 | M7.1

## User story US1 (P0)
As an author, I can transfer one approved source document into a LinkedIn draft with transparent accounting.

## Acceptance scenarios
- Given an approved representative source, when I import, preview and copy it, then every element is accounted for and the target editor can be manually verified after reopening.
- Given an unsupported element or denied clipboard permission, when conversion or copy fails, then the reason and recovery path are visible.

## Requirements and success criteria
FR-01–10; AC-01–06,08. See [PRD](../../docs/product/product-requirements.md) and [acceptance criteria](../../docs/testing/acceptance-criteria.md); agreed targets apply, candidate targets are not measured results.

## Scope and exclusions
Only approved LinkedIn Articles MVP; no publishing automation, mandatory upload or AI. P1 and future destinations excluded. See [MVP scope](../../docs/product/mvp-scope.md).

## Dependencies and open questions
M6 readiness; M2/M5 approval; M3 profile evidence. Clarify exact supported subset, profile, fixtures and applicable owner decisions before plan approval. No code-level design chosen.

## Next
[Plan](plan.md) | [Tasks](tasks.md)
