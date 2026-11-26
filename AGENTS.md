# Agent instructions

ScribeRelay is in documentation-first discovery. Read README.md and docs/README.md before modifying anything.

- Do not implement production application code until requirements and architecture have been approved.
- Isolated, disposable feasibility spikes may be performed after owner approval of the experiment scope. Keep them separate from production code; use synthetic data, document results and do not commit to production dependencies or infrastructure.
- Preserve author intent and account for all content elements; never hide conversion losses.
- Separate observations, hypotheses, accepted decisions and validated results.
- Never claim a feature is supported by LinkedIn without evidence; respect platform rules and avoid unauthorized automation.
- Prefer local-first processing, sanitized input/output and minimum permissions; never commit credentials or private fixtures.
- Keep changes scoped to a reviewable branch and pull request. Do not merge without owner approval or force-push.
- Document unresolved assumptions, alternatives and test limitations.
- Technology choices and licensing remain provisional. Do not introduce production dependencies or infrastructure without review.

- Maintain native GitHub Epic → Feature → PBI → Task sub-issue relationships. Verify the parent before claiming backlog completion; if connector writes are unavailable, report the gap and use an owner-approved native GitHub mechanism. Do not substitute parent text for a native relationship.

- Every pull request must identify the relevant existing task issue(s) in a dedicated Task traceability section of its description, using GitHub issue links and the stable task IDs. Distinguish tasks advanced from related dependencies or debt; state whether completion evidence is satisfied. Use closing keywords only when the task's completion criteria are met and the required approvals are recorded. Prefer native PR-to-issue linkage when available; ordinary cross-references do not substitute for verified native linkage. Report any connector limitation explicitly.
