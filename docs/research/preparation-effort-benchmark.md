# M3.5 / F11 preparation effort benchmark

Status: proposed protocol; no measured baseline | 2026-11-25
Refs #93, AC-12. Dependency M3.2.b (#83) remains open. This prepares the measurement artifact without claiming that the blocked baseline task is complete.

## Comparison arms and fixtures

A = manual reconstruction using the native LinkedIn Article editor, without a formatter.
B = ToolHa-assisted preparation and native editor corrections, where the tool accepts the same synthetic input.
C = ScribeRelay-assisted preparation, deferred until a functioning candidate in M7.

Use identical authored content and expected inventory across arms. Start with the synthetic HTML fixture E01–E11 and media fixture; add a synthetic Markdown and generated DOCX article with human-reviewed inventory. Record exact fixture hash, input representation and any conversion needed to make an arm accept it. Include that conversion time; do not silently substitute an easier fixture. A real certification article requires separate sanitization and owner permission. Do not upload private documents to external tools.

## Measurement boundary

Start at the first preparation action with source available and editor ready. Stop when the unpublished draft meets the predefined content/formatting target and is ready for reopen inspection. Include source conversion, clipboard, manual formatting, image placement, correction and active verification. Measure active seconds; record waiting seconds separately (including autosave). Record elapsed wall time separately. Pause active timing only during genuinely idle waits or interruptions; log reason. Record clicks, edits, media actions, omissions, transformations and unresolved issues. Report actual reopen observations separately; failed persistence prevents an equivalent successful result. No publishing or automated LinkedIn interaction.

## Run schedule

For each fixture and reference browser/device, perform three paired A/B runs as a baseline, using orders AB, BA, AB (reverse starting order on the next fixture). At M7 perform at least three paired A/C runs on the same fixture and comparable environment, using AC, CA, AC or reverse. Re-measure A when environment or editor changes materially. Keep fresh drafts, same tester, comparable starting state, and record practice runs separately. Three is the minimum, not statistical proof. Use identical target quality in each pair; record failed/abandoned attempts, do not substitute zeros or cherry-pick faster successes. Mark unavailable arms as unavailable with reason.

## Run record (duplicate per arm)

| Field | Value |
|---|---|
| Pair ID, fixture ID/hash, arm, order | Pending |
| Date, tester, OS/browser/tool version, device | Pending |
| Starting state / preparation route | Pending |
| Active seconds by preparation, transfer, correction, media, verification | Pending |
| Idle seconds and reason / elapsed seconds | Pending |
| Clicks, edits, media insertion actions | Pending |
| Expected inventory total, preserved, transformed, manual, unsupported, unknown | Pending |
| Target equivalence and paste/reopen outcome | Pending |
| Failed/abandoned reason, sanitized evidence | Pending |

## Analysis

For each fixture report sample counts, individual paired observations, median active seconds for each arm, absolute difference, reduction = 100 × (median A − median comparison) / median A when median A > 0, and median paired reductions separately. Do not combine unequal fixture sets. Disclose failures and unavailable arms; report timing comparisons only for equivalent successful pairs with at least three pairs, otherwise insufficient evidence. AC-12's proposed ≥50% median active time reduction applies to A/C, not to A/B. Report quality and unresolved loss alongside time; a faster but incomplete draft is not success. No claim of statistical significance from three pairs.

## Existing baseline evidence

The [ToolHa evaluation](competitor-evaluations.md) records a qualitative user observation of acceptable text transfer, with inline images trimmed from the shared output. No timings, paired runs or per-element persistence results exist. Therefore manual baseline = unknown, ToolHa baseline = unknown, ScribeRelay comparison = not yet available. Do not infer a numeric improvement.

## Gate

M3.5 remains open until manual baseline evidence is recorded or explicitly dispositioned by owner. M7 owns final A/C comparison. #151 parser reproducibility and F01–F08 destination validation are not waived. No production implementation, compatibility profile promotion or new acceptance targets.
