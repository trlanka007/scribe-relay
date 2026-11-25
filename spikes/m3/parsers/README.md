# M3.4 parser comparison — initial evidence (F09/F10)

Run: 2026-11-25, isolated Linux Python 3.13.5 environment. Candidate versions: markdown-it-py 4.2.0, mistune 3.2.1, python-docx 1.2.0, Pillow 12.3.0. No production dependencies selected. The local experiment used the same synthetic Markdown text as fixture.md (normalized UTF-8 SHA-256 169d699993517435c87ee15388b718141a38799a1149a0ec4a9f20200fa5410e). The DOCX is generated in memory each run; no private inputs, network fetching or rendering of untrusted HTML.

## Reproduce
In a disposable virtual environment, install requirements.txt in this directory and run `python compare.py`. Record JSON stdout and environment. The local execution used an equivalent script with a fallback copy of the Markdown fixture; the committed script reads fixture.md directly. The exact committed checkout has not yet been independently executed.

## Observed results
| Check | markdown-it-py | Mistune AST |
|---|---|---|
| Headings, emphasis, lists, quote, code, divider | Corresponding tokens present | Corresponding nodes present |
| Table extension | table_open, row and cell tokens | table, row and cell nodes |
| Raw HTML | html_inline tokens | inline_html nodes |
| Safe hyperlink | href retained | URL retained |
| Local and missing image references | Both src values retained; alt label in token content rather than attrs.alt | Both URL values and child text retained |
| Unsafe javascript link | No link_open token for unsafe target | Link node retains javascript target |
| Provenance | Block token line maps exposed; inline token maps absent in observed link/image entries | AST structure exposed; precise source offsets not established |

The unsafe-link difference is important: absence of a link node cannot be equated with complete accounting of the source construct; retaining a target cannot be equated with safe output. Require source-level reconciliation and independent URL policy. Neither parser was allowed to render or fetch anything.

## DOCX synthetic expected inventory
Two headings (Title and Heading 2); Unicode paragraph with bold and italic runs; two numbered-style paragraphs; 2x2 table (Feature/Value, Alpha/One); image between Before image and After image anchors; one embedded PNG. Section metadata is not authored body content.

Observed package body order: p,p,p,p,p,tbl,p,p,p,sectPr. XML text includes every table cell; python-docx paragraphs alone omit table cells and expose an empty paragraph for the image. Separate table API exposes both rows and cells; inline_shapes count = 1; package contains word/media/image1.png and one drawing reference. All three executable assertions passed (table recognition, drawing/table inventory, paragraph-only omission). This is evidence of a simple case, not complete DOCX fidelity.

## Recommendation for next spike
Use semantic library extraction plus an independent inventory/reconciliation layer. For Markdown, compare token line mapping and source-span recovery before choosing a library. For DOCX, preserve ordered blocks, resolve relationship IDs and styles/numbering; do not rely on paragraphs alone. Before accepting F09/F10, extend fixtures to hyperlinks, tracked changes, footnotes, text boxes, nested/merged tables, external relationships, corrupt ZIP/XML, resource limits, malformed Markdown and unsafe URI variants. Implement explicit rejection and no implicit fetch; current probe accepts only trusted generated data and does not test hostile DOCX. Full per-element reconciliation and safe rejection remain pending.

Refs #91 #92. No compatibility matrix promotion or production stack decision.
