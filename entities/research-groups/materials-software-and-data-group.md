---
schema_version: 2
entity_type: research-group
id: RG-PSI-MSD
name: Materials Software and Data Group
status: reviewed
created_at: "2026-07-11"
updated_at: "2026-07-11"
last_review: "2026-07-11"
confidence: high
source_ids:
  - SRC-PSI-MSD-GROUP
  - SRC-PSI-AIIDALAB-2026
organization_id: ORG-PSI
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
software_ids:
  - SW-AIIDA-CORE
website: https://www.psi.ch/en/lms/msd-group
relationship_assertions:
  - predicate: belongs_to
    target_id: ORG-PSI
    source_ids: [SRC-PSI-MSD-GROUP]
    confidence: high
    evidence_window: 2026-07
  - predicate: develops
    target_id: SW-AIIDA-CORE
    source_ids: [SRC-PSI-MSD-GROUP, SRC-PSI-AIIDALAB-2026]
    confidence: high
    evidence_window: 2026-02 to 2026-07
    notes: PSI describes the group's AiiDA-engine development as shared with the broader community; this does not assert exclusive development.
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-PSI-MSD-GROUP, SRC-PSI-AIIDALAB-2026]
    confidence: high
    evidence_window: 2026-02 to 2026-07
---

# Materials Software and Data Group

The Materials Software and Data Group is the research-group node in this slice.
It is the direct source of the documented development relationship to AiiDA;
the related AiiDA ecosystem and its other participants remain separate nodes.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PSI-MSD-GROUP` | [PSI Materials Software and Data Group](https://www.psi.ch/en/lms/msd-group) says the group develops simulation software and algorithms for novel materials and provides an open-science platform based on the AiiDA workflow engine. Accessed 2026-07-11. |
| `SRC-PSI-AIIDALAB-2026` | [PSI, 17 February 2026: AiiDAlab Quantum ESPRESSO app](https://www.psi.ch/en/lms/scientific-highlights/theres-an-app-for-that-atomistic-materials-calculations-made-more) states that AiiDA-engine development is led by this group and describes it as automating complex simulations in materials science. Accessed 2026-07-11. |

## Relationship note

The `software_ids` field is the normalized graph join used by future views. The
typed `develops` assertion is the evidence-bearing statement that gives the
join its precise meaning. It does not imply that every group member is an
individual AiiDA maintainer.
