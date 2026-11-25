# MVP scope

Version 0.1 | Status: Proposed | 2026-11-25

## In scope
- LinkedIn Articles as the sole destination.
- Markdown, DOCX and pasted rich text import (FR-01–03).
- Destination-specific conversion, preview and reconciliation report (FR-04–06, FR-10).
- Embedded media extraction and ordered manual insertion assistance (FR-07, FR-09).
- Rich-text clipboard handoff with plain-text fallback (FR-08).
- Local-first, deterministic and privacy-conscious operation (NFR-01–07).

## Conditional / stretch
Basic editing and recovery package (FR-11–12); direct inline image paste only if verified. Supported formatting means evidenced support for a specific browser/editor/profile, not every feature of the source format.

## Deferred
Automatic native draft creation, auto-publishing, LinkedIn DOM automation, additional publishing destinations, user accounts, cloud storage/sync, AI rewriting, scheduling, full authoring studio, legacy .doc, PDF import and collaborative editing. Revisit only with evidence and owner approval.

## Format boundary (candidate)
Baseline: paragraphs, Unicode text, headings, emphasis, links, lists and breaks. Investigate code blocks, quotes, tables, nested lists and images; preserve, transform with disclosure, or provide manual/recovery path. Complex DOCX layout, macros, tracked changes, comments, equations and embedded objects must be detected or explicitly rejected as outside the supported subset; no promise of pixel-perfect Word layout.

## Release gate
All P0 requirements and agreed acceptance tests pass; every supported test fixture reconciled; target-editor paste and saved-draft checks recorded; no unresolved critical security or silent-loss defects. If direct image transfer fails, assisted placement is an acceptable MVP path. If rich-text handoff fails for the agreed browser baseline, revisit the MVP rather than silently reducing it to plain text.

See [PRD](product-requirements.md) and [acceptance criteria](../testing/acceptance-criteria.md).
