---
schema_version: 2
entity_type: research-group
id: RG-CEDER-GROUP
name: Computational and Experimental Design of Emerging Materials Research Group (CEDER)
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-UC-BERKELEY-CEDER-PROFILE
  - SRC-CEDER-GROUP-AUTONOMOUS-EXPERIMENTATION
  - SRC-CEDER-GROUP-CHGNET
institution_id: UNIVERSITY-UC-BERKELEY
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-AI-FOR-MATERIALS
  - AREA-MACHINE-LEARNED-POTENTIALS
software_ids:
  - SW-CHGNET
website: https://ceder.berkeley.edu/
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-UC-BERKELEY
    source_ids: [SRC-UC-BERKELEY-CEDER-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-UC-BERKELEY-CEDER-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-AI-FOR-MATERIALS
    source_ids: [SRC-UC-BERKELEY-CEDER-PROFILE, SRC-CEDER-GROUP-AUTONOMOUS-EXPERIMENTATION]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-MACHINE-LEARNED-POTENTIALS
    source_ids: [SRC-CEDER-GROUP-CHGNET]
    confidence: high
    evidence_window: 2026-07
    notes: The group states it developed CHGNet, a universal machine-learning potential; this does not establish model performance, every group member's role, or a complete atomistic-modelling portfolio.
  - predicate: develops
    target_id: SW-CHGNET
    source_ids: [SRC-CEDER-GROUP-CHGNET]
    confidence: high
    evidence_window: 2026-07
    notes: The group states that it developed CHGNet; this does not establish an individual maintainer roster, ownership of every release, or a current contributor role.
---

# CEDER Group

The Computational and Experimental Design of Emerging Materials Research Group
(CEDER) is the UC Berkeley-hosted group node in this slice. Official UC
Berkeley material describes computational and experimental materials design,
high-throughput computation, Materials Project contribution, machine learning,
and AI-driven autonomous materials work. Those source-backed themes support
the three controlled area links without turning every method, project, facility,
publication, or collaboration into a canonical record.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-UC-BERKELEY-CEDER-PROFILE` | [UC Berkeley Research: Gerbrand Ceder](https://vcresearch.berkeley.edu/faculty/gerbrand-ceder) identifies the Computational and Experimental Design of Emerging Materials Research group as part of UC Berkeley's Materials Science and Engineering department, describes its computational/high-throughput materials work and Materials Project contribution, and states that it has built an AI-driven autonomous laboratory for materials synthesis and characterization. Accessed 2026-07-12. |
| `SRC-CEDER-GROUP-AUTONOMOUS-EXPERIMENTATION` | [CEDER Group: Autonomous experimentation for accelerated materials discovery](https://ceder.berkeley.edu/research-areas/autonomous-experimentation-for-accelerated-materials-discovery/) describes robotic synthesis/characterization, machine-learned interpretation, and AI-enabled decision making in the group's A-Lab work. Accessed 2026-07-12. |
| `SRC-CEDER-GROUP-CHGNET` | [CEDER Group: Openings](https://ceder.berkeley.edu/contact-us/openings/) states that the group has developed CHGNet, a universal machine-learning potential, in its Modeling AI/ML description. The source also contains time-sensitive opportunity content, which is not used by this record. Accessed 2026-07-12. |

## Boundary and limitations

This record does not create an exhaustive roster, experimental-facility,
software, project, funder, industry-partner, publication, or autonomous-lab
graph. The public material is not treated as a current opening, admission,
funding, supervision, mentoring, or career-outcome claim. The group's stated
Materials Project contribution does not establish individual software
maintenance or ownership.
