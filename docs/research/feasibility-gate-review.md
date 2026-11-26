# M3.6 interim feasibility gate review

Status: review draft; gate remains open | 2026-11-25 ET
Refs #94 #95. Baseline: merged PR #153 (15bdf3e). This is an interim reconciliation, not completion of blocked tasks or owner acceptance.

## Evidence register

| Package | Evidence available | Remaining before acceptance |
|---|---|---|
| M3.1 / #81 | [Official documentation recheck](official-platform-evidence-2026-11-25.md), #137 | Owner acceptance of bounded research |
| M3.2 / #82–87 | [Text run sheet](../testing/manual-linkedin-article-run-sheet.md), local clipboard probe #138 | Actual Edge/Chrome local clipboard, permissions/fallback and human Article paste/reopen evidence |
| M3.3 / #88–90 | [Media run sheet](../testing/manual-linkedin-media-run-sheet.md), exporter #152 | Actual PNG generation and hash, body/cover upload, direct image paste and persistence |
| M3.4 / #91–92, #151 | [Parser synthesis](parser-feasibility-synthesis.md), #148–150 follow-up probes and aggregate runner | Pinned regression, semantic reconciliation and explicit unsupported-content boundaries |
| M3.5 / #93 | [Benchmark protocol](preparation-effort-benchmark.md), #153 | Equivalent paired manual/ToolHa baseline or explicit owner disposition of unavailable arms |
| M3.6 / #94–95 | This interim review | Reconcile actual outcomes and record owner risk decision |

No new runtime results in this review. The existing [compatibility matrix](../testing/formatting-compatibility-matrix.md) remains unchanged: no evidence supports promoting any unknown paste/reopen state. Native documentation is not clipboard evidence. Parser evidence is not destination evidence.

## Critical risk dispositions (recommendations, not accepted decisions)

| Risk | Consequence | Required evidence / response |
|---|---|---|
| R1 Core text rich-paste or persistence fails | First destination may not meet P0 | Record F01–F04/F07 in agreed baseline browsers; if core text/links fail, revisit scope before accepting gate |
| R2 Clipboard access denied or representation lost | Copy workflow fails | F08 local diagnostic and manual fallback; show explicit error, never label plain fallback rich success |
| R3 Images stripped or misplaced | Author intent compromised | F05/F06 native body/cover recovery and anchors; direct transfer optional only if agreed requirements allow it |
| R4 Import loses authored text or order | Silent loss, unacceptable | Independent inventory, ordered reconciliation and explicit rejection where accounting cannot be established |
| R5 Parser dependency or source drift | Historical results not reproducible | #151 clean LF pinned run; record all eight scripts and ten identities, no pin relaxation merely to pass |
| R6 Unsafe input or external fetch | Privacy/security violation | Keep spikes isolated; production threat model, sanitization and resource contracts in M6 with verification in M7 |
| R7 Preparation benefit unmeasured | Product value uncertain | #93 baseline or owner disposition; final A/C AC-12 measurement in M7 |
| R8 Unsupported native article draft API or policy | Automation risk | Manual authenticated user handoff only; no private endpoints or automated editor interaction |

## Parallel work boundaries

The milestone plan explicitly permits drafting M4 in parallel with M3. Draft M4.1 personas, jobs and journey from existing requirements, clearly marked proposed; #96 and related tasks retain their actual prerequisites. Draft platform-independent import, preview, report and recovery concepts only, with unknown destination behavior represented explicitly. Do not finalize clipboard/media controls or claim approved accessibility flows until relevant evidence and owner review. M5 formal architecture approval remains dependent on critical M3 findings and M4. M6 readiness and M7 production implementation remain gated; no new production dependencies or scope reduction.

## Minimum owner-assisted evidence sequence

1. Local clipboard diagnostic in Edge and Chrome: record rich/plain representations and fallback/denial; no authenticated automation.
2. Manual fresh Article draft, E01–E11 observations at paste and reopen, separate browser records.
3. Generate and independently hash PNG; perform separate direct paste, native body placement and cover upload runs, each with reopen.
4. Run pinned parser regression in clean LF environment; retain safe synthetic evidence; explicitly account for remaining parser gaps.
5. Gather benchmark baseline using equivalent final quality and reopen checkpoints, or request explicit disposition of unavailable arms.
6. Reconcile matrix and risk dispositions, then obtain explicit owner decision on M3. No publication; delete test drafts manually.

## Gate recommendation

Keep M3 open. Proceed only with eligible proposed M4 drafting and outstanding approved synthetic experiments. If core clipboard/media evidence is unavailable or negative, owner must explicitly decide whether to change scope or defer the relevant capability; an unknown cannot become supported by waiver. M2/M5 approvals and M6 gate remain mandatory for M7. No issue closures or hierarchy changes in this review.
