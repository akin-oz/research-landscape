---
schema_version: 2
entity_type: research-group
id: RG-SOLGROUP
name: SOLgroup
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-SOLGROUP-HOME
  - SRC-HU-DRAXL-PROFILE
institution_id: UNIVERSITY-HU-BERLIN
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://sol.physik.hu-berlin.de/
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-HU-BERLIN
    source_ids: [SRC-SOLGROUP-HOME]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-SOLGROUP-HOME]
    confidence: high
    evidence_window: 2026-07
---

# SOLgroup

SOLgroup is the Humboldt-Universität zu Berlin-hosted solid-state-theory group
in this slice. Its public description supports a focused Computational Materials
Science connection; the mention of NOMAD and FAIRmat is not expanded into an
unsupported group-wide software-maintenance claim.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SOLGROUP-HOME` | [SOLgroup](https://sol.physik.hu-berlin.de/) identifies the solid-state theory group at the Physics Department of Humboldt-Universität zu Berlin as led by Prof. Claudia Draxl and dedicated to condensed-matter theory and computational materials science. Accessed 2026-07-12. |
| `SRC-HU-DRAXL-PROFILE` | [Humboldt-Universität zu Berlin: Claudia Draxl](https://www.hu-berlin.de/personen/prof-dr-dr-hc-claudia-draxl) identifies Draxl as a professor in the Institute of Physics, Theoretical Physics (Solid State Theory). Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate personnel, treat the group’s research themes as
separate projects, or infer group-wide NOMAD or FAIRmat ownership,
development, or maintenance. It makes no claim about openings, mentoring,
admissions, funding, language, or applicant fit.
