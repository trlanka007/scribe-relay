# 5,000 feet — system context

Proposed | Scope: ScribeRelay and external actors/systems.

```mermaid
flowchart LR
 U["Person: Author"] -->|Imports and reviews| SR["System: ScribeRelay"]
 S["External authoring tools<br/>Word / Markdown / AI editors"] -->|Files or copied content via author| U
 SR -->|Prepared body, report, assets| U
 U -->|Manual paste, media insertion, draft review| L["External system: LinkedIn Articles"]
 L -->|Draft and publishing controls| U
 SR -.->|Future destination support, not MVP| B["External publishing platforms"]
```

SR owns conversion and preparation, not authoring or publication. No direct LinkedIn API or automated DOM connection is part of MVP. Authoring tools are sources, not required integrations. Future destinations are conceptual. Trust boundary: external files and clipboard data are untrusted; LinkedIn is outside SR control. See FR-01–10, NFR-01–02 and [feasibility](../feasibility-and-constraints.md).
