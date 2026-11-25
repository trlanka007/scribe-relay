# M3.4 OPC relationship probe

Refs #91 #92. Run `python -B spikes/m3/parsers/opc_probe.py` from repository root. Ten unittest cases passed in an in-memory Python 3.12 source execution on 2026-11-25, including raw and percent-encoded control targets; the exact file invocation remains pending. PR #142 separately records 11 passing safety tests at 2d65ca5 and a traversal mutation check.

## Candidate design
Resolve references by (source part, relationship ID), not globally. Inventory ordered occurrences independently of asset identity: an image referenced twice is two placements but may share one asset. Distinguish resolved, missing, invalid, external and unbound references. Never fetch external resources implicitly. Retain source part and structural path. Avoid recursive graph expansion without visited-set and resource bounds.

## Proposed supported subset (not accepted)
Main document paragraphs, headings, emphasis, ordinary lists, links, simple tables, inline embedded raster images. Complex numbering, nested/merged tables, floating shapes, tracked changes, headers/footers, footnotes, comments, charts and embedded objects require explicit inventory and recovery or rejection; no silent omission. External media remains unresolved/manual. This is a candidate boundary, subject to owner review and feasibility evidence, not a scope reduction.

## Limitations
Synthetic in-memory part map, not an OPC-compliant package parser. No content-type validation, strict namespace coverage, full URI semantics, real Word fixtures or browser tests. Conservative target rejection may exclude valid OPC constructs; unresolved targets must be reported. XML path is structural provenance, not a byte span. No production dependency or compatibility profile change. Actual execution and integrated package comparison remain pending.
