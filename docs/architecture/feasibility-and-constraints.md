# Platform feasibility and constraints

Version 0.1 | Status: Proposed; documentation research completed, experiments pending | 2026-11-25

## Decision under investigation
Can ScribeRelay prepare a high-fidelity LinkedIn Article draft through a user-controlled handoff without unauthorized platform automation? See [PRD](../product/product-requirements.md) FR-04–10 and [acceptance criteria](../testing/acceptance-criteria.md) AC-03–07.

## Evidence from official documentation (reviewed 2026-11-25)
- [LinkedIn article editor](https://www.linkedin.com/help/linkedin/answer/a522427/publishing-articles-on-linkedin?lang=en): desktop authoring supports a separate title and cover, body formatting, links, lists, quotes, dividers, code and media insertion. Native controls do not establish HTML paste fidelity.
- [LinkedIn draft management](https://www.linkedin.com/help/linkedin/answer/a523042/share-a-draft-of-your-article-before-publishing?lang=en): articles autosave when writing begins; drafts can be reopened using Manage > Drafts. Formatting may differ after publication. Do not share test draft URLs or publish test articles.
- [Posts API, version 2026-07](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api?view=li-lms-2026-07): article post example references a source URL with metadata and uses PUBLISHED. This is a feed post, not a native long-form article body. No supported native article draft-creation endpoint was identified in reviewed public documentation. This is a finding bounded to the reviewed sources, not proof that no partner integration exists.
- [LinkedIn automated activity policy](https://www.linkedin.com/help/linkedin/answer/a1341543): third-party software must not scrape, modify or automate activity on LinkedIn. Avoid extensions that manipulate its editor, private endpoints and simulated user actions.
- [MDN Clipboard.write](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/write), [ClipboardItem](https://developer.mozilla.org/en-US/docs/Web/API/ClipboardItem), [Clipboard API security](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API): HTML and plain text may be representations of one item; secure context and browser-dependent permission/user activation apply. Clipboard availability does not prove destination acceptance.

## Integration alternatives
| Alternative | Assessment |
|---|---|
| Standalone local-first formatter + user-initiated rich clipboard | Recommended hypothesis; low integration dependency; actual paste fidelity pending |
| Native API draft creation | Not established by reviewed public API; defer |
| LinkedIn editor manipulation or browser automation | Excluded by platform policy and product principles |
| Manual HTML selection/copy fallback | Candidate when async clipboard unavailable; test independently |
| Plain text fallback | Recovery only; explicitly warn about formatting loss; not sufficient for MVP rich-text gate |

## Proposed handoff
Separate title, body and cover/media assets. User clicks copy in ScribeRelay, opens the native editor, pastes body, inserts missing media using native controls, then reopens autosaved draft to verify. ScribeRelay cannot assert that the actual draft matches its preview without user inspection.

## Critical risks and gates
| Risk | Experiment | Exit condition |
|---|---|---|
| HTML sanitization or flattening | F01–F04 | Agreed core supported elements survive paste and reopen |
| Embedded images not transferred | F05–F06 | Either direct transfer proven or ordered manual insertion demonstrated |
| Tables/code lose semantics | F07 | Explicit fallback with text recovery and owner approval |
| Browser permissions | F08 | Rich clipboard or rich selection fallback works in agreed baseline |
| DOCX parsing loses content | F09 | Inventory reconciliation or explicit rejection, including complex objects |
| Markdown dialect/asset ambiguity | F10 | Supported subset and unresolved references documented |
| Manual effort exceeds benefit | F11 | Paired benchmark against manual workflow and ToolHa |

See [experiment protocol](../research/platform-compatibility.md) and [matrix](../testing/formatting-compatibility-matrix.md).

## Governance
This PR proposes only a bounded exception for disposable local feasibility experiments, subject to owner approval through merge. No production code, dependency commitment, authenticated automation or deployment. Record experiment evidence separately. Do not select production stack until architecture review.
