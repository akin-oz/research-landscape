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
  - SRC-SOLGROUP-PUBLICATIONS
  - SRC-SOLGROUP-CODE-DEVELOPMENT
  - SRC-EXCITING-PROJECT
  - SRC-SOLGROUP-PEOPLE
  - SRC-SOLGROUP-STUDENT-TOPICS
  - SRC-SOLGROUP-GRAFOX
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

Its public pages describe theoretical spectroscopy, electron-phonon coupling,
interfaces, nanostructures, thermoelectricity, oxides, and solar-cell
materials. The group states that it is the core developer team of the
electronic-structure code `exciting` and the cluster-expansion package CELL;
the official `exciting` project page identifies it as GPL-licensed open-source
software. The group site also displays a current roster, a dated former-member
archive, an extensive chronological publication list, student-topic discovery
pages, and a GraFOx partnership page. These sources are not a complete
employment, career, funding, or collaboration record.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SOLGROUP-HOME` | [SOLgroup](https://sol.physik.hu-berlin.de/) identifies the solid-state theory group at the Physics Department of Humboldt-Universität zu Berlin as led by Prof. Claudia Draxl and dedicated to condensed-matter theory and computational materials science, including theoretical spectroscopy, electron-phonon coupling, and several materials topics. It contextualizes NOMAD and FAIRmat without establishing group-wide software governance. Accessed 2026-07-12. |
| `SRC-HU-DRAXL-PROFILE` | [Humboldt-Universität zu Berlin: Claudia Draxl](https://www.hu-berlin.de/personen/prof-dr-dr-hc-claudia-draxl) identifies Draxl as a professor in the Institute of Physics, Theoretical Physics (Solid State Theory). Accessed 2026-07-12. |
| `SRC-SOLGROUP-PUBLICATIONS` | [SOLgroup: Publications](https://sol.physik.hu-berlin.de/index.php?page=publications) is the group’s chronological peer-reviewed-publication surface, including dated 2026 entries and linked DOI/data records. It is not a productivity, quality, or individual-attribution metric. Accessed 2026-07-12. |
| `SRC-SOLGROUP-CODE-DEVELOPMENT` | [SOLgroup: Code development](https://sol.physik.hu-berlin.de/index.php?page=exciting-code) says the group develops DFT/beyond-DFT code and is the core developer team of `exciting` and CELL. It does not establish individual roles, complete governance, or all codebases associated with the group. Accessed 2026-07-12. |
| `SRC-EXCITING-PROJECT` | [exciting: About](https://exciting-code.org/home/about/exciting) identifies `exciting` as an open-source, GPL-licensed all-electron electronic-structure code with source management, build, tests, and tutorials. It supports the software’s public surface, not individual SOLgroup roles or a general license claim for CELL or other group outputs. Accessed 2026-07-12. |
| `SRC-SOLGROUP-PEOPLE` | [SOLgroup: Former members](https://sol.physik.hu-berlin.de/index.php?page=former-members) records prior group roles and periods, while the home page displays people currently working in the group. These lists are not complete employment records, current headcounts, or career-outcome statistics. Accessed 2026-07-12. |
| `SRC-SOLGROUP-STUDENT-TOPICS` | [SOLgroup: Job opportunities](https://sol.physik.hu-berlin.de/index.php?page=job-opportunities) describes master/bachelor topic areas, including `exciting`-related method work. It does not establish a specific current opening, eligibility, funding, or supervision capacity. Accessed 2026-07-12. |
| `SRC-SOLGROUP-GRAFOX` | [SOLgroup: GraFOx](https://sol.physik.hu-berlin.de/index.php?page=grafox) identifies SOLgroup as a main partner in the GraFOx ScienceCampus and describes oxide research using DFT, MD, and many-body perturbation theory. It does not establish a complete partner, funding, or project-governance graph. Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate personnel, treat the group’s research themes as
separate projects, or infer group-wide NOMAD or FAIRmat ownership,
development, or maintenance. It makes no live-opening, admissions, group-wide
funding, language, applicant-fit, mentoring-quality, or career-outcome claim.
