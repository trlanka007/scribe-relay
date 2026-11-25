# Product requirements (PRD)

Version 0.1 | Status: Proposed | 2026-11-25

## Context and outcome
Based on [vision](vision.md) and [competitive analysis](competitive-analysis.md). Enable authors to bring an existing formatted document into LinkedIn Articles with less manual reconstruction, transparent fidelity reporting and control over final publication. No claim of automatic native LinkedIn draft creation.

Primary user: technical professional or blogger with a finished Word/Markdown article; secondary user: creator copying rich text from an AI or other editor.

## User journey
Import → inspect source inventory → select destination (LinkedIn Articles in MVP) → preview conversion → review/resolve issues → copy formatted body and prepare media → paste in LinkedIn → manually save/verify draft. No LinkedIn login or publishing permission required by ScribeRelay.

## Functional requirements
All requirements below are proposed. P0 is release-critical; P1 is optional for MVP.

| ID | Priority | Requirement |
|---|---|---|
| FR-01 | P0 | Import local UTF-8 Markdown, DOCX and clipboard rich text; provide actionable errors for invalid, unsupported or oversized inputs. |
| FR-02 | P0 | Inventory source text, blocks, headings, lists, links, emphasis, code, tables and image references; flag unrecognized structures rather than silently dropping them. |
| FR-03 | P0 | Normalize document semantics and retain original source or sufficient provenance for reconciliation during the session. |
| FR-04 | P0 | Convert to a LinkedIn Article-targeted representation using an evidenced compatibility profile; distinguish unknown from unsupported. |
| FR-05 | P0 | Preview output and display source-to-output report with preserved, transformed, manual-action, unsupported or unknown classifications. |
| FR-06 | P0 | Allow user to review transformations and choose safe available alternatives; warn before exporting unresolved losses; retain original content for recovery. |
| FR-07 | P0 | Extract accessible embedded images with source order, placement context and alt text where available; flag unresolved external or relative references. |
| FR-08 | P0 | Copy HTML and plain-text clipboard representations when supported; provide explicit fallback and failure feedback. |
| FR-09 | P0 | Provide separate title, body and media handoff guidance; user opens LinkedIn, pastes, inserts required media and saves draft. |
| FR-10 | P0 | Show compatibility profile date and limitations; never claim to have verified the user's actual LinkedIn draft automatically. |
| FR-11 | P1 | Allow basic title/body formatting edits in preview, with user edits distinguished from conversion changes. |
| FR-12 | P1 | Export recovery package with media and compatibility report. |

## Non-functional requirements
| ID | Requirement |
|---|---|
| NFR-01 | Local-first processing; no mandatory document upload, account, AI or server dependency for conversion. |
| NFR-02 | Treat document and clipboard input as untrusted; sanitize executable markup and unsafe links; avoid implicit external image fetches. |
| NFR-03 | Deterministic semantic conversion for identical input, options and compatibility profile. |
| NFR-04 | Keyboard-operable import, issue review and export; readable labels and accessible error messages. |
| NFR-05 | Clear progress/failure feedback; proposed performance and input limits in acceptance criteria subject to spikes. |
| NFR-06 | Separate import semantics from destination policy; adding a destination should not require changes to existing importers unless source capability changes. |
| NFR-07 | No hidden telemetry containing document text or assets; explicit opt-in for any future telemetry. |

## Evidence and constraints
The user verified qualitative ToolHa paste compatibility, not full element-level fidelity. Current LinkedIn support for individual formats, clipboard behavior, media transfer and native draft APIs must be verified in the feasibility phase. Do not automate LinkedIn DOM or use undocumented APIs. A preview is a simulation, not proof of destination rendering.

## Open decisions
Supported browser/OS baseline; Markdown dialect and assets bundle support; DOCX feature boundary; table/code fallback policy; severity and export acknowledgement UX; size limits; manual effort baseline; optional local persistence. Resolve with feasibility evidence and owner review.

See [MVP scope](mvp-scope.md), [roadmap](roadmap.md) and [acceptance criteria](../testing/acceptance-criteria.md).
