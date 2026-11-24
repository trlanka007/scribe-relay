# Competitor evaluation log

Status: Initial observations; incomplete evidence | 2026-11-24

Source: user-reported observations from the project conversation **Track formatter tests**. This baseline does not include raw clipboard payloads, original fixtures, or screenshots.

## ToolHa — initial test
- User reported that LinkedIn Article editor compatibility was fine after checking.
- User reported trimming off inline images and that the remaining output looked mostly fine to the naked eye.
- The shared output retained some literal Markdown heading markers; whether those markers persisted in the final LinkedIn editor is not established.
- The exact cause of image omission, link fidelity, list nesting, spacing and content completeness has not been measured.

Result: qualitative validation that externally formatted text can be transferred to LinkedIn Articles. This does not validate our own converter or establish a complete compatibility matrix.

## Markdown Publishing Toolkit
User encountered a different-language interface and chose not to continue testing. No fidelity verdict.

## Typefully
Evaluation requested in sibling conversation; no result established in this baseline.

## Other products
DraftBridge, DraftFlow and ScribeFlow: preliminary documentation-based research only.

## Reproducible follow-up
Use a sanitized representative certification article fixture plus synthetic DOCX/Markdown fixtures with headings, links, nested lists, tables, code, Unicode, and embedded images. Record source elements, converter version/date, browser, clipboard MIME types, target editor result, lost/transformed elements, manual steps and screenshots. Distinguish converter preview from actual paste and saved-draft results. Never include private source material without owner approval.
