---
schema_version: 2
entity_type: research-ecosystem
id: ECO-ASE
name: Atomic Simulation Environment Ecosystem
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-ASE-DOCUMENTATION
  - SRC-DTU-CAMD-RESEARCH
  - SRC-ASE-DEVELOPMENT
  - SRC-ASE-CONTACT
ecosystem_kind: atomistic simulation software ecosystem
website: https://wiki.fysik.dtu.dk/ase/ecosystem.html
software_ids:
  - SW-ASE
research_group_ids:
  - RG-DTU-CAMD
relationship_assertions:
  - predicate: includes
    target_id: SW-ASE
    source_ids: [SRC-ASE-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: RG-DTU-CAMD
    source_ids: [SRC-DTU-CAMD-RESEARCH]
    confidence: high
    evidence_window: 2026-07
    notes: CAMD publicly documents a shared ASE development role; this does not claim it is the ecosystem's only participating group.
---

# Atomic Simulation Environment Ecosystem

The ASE ecosystem is represented separately from the ASE software artifact.
It connects the documented atomistic-simulation tooling to the CAMD group
without claiming that the recorded group exhausts the broader ecosystem.

The upstream project documents a public development and support surface around
the software—GitLab, merge requests, mailing list, Matrix chat, and a community
forum. These participation channels add ecosystem context without becoming
claims that CAMD, DTU, or any individual controls every contribution or support
interaction.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-ASE-DOCUMENTATION` | [Atomic Simulation Environment documentation](https://wiki.fysik.dtu.dk/ase/index.html) describes ASE as Python tools and modules for atomistic simulations and links an ASE ecosystem page. Accessed 2026-07-12. |
| `SRC-DTU-CAMD-RESEARCH` | [DTU Physics: Atomic-scale Materials Design](https://physics.dtu.dk/research/sections/camd/research/atomic-scale-materials-design) identifies CAMD's development of ASE. Accessed 2026-07-12. |
| `SRC-ASE-DEVELOPMENT` | [ASE documentation: Development](https://wiki.fysik.dtu.dk/ase/development/development.html) documents contribution, GitLab, code review, coding conventions, testing, and release-development guidance. Accessed 2026-07-12. |
| `SRC-ASE-CONTACT` | [ASE documentation: Contact](https://wiki.fysik.dtu.dk/ase/contact.html) documents the mailing list, Matrix chat, community forum, and public GitLab issues/merge requests. Accessed 2026-07-12. |

## Boundary and limitations

This record does not treat CAMD as the sole host or owner of ASE, enumerate
every plugin or contributing group, or infer individual maintainer roles,
funding, openings, mentoring, admissions, or applicant fit.
