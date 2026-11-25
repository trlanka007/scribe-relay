# MVP acceptance criteria

Version 0.1 | Status: Proposed targets, not validated | 2026-11-25

## Measurement protocol
Create a sanitized certification-article fixture and synthetic Markdown, DOCX and HTML fixtures. Define a human-reviewed semantic inventory before import (text spans, blocks, headings, links, lists, assets and unsupported features). Record browser/OS, profile version, date, input hash, output, report, actual LinkedIn paste and saved-draft observations separately. Include malformed and adversarial fixtures. Use identical documents for baseline comparisons.

| ID | Requirement | Proposed pass condition |
|---|---|---|
| AC-01 | FR-01–03 | Every inventory element in agreed fixtures is mapped to a source record or explicit import error; 100% source text accounted for, including text in unsupported structures. Reject files when reliable accounting is impossible. |
| AC-02 | FR-04–06 | Zero unreported omissions or transformations; classifications reconcile to inventory total; unknown support never marked preserved at destination without evidence. |
| AC-03 | FR-04,08 | 100% of valid links, semantic headings and other elements designated supported in the approved profile match expected values in real target-editor tests; compare normalized text rather than pixel layout. |
| AC-04 | FR-07,09 | 100% of source image references accounted for; accessible embedded images extracted with correct order/context; missing or blocked assets explicitly reported. |
| AC-05 | FR-05,06,10 | Preview/report identify location, reason and available recovery for each non-preserved item; unresolved losses visible before copying. |
| AC-06 | FR-08,09 | User can copy HTML and text, paste into LinkedIn and manually save/reopen a draft in every agreed baseline browser; failure or fallback is explicit. No automatic publishing. |
| AC-07 | NFR-01,02,07 | With network disabled after application load, import, preview and copy work for local fixtures; network inspection shows no document upload; unsafe markup/link fixtures cannot execute or trigger implicit requests. |
| AC-08 | NFR-03 | Repeated conversion of same fixture/options/profile produces equivalent normalized output and report (excluding timestamps/session identifiers). |
| AC-09 | NFR-04 | Complete core flow using keyboard; controls have accessible names, errors readable, focus visible. |
| AC-10 | NFR-05 | Candidate benchmark: 95th percentile conversion ≤ 3 seconds for local fixtures up to 1 MB text or 10 MB DOCX with 20 images on an agreed reference device; no UI lockup or crash; limits and device to be confirmed by spikes. |
| AC-11 | NFR-06 | Architecture review and eventual test adapter demonstrate a new destination can consume canonical model without editing existing importers. |
| AC-12 | Product outcome | Candidate: ≥ 50% reduction in median active manual preparation time compared with manual reconstruction on same fixtures; record clicks, edits and image insertion separately; at least 3 paired runs per fixture, counterbalance order; validate target before release. |

## Interpretation
Accounted-for is not equivalent to preserved. Reported loss may satisfy accounting but not supported-element fidelity. A conversion preview cannot pass destination acceptance; actual user-controlled paste and saved-draft inspection are required. Record baseline browser/version, fixture set, sample size and exceptions before claiming compliance. No metrics have been measured yet.
