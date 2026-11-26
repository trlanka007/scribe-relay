# M3.4 — Partial regression execution evidence

Date: 2026-11-26 | Task #151 (M3.4.c), related #91. Baseline main: 8d3e4fe1cbb5be67a20957e7d513c16fba01d727.

## Actual execution

A local Linux analysis container reported Python 3.13.5. Direct git ls-remote against the repository failed with "Could not resolve host: github.com". This environment is not a clean repository checkout. Installed package metadata was inspected before attempting validation:

| Package | Repository pin | Installed |
|---|---|---|
| markdown-it-py | 4.2.0 | 4.2.0 |
| mistune | 3.3.4 | 3.2.1 |
| python-docx | 1.2.0 | 1.2.0 |
| Pillow | 13.0.0 | 12.3.0 |

Pins do not match. No packages installed or pins altered.

Fetched disposition_probe.py through the repository connector, reconstructed its exact UTF-8 LF source in a temporary local directory and verified with git hash-object. Actual blob 7f5f605728ba3e816b114f5c1b650a1c18162888 equals the repository and runner manifest identity. Executed from that directory:

```sh
env -u PYTHONOPTIMIZE python -X utf8 -B disposition_probe.py
```

Actual output: seven tests passed, exit 0; unittest reported 0.001 seconds (not a performance benchmark).

```text
test_complete ... ok
test_encoded_targets ... ok
test_explanation ... ok
test_missing_and_overlap ... ok
test_unaccounted ... ok
test_unsupported ... ok
test_utf8_boundary ... ok
Ran 7 tests in 0.001s
OK
```

This script uses standard library only. Results apply to this exact blob in this Python environment, not to browser URL semantics, production security or semantic extraction. Other scripts were not executed in this run. The aggregate runner was not executed; ten-blob verification and pinned environment remain outstanding.

## Next action for #151

Use an owner-controlled clean LF checkout and isolated environment with exact requirements. The existing runner must record all ten blob identities, package versions and eight child outputs. Do not relax hash/pin checks to turn a diagnostic run into a pass. If pins cannot be installed, preserve the actual installation failure and review dependency choices separately. See [regression protocol](../../spikes/m3/parsers/regression-run.md).

#151 remains open; this is partial evidence only. No changes to source, dependencies, compatibility matrix or production gates. M3.2/3.3 still require manual destination evidence; M2/M5/M6 approval remains mandatory before M7.
