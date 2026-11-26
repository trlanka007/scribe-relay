# M4.3 — Handoff, media recovery and accessibility

Status: proposed design draft; not approved or implemented | 2026-11-25 ET
Task #98 (M4.3.a), parent PBI #65 as recorded in issue. Extends [W01–W05](ux-design.md) and [author workflows](user-workflows.md). M4.2 review and M3.2/M3.3 evidence remain outstanding. This is parallel conceptual drafting, not a finalized platform interaction or supported browser commitment.

## W06 — Review before handoff

```text
+------------------------------------------------------------------+
| Prepare LinkedIn Article handoff                                 |
| Source: Article.docx   Profile: version/date/limitations          |
| Output revision: current   Preview: simulation only              |
| Blocking issues: 0 (illustrative)                                |
| Review required: table representation, image placements, unknown |
| [Inspect report]   [Return to preview]                            |
| [ ] I reviewed the listed eligible limitations for this output.  |
| [Continue to handoff]                                             |
+------------------------------------------------------------------+
```

Proposed eligibility rules:

| Condition | Behavior | Can acknowledgement override? |
|---|---|---|
| Unaccounted content, unsafe output, failed validation | Block export; explain and offer source recovery | No |
| Accounted transformation with safe representation | Explain before/after and offer alternatives; require review where material | Review only; does not imply preservation |
| Manual media placement with accessible asset | Show occurrence and placement instructions; keep pending after copy | No automatic completion |
| Missing or unresolved asset | Preserve reference; disclose missing asset; offer only supported safe recovery | Only if owner-approved policy permits an explicitly incomplete handoff |
| Unknown destination fidelity | Show evidence gap, verification instructions and eligible warning | Does not establish support |
| No eligible warnings or blocking issues | Proceed without unnecessary confirmation | Not applicable |

The acknowledgement policy is a proposal subject to owner review. Bind acknowledgement to the current source, conversion options, output and profile revision; invalidate it when any changes. Never persist an acknowledgement across unrelated documents. An acknowledged omission is not a preserved item. No default-checked consent, no blanket override of blocking conditions, no hiding unresolved warnings after acknowledgement.

## W07 — Separate title, body and media preparation

```text
+------------------------------------------------------------------+
| Article handoff                         [Return to review]       |
| Title: Synthetic article               [Copy title]              |
| Body: destination preview             [Copy formatted body]     |
| Copy status: Not attempted                                       |
| [Plain-text fallback] (explicit choice, formatting warning)      |
| Body media: 2 occurrences / 1 local asset                        |
| A1 after paragraph 3, before paragraph 4  [Inspect placement]    |
| A2 after paragraph 7, before paragraph 8  [Inspect placement]    |
| Cover: separate candidate, if provided    [Inspect cover]        |
| Next: manually paste and insert media in LinkedIn Articles        |
| [Draft verification checklist]                                  |
+------------------------------------------------------------------+
```

Title is separate from body only when a title candidate is identified and confirmed; never silently remove the first heading. Otherwise display no inferred title and preserve all authored body content. Copy actions are individually user-triggered; warn that copying one representation replaces the prior clipboard content. Copy formatted body requests HTML and plain text representations of the same body where supported; no unannounced fallback. Clipboard behavior and permissions remain evidence-dependent. No hidden clipboard read, upload, external navigation or automated editor action.

| Copy state | Proposed feedback / recovery |
|---|---|
| Not attempted | Explain what will be copied |
| Pending | Show operation in progress, guard against competing requests |
| Browser reports successful rich write | Report local write success only; instruct author to paste and verify |
| Rejected / permission denied / unavailable | Explain failure, retry from explicit user action or choose supported manual-selection fallback |
| Plain fallback explicitly selected | Disclose formatting and media limitations before copy; distinguish result from rich write |
| Source/profile/output changes | Mark previous copy result stale; require fresh review and copy |
| Manual selection used | Record that user must copy manually; do not claim application verified clipboard contents |

A late browser response cannot mark a newer revision copied. An old clipboard write may remain on the operating system clipboard; warn the author to recopy current output rather than promise revocation.

## W08 — Media placement and recovery

```text
+------------------------------------------------------------------+
| Image occurrence A2 — pending manual placement                  |
| Asset: Image A (same bytes as A1)                                 |
| Source location: paragraph 7 / image / paragraph 8               |
| Destination context: before and after text snippets              |
| Caption and alt: source values, if present                       |
| [Inspect local asset] [Save local asset, if supported]            |
| [Copy caption] [Copy alt text]                                   |
| [Previous occurrence] [Next occurrence]                          |
| [Mark as placed by me]                                           |
+------------------------------------------------------------------+
```

