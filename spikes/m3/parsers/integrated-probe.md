# Integrated synthetic package probe

Refs #91 #92. Run `python -B spikes/m3/parsers/integrated_probe.py` from repository root. Five test cases cover ordered main-body text, repeated asset occurrences, external links and header references, missing assets, and a table reorder. Runtime results are pending; these are expectations, not passing results.

Uses the merged PR #142 preflight and PR #143 relationship probe together on a small generated ZIP. The image part is a placeholder, not a valid PNG; this is not a Word-authored or schema-validated DOCX. Header content is not included in the main-body text inventory; its relationship is observable and requires separate accounting or rejection in production. The experiment checks one known main-part path and does not validate the relationship type or general OPC content types. The reorder test detects a table moving across paragraphs, not every possible semantic reorder.

## Evidence carried forward
- PR #142: eleven tests and traversal mutation check, as recorded in merged PR.
- PR #143: eleven tests passed by in-memory Python 3.12 execution; review strengthened malformed target rejection.
- Initial Markdown comparison: candidate parsers differed on unsafe link representation. Neither replaces independent reconciliation and URL policy.

## Next decision
Keep structural provenance and relationship occurrence identity distinct from deduplicated asset identity. Require real generated DOCX comparison, explicit unsupported-part accounting and bounded safe rejection before treating the candidate subset as verified. No destination profile or production dependency changes.
