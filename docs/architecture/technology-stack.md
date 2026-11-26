# M5.4 — Technology stack evaluation and decision preparation

Status: proposed shortlist; no accepted stack or dependency versions | 2026-11-26 ET
Task #102 (M5.4.a), parent PBI #69 as recorded in issue. M5.1–3 and critical M3/M4 gates remain open. This is review preparation, not formal completion. See [solution architecture](solution-architecture.md), [canonical model](canonical-document-model.md), [conversion specification](conversion-specification.md), [destination adapters](destination-adapters.md).

## Decision criteria

Hard gates: local conversion without mandatory upload/account/server; safe bounded source parsing; independent ordered source accounting; deterministic conversion; explicit clipboard result and user-controlled handoff; accessible core workflow; acceptable dependency licensing and maintenance. A failure of a hard gate cannot be offset by developer convenience. Compare performance against proposed AC-10 only in the agreed device/fixture environment; AC-12 is a product outcome, not a library benchmark.

## Runtime and application alternatives

| Candidate | Why evaluate | Key uncertainty |
|---|---|---|
| TypeScript browser application (React or lightweight DOM UI) | Natural integration with browser files, clipboard, workers; shared language for UI and domain | DOCX completeness, bounded ZIP/XML parsing, runtime validation of untrusted data, browser memory |
| .NET browser runtime (Blazor WebAssembly) | Strong typed domain modeling; possible reuse of .NET document tooling | Library compatibility with browser runtime, download/startup cost, JS interop and clipboard activation, worker strategy |
| Installed desktop (e.g. .NET desktop or packaged web UI) | Local filesystem and native clipboard affordances | Signing, distribution, OS coverage, support and updates; native clipboard does not prove LinkedIn fidelity |
| Python local companion | Reuses research ecosystem conceptually | Installation, IPC/loopback security, maintenance; research probes not production-ready |
| Mandatory remote conversion | Server parser ecosystem | Fails local-first requirement; excluded unless scope explicitly changes |

Initial evaluation priority: TypeScript browser-local candidate; .NET WebAssembly is a meaningful alternative, not rejected. Desktop/companion only if measured browser constraints justify added deployment complexity. Framework selection remains open; compare React against a smaller UI approach using keyboard/focus, state/revision handling and maintenance needs. No version or provider selection.

## Candidate library evaluation matrix

Names below are candidates to investigate, not verified package recommendations. Links identify upstream projects/documentation; current versions, exact license terms, transitive dependencies, vulnerabilities, browser compatibility and maintenance status have not been checked in this review.

| Concern | Candidates / reference | Evidence needed before decision |
|---|---|---|
| Markdown | [markdown-it](https://github.com/markdown-it/markdown-it), [remark/mdast](https://github.com/remarkjs/remark) | Dialect/extension policy, exact source positions, malformed syntax, raw HTML/URL handling, independent byte/semantic coverage |
| DOCX semantic extraction | [Mammoth.js](https://github.com/mwilliamson/mammoth.js), [Open XML SDK](https://github.com/dotnet/Open-XML-SDK) for .NET candidate, bounded package/XML extraction | Authored story and table ordering, scoped relationships, repeated media, numbering/styles, unsupported parts and explicit rejection; HTML conversion alone is not inventory |
| ZIP package | [fflate](https://github.com/101arrowz/fflate), [JSZip](https://github.com/Stuk/jszip) or runtime-native package tooling | Enforce limits before/during expansion, duplicate paths, malformed archives, cancellation; no reliance on post-expansion checks alone |
| XML/HTML parsing | Browser-native APIs or reviewed bounded parser | Inert parsing, no implicit resource fetch, reject DTD/entities as appropriate, source locator fidelity |
| Sanitization | [DOMPurify](https://github.com/cure53/DOMPurify) or explicit allowlisted serializer plus independent validation | No execution/fetch in import, preview or clipboard output; URI scheme rules, final-output reconciliation after sanitization |
| Clipboard | Browser Clipboard API and explicit rendered-selection fallback | User activation, secure context, denial, exact MIME representations, F08 and actual manual LinkedIn tests |
| Tests | [Vitest](https://vitest.dev/), [Playwright](https://playwright.dev/), or .NET-native unit tests for alternative runtime | Deterministic domain tests, fixtures, local-only browser tests, offline/no-network checks, keyboard coverage; never automate LinkedIn |
| Delivery | Static HTTPS hosting; installed distribution alternatives if necessary | Immutable build artifacts, security headers, offline after load, rollback, cost/operations, no content telemetry |

Python markdown-it-py, mistune, python-docx and Pillow were used or pinned in isolated M3 research. The [parser synthesis](../research/parser-feasibility-synthesis.md) records historical evidence with limitations; #151 pinned reproducibility remains outstanding. None of those dependencies is selected for production, and results do not transfer automatically to similarly named JavaScript libraries.

## Evaluation protocol (proposed, no execution here)

Use the same synthetic Markdown, DOCX and HTML fixtures and independent expected inventory across viable runtime candidates. Record exact versions, source revision, licenses and transitive dependencies, device/browser and route. Test source coverage/order and negative cases first; reject candidates that cannot account for unsupported structures or enforce limits safely. Then test offline operation, memory/cancellation, proposed latency limits, clipboard and accessibility. Compare implementation effort and long-term maintenance only among candidates meeting hard gates. Record failed/unavailable runs rather than assigning invented scores. Review dependency licenses and security advisories at exact selected versions before any acceptance. No production package installs, hosting setup or CI changes authorized by this document.

## Decision records

See [proposed ADR packet](adr/proposed-stack-decisions.md). Each proposal has alternatives, consequences, evidence required and reversal triggers. All remain Proposed; merge of review material does not accept an ADR. Final decision needs M3/M4 evidence, M5.1–3 approval and explicit owner acceptance. M6 readiness remains a separate gate. No issue closure or compatibility promotion.