Maintain one entry per placement, even when assets are deduplicated. Use stable occurrence identity and surrounding source/output context; distinguish repeated text with order and location. Display intended placement separately from actual destination state, which is unknown unless the author reports it. Placement markers in a preview are guidance, not silently injected article text. Any optional temporary placeholder in copied output would require explicit review, disclosure and removal guidance; not committed by this design.

Accessible local assets can be prepared for manual insertion; exact file formats, export controls and direct image-copy options depend on M3.3. Missing/blocked/external assets show original references inertly with reason; no automatic fetching. Preserve captions and alt text for recovery, but do not claim destination controls exist until verified. Cover is a separate role, not another body occurrence; never infer a cover from the first image without confirmation. Manual check-off is author-reported and does not certify upload, placement or persistence.

## W09 — Author verification checklist

```text
+------------------------------------------------------------------+
| Verify your draft (manual)                                       |
| [ ] Title and body transferred                                    |
| [ ] Heading structure, lists, links, tables/code checked          |
| [ ] Each required image and separate cover checked                |
| [ ] Caption/alt values checked where controls permit              |
| [ ] Draft saved and reopened; intended content checked again     |
| Unresolved items remain visible in the compatibility report.     |
| [Return to review] [Finish preparation session]                  |
+------------------------------------------------------------------+
```

The user manually opens the native editor, pastes, inserts media, saves/reopens and decides whether to publish. These checkboxes represent user-reported actions only, not an application observation or platform API result. If reopen cannot be confirmed, persistence remains Unknown. If the author finds a mismatch, return to report/recovery without overwriting the original. No publication button, private draft URLs, LinkedIn credentials or mandatory account in ScribeRelay. Finish/clear session behavior requires a retention decision; do not imply recovery after reload.

## Keyboard and accessibility path (proposed)

1. Tab through named import controls and explicitly paste or select file; announce inspection status.
2. On validation failure focus the error summary; on success focus the inventory heading, then Continue.
3. Navigate source, preview and report in logical reading order; select issue details with keyboard. Return restores focus to originating row.
4. Navigate review summary, eligible warning acknowledgement and Continue; blocked output offers actionable recovery rather than an unexplained disabled control.
5. Navigate title/body copy controls, explicit fallback, media entries and verification checklist. Announce copy result in a readable status region without stealing focus; expose failure details and recovery.
6. Navigate each placement by keyboard, copy caption/alt separately and mark user-reported completion if desired. No drag-only control.
7. Return to review or finish session with clear focus. At narrow widths maintain the same sequence and available actions.

Use semantic controls, accessible names, visible focus, text plus color status, readable error messages and no keyboard trap. If a modal is chosen later, define focus containment, Escape behavior and return focus. Do not claim WCAG conformance from a textual design.

## Scenario review matrix

| Scenario | Expected design response | Trace |
|---|---|---|
| Clean accounted output | Separate title/body handoff; local copy result only | FR-08/09, AC-06 |
| Unknown compatibility | Visible profile uncertainty and manual verification | FR-04/10, AC-02/03 |
| Unsafe/unaccounted content | Block regardless of acknowledgement | FR-02/06, AC-01/07 |
| Repeated embedded asset | Two ordered placements, one asset identity | FR-07, AC-04 |
| Missing image | Report reference and unresolved recovery; no fetch | FR-07, AC-04/07 |
| Copy denied | Retry or explicit fallback; no false success | FR-08, AC-06 |
| Conversion changes after review | Invalidate acknowledgement and stale copy status | FR-05/06, AC-02/05 |
| Author finds mismatch after reopen | Return to report, retain original, no verification claim | FR-09/10, AC-03/06 |
| Keyboard-only journey | All core actions reachable and readable | NFR-04, AC-09 |

## Remaining decisions and gate

Review warning eligibility, title selection, temporary marker policy, asset preparation controls, clipboard fallback, session retention and author-reported checklist with owner. M3 F05/F06/F08 evidence is required before finalizing corresponding controls. M4 acceptance requires reviewed scenarios and keyboard path; actual accessibility and browser behavior require implementation tests. No runtime, visual rendering or usability tests performed; no native platform compatibility promoted, no production code, no task closure or M5/M6/M7 gate waiver.
