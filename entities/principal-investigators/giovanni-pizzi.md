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
  - SRC-AIIDA-DEVELOPMENT-TEAM
  - SRC-WANNIER90-REPOSITORY
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
  - predicate: develops
    target_id: SW-AIIDA-CORE
    role: development-team-member
    source_ids: [SRC-AIIDA-DEVELOPMENT-TEAM]
    confidence: high
    evidence_window: 2026-07
    notes: The official AiiDA Team page lists Pizzi in the AiiDA Development team. This does not establish exclusive ownership, a current maintainer assignment, code-review authority, or a guarantee of ongoing contribution.
  - predicate: develops
    target_id: SW-WANNIER90
    role: developer-group-member
    source_ids: [SRC-WANNIER90-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The official Wannier90 repository lists Pizzi in the Wannier90 Developer Group. This does not establish exclusive ownership, a current maintainer assignment, code-review authority, or a guarantee of ongoing contribution.
---

# Giovanni Pizzi

Giovanni Pizzi is represented for the public, evidenced AiiDA development-team
role and PSI group leadership needed by the AiiDA reference slice. This record
makes no claim about current openings, supervision capacity, working language,
or personal fit.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PSI-PIZZI-PROFILE` | [PSI profile: Dr. Giovanni Pizzi](https://www.psi.ch/en/lms/people/giovanni-pizzi) identifies him as “Group leader MSD,” gives the PSI affiliation and publishes the ORCID recorded above. Accessed 2026-07-11. |
| `SRC-PSI-MSD-GROUP` | [PSI Materials Software and Data Group](https://www.psi.ch/en/lms/msd-group) lists Giovanni Pizzi as the group's leader. Accessed 2026-07-11. |
| `SRC-AIIDA-DEVELOPMENT-TEAM` | [AiiDA Team](https://aiida.net/team/) lists Giovanni Pizzi in “The AiiDA Development team” as Group Leader of the Materials Software and Data Group at PSI. It supports a bounded software-development-team role, not an exhaustive maintainer roster or current contribution-frequency claim. Accessed 2026-07-12. |
| `SRC-WANNIER90-REPOSITORY` | [wannier-developers/wannier90](https://github.com/wannier-developers/wannier90) lists Giovanni Pizzi in the Wannier90 Developer Group. It supports only the bounded developer-group relation, not exclusive ownership, current maintenance, review authority, or contribution frequency. Accessed 2026-07-13. |

## Compatibility

The legacy Giovanni Pizzi dossier remains a dated, applicant-oriented analysis.
It links here for reusable public facts; this canonical record does not absorb
the dossier's recommendations or private decision-support context.
