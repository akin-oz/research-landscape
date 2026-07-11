---
schema_version: 2
entity_type: research-area
id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
name: Computational Materials Science
status: reviewed
created_at: "2026-07-11"
updated_at: "2026-07-11"
last_review: "2026-07-11"
confidence: high
source_ids:
  - SRC-PSI-AIIDALAB-2026
label: Computational Materials Science
---

# Computational Materials Science

This controlled research-area record is intentionally narrow: it classifies the
documented use of AiiDA to automate complex simulations in materials science.
It does not impose a broader subject taxonomy or classify every AiiDA plugin.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PSI-AIIDALAB-2026` | [PSI, 17 February 2026: AiiDAlab Quantum ESPRESSO app](https://www.psi.ch/en/lms/scientific-highlights/theres-an-app-for-that-atomistic-materials-calculations-made-more) describes the AiiDA engine as automating complex simulations in materials science. Accessed 2026-07-11. |

## Metadata note

Both `name` and `label` are present. The vNext schema requires `label`, while
the entity-model prose describes `name` as the core area field; the reference
implementation review records that contract mismatch without changing either
architecture document.
