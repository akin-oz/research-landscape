---
schema_version: 2
entity_type: research-group
id: RG-RIKEN-COMPUTATIONAL-MATERIALS-SCIENCE
name: Computational Materials Science Research Team
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-RIKEN-CMS-TEAM
  - SRC-RIKEN-CCS-OVERVIEW
organization_id: ORG-RIKEN-CCS
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://www.r-ccs.riken.jp/en/research/labs/cmasrt/
relationship_assertions:
  - predicate: belongs_to
    target_id: ORG-RIKEN-CCS
    source_ids: [SRC-RIKEN-CCS-OVERVIEW, SRC-RIKEN-CMS-TEAM]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-RIKEN-CMS-TEAM]
    confidence: high
    evidence_window: 2026-07
---

# Computational Materials Science Research Team

The Computational Materials Science Research Team is the R-CCS-hosted
research-group node in this slice. Its current public description supports a
Computational Materials Science connection through numerical methods and
simulations for quantum systems.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-RIKEN-CMS-TEAM` | [RIKEN Computational Materials Science Research Team](https://www.r-ccs.riken.jp/en/research/labs/cmasrt/) identifies Seiji Yunoki as Team Principal and describes quantum Monte Carlo, tensor-network, quantum-algorithm, and supercomputer-based simulations for quantum systems. Accessed 2026-07-12. |
| `SRC-RIKEN-CCS-OVERVIEW` | [RIKEN Center for Computational Science](https://www.riken.jp/en/research/labs/r-ccs/index.html) lists the Computational Materials Science Research Team and Seiji Yunoki in its organization. Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate personnel, turn the team’s reference to software
applications into a named software-maintainer claim, or infer a graduate route,
funding, openings, mentoring, admissions, language, or applicant fit.
