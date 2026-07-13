---
schema_version: 2
entity_type: research-software
id: SW-DFTK
name: DFTK
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-DFTK-REPOSITORY, SRC-DFTK-DOCUMENTATION]
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE]
open_source: "yes"
website: https://docs.dftk.org/
repository_url: https://github.com/JuliaMolSim/DFTK.jl
license: MIT
programming_language_ids: [PROGRAMMING-LANGUAGE-JULIA]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-JULIA
    source_ids: [SRC-DFTK-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# DFTK

DFTK is an open-source collection of Julia routines for plane-wave
density-functional theory. Its separate ecosystem record owns public source,
documentation, tutorial, issue, and contribution routes.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-DFTK-REPOSITORY` | [JuliaMolSim/DFTK.jl](https://github.com/JuliaMolSim/DFTK.jl) describes DFTK as Julia routines for plane-wave DFT, displays MIT licensing, and documents issues and pull-request contribution routes. Accessed 2026-07-13. |
| `SRC-DFTK-DOCUMENTATION` | [DFTK documentation](https://docs.dftk.org/dev/) describes DFTK as a Julia library for plane-wave DFT algorithms and links its public source. Accessed 2026-07-13. |

## Boundary and limitations

This record makes no claim about performance, correctness, support, funding,
openings, mentoring, admissions, or applicant fit.
