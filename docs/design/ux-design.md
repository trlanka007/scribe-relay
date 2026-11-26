# M4.2 — Import, preview and report wireframes

Status: low-fidelity proposed design; not approved or implemented | 2026-11-25 ET
Task #97 (M4.2.a), parent PBI #64 as recorded in issue. Based on [user journeys](user-workflows.md), [PRD](../product/product-requirements.md), and [M3 gate review](../research/feasibility-gate-review.md). M4.1 acceptance and M3.2 evidence remain outstanding; this is permitted parallel drafting only.

## Design intent

A single local preparation workspace, not a writing studio. Keep the source immutable, show source inventory and destination simulation side by side on wide screens, and use sequential sections at narrow widths. The author can navigate among import, inspection and review without losing the current valid session. No account or LinkedIn integration is implied. All screen text and controls below are proposals; examples are synthetic, not measured results.

## W01 — Empty / import (FR-01, NFR-01/04)

```text
+-----------------------------------------------------------+
| ScribeRelay                    Import > Review > Handoff   |
| Bring an existing article                                 |
| [ Choose Markdown or Word file ]                          |
| or                                                        |
| Paste rich text here                                      |
| [                                                         ]|
| [                                                         ]|
| [ Inspect pasted content ]                                |
| Destination: LinkedIn Articles (initial destination)      |
| Local processing. No document upload required.             |
+-----------------------------------------------------------+
```

File chooser has an accessible label; drag/drop may supplement but never replace keyboard entry. Paste is explicit and user-controlled; no background clipboard reading. Show the actual representation received (rich HTML, plain text, or unsupported). If only plain text is received, disclose that original formatting cannot be established and let the user choose retry or inspect plain text. No automatic reinterpretation of a pasted plain-text selection as Markdown.

## W02 — Inspecting and source inventory (FR-02/03, NFR-05)

```text
+-----------------------------------------------------------+
| Article.md   | Inspecting source ...       [Cancel]       |
| Stage: validate input / inventory / reconcile             |
| Status: working; no output ready                          |
+-----------------------------------------------------------+
| Source inventory (after successful inspection)            |
| Text blocks  4     Links  2     Image occurrences  2     |
| Unique assets 1    Unrecognized structures 0              |
| [Inspect source locations]      [Continue to review]      |
+-----------------------------------------------------------+
```

Show real stage rather than invented percent progress. Example counts illustrate distinct occurrence and asset totals; they are not a fixture result. If a new import fails, retain the previous valid session and clearly label which document is shown. Cancel invalidates in-flight work so stale results cannot overwrite a newer session. Original input remains unmodified. If reliable accounting cannot be established, transition to W05; no output readiness.

## W03 — Review workspace (FR-04/05/10)

```text
+-------------------------------------------------------------------+
| Article.md   [Change source]  Destination: LinkedIn Articles       |
| Profile: version/date/limitations   [View profile evidence]       |
| Preview is a simulation; actual editor fidelity is not verified.  |
+-------------------------------+-----------------------------------+
| Source (read-only)            | Destination preview (simulation)  |
| Heading                       | Heading                           |
| A paragraph and link          | A paragraph and link              |
| Image occurrence A1           | Image placement marker A1          |
| Image occurrence A2           | Image placement marker A2          |
+-------------------------------+-----------------------------------+
| Compatibility report                                              |
| Preserved | Transformed | Manual | Unsupported | Unknown          |
| [All items] [Needs attention] [Filter by source location]         |
| Row: A1 | Manual | Image placement | [Inspect details]             |
| Row: H1 | Unknown | Target fidelity not tested | [Inspect details] |
| [Review issues]                         [Prepare handoff]         |
+-------------------------------------------------------------------+
```

Report total reconciles to the defined source occurrence inventory; asset deduplication does not remove placements. Each row identifies source location, predicted disposition, reason, evidence level, available recovery and output location if present. Preserved means preserved in the stated representation, not guaranteed in LinkedIn: keep target status separately Unknown until supported profile evidence exists. Selecting a row navigates to matching source and preview context without relying on color. Untrusted HTML and assets cannot execute or implicitly fetch in either pane. Basic editing remains P1; do not introduce it here as required behavior.

## W04 — Warning / recovery detail (FR-05/06/07, AC-02/04/05)

```text
+-----------------------------------------------------------+
| Review issue A1 — image occurrence                        |
| Source: after paragraph 3, before paragraph 4             |
| Asset: local embedded image; occurrence 1 of 2            |
| Proposed disposition: manual placement                    |
| Reason: direct image transfer not established             |
| Recovery: retain asset and placement context              |
| [Inspect asset] [View placement context]                  |
| [Return to report]                                        |
| Remaining destination uncertainties: visible              |
+-----------------------------------------------------------+
```

For a missing image, show original reference and explain no implicit fetch; offer only safe supported recovery, not a fabricated image. For a transformed table, show original ordered cells and proposed readable representation side by side; disclose change. For an unsafe link, retain source context inertly and offer a safe alternative only if supported; do not emit an unsafe target. Recompute inventory/report after alternative choice, invalidate stale preview and any prior acknowledgement for changed output. Manual recovery and unsupported/unknown states must remain distinct. Detailed acknowledgement rules and media controls belong to M4.3.

## W05 — Rejected input / blocked output (FR-01/02/06, AC-01)

```text
+-----------------------------------------------------------+
| Cannot safely prepare this document                       |
| Reason: source content could not be reliably accounted for|
| Location: reported source part or span, if known           |
| Your original file has not been modified.                 |
| [Inspect available diagnostic details]                    |
| [Choose another source] [Return to prior valid session]   |
| Prepare handoff: unavailable for this input               |
+-----------------------------------------------------------+
```

Distinguish invalid encoding/package, unsupported format, agreed resource-limit violation, unsafe content and unaccounted content. Do not expose sensitive paths in diagnostic output or claim exact location when unknown. Acknowledgement cannot override unaccounted content or unsafe output. Partial diagnostics are not a successful conversion. Prior valid session action appears only if such a session exists.

## State and interaction contract (proposed)

| State | Primary action | Exit / failure |
|---|---|---|
| Empty | Choose file or explicitly paste | Cancel leaves empty |
| Inspecting | Cancel | Accounted inventory -> review; invalid -> rejected |
| Accounted review | Inspect issues, select safe alternatives | Recompute; blocking issue -> blocked |
| Review with eligible warnings | Review recovery and limitations | Handoff eligibility subject to M4.3 policy and profile evidence |
| Blocked / rejected | Recover or change source | No export for blocked input |
| Handoff preparation | Continue to separate M4.3 design | No claim of clipboard success or external draft state |

Keyboard order follows import controls, inventory, destination, source/preview, report and review actions; use semantic headings, text labels, visible focus and readable status/error announcements. On validation failure focus an actionable error summary; returning from detail restores focus to its initiating report row. Use text labels in addition to severity color. At narrow widths source, preview and report remain accessible in sequence, without requiring a pointer or simultaneous panes. Accessibility details require review and real testing.

## Acceptance and next steps

Review these wireframes for success, warning and rejection scenarios against FR-01–07/10, NFR-01/02/04/05 and AC-01/02/04/05. Validate with representative author scenarios from M4.1. M4.3 (#98) will detail acknowledgement, separate title/body/media handoff, clipboard error/fallback and manual verification, subject to M3 findings. No finalized browser baseline, compatibility promotion, production implementation, dependency changes, issue closure or approval. No visual rendering or usability test performed; these are text wireframes only.
