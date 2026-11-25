# Feature specifications — proposed seeds

This directory is a repository-owned Spec Kit-inspired structure, not an initialized Spec Kit distribution. See [workflow](../docs/engineering/spec-driven-workflow.md), [constitution](constitution.md), [backlog index](../docs/engineering/github-backlog-index.md).

Each core slice has spec.md (what/why and acceptance), plan.md (candidate plan and open decisions), tasks.md (issue-linked ordered task seeds). Review/clarify before planning; no production implementation until M2/M5/M6 gates. Other features use their authoritative milestone documents and issues; create a standalone spec only when the package needs one. M3 is an experiment, not production work; see the existing [protocol](../docs/research/platform-compatibility.md).

| Feature | Specification |
|---|---|
| M7.1 | [Vertical slice](001-vertical-slice/spec.md) |
| M7.2 | [Import and assets](002-import-assets/spec.md) |
| M7.3 | [Conversion and reconciliation](003-conversion-reconciliation/spec.md) |
| M7.4 | [Preview and handoff](004-preview-handoff/spec.md) |
| M7.5 | [Acceptance and regression](005-acceptance-regression/spec.md) |

P1 editing and recovery export remain deferred; post-MVP destinations and other roadmap candidates require explicit approval.
