# M3.4 integrated DOCX package evidence

Refs #91 #92 | 2026-11-25 | Baseline: merged PR #143 (e563927).

## Reproducible run

Run `python -B spikes/m3/parsers/package_probe.py` in an isolated environment with python-docx and Pillow installed. This experiment generates its own trusted DOCX in memory and never opens arbitrary user inputs or fetches URLs.

Actual local execution: Linux, Python 3.13.5, python-docx 1.2.0, Pillow 12.3.0. Five unittest cases passed. The exact tested source was verified against the GitHub branch blob SHA `ea634c302ae6a6a31237d5fe7462aaa27e30949e`. The current repository experiment requirements specify Pillow 13.0.0, not available in the local environment; rerun against the repository-pinned environment before claiming that configuration is validated. No requirement pins changed.

## Fixture and results

The hand-written expected ordered sequence has ten records: title text, before-link text, hyperlink label and target, after-link text, table with two cells, first placement anchor, image digest, second placement anchor, same image digest, end text. A distinct header sentinel is expected outside the main body.

| Test | Result |
|---|---|
| Both raw XML/relationship view and ordered python-docx view agree with the expected ten-record sequence | PASS |
| Header sentinel accounted for separately in both views | PASS |
| Two inline image occurrences share one image relationship | PASS |
| Reordered expected records demonstrate why multiset equality alone is insufficient | PASS |
| Paragraph-only API omits table cell content | PASS |

The same generated PNG bytes were hashed independently from ZIP content and the semantic library relationship target. The fixture intentionally includes a hyperlink and repeated embedded image, along with interleaved paragraphs and a table. No external URL is contacted.

## Design implications for M5

- Compare ordered occurrence records, not only sets or counts. Keep asset identity distinct from occurrence identity.
- Include source part, structural path, relationship identity and sequence position in source provenance.
- Reconcile non-body parts explicitly; headers, footnotes and comments cannot silently disappear just because the destination lacks equivalent constructs.
- Use ordered semantic iteration, supplemented by a lower-level inventory for unsupported content and relationship resolution. A paragraph-only API is insufficient.

## Limitations and next evidence

This is a narrow, valid generated package, not a Word application round trip or proof of general OPC support. The two views use different APIs over the same source and share the fixture generator's assumptions. The semantic view uses private XML APIs for image enumeration; it is not a recommended stable production interface. It is not an independent production parser. Only simple table cells and separate text/image runs are tested; mixed runs, nested tables, merged cells, numbering, formatting and arbitrary non-body parts remain unvalidated. The ordering test mutates a sequence, not a package. No untrusted package is passed to the probe, and its simple relationship path handling is not a security boundary. Prior safety and OPC probes remain separate; their integrated use against arbitrary inputs is not established.

PR #143's owner/Copilot review tightened invalid target handling and recorded eleven passing synthetic tests. PR #142 recorded eleven passing safety tests. Those are distinct historical suites, not rerun by this experiment. The new evidence narrows F09 uncertainty, but F09/F10 and #91/#92 remain open. No browser/LinkedIn support or production stack selection is implied.
