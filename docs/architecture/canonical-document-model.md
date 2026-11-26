# M5.2 — Canonical document model and provenance review

Status: provisional review material; not an approved schema | 2026-11-25 ET
Task #100 (M5.2.a), parent PBI #67 as recorded in issue. M3.4 and M5.1 prerequisites remain open. This is review preparation, not execution or acceptance of the blocked architecture gate. Based on [solution architecture](solution-architecture.md), [ground-level C4](c4/04-detail.md), [parser evidence](../research/parser-feasibility-synthesis.md) and FR-02/03/07, AC-01/02/04/08.

## Model boundaries

Source evidence, canonical semantics, binary assets, destination conversion and report are distinct models. The canonical model does not encode LinkedIn formatting, clipboard MIME representations or UI status. It preserves authored semantics and provenance; adapter policy is applied to a separate output revision. Source inventory is independent of the semantic extraction output and cannot be reconstructed solely from it.

| Concept | Candidate fields and responsibility |
|---|---|
| Source snapshot | Source ID, immutable bytes or captured representations, media type, encoding, content digest, inventory policy version; session-local |
| Source locator | Discriminated locator: byte range for Markdown, part/path and optional text range for DOCX, captured representation/path for rich text |
| Inventory unit | Unit ID, source locator, kind, content or recoverable reference, story/order, parent/children where appropriate, accounting role |
| Document | Model version, source snapshot reference, ordered body nodes, auxiliary stories, metadata candidates, import diagnostics |
| Node | Node ID, kind, ordered children, semantic attributes, source unit references, optional generated-value reason |
| Asset | Asset ID, content digest, verified media type, byte size, local content handle; no placement fields |
| Media occurrence | Occurrence ID, node ID, asset ID or unresolved reference, locator, order, caption/alt provenance, role |
| Import reconciliation | Source unit to canonical node/reference mapping, coverage evidence, transformations, recovery and blockers |
| Revision | Immutable identity for current semantic result, source/policy/model versions; destination and user edits tracked separately |

Identifiers are opaque, scoped to the snapshot and inventory/model policy. Deterministic identity across identical input/options/version is a goal; exact algorithm and cross-version stability are open. Do not use text or asset hash alone as occurrence identity. Changing a source snapshot or interpretation policy creates a new revision. Never expose document hashes or content to telemetry.

## Provenance and accounting

- Markdown: use half-open UTF-8 byte intervals [start,end) into the original captured bytes; require valid code-point boundaries. Preserve CRLF, Unicode and syntax spans. Block token maps may guide interpretation but do not prove inline coverage. Separate syntax/trivia accounting from authored content; raw HTML remains inert or explicitly rejected.
- DOCX: identify package part, structural path with explicit namespace and sibling-index convention, optional text range with declared coordinate unit. Relationship IDs are scoped to their source part. Auxiliary stories are inventoried separately; do not concatenate headers, footnotes and body as though they have one authored order. Track missing/unbound/invalid/external references without fetching.
- Rich text: capture representations received by explicit user action. Record HTML tree locator and plain representation separately when available; the plain representation may be an alternative of the same selection rather than additional authored text. Cannot claim fidelity to the originating editor beyond captured source.
- Distinguish hierarchical structural units from atomic accounting units. Parent/container summaries may reference children but cannot double-count their authored content. Independent inventory must cover authored text, structure and asset occurrences, including unrecognized items; byte coverage alone is not semantic accounting.

## Candidate semantic vocabulary

| Block / inline family | Candidate semantics |
|---|---|
| Document/story | Ordered body; auxiliary stories separate; title candidates require confirmation |
| Paragraph/heading | Ordered inline spans; heading level where known; explicit breaks |
| Text/emphasis | Text, strong/emphasis/underline/strike when observed, unknown style metadata |
| Link | Label/content children, original target provenance, resolved/unsafe/unresolved state; raw target never executable |
| List/list item | Ordered/unordered, nesting, start value if known, children and numbering provenance |
| Quote/divider | Structural boundary, ordered children where applicable |
| Code | Literal text including whitespace; optional language evidence |
| Table/row/cell | Ordered rows/cells, explicit spans if known; complex structures retained or rejected with evidence |
| Media | Occurrence reference; caption/alt and placement context, separate cover candidate role |
| Unsupported/unknown | Recoverable reference and diagnostic; no fabricated semantic interpretation |

