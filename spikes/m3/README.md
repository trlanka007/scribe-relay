# M3 disposable feasibility kit

Owner authorized isolated synthetic feasibility experiments after PR #137. This does not approve the PRD, architecture, production dependencies, publication or LinkedIn automation.

## Run locally
From the repository root, run `python -m http.server 8765 --bind 127.0.0.1`, then open `http://localhost:8765/spikes/m3/clipboard/` in Edge and Chrome. Stop the server afterward. Alternatively open index.html directly; record origin and secure-context behavior separately. Do not expose the server externally.

1. Click Copy HTML + plain text and paste into the diagnostic receiver. Record MIME types, text, formatting markup and any error. The receiver displays strings as inert text and never executes pasted markup.
2. Repeat with explicit plain text and manual selection fallback. Record failure without claiming rich copy success. Test a denied clipboard permission where the browser exposes the control.
3. Use the existing manual run sheet (../../docs/testing/manual-linkedin-article-run-sheet.md) for the actual LinkedIn paste and reopen. Only the human tester interacts with LinkedIn. Do not publish.
4. For F05/F06 open media/index.html, copy rendered image with surrounding anchors, and inspect draft paste/reopen. For native upload use the [local PNG exporter](media/export.html) rather than assuming SVG is accepted. Follow the [media run sheet](../../docs/testing/manual-linkedin-media-run-sheet.md). Record original and PNG hashes, order, caption/alt text, placement and cover behavior separately.

## Parser evaluation
The Markdown fixture includes headings, Unicode, emphasis, inline and fenced code, hyperlink, ordered/nested list, quote, divider, table, local and missing image references, raw HTML and unsafe link. Expected: account for all content, report unresolved references, never fetch assets implicitly, never execute raw HTML or unsafe links. Compare a token/AST-capable Markdown parser with another candidate; compare DOCX XML/package inventory with a semantic library. No candidate selected as production dependency. DOCX fixture and executable comparisons are next; no parser results are claimed here.

## Evidence and gates
| Task | Artifact / state |
|---|---|
| #82–85 | Existing manual worksheet; actual browser/OS and target results pending |
| #86 | Clipboard probe created; browser runtime verification pending |
| #87 | F08 real-browser test pending |
| #88 | SVG, placement HTML and PNG exporter created; browser export and saved-file hash verification pending |
| #89–90 | Actual LinkedIn image experiments pending |
| #91 | Markdown seed created; DOCX and inventory refinement pending |
| #92 | Parser comparison pending |

For every run record date, browser/OS or parser version, origin, fixture identity (git hash-object or SHA-256 with algorithm named), copy method, expected/actual results, error/recovery and limitations. Never store private clipboard content or authenticated URLs. All destination compatibility statuses remain Unknown until actual evidence. No issue is closed merely because an artifact exists.
