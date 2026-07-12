---
schema_version: 2
entity_type: research-group
id: RG-PSI-MSD
name: Materials Software and Data Group
status: reviewed
created_at: "2026-07-11"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-PSI-MSD-GROUP
  - SRC-PSI-AIIDALAB-2026
organization_id: ORG-PSI
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-SCIENTIFIC-SOFTWARE-ENGINEERING
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
  - predicate: works_on
    target_id: AREA-SCIENTIFIC-SOFTWARE-ENGINEERING
    source_ids: [SRC-PSI-MSD-GROUP, SRC-PSI-AIIDALAB-2026]
    confidence: high
    evidence_window: 2026-02 to 2026-07
    notes: PSI describes advanced simulation software/algorithms and group-led AiiDA-engine development. This supports a scientific-software-engineering connection, not a claim that every group activity or member is a software engineer.
---

# Materials Software and Data Group

The Materials Software and Data Group is the research-group node in this slice.
It is the direct source of the documented development relationship to AiiDA;
the related AiiDA ecosystem and its other participants remain separate nodes.

The PSI group page presents a software-and-data research environment around
advanced simulation algorithms, spectroscopies, AiiDA, AiiDAlab, Materials
Cloud, high-throughput simulations, web interfaces, curated datasets, and an
autonomous-laboratories long-term goal. It publicly displays a group leader,
scientist, postdoctoral, and PhD-student roles, an October 2025 group photo, a
publication list, and internal PSI project/software links. These public surfaces
do not establish a complete roster, every code's individual maintainer,
project/funding scope, live opening, supervision capacity, or outcome record.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PSI-MSD-GROUP` | [PSI Materials Software and Data Group](https://www.psi.ch/en/lms/msd-group) describes advanced simulation software/algorithms; spectroscopic applications; AiiDA, AiiDAlab, and Materials Cloud; high-throughput simulations, web interfaces, curated datasets, an autonomous-laboratories goal, public role categories, internal project/software links, and a group publication list. It is not a complete personnel, project, funding, maintenance, opportunity, or outcome record. Accessed 2026-07-12. |
| `SRC-PSI-AIIDALAB-2026` | [PSI, 17 February 2026: AiiDAlab Quantum ESPRESSO app](https://www.psi.ch/en/lms/scientific-highlights/theres-an-app-for-that-atomistic-materials-calculations-made-more) states that AiiDA-engine development is led by this group and describes it as automating complex simulations in materials science. Accessed 2026-07-12. |

## Relationship note

The `software_ids` field is the normalized graph join used by future views. The
typed `develops` assertion is the evidence-bearing statement that gives the
join its precise meaning. It does not imply that every group member is an
individual AiiDA maintainer.

## Boundary and limitations

The displayed people and publication lists are not normalized into new people
or publication entities by this slice. PSI's links to group projects, software,
and openings are not treated as a complete funding/project catalog, a current
vacancy, eligibility, admissions, supervision capacity, or a promise of access
to AiiDAlab, Materials Cloud, datasets, high-throughput services, or automated
laboratories. The public software framing does not establish a group-wide
language policy, every code's license/governance, or a complete contributor
roster.
