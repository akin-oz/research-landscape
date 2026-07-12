---
schema_version: 2
entity_type: organization
id: ORG-RIKEN-CCS
name: RIKEN Center for Computational Science
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-RIKEN-CCS-OVERVIEW
  - SRC-RIKEN-CCS-CONTACT
country_id: COUNTRY-JP
city: Kobe
organization_kind: national research center
website: https://www.r-ccs.riken.jp/en/
relationship_assertions:
  - predicate: located_in
    target_id: COUNTRY-JP
    source_ids: [SRC-RIKEN-CCS-OVERVIEW, SRC-RIKEN-CCS-CONTACT]
    confidence: high
    evidence_window: 2026-07
---

# RIKEN Center for Computational Science

RIKEN Center for Computational Science (R-CCS) is represented as the
non-university direct host for the Computational Materials Science Research
Team. Its public materials center the organization on high-performance
computing and computation-driven science.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-RIKEN-CCS-OVERVIEW` | [RIKEN Center for Computational Science](https://www.riken.jp/en/research/labs/r-ccs/index.html) describes R-CCS as a RIKEN research center centered on supercomputing and lists the Computational Materials Science Research Team with Seiji Yunoki. Accessed 2026-07-12. |
| `SRC-RIKEN-CCS-CONTACT` | [RIKEN Center for Computational Science: Access](https://www.r-ccs.riken.jp/access/) gives the Kobe campus address in Hyogo, Japan. Accessed 2026-07-12. |

## Boundary and limitations

This organization record covers the public team host and geographic relationship
used by this slice. It does not claim that every R-CCS team works on materials,
that R-CCS is the sole host of all Yunoki roles, or that its public programs
establish an opening or degree route.
