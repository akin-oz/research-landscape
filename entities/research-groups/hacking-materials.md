---
schema_version: 2
entity_type: research-group
id: RG-HACKING-MATERIALS
name: Hacking Materials
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-HACKING-MATERIALS-GROUP
  - SRC-LBNL-JAIN-PROFILE
organization_id: ORG-LBNL
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://hackingmaterials.lbl.gov/
relationship_assertions:
  - predicate: belongs_to
    target_id: ORG-LBNL
    source_ids: [SRC-HACKING-MATERIALS-GROUP]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-HACKING-MATERIALS-GROUP, SRC-LBNL-JAIN-PROFILE]
    confidence: high
    evidence_window: 2026-07
---

# Hacking Materials

Hacking Materials is the Berkeley Lab-hosted research-group node in this
slice. Its public description supports a focused connection to Computational
Materials Science without expanding its listed research themes into separate
project, software, or funding records.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-HACKING-MATERIALS-GROUP` | [Hacking Materials](https://hackingmaterials.lbl.gov/) labels the group “computational materials science at Berkeley Lab,” identifies Dr. Anubhav Jain as group lead, and describes theory, high-performance computing, and AI work for energy-relevant materials. Accessed 2026-07-12. |
| `SRC-LBNL-JAIN-PROFILE` | [Berkeley Lab Energy Technologies Area: Anubhav Jain](https://eta.lbl.gov/people/anubhav-jain) says Jain leads a research group studying new-materials design with theory, computing, and artificial intelligence. Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate group personnel, infer that each named research
theme is a separately governed project, or attribute Materials Project,
FORUM-AI, or software ownership and maintenance to every group member. It makes
no claim about openings, mentoring, admissions, funding, language, or
applicant fit.