This vocabulary is not a supported-input or destination compatibility promise. Complex numbering, tracked changes, text boxes, nested/merged tables and auxiliary content need further inventory validation. If reliable accounting is impossible, reject rather than return successful partial output.

## Representative examples (illustrative, not measured)

### A — Markdown source spans

Source bytes for `# Café\n\nHi\n` (UTF-8, LF): 12 bytes. Heading marker + space [0,2), authored heading text [2,7), line/blank separators [7,9), authored paragraph [9,11), terminal LF [11,12). The é occupies two bytes. An independent ledger accounts for all intervals, then heading H1 maps authored span [2,7) and paragraph P1 maps [9,11); structural syntax is separately accounted. A parser that returns only H1 and P1 without trustworthy coverage cannot establish completeness.

### B — DOCX repeated image and table

```text
main story: P1 -> image I1 -> table T1(row R1: C1, C2) -> image I2 -> P2
auxiliary story: header H1
asset A1: one local verified image
I1 -> A1 via document part relationship rId7
I2 -> A1 via document part relationship rId7
H1: separately inventoried text, not implicitly inserted in body
```

Two distinct occurrences and locators remain even if bytes are deduplicated. Cell order is part of semantics; reversing cells with identical aggregate text counts must fail ordered reconciliation unless an explicit, reviewed transformation accounts for it. A header relationship with rId7 would be resolved in header scope, not document scope.

### C — Unresolved image and unsafe link

An image occurrence retains its original relative/external reference, source locator and unresolved reason; it has no local asset handle. A link retains label and original target provenance but marks an unsafe target non-emittable. Safe recovery options are determined later; no implicit fetch or executable link. If unsupported material cannot be accounted for reliably, import is blocked, not merely acknowledged.

## Model invariants and proposed verification

| Invariant | Negative example / expected behavior |
|---|---|
| Ordered graph is well-formed, acyclic, scoped to current revision | Dangling child, duplicate occurrence ID or cross-revision reference -> reject |
| Source locators valid in their snapshot and coordinate system | Out-of-range byte span or split UTF-8 character -> reject |
| Atomic inventory coverage is complete, multiplicity and order reconciled | Missing cell, repeated text mistaken for one occurrence or unexplained reorder -> block success |
| Every canonical authored value traces to source evidence; generated values explicitly identified | Invented text or unexplained normalization -> block success |
| Asset identity independent of placement | Two drawings with same bytes -> retain two placements; missing asset remains explicit |
| Auxiliary stories and unsupported material accounted without invented body order | Header silently discarded -> block success |
| Unsafe references inert and external assets never fetched implicitly | Raw executable URL or unexpected network request -> block unsafe output |
| Deterministic semantics for same input/options/model policy | Equivalent normalized result and report on repeated run; exclude session metadata only |
| Immutable source, separate user/adapter revisions | Adapter overwrites source or stale acknowledgement survives revision change -> reject |

Accounting is necessary but not sufficient for preservation: source-to-output classifications and target evidence belong to M5.3. Acknowledgement does not waive missing accounting or safety checks.

## Review decisions and limits

Review locator granularity, atomic accounting policy, node identity algorithm, schema versioning/migration, content digest strategy, unsupported-source boundary, asset validation and memory limits. No executable schema, production parser, serialization format, storage or framework selected. Examples above are conceptual; no runtime test performed. M3.4/#151 and M5.1 approval remain outstanding. M5.3 contract review depends on accepted model boundaries. No task closure, gate waiver or production implementation.
