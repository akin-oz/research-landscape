---
schema_version: 2
entity_type: research-software
id: SW-PHONOPY
name: Phonopy
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-PHONOPY-DOCUMENTATION, SRC-PHONOPY-REPOSITORY]
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE]
open_source: "yes"
website: https://phonopy.github.io/phonopy/
repository_url: https://github.com/phonopy/phonopy
license: BSD-3-Clause
programming_language_ids: [PROGRAMMING-LANGUAGE-PYTHON]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-PHONOPY-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The upstream repository describes Phonopy as mainly written in Python. This does not model every backend language, contributor skill, or a group-wide language policy.
---

# Phonopy

Phonopy is an open-source package for harmonic and quasi-harmonic phonon
calculations. Its separate ecosystem record owns the public documentation,
issue, pull-request, and mailing-list routes.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PHONOPY-DOCUMENTATION` | [Phonopy documentation](https://phonopy.github.io/phonopy/) describes Phonopy as an open-source package for phonon calculations at harmonic and quasi-harmonic levels, documents its Python API and interfaces to atomistic calculators, and states the New BSD license from version 1.3. Accessed 2026-07-13. |
| `SRC-PHONOPY-REPOSITORY` | [phonopy/phonopy](https://github.com/phonopy/phonopy) is the public source repository. Its README describes Phonopy as a phonon code mainly written in Python, identifies a Rust compute backend, displays BSD-3-Clause licensing, and documents issues and pull requests as project-development routes. Accessed 2026-07-13. |

## Boundary and limitations

This record makes no claim about a complete backend-language inventory,
performance, support, funding, mentoring, admissions, applicant fit, or every
Phonopy contributor, interface, or calculator integration.
