---
schema_version: 2
entity_type: research-group
id: RG-MATERIALYZE-AI
name: Materialyze.AI Lab
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-NUS-ONG-PROFILE
  - SRC-MATERIALYZE-TEAM
institution_id: UNIVERSITY-NUS
research_area_ids:
  - AREA-MATERIALS-INFORMATICS
website: https://www.materialyze.ai/
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-NUS
    source_ids: [SRC-NUS-ONG-PROFILE, SRC-MATERIALYZE-TEAM]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-MATERIALS-INFORMATICS
    source_ids: [SRC-NUS-ONG-PROFILE]
    confidence: high
    evidence_window: 2026-07
---

# Materialyze.AI Lab

Materialyze.AI Lab is the NUS-hosted research-group node in this slice. Its
public NUS profile identifies it as a materials-informatics group; the group
record deliberately does not infer a lab-wide pymatgen development role from
the separately documented PI-level stewardship.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NUS-ONG-PROFILE` | [NUS Materials Science and Engineering: Shyue Ping Ong](https://cde.nus.edu.sg/mse/staff/shyue-ping-ong/) identifies him as an NUS professor who leads the Materialyze.AI lab, a materials informatics research group integrating materials science with data science and artificial intelligence. Accessed 2026-07-12. |
| `SRC-MATERIALYZE-TEAM` | [Materialyze.AI: Team](https://www.materialyze.ai/team) identifies Shyue Ping Ong as an NUS professor and records his 2026– NUS appointment. Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate personnel, represent every cross-site
collaboration, or claim group-wide pymatgen development, maintenance, funding,
openings, mentoring, admissions, language, or applicant fit.
