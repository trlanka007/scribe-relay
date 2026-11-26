# M3.3 manual media experiment — F05/F06

Refs #88 #89 #90. Status: ready-to-run instructions, no destination results. Scope authorized for synthetic manual experiments; never automate LinkedIn, publish, or share private draft URLs.

## Fixture preparation

From repository root run `python -m http.server 8765 --bind 127.0.0.1`. Open `http://localhost:8765/spikes/m3/media/` for the rendered selection test. For native upload open `http://localhost:8765/spikes/m3/media/export.html`, click Generate PNG and SHA-256, then save the generated anchor.png. Stop server after testing. The exporter uses canvas and local SVG only; it does not upload. Record the digest and byte size and independently check the saved file (PowerShell `Get-FileHash -Algorithm SHA256 -Path anchor.png` or `sha256sum anchor.png`). Match the two values before proceeding. Browser fonts and encoders may produce different valid PNG bytes; do not assume a fixed PNG hash across environments.

Expected source: `anchor.svg` Git blob `f807403ee6dede83bdc2ada441b946a258e59f54`; 480 x 240; visible Synthetic image A / Placement checkpoint; alt Synthetic image A: placement checkpoint. Ordered body inventory: heading Synthetic media placement; Anchor A — before image.; image A; Caption A — image between anchors.; Anchor B — after image. Exclude the trailing instructional paragraph from the rendered selection. Verify source identity before each run.

## Run metadata (one sheet per browser and method)

Date/time, tester, OS/browser version, source revision, source SVG hash, PNG SHA-256/byte count, local origin, editor context, permissions, method, elapsed active time, actions, sanitized evidence reference. All fields pending.

## Separate manual runs

1. F05: copy rendered selection from heading through Anchor B, paste once into a fresh personal Article draft, record text, image, placement, caption/alt controls and any warnings before correction. Allow autosave, leave and reopen through Manage > Drafts, record again.
2. F06 body: in a fresh draft, enter anchors and insert the generated local PNG through native editor controls. Record actual placement, caption and alt availability, visible size/crop and steps. Reopen after autosave and inspect again.
3. F06 cover: upload the PNG through the cover control in a distinct fresh draft. Record acceptance, crop, displayed text visibility and persistence separately from body media. Do not infer cover results from body results.
4. Repeat separately in Edge and Chrome. Do not publish. Manually delete synthetic drafts when finished.

| Observation | At paste/upload | After reopen | Outcome / recovery |
|---|---|---|---|
| Anchor A and B text/order | Pending | Pending | Unknown |
| Body image presence/count | Pending | Pending | Unknown |
| Image placement between anchors | Pending | Pending | Unknown |
| Image visible content/crop | Pending | Pending | Unknown |
| Caption text/position | Pending | Pending | Unknown |
| Alt availability/value via editor controls | Pending | Pending | Unknown |
| Separate cover acceptance/crop | Pending | Pending | Unknown |

Mark not applicable for rows outside the specific run, not preserved. If a control is absent or unobservable, record Unknown or observed unsupported with reason; never infer alt text or persisted binary equality from appearance. Record active duration, manual edits and recovery steps separately. No matrix promotion without repeatable evidence.

## Limitations
Exporter source inspected only; browser runtime and actual PNG generation/hash remain pending. The fixture is synthetic and tests a single image. No actual LinkedIn media or cover compatibility established.
