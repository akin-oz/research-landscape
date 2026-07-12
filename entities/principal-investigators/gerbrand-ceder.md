---
schema_version: 2
entity_type: principal-investigator
id: PI-GERBRAND-CEDER
name: Gerbrand Ceder
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-UC-BERKELEY-CEDER-PROFILE
  - SRC-UC-BERKELEY-MSE-CEDER
affiliation_ids:
  - UNIVERSITY-UC-BERKELEY
research_group_ids:
  - RG-CEDER-GROUP
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-AI-FOR-MATERIALS
website: https://ceder.berkeley.edu/
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-UC-BERKELEY
    source_ids: [SRC-UC-BERKELEY-CEDER-PROFILE, SRC-UC-BERKELEY-MSE-CEDER]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-CEDER-GROUP
    role: principal-investigator
    source_ids: [SRC-UC-BERKELEY-CEDER-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-UC-BERKELEY-CEDER-PROFILE, SRC-UC-BERKELEY-MSE-CEDER]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-AI-FOR-MATERIALS
    source_ids: [SRC-UC-BERKELEY-CEDER-PROFILE, SRC-UC-BERKELEY-MSE-CEDER]
    confidence: high
    evidence_window: 2026-07
---

# Gerbrand Ceder

Gerbrand Ceder is represented for UC Berkeley affiliation, CEDER Group
leadership, and explicitly documented computational-materials and
AI/ML-for-materials work. The record does not translate the group’s broad
public research description into software ownership, project governance, or
personal availability claims.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-UC-BERKELEY-CEDER-PROFILE` | [UC Berkeley Research: Gerbrand Ceder](https://vcresearch.berkeley.edu/faculty/gerbrand-ceder) identifies Ceder as a professor, describes the CEDER group at UC Berkeley, and describes computational approaches, high-throughput materials work, machine learning, and an AI-driven autonomous materials laboratory. Accessed 2026-07-12. |
| `SRC-UC-BERKELEY-MSE-CEDER` | [UC Berkeley Materials Science & Engineering: Gerbrand Ceder](https://mse.berkeley.edu/people_new/ceder/) identifies him as a Professor of Materials Science & Engineering and describes computational, experimental, and machine-learning methods for novel materials design in energy applications. Accessed 2026-07-12. |

## Boundary and limitations

This record makes no claim about current openings, supervision capacity,
mentoring, admissions, funding, working language, or applicant fit. Public
research descriptions do not establish a personal role in every group project,
Materials Project component, or software artifact.
