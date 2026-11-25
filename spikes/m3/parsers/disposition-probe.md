# F10 disposition contract experiment

Refs #91 #92. Run `python -B spikes/m3/parsers/disposition_probe.py` from repository root. Seven standard-library unittest cases are supplied; runtime execution is pending. Source blob: `7f5f605728ba3e816b114f5c1b650a1c18162888`.

The probe checks contiguous UTF-8 byte coverage, missing/overlapping spans, unknown dispositions, missing explanations, explicitly unsupported spans and split multibyte characters. Candidate URL checks exercise entity-encoded and percent-encoded unsafe targets, control characters and a safe HTTPS example. No output is rendered, fetched or published.

The dispositions are manually assigned test inputs, not inferred from Markdown tokens. Passing coverage checks do not establish semantic preservation: a caller could incorrectly mark a changed span as preserved. A future contract must bind each occurrence to an output element or an explicit recovery record and verify order and text/semantic equivalence. Manual recovery is not automatic preservation. Unsupported spans block success in this experiment; exact product recovery policy remains proposed.

The candidate URL check is deliberately conservative and can reject legitimate URLs (including query strings with ampersands and encoded characters). It is not a browser-equivalent URL parser or production sanitizer. Validate the actual emitted target with an appropriate platform URL parser and output-context escaping before production use. No production dependency changes or issue closure.
