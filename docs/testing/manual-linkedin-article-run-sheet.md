# M3.2 manual LinkedIn Article paste/reopen run sheet (F01–F04, F07–F08)

Status: **Ready-to-fill template, not executed results** | 2026-11-25  
Tasks: [M3.2.a #82](https://github.com/trlanka007/scribe-relay/issues/82), [M3.2.b #83](https://github.com/trlanka007/scribe-relay/issues/83), [M3.2.c #84](https://github.com/trlanka007/scribe-relay/issues/84), [M3.2.d #85](https://github.com/trlanka007/scribe-relay/issues/85), [M3.2.e #86](https://github.com/trlanka007/scribe-relay/issues/86), [M3.2.f #87](https://github.com/trlanka007/scribe-relay/issues/87).

This template reduces the effort of running the already [proposed experiment protocol](../research/platform-compatibility.md). **It is not evidence that a test ran.** Owner approval for hands-on scope is still required. Never automate LinkedIn interactions or publish test content.

## 1. Environment and provenance (fill once per run)

| Field | Value |
|---|---|
| Run ID, timestamp, tester | **PENDING** |
| Scope approval / reference | **PENDING** |
| OS and build | **PENDING** |
| Browser/version (Edge first, Chrome second) | **PENDING** |
| Editor context (personal Article vs Page; no draft URL) | **PENDING** |
| Copy route (rendered selection vs later user-activated spike) | **PENDING** |
| URL/origin used for fixture (`file:` or localhost; no sensitive URL) | **PENDING** |
| Conflicting extensions / permissions / clipboard error | **PENDING** |
| Fixture file and immutable identity | `tests/fixtures/linkedin-rich-text.html`; Git blob SHA **`860c6aaa8cc2bb9415983129ca4fdf226744caa6`** (as inspected on 2026-11-25). Recheck against actual file before each run. |
| Source revision and SHA-256 (optional extra) | **PENDING** |
| Paste/reopen wait and exact observation times | **PENDING** |
| Result evidence location (sanitized notes only; no draft URLs) | **PENDING** |

For blob verification in a local Git checkout run `git hash-object tests/fixtures/linkedin-rich-text.html`. Do not mistake this Git blob ID for a SHA-256 checksum of file contents. Exact versions and timestamps must be supplied by the tester; this repo does not infer their local system state.

## 2. Expected fixture semantic inventory

Fixture: [linked synthetic HTML](../../tests/fixtures/linkedin-rich-text.html). Select and copy the **rendered body**, not the HTML source and not the document title in the browser tab. Values below are source expectations, **not** destination pass claims.

| ID | Expected source element / value | Experiment |
|---|---|---|
| E01 | H2: “F02 — Formatting checkpoint” | F02 |
| E02 | Paragraph: “F01 — Unicode: café, తెలుగు, 日本語, αβγ.” followed by a line break and “Second line.” | F01 |
| E03 | Paragraph with **Bold text**, *italic text* and literal `inlineCode()` | F02/F07 |
| E04 | H3: “F03 — Links and lists” | F02 |
| E05 | Link text “Example reference” pointing to `https://example.com/` (verify target, not only appearance) | F03 |
| E06 | Ordered list: “First ordered item”, “Second ordered item”, in order | F03 |
| E07 | Unordered list: “Parent item” with nested “Nested item”, then “Second unordered item” | F03 |
| E08 | Blockquote: “F04 — Synthetic quotation.” | F04 |
| E09 | Horizontal divider | F04 |
| E10 | Table: headers “Feature” and “Value”; rows “Alpha / One”, “Beta / Two” | F07 |
| E11 | Preformatted four-line JavaScript block: `const value = 42;`, `if (value > 0) {`, `  console.log("fixture");` and closing `}` | F07 |

All 11 IDs must receive individual paste, post-correction and reopen observations. Record structural fidelity *and* text preservation separately. For example, a flattened table with all cell text is transformed, not an unqualified preserved table. For code, record exact whitespace and newlines even if visual syntax highlighting changes.

## 3. Manual run procedure (no publishing)

1. After approved scope, open the HTML fixture in a supported desktop browser. Record OS/browser version, document source revision and exact copy route. Ensure no private documents, remote tracking images or browser-based automation.
2. Select rendered fixture body and copy using normal OS controls. Open the LinkedIn **Article** editor manually and create a fresh unpublished test draft. Enter a distinct synthetic title *separately*.
3. Paste once into the body with native keyboard paste. Note any warnings or manual correction **without silently fixing failures** before the first observation. For each E01–E11, fill the *Paste* column below, including exact hyperlink target, list nesting and code whitespace.
4. Perform and record any manual corrections, then fill the *Post-correction* column for the final draft before leaving. Include correction actions in the timing record; do not overwrite initial paste observations.
5. Allow normal autosave, leave and manually reopen using **Manage → Drafts**. Record any change in the *Reopen* column. Do not publish, share a draft URL or record a private URL.
6. Repeat as a distinct run on Chrome. Later F08: test `text/html` + `text/plain` write and permission/error/fallback only using an owner-approved isolated, user-triggered clipboard spike. Never programmatically interact with LinkedIn.
7. Record active preparation time, manual edits and uncertainties. Populate the [compatibility matrix](formatting-compatibility-matrix.md) only from supported, reproducible run evidence; keep cells **Unknown** otherwise.

## 4. Per-element result sheet (duplicate for each run)

Choose **Preserved / Transformed / Manual action / Unsupported / Unknown**, with reason and recovery. Use **Unknown** if not observed. After reopening, do not infer success from initial paste. Examples in parentheses are prompts, not result values.

| Element | Paste: text + structure + link target | Post-correction: text + structure + link target | Reopen: text + structure + link target | Outcome | Reason / recovery / evidence |
|---|---|---|---|---|---|
| E01 | PENDING | PENDING | PENDING | Unknown | |
| E02 | PENDING | PENDING | PENDING | Unknown | |
| E03 | PENDING | PENDING | PENDING | Unknown | |
| E04 | PENDING | PENDING | PENDING | Unknown | |
| E05 | PENDING | PENDING | PENDING | Unknown | |
| E06 | PENDING | PENDING | PENDING | Unknown | |
| E07 | PENDING | PENDING | PENDING | Unknown | |
| E08 | PENDING | PENDING | PENDING | Unknown | |
| E09 | PENDING | PENDING | PENDING | Unknown | |
| E10 | PENDING | PENDING | PENDING | Unknown | |
| E11 | PENDING | PENDING | PENDING | Unknown | |

**F08 only:** record secure origin, browser activation/permission settings, precise copy success/error, rich versus plain-text representation observed, and fallback route. Keep the manual-selection baseline distinct from programmatic clipboard evidence.

## 5. Run reconciliation and decision

| Measure / decision | Value |
|---|---|
| E01–E11 individually observed at paste | **PENDING** (0/11) |
| E01–E11 individually observed after corrections | **PENDING** (0/11) |
| E01–E11 individually observed after reopen | **PENDING** (0/11) |
| Text omissions / link-target defects / structural changes | **UNKNOWN** |
| Manual corrections and number of actions | **PENDING** |
| Active paste/reopen preparation duration | **PENDING** |
| Exceptions, security concerns and next run | **PENDING** |
| Owner acceptance / approved profile update | **PENDING** |

A run is **not complete** until environment, fixture identity, all E01–E11 results at paste, after corrections and after reopen, plus known limitations, are populated. Assess target quality after corrections and after reopen; retain initial paste differences and record their correction effort. No single successful run establishes a generally supported LinkedIn browser profile. M3.3 image behavior, M3.4 parser fidelity and F11 comparative benefit are separate work packages.
