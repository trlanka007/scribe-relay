# M3.1 official platform evidence recheck

Status: **Documentation evidence — review requested; no live LinkedIn paste tests performed**  
Reviewed: **2026-11-25** | Work item: M3.1.a / [#81](https://github.com/trlanka007/scribe-relay/issues/81) | PBI: [#57](https://github.com/trlanka007/scribe-relay/issues/57)

## Scope and method

Rechecked primary LinkedIn Help, LinkedIn's public marketing Posts API documentation (version 2026-07), and MDN Clipboard API references. Findings below concern *documented native editor controls, public API semantics, restrictions and browser API mechanisms*; they are not observations of HTML being pasted into a LinkedIn Article or surviving a saved-draft reopen. Article editor and feed Posts API are different publishing surfaces. No authenticated testing, automation, code execution, native API calls, uploads or publications were performed.

| Evidence / official source | What the source establishes | What remains unverified for ScribeRelay |
|---|---|---|
| [LinkedIn: Write and publish articles](https://www.linkedin.com/help/linkedin/answer/a522427) | Desktop Article editor has a separate title and cover-upload action, image/video upload, links, code snippets, embedded content, text styles, lists, quotes and dividers. | Whether pasted HTML preserves each construct; which heading levels survive; pasted image support; table and nested-list behavior. |
| [LinkedIn: Manage, share, or duplicate article drafts](https://www.linkedin.com/help/linkedin/answer/a523042/share-a-draft-of-your-article-before-publishing?lang=en) | Article drafts autosave when writing begins; Manage → Drafts allows reopening; formatting after publication may differ; mobile app does not offer this feature. | Timing/reliability of autosave for our fixture; exact element fidelity after reopening; appearance after actual publication. |
| [LinkedIn: Posts API (2026-07)](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api?view=li-lms-2026-07) | API `content.article` is an *article/link feed-post representation* with a source URL and metadata. The API also discusses `DRAFT` lifecycle state for **posts** in author view. | Neither the `article` content type nor the post `DRAFT` lifecycle documents a public endpoint to create/edit the body of a **native long-form LinkedIn Article draft**. Public sources reviewed do not establish such an endpoint; this does **not** prove that none exists in restricted/partner integrations. |
| [LinkedIn: Automated activity](https://www.linkedin.com/help/linkedin/answer/a1341543) and [prohibited software/extensions](https://www.linkedin.com/help/linkedin/answer/a1341387/prohibited-software-and-extensions) | LinkedIn prohibits third-party tools that scrape, alter the appearance of, or automate activity on its website. | Any alternative requiring private endpoints or simulated editor interaction is outside the approved ScribeRelay approach, regardless of technical feasibility. |
| [MDN: Clipboard.write](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/write), [ClipboardItem](https://developer.mozilla.org/en-US/docs/Web/API/ClipboardItem), [Clipboard API security](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API) | A `ClipboardItem` can contain `text/html` and `text/plain` as representations of the same item. Async clipboard writes need secure context and browser-dependent permission or transient user activation; behavior varies by browser. | Successful clipboard write does not prove that LinkedIn accepts/persists the representation. `file:` origin and permission behavior must be recorded for any local spike, rather than assumed. |

## Conclusions: documentation versus destination validation

1. **Candidate supported approach (hypothesis only):** prepare body markup and plain text locally, provide explicit Copy, and let the user use native Article editor paste, separate title/cover controls and manual media insertion.
2. **No native article draft API is established:** the Posts API's `content.article` and `DRAFT` terminology must not be conflated with the Article editor. Do not claim either impossibility of partner support or a supported API handoff.
3. **No rich-paste fidelity is proven:** all F01–F08 paste/reopen matrix cells stay **Unknown** until a user manually tests the saved draft. Native editor features alone do not count as paste evidence.
4. **No automated LinkedIn interaction:** manual authenticated user behavior only; never use bot-driven paste, DOM inspection, browser extension editor modification or unapproved endpoints.
5. **No approval inference:** this review does not accept M2/M3 gates, authorize production code or choose a production framework.

## Hand-off to M3.2 and M3.3

Use the [manual run sheet](../testing/manual-linkedin-article-run-sheet.md) with the existing [synthetic HTML fixture](../../tests/fixtures/linkedin-rich-text.html). Record Edge and Chrome version separately, copy method, visual paste outcome, reopened draft outcome, and each unsupported or manual recovery. Test F05–F06 using a separate approved synthetic image fixture. F08 async write and permissions require an explicitly approved isolated spike; the first baseline is manual selection/copy.

**Decision requested of owner:** accept this bounded *documentation recheck* as satisfying M3.1.a once the PR is reviewed; confirm the allowed M3 hands-on experiment scope before conducting tests. M3.1 feature and M3 feasibility gate remain open pending review and actual evidence.

## Refresh triggers

Recheck when LinkedIn's Article editor/Help or developer APIs change, when browser clipboard behavior changes, and before approving a supported compatibility profile. Retain dates and precise source/experiment boundaries; do not replace historical runs with extrapolations.
