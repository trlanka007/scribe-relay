# LinkedIn Article compatibility matrix

Version 0.1 | Status: Initial profile; paste and draft persistence untested | 2026-11-25

Native editor capability is documentation evidence, not proof of clipboard interoperability. Source: [LinkedIn editor help](https://www.linkedin.com/help/linkedin/answer/a522427/publishing-articles-on-linkedin?lang=en). All unknowns must remain unknown until tests are recorded per browser and copy method.

| Element | Native editor evidence | HTML paste | Reopen | Candidate recovery | Experiment |
|---|---|---|---|---|---|
| Paragraph/Unicode | Body editing | Unknown | Unknown | Text fallback with warning | F01 |
| Line breaks | Body editing; exact behavior unknown | Unknown | Unknown | Normalize with disclosure | F01 |
| H1–H6 | Style controls; exact levels unverified | Unknown | Unknown | Map to tested heading levels | F02 |
| Bold/italic | Documented | Unknown | Unknown | Manual formatting | F02 |
| Underline/strike | Unverified | Unknown | Unknown | Preserve text; report style change | F02 |
| Hyperlinks | Documented | Unknown | Unknown | Native link insertion | F03 |
| Ordered/unordered lists | Documented | Unknown | Unknown | Text list fallback | F03 |
| Nested lists | Unverified | Unknown | Unknown | Flatten with explicit hierarchy | F03 |
| Quote/divider | Documented | Unknown | Unknown | Text/paragraph fallback | F04 |
| Inline images | Native upload documented | Unknown | Unknown | Extract local asset, placement guide | F05/F06 |
| Cover image | Separate upload documented | Not applicable to body paste | Unknown | Separate asset | F06 |
| Caption/alt text | Unverified | Unknown | Unknown | Preserve in report | F06 |
| Table | Unverified | Unknown | Unknown | Readable text or optional image with original data retained | F07 |
| Inline code/code block | Native code snippet documented | Unknown | Unknown | Preserve literal text; native snippet | F07 |
| Complex DOCX objects | Unverified | Unknown | Unknown | Explicit rejection or recovery | F09 |

## Profile lifecycle
Version by destination, browser and copy method. Each supported designation needs repeatable paste and reopen results; native-only support may inform manual recovery but does not imply paste support. Record date and limitations; re-test on editor changes. Keep source inventory independent of destination rules.
