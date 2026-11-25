# M3.4 parser feasibility synthesis — F09/F10

Status: interim evidence and proposed boundaries; not gate acceptance | 2026-11-25
Refs #91 #92. Scope remains as defined in the PRD and acceptance criteria.

## Evidence ledger

| Evidence | Observed or recorded result | Confidence boundary |
|---|---|---|
| [Initial comparison](../../spikes/m3/parsers/README.md), #139 | Markdown candidates recognize common constructs but differ on unsafe link representation; simple DOCX table and drawing inventory | Equivalent local script, not exact checkout; precise inline source spans unknown |
| [Safety probe](../../spikes/m3/parsers/safety-probe.md), #142 | Merged PR records 11 passing tests and traversal mutation check | Synthetic ZIP/XML only, not production preflight |
| [OPC probe](../../spikes/m3/parsers/opc-probe.md), #143 | Scoped IDs, missing/invalid/external references, repeated occurrences; 11 tests recorded passing | Conservative subset of URI handling; not full OPC |
| [Integrated probe](../../spikes/m3/parsers/integrated-probe.md), #145 | Five executable tests supplied | Runtime evidence not established in merged PR |
| [Generated DOCX](../../spikes/m3/parsers/generated-probe.md), #146 | Recorded 4 passing generated-document tests plus 11 OPC regression tests; ordered paragraphs/table agree, two image placements share one asset, header separately recoverable | Trusted generated fixture only; tested Pillow version differs from current pin |

These are historical run records, not a new independent execution. Do not add counts across repeated runs as unique tests.

## Candidate source subset (proposed, not destination compatibility)

| Construct | Candidate disposition | Remaining evidence |
|---|---|---|
| DOCX paragraphs, ordinary headings/emphasis, lists | Preserve text, semantics and order | Validate styles, numbering, whitespace and breaks against independent expectations |
| DOCX simple tables | Preserve cell order and boundaries | Multirow/multicell reconciliation; nested/merged recovery |
| DOCX inline embedded raster images | Preserve occurrence order, asset identity and original bytes | Validate image type, limits, captions/alt and actual placement |
| DOCX hyperlinks | Preserve label and validated target | Real generated hyperlink, anchor and invalid relationship tests |
| DOCX headers/footers, footnotes, tracked changes, text boxes, comments, charts, embedded objects | Inventory separately, report recoverable content or explicitly reject | Complete authored-part discovery, policy and recovery verification |
| Markdown common blocks and inline markup, tables | Preserve semantics and source text | Dialect decision, line/inline provenance and reconciliation |
| Markdown raw HTML, malformed syntax and unsafe URLs | Retain source accounting; inert handling or explicit rejection | Adversarial fixture suite, safe output checks |
| External/missing assets (all sources) | Report unresolved, offer manual recovery; no implicit fetch | Verify missing-reference and recovery behavior |

No feature is silently dropped. A candidate disposition is a hypothesis, not a promise of supported input or LinkedIn output. Where full authored-content accounting cannot be established, fail explicitly rather than emit a deceptively complete article.

## Architectural recommendations for M5/M6 (proposed)

1. Separate package safety, independent source inventory, semantic extraction and reconciliation. For Markdown, preserve original source spans and parser interpretation separately.
2. Track stable occurrence IDs, source-part/path or source-span provenance and ordered relationships. Deduplicate assets independently of their occurrences.
3. Distinguish semantic preservation, reported transformation, manual recovery, unsupported and unaccounted content. Unaccounted content blocks successful conversion. Compare ordering as well as multiplicity, not merely aggregate text.
4. Treat URL validation, package path normalization, content-type checks, resource limits and no-network policy as explicit security contracts. The synthetic safety limits are not the proposed production limits.
5. Evaluate candidate libraries in the eventual deployment environment before any ADR; Python probes are evidence, not a production language decision.

## Outstanding work and disposition

| Gap | Next action | Gate |
|---|---|---|
| Exact reproducibility, dependency drift | Run all committed probes, record exact versions and file identities; reconcile current pins with observed runs | M3.4 |
| Markdown source accountability and dialect | Extend F10 with malformed/raw HTML, unsafe URI variants and reference-style syntax; compare source spans and preserved text | M3.4 |
| DOCX unsupported content and safe rejection | Expand fixtures for auxiliary parts, hyperlinks, styles/numbering and complex structures; record explicit gaps | M3.4 |
| Complete reconciliation and security | Specify contracts and limits; verify against implementation before MVP acceptance | M5/M6/M7 |
| Actual clipboard/editor fidelity | Human F01–F08 paste/reopen runs, native media recovery | M3.2/M3.3 |
| Benchmark | Manual/ToolHa baseline now, functioning candidate comparison at M7 | M3.5/M7 |

M3.4 is not accepted, #91/#92 remain open, and F09/F10 cannot be marked fully validated. No compatibility matrix changes, production stack selection, scope reduction or gate waiver. This synthesis prepares the next experiments and the M5 review.
