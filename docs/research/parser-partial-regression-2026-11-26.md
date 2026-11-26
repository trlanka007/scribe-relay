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


## Independent follow-up execution (after PR #165 merge)

Baseline main e421204b2dc64f5186dc2dfb9bd2c65582eaa0ce. Actual container command output confirmed Python 3.13.5, the same four installed versions listed above, and git ls-remote exit 128 (Could not resolve host: github.com). No checkout or package installation succeeded or was claimed.

Reconstructed two connector-fetched scripts as UTF-8 LF files in a temporary directory. Before running each, compared git hash-object to its manifest identity. Both matched exactly:

| Script | Actual Git blob | Exit | unittest result |
|---|---|---:|---|
| disposition_probe.py | 7f5f605728ba3e816b114f5c1b650a1c18162888 | 0 | 7 tests, OK (0.001s) |
| safety_probe.py | ee9d3a953b294fbf9c2cba3de54548fe511ceedd | 0 | 11 tests, OK (0.004s) |

Commands: git hash-object on each file, followed on identity match by env -u PYTHONOPTIMIZE python -X utf8 -B <script>. Both standard-library probes, no network calls needed for execution. The disposition result independently confirms the earlier recorded result; do not count it twice as unique coverage. Actual safety unittest output (test names and outcomes):

```text
test_bad_xml ... ok
test_complex_inventory ... ok
test_dtd ... ok
test_duplicate ... ok
test_external ... ok
test_invalid_zip ... ok
test_missing_body ... ok
test_path ... ok
test_reconciliation ... ok
test_size ... ok
test_urls ... ok

Ran 11 tests in 0.004s
OK
```

18 unique test methods passed across two exact-blob scripts in this follow-up. This is not a pinned-environment aggregate run: six scripts remain unexecuted in this follow-up, the manifest is not fully verified locally, and two package pins differ. The safety probe uses deliberately small synthetic limits and a multiset reconciliation check, not full ordered semantics, OPC conformance or production security assurance. No source changes or acceptance promotion. #151 stays open.


## OPC relationship regression (after PR #166 merge)

Baseline main: 8199b7759273e57499467c6ce70ee1a74ba209c2. Actual execution in local Python 3.13.5 environment. Reused the previously reconstructed standard-library safety and disposition files and reconstructed the connector-fetched OPC source with LF line endings. Verified each Git blob against the repository manifest, then executed each using env -u PYTHONOPTIMIZE python -X utf8 -B <script>.

| Script | Git blob | Result |
|---|---|---|
| safety_probe.py | ee9d3a953b294fbf9c2cba3de54548fe511ceedd | 11 tests, OK (0.003s) |
| disposition_probe.py | 7f5f605728ba3e816b114f5c1b650a1c18162888 | 7 tests, OK (0.001s) |
| opc_probe.py | cf5c48a6ec1623e2c7a89bbfab256db81c599b05 | 11 tests, OK (0.002s) |

OPC test output (names and outcomes):

```text
test_cycle_is_finite ... ok
test_duplicate ... ok
test_invalid_targets ... ok
test_malformed_target_aliases ... ok
test_occurrences ... ok
test_orphan_relationship_part ... ok
test_raw_and_encoded_controls ... ok
test_relative_and_absolute ... ok
test_root ... ok
test_scoped_ids ... ok
test_unknown_mode ... ok
Ran 11 tests in 0.002s
OK
```

29 unique unittest methods passed across three exact-blob scripts; repeated safety/disposition runs are not additional unique coverage. The OPC results establish only the synthetic relationship subset: part-scoped IDs, repeated occurrence order, missing/external/unbound states, conservative target rejection, and finite cycle recording. They do not establish full OPC compliance or safe parsing of arbitrary Office documents.

The installed pins remain markdown-it-py 4.2.0, mistune 3.2.1, python-docx 1.2.0 and Pillow 12.3.0; mistune and Pillow differ from the manifest requirements. No aggregate run, clean checkout or full manifest verification performed. The integrated probe source was inspected but not executed this iteration. Five child scripts remain to execute independently; #151 remains open until the exact pinned aggregate evidence is available. No source or dependency changes, compatibility promotion or gate acceptance.


## Integrated package regression (after PR #167 merge)

Baseline main: 92cf32fd4bd1b3eda0c3dc5eca45a208eccb2f3f. Actual local execution in Python 3.13.5. Reconstructed integrated_probe.py from connector-fetched source in the same temporary directory as its two standard-library dependencies. Verified all four local script blobs before execution against the manifest.

| Script | Actual Git blob | Result |
|---|---|---|
| safety_probe.py | ee9d3a953b294fbf9c2cba3de54548fe511ceedd | 11 tests, OK (0.003s) |
| disposition_probe.py | 7f5f605728ba3e816b114f5c1b650a1c18162888 | 7 tests, OK (0.001s) |
| opc_probe.py | cf5c48a6ec1623e2c7a89bbfab256db81c599b05 | 11 tests, OK (0.002s) |
| integrated_probe.py | cba2614ab39575a3a4a6ffa19823988fb1106bf1 | 5 tests, OK (0.003s) |

Each command used env -u PYTHONOPTIMIZE python -X utf8 -B <script>; all returned 0. Actual integrated test names and outcomes:

```text
test_asset_identity_and_occurrences ... ok
test_external_and_header ... ok
test_missing_asset ... ok
test_order ... ok
test_reordering_is_detectable ... ok
Ran 5 tests in 0.003s
OK
```

34 unique unittest methods passed across four exact-blob scripts. Repeat executions are not counted as additional unique tests. This establishes bounded synthetic integration of archive preflight, relationship graph and main-story inventory with repeated/missing asset occurrences, external link/header relationship resolution and detection of changed block order. Header relationship resolution does not establish complete auxiliary-story text accounting. The image is placeholder bytes, not a validated or decoded raster. Reordering detection is not full semantic reconciliation or a production security guarantee.

Four child scripts remain to execute independently (package_probe.py, generated_probe.py, markdown_probe.py, compare.py). The installed dependency versions and mismatches remain as recorded above; no clean pinned checkout, full ten-blob verification or aggregate execution performed. #151 stays open. No source/dependency changes, compatibility promotion, task closure or gate acceptance.
