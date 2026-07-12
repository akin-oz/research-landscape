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
  - SRC-HACKING-MATERIALS-HANDBOOK
  - SRC-HACKING-MATERIALS-AMSET
organization_id: ORG-LBNL
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-AI-FOR-MATERIALS
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
  - predicate: works_on
    target_id: AREA-AI-FOR-MATERIALS
    source_ids: [SRC-HACKING-MATERIALS-GROUP]
    confidence: high
    evidence_window: 2026-07
mentorship_process_evidence:
  - category: onboarding-training
    source_ids: [SRC-HACKING-MATERIALS-HANDBOOK]
    scope: "Hacking Materials group handbook"
    evidence_window: "handbook reports last update approximately two years before review"
    confidence: medium
    limitation: "Documents stated onboarding and guidance only; it does not establish current practice, individual support quality, availability, or outcomes."
---

# Hacking Materials

Hacking Materials is the Berkeley Lab-hosted research-group node in this
slice. Its public description supports a focused connection to Computational
Materials Science without expanding its listed research themes into separate
project, software, or funding records.

The group’s public site describes theory, high-performance computing, AI,
community data and software infrastructure, and work with experimental and
autonomous labs on energy-relevant materials. It publicly identifies Materials
Project, FORUM-AI, data-driven synthesis, DuraMAT data and analytics, and
open-source high-throughput workflow and crystal-structure tools as current
research areas, without treating each as a new canonical project or software
record. The same page displays a small current roster and an alumni section;
neither is a complete employment record or a placement statistic.

The linked group handbook documents onboarding, communications, graduate-study
guidance, writing/presentation practices, and computing-system context, but
the handbook itself reports that it was last updated two years earlier. It is
useful process evidence, not a current mentoring, resource-access, or outcome
guarantee. Separately, AMSET documentation identifies group-led development
and a DOE Early Career funding context for that software, not a group-wide
funding ledger.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-HACKING-MATERIALS-GROUP` | [Hacking Materials](https://hackingmaterials.lbl.gov/) labels the group “computational materials science at Berkeley Lab,” identifies Dr. Anubhav Jain as group lead, and describes theory, high-performance computing, AI, community data/software infrastructure, experimental/autonomous-lab collaboration, current research areas, role categories, participation routes, and an alumni section. It is not a complete personnel, funding, partner, or outcomes record. Accessed 2026-07-12. |
| `SRC-LBNL-JAIN-PROFILE` | [Berkeley Lab Energy Technologies Area: Anubhav Jain](https://eta.lbl.gov/people/anubhav-jain) says Jain leads a research group studying new-materials design with theory, computing, and artificial intelligence. Accessed 2026-07-12. |
| `SRC-HACKING-MATERIALS-HANDBOOK` | [Hacking Materials Handbook](https://hackingmaterials.gitbook.io/hm-handbook) describes group onboarding, communication channels, graduate-study and research-writing guidance, and computing-system context. The handbook says it was last updated two years ago, so it is time-bounded process evidence rather than a current mentoring, resource, or outcome guarantee. Accessed 2026-07-12. |
| `SRC-HACKING-MATERIALS-AMSET` | [AMSET contributors](https://hackingmaterials.lbl.gov/amset/contributors/) says AMSET development is led by Hacking Materials and identifies a DOE Early Career funding context for that software. It does not establish group-wide funding, individual roles beyond those expressly listed, or a current award ledger. Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate group personnel, infer that each named research
theme is a separately governed project, or attribute Materials Project,
FORUM-AI, or software ownership and maintenance to every group member. It makes
no live-opening, admissions, group-wide funding, language, applicant-fit,
mentoring-quality, or career-outcome claim.
