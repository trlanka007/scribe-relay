# M6.3 — Deployment strategy review

Status: proposed operational controls, not approved or implemented | 2026-11-26 ET
Task #105; parent PBI #72 as recorded in issue. Depends on M5.4 accepted stack. [Development guide](development-guide.md), [architecture alternatives](../architecture/solution-architecture.md), [threat model](../architecture/security-and-privacy.md).

## Candidate delivery model

Browser-local conversion with static HTTPS delivery remains preferred for evaluation only. Hosting serves application resources, not user documents. No required backend, database, account, server-side parser, analytics or AI. No hosting provider, public domain or deployment budget selected. If desktop/companion is chosen, reassess signing, distribution, update and local IPC risks rather than applying static-hosting assumptions.

| Environment | Purpose | Data and access |
|---|---|---|
| Local development | Build and isolated fixture tests | Synthetic only, no production credentials |
| CI validation | Reproducible build and local browser checks | Synthetic only, least privilege |
| Private preview/staging | Owner-approved release candidate smoke and security checks | Access model TBD, no private article uploads |
| Private pilot/release | Approved M8 distribution | Explicit authorization; local conversion; no public brand commitment |

These are proposed logical environments, not provisioned resources. Private repository does not automatically make hosted assets private; review hosting access and public exposure before deployment.

## Build, promote and verify

Build from a reviewed commit using accepted pinned toolchain and dependency lock. Capture source commit, artifact digest, toolchain/lock identity, test evidence, dependency review, and profile versions. Promote the same immutable artifact where practicable; if environment-specific rebuilding is necessary, record identity and rerun applicable checks. Keep environment configuration free of secrets in client bundles. Prefer manual owner-approved promotion until deployment controls are accepted.

Review HTTPS, restrictive security headers and CSP, cache behavior, no external content requests, offline after load, clipboard secure context and local asset handling. Verify actual deployed configuration and network behavior. Do not infer that static hosting or CSP alone guarantees privacy. Avoid mandatory service workers or durable document persistence until separately approved. If application caching is introduced, ensure compatible asset/profile versions and safe update behavior; do not cache authored content.

Smoke verification: load exact candidate artifact, import synthetic fixture, inspect report, exercise safe preview and local copy, verify blocked malformed input, keyboard flow and no unauthorized requests. Human destination paste/reopen remains separate. Record version, environment and actual evidence. No automated publication.

## Rollback and failure response

Keep last approved artifact and its compatible configuration/profile identity available. Trigger rollback or disable distribution for unsafe output, unauthorized data transfer, severe integrity/security regression or failed release smoke. Proposed sequence: stop promotion, identify affected artifact, restore known-good immutable artifact/configuration, verify identity and smoke checks, record incident and owner disposition. If no known-safe version exists, withdraw affected distribution rather than roll back blindly.

Browser caches and already-open sessions may retain older code; document version display, reload guidance and cache invalidation. Rollback cannot revoke user clipboard contents, files or already-transferred drafts. Do not promise instantaneous removal or physical memory erasure. Test rollback in approved staging before release.

## Readiness and release approval

M6 approval requires accepted stack, dependency/license/security controls, agreed CI gates, environment/access and rollback plan. M7 requires implementation evidence against P0 acceptance. M8 requires pilot feedback, known limitations, release smoke, demonstrated rollback and explicit owner authorization. Public launch/branding/licensing remain separate decisions.

No provider comparison with verified current pricing, infrastructure provisioning, deployment, CI workflow, rollback execution or approved controls in this PR. Formal M6.3 and M7 remain blocked by prerequisites.
