# Product vision

Version 0.1 | Status: Proposed for review | 2026-11-24

## Problem
Authors prepare technical articles and other structured content in Word, Markdown editors, AI-assisted tools and other authoring environments. Moving that content into publishing editors can require reconstructing headings, links, lists, spacing, tables and images. Existing conversion tools can leave formatting inconsistencies or require manual media placement.

## Vision
ScribeRelay bridges authoring and publishing ecosystems through source-agnostic, destination-aware conversion. Authors retain their preferred writing environment and control over publication.

## Audience
Technical professionals, bloggers, knowledge workers and creators publishing existing long-form content.

## Principles
- Preserve author intent; do not silently rewrite or omit content.
- Maximize fidelity within destination capabilities; account for transformations and unsupported elements.
- Make unavoidable manual actions explicit and convenient.
- Prefer local-first processing and minimal retention.
- Respect platform boundaries; no unauthorized editor automation.
- Keep deterministic conversion independent of optional AI.
- Design for future sources and destinations without committing to premature infrastructure.

## Proposed initial scope
Markdown, DOCX and pasted rich text; destination-aware preview and compatibility report; rich-text clipboard transfer to LinkedIn Articles; media extraction and placement assistance. Direct inline media transfer is a feasibility question. Native LinkedIn draft creation is not promised: the author pastes and saves in LinkedIn.

## Success
A representative formatted document can be transferred with supported content and structure intact; every source element is accounted for as preserved, transformed, requiring manual action, or unsupported. Destination fidelity must be verified by actual paste tests, not preview alone. Quantitative targets await the PRD.

## Non-goals
A full authoring studio, social scheduling platform, autonomous publishing or mandatory AI. Future blog adapters and other integrations depend on feasibility and demand.
