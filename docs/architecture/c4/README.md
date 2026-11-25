# C4-inspired architecture views

Version 0.1 | Proposed hypothesis, not M5 approval | 2026-11-25

The formal C4 model describes software structure at system context, container, component and code levels. Our altitude labels are navigation aids. For project execution rather than software structure, see [milestone plan](../../engineering/milestone-execution-plan.md).

| Altitude | C4 view | Detail maturity |
|---|---|---|
| 5,000 feet | [System context](01-context.md) | Product boundaries grounded in PRD |
| 2,000 feet | [Container view](02-containers.md) | Local-first candidate; deployment undecided |
| 1,000 feet | [Component view](03-components.md) | Logical responsibilities, not packages |
| Ground level | [Contracts and runtime scenarios](04-detail.md) | Conceptual data/behavior; code-level design deferred |

Diagrams use GitHub-renderable Mermaid flowcharts rather than a specialized C4 renderer. Stable IDs connect views. No frameworks, libraries, class hierarchy, storage technology or production hosting are selected. Revisit after M3 experiments; M5 approval is still required.
