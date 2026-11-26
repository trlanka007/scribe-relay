# Aggregate parser regression checkpoint

Refs #91 #92. Baseline: PR #149 merged. Run in an isolated environment from repository root:

```sh
python -m venv .venv-m3
# Activate the virtual environment for your shell.
python -m pip install -r spikes/m3/parsers/requirements.txt
python -B spikes/m3/parsers/run_regression.py > m3-regression.json
```

The runner records exact installed versions, Git blob identities, subprocess return codes, stdout/stderr and per-script timeout. It runs eight explicitly enumerated synthetic probes, including the initial comparison. An overall exit code of zero requires all scripts to succeed, all pinned direct dependency versions to match, and all ten source/input blob identities to match. A mismatch in dependencies does not suppress diagnostic execution, but prevents an overall pass. A blob mismatch suppresses execution. Use a checkout with LF line endings for byte-for-byte verification. Keep generated logs outside version control unless reviewed for safe synthetic-only content.

The manifest intentionally fixes this baseline; a future source or requirements change needs a reviewed manifest refresh. It does not lock transitive dependencies or interpreter builds, and is not a general CI or production test harness.

## Evidence status
No aggregate execution was performed for this PR. Historical runs used differing Mistune/Pillow versions; current pins are retained without assuming installation or compatibility. The new runner makes this discrepancy visible and prevents reporting a pinned-environment pass when versions differ. PR #145 and #149 runtime evidence remains outstanding until execution is recorded. No production dependency changes, issue closure, or LinkedIn validation.
