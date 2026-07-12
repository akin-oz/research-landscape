---
schema_version: 2
entity_type: principal-investigator
id: PI-ANUBHAV-JAIN
name: Anubhav Jain
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-LBNL-JAIN-PROFILE
  - SRC-HACKING-MATERIALS-GROUP
affiliation_ids:
  - ORG-LBNL
research_group_ids:
  - RG-HACKING-MATERIALS
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://hackingmaterials.lbl.gov/
relationship_assertions:
  - predicate: affiliated_with
    target_id: ORG-LBNL
    source_ids: [SRC-LBNL-JAIN-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-HACKING-MATERIALS
    role: principal-investigator
    source_ids: [SRC-HACKING-MATERIALS-GROUP]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-LBNL-JAIN-PROFILE, SRC-HACKING-MATERIALS-GROUP]
    confidence: high
    evidence_window: 2026-07
---

# Anubhav Jain

Anubhav Jain is represented for his Berkeley Lab affiliation, leadership of the
Hacking Materials group, and computational-materials research connection.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-LBNL-JAIN-PROFILE` | [Berkeley Lab Energy Technologies Area: Anubhav Jain](https://eta.lbl.gov/people/anubhav-jain) identifies Jain as leading a group on new-materials design using theory, computing, and artificial intelligence; it also identifies him as Associate Director of Berkeley Lab's Materials Project program. Accessed 2026-07-12. |
| `SRC-HACKING-MATERIALS-GROUP` | [Hacking Materials](https://hackingmaterials.lbl.gov/) identifies the Hacking Materials research group as computational materials science at Berkeley Lab, led by Dr. Anubhav Jain, and describes its use of theory, high-performance computing, and AI for energy-relevant materials. Accessed 2026-07-12. |

## Boundary and limitations

This record does not make a claim about Jain's role in every Materials Project
component, group-wide ownership or maintenance of any software, FORUM-AI
governance or funding, current openings, supervision capacity, mentoring,
admissions, working language, or applicant fit.
