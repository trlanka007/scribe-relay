# Platform compatibility experiment protocol

Version 0.1 | Status: Proposed; no new hands-on results | 2026-11-25

## Existing observation
The user's ToolHa experiment qualitatively established that formatted text could be pasted into LinkedIn Articles. Inline images were trimmed from the shared output; the cause and per-element outcomes were not measured. See [competitor evaluations](competitor-evaluations.md).

## Test setup
Candidate baseline: current desktop Edge and Chrome on Windows; record exact versions, OS, date, account/editor context (personal article, not newsletter), copy method and fixture hash. Firefox/Safari are follow-up candidates, not release commitments. Use synthetic content only; no real customer data or shared draft URLs. Use a fresh unpublished draft per run. Disable conflicting extensions as needed and record that fact.

## Procedure
1. Review the fixture and record expected semantic inventory.
2. Open the local HTML fixture in the browser, select rendered body and copy normally. This establishes a low-cost rich-text baseline without application code.
3. Paste into a fresh LinkedIn Article body; enter title separately. Record visible structure and link targets with normal editor controls, not DOM inspection or automation.
4. Navigate to Manage > Drafts after autosave, reopen, and repeat observations. Do not publish or share.
5. Repeat using a user-triggered local clipboard spike (one item with text/html and text/plain) only after governance approval; compare with manual selection.
6. For media, test copy of rendered image alongside text, then separate local PNG insertion using native media controls. Record exact behavior and number of steps. Never use sensitive images or remote tracking URLs.
7. Record per-element results in the matrix; retain sanitized evidence locally or in repo only with owner approval. Delete test drafts manually when finished.

## Experiments
| ID | Scope | Expected evidence |
|---|---|---|
| F01 | Paragraphs, Unicode, breaks | Normalized text matches before and after reopen |
| F02 | Heading levels and inline emphasis | Semantic/style mapping and any flattening |
| F03 | Links, ordered/unordered/nested lists | Link targets, order, nesting |
| F04 | Quotes and dividers | Native-equivalent representation or transformation |
| F05 | Inline image paste | Whether retained, uploaded, stripped or altered |
| F06 | Manual image/cover insertion | Placement anchors, captions, alt text if available, time |
| F07 | Tables and code | Text completeness, structure, usable fallback |
| F08 | Clipboard permissions and browser variations | Success/failure, secure context, user activation, fallback |
| F09 | DOCX parser comparison | Human-reviewed source inventory vs parser output; complex features and safe rejection |
| F10 | Markdown parser comparison | Dialect, HTML handling, asset references and error cases |
| F11 | Effort comparison | Three paired runs per fixture, counterbalanced; active time and edits |

F09/F10 require disposable parser spikes and additional fixtures; neither library nor stack is selected. F11 follows a functioning conversion candidate. Current protocol is not evidence of test completion.

## Result record template
Run ID; date; tester; browser/OS; fixture hash; copy method; element ID; expected; actual on paste; actual on reopen; outcome (preserved/transformed/manual/unsupported/unknown); evidence reference; recovery steps; duration; notes.

## Decision gates
Approve browser/profile only after repeatable F01–F08 evidence. If core rich text fails, revise MVP. If images fail direct transfer, verify manual path. If parser cannot account for content, reject unsupported files or revise scope. Compare against PRD and acceptance criteria; no automatic claim of validation.
