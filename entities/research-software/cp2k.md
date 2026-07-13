---
schema_version: 2
entity_type: research-software
id: SW-CP2K
name: CP2K
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-CP2K-REPOSITORY
  - SRC-CP2K-DOWNLOAD
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
open_source: "yes"
website: https://www.cp2k.org/
repository_url: https://github.com/cp2k/cp2k
license: GPL-2.0-only
programming_language_ids:
  - PROGRAMMING-LANGUAGE-FORTRAN
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-FORTRAN
    source_ids: [SRC-CP2K-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The public CP2K repository identifies Fortran 2008 as the implementation language. This is a software implementation relation, not an assertion of group-wide practice or individual skill.
---

# CP2K

CP2K is represented as the distinct public software package for quantum
chemistry, solid-state physics, and atomistic simulation. The separate CP2K
ecosystem record owns the contribution and community surface; this record does
not turn every simulation method, library, test, accelerator, release,
dependency, or user into a canonical artifact.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-CP2K-REPOSITORY` | [cp2k/cp2k](https://github.com/cp2k/cp2k) describes CP2K as a quantum-chemistry and solid-state-physics package for atomistic simulation, including materials and periodic systems; it identifies Fortran 2008 implementation, public source access, and GPL-2.0 licensing. Accessed 2026-07-13. |
| `SRC-CP2K-DOWNLOAD` | [CP2K: Downloading CP2K](https://www.cp2k.org/download) states that CP2K source is open and freely available under the GPL license, identifies the public GitHub project for releases and development versions, and links installation guidance. Accessed 2026-07-13. |

## Boundary and limitations

This record does not enumerate every method, module, basis set,
pseudopotential, library, accelerator, interface, build configuration,
benchmark, contributor, institution, funder, or user. It makes no claim about
performance, correctness, support, review, funding, openings, mentoring,
admissions, or applicant fit.
