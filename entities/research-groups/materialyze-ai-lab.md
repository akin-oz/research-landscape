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
  - SRC-MATERIALYZE-HOME
  - SRC-MATERIALYZE-JOIN-US
institution_id: UNIVERSITY-NUS
research_area_ids:
  - AREA-MATERIALS-INFORMATICS
  - AREA-AI-FOR-MATERIALS
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
  - predicate: works_on
    target_id: AREA-AI-FOR-MATERIALS
    source_ids: [SRC-NUS-ONG-PROFILE]
    confidence: high
    evidence_window: 2026-07
mentorship_process_evidence:
  - category: supervision-process
    source_ids: [SRC-MATERIALYZE-JOIN-US]
    scope: "Materialyze.AI Lab public postdoctoral/PhD application process"
    evidence_window: "post dated 2025-10-10 and displayed as updated 2026-02-06"
    confidence: medium
    limitation: "States onboarding and mentorship practices in a public process post; it does not establish supervision capacity, current availability, effectiveness, or outcomes."
---

# Materialyze.AI Lab

Materialyze.AI Lab is the NUS-hosted research-group node in this slice. Its
public NUS profile identifies it as a materials-informatics group; the group
record deliberately does not infer a lab-wide pymatgen development role from
the separately documented PI-level stewardship.

The group's own public material presents theory, data, learning, translation,
and community as its research pillars. It describes first-principles and
molecular-dynamics methods, AI-ready datasets, physics-informed AI, batteries,
aerospace alloys, semiconductors, open data/APIs/software, and a public
software portfolio. The Team page displays research-fellow, postdoctoral, and
graduate-student roles, but mixes NUS and UC San Diego context and is not used
as a complete NUS roster. A dated Join Us post documents an application process
and stated onboarding/mentorship practices; it is not treated as a live vacancy
or a guarantee of supervision, funding, admission, or response time.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NUS-ONG-PROFILE` | [NUS Materials Science and Engineering: Shyue Ping Ong](https://cde.nus.edu.sg/mse/staff/shyue-ping-ong/) identifies him as an NUS professor who leads the Materialyze.AI lab, a materials informatics research group integrating materials science with data science and artificial intelligence. Accessed 2026-07-12. |
| `SRC-MATERIALYZE-TEAM` | [Materialyze.AI: Team](https://www.materialyze.ai/team) identifies Shyue Ping Ong as an NUS professor and records his 2026– NUS appointment. Accessed 2026-07-12. |
| `SRC-MATERIALYZE-HOME` | [Materialyze.AI: Home](https://www.materialyze.ai/) describes the lab's theory, data, learning, translation, and community pillars; first-principles/phenomenological theory, AI-ready data, physics-informed AI, batteries/aerospace alloys/semiconductors, open data/APIs/software, and linked public software. It supplies group-level public research and software context, not a complete software-maintainer roster, project inventory, funding ledger, or performance claim. Accessed 2026-07-12. |
| `SRC-MATERIALYZE-JOIN-US` | [Materialyze.AI: Join the Team](https://www.materialyze.ai/post/join-our-team-at-materialyze-ai-lab), posted 2025-10-10 and displayed as updated 2026-02-06, describes a public postdoctoral/PhD application route, Theory & AI and Experimental Materials & AI work, contribution to open-source software/benchmarks/datasets, and stated onboarding and mentorship. It is a dated public process description, not a current vacancy, admissions decision, funding assurance, supervision capacity, or outcome guarantee. Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate personnel, represent every cross-site
collaboration, turn the public software portfolio into an individual or
exclusive maintainer roster, or claim a live opening, funding, admissions,
supervision capacity, language policy, applicant fit, mentoring quality, or
career outcome.
