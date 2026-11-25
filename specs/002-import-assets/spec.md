# Feature specification: Import and assets

Status: Proposed; blocked | Feature #43 | PBI #74 | M7.2

## User story US1 (P0)
As an author, I can import supported Markdown, DOCX and rich text without losing track of any source content or media.

## Acceptance scenarios
- Given approved fixtures for each source format, when imported, then every inventory item maps to a canonical record or explicit rejection and media references are ordered and recoverable.
- Given malformed, unsafe or unsupported content, when imported, then safe rejection or disclosed recovery occurs without implicit network fetch.

## Requirements and success criteria
FR-01–03,07; AC-01,04. See [PRD](../../docs/product/product-requirements.md) and [acceptance criteria](../../docs/testing/acceptance-criteria.md); agreed targets apply, candidate targets are not measured results.

## Scope and exclusions
Only approved LinkedIn Articles MVP; no publishing automation, mandatory upload or AI. P1 and future destinations excluded. See [MVP scope](../../docs/product/mvp-scope.md).

## Dependencies and open questions
M7.1; F09/F10; approved format subset. Clarify exact supported subset, profile, fixtures and applicable owner decisions before plan approval. No code-level design chosen.

## Next
[Plan](plan.md) | [Tasks](tasks.md)
