---
schema_version: 2
entity_type: principal-investigator
id: PI-GIOVANNI-PIZZI
name: Giovanni Pizzi
status: reviewed
created_at: "2026-07-11"
updated_at: "2026-07-11"
last_review: "2026-07-11"
confidence: high
source_ids:
  - SRC-PSI-PIZZI-PROFILE
  - SRC-PSI-MSD-GROUP
affiliation_ids:
  - ORG-PSI
research_group_ids:
  - RG-PSI-MSD
website: https://www.psi.ch/en/lms/people/giovanni-pizzi
orcid: https://orcid.org/0000-0002-3583-4377
relationship_assertions:
  - predicate: affiliated_with
    target_id: ORG-PSI
    source_ids: [SRC-PSI-PIZZI-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: leads
    target_id: RG-PSI-MSD
    role: group-leader
    source_ids: [SRC-PSI-PIZZI-PROFILE, SRC-PSI-MSD-GROUP]
    confidence: high
    evidence_window: 2026-07
---

# Giovanni Pizzi

Giovanni Pizzi is represented here only for the public, evidenced relationship
chain needed by the AiiDA reference slice. This record makes no claim about
current openings, supervision capacity, working language, or personal fit.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PSI-PIZZI-PROFILE` | [PSI profile: Dr. Giovanni Pizzi](https://www.psi.ch/en/lms/people/giovanni-pizzi) identifies him as “Group leader MSD,” gives the PSI affiliation and publishes the ORCID recorded above. Accessed 2026-07-11. |
| `SRC-PSI-MSD-GROUP` | [PSI Materials Software and Data Group](https://www.psi.ch/en/lms/msd-group) lists Giovanni Pizzi as the group's leader. Accessed 2026-07-11. |

## Compatibility

The legacy Giovanni Pizzi dossier remains a dated, applicant-oriented analysis.
It links here for reusable public facts; this canonical record does not absorb
the dossier's recommendations or private decision-support context.
