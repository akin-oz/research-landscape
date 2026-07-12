---
schema_version: 2
entity_type: research-ecosystem
id: ECO-FAIRMAT
name: FAIRmat
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-FAIRMAT-OVERVIEW
  - SRC-FAIRMAT-TEAM
  - SRC-FAIRMAT-STORY
ecosystem_kind: materials research-data infrastructure ecosystem
website: https://www.fairmat-nfdi.eu/fairmat/
software_ids:
  - SW-NOMAD
relationship_assertions:
  - predicate: includes
    target_id: SW-NOMAD
    source_ids: [SRC-FAIRMAT-OVERVIEW]
    confidence: high
    evidence_window: 2026-07
    notes: FAIRmat describes itself as developing the infrastructure for the NOMAD Laboratory; this does not equate the ecosystem with the single software artifact.
  - predicate: connects
    target_id: PI-CLAUDIA-DRAXL
    role: spokesperson
    source_ids: [SRC-FAIRMAT-TEAM]
    confidence: high
    evidence_window: 2026-07
---

# FAIRmat

FAIRmat is represented as a research-data infrastructure ecosystem, distinct
from the NOMAD software artifact. Its public materials describe a federated
infrastructure for condensed-matter physics and the chemical physics of solids.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-FAIRMAT-OVERVIEW` | [FAIRmat](https://www.fairmat-nfdi.eu/fairmat/) describes FAIRmat as a federated infrastructure that develops the infrastructure for the NOMAD Laboratory. Accessed 2026-07-12. |
| `SRC-FAIRMAT-TEAM` | [FAIRmat Team](https://www.fairmat-nfdi.eu/fairmat/about-fairmat/team-fairmat) identifies Claudia Draxl as FAIRmat spokesperson and leader for Areas F and G. Accessed 2026-07-12. |
| `SRC-FAIRMAT-STORY` | [FAIRmat: Our Story](https://fairmat-nfdi.eu/fairmat/projects-fairmat/story-fairmat) describes FAIRmat as the NFDI consortium for condensed-matter physics and the chemical physics of solids, and distinguishes it from the broader NOMAD and FAIR-DI history. Accessed 2026-07-12. |

## Boundary and limitations

This record does not claim exclusive hosting, ownership, development, funding,
or governance of NOMAD by FAIRmat or by the linked PI. It does not enumerate
FAIRmat's multi-institutional participants, components, or data domains, and
makes no claim about current openings, mentoring, admissions, or applicant fit.
