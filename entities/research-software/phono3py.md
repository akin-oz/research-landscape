---
schema_version: 2
entity_type: research-software
id: SW-PHONO3PY
name: Phono3py
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-PHONO3PY-DOCUMENTATION, SRC-PHONO3PY-REPOSITORY]
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-COMPUTATIONAL-PHONON-CALCULATIONS]
open_source: "yes"
website: https://phonopy.github.io/phono3py/
repository_url: https://github.com/phonopy/phono3py
license: BSD-3-Clause
programming_language_ids: [PROGRAMMING-LANGUAGE-PYTHON]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-PHONO3PY-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The upstream repository describes Phono3py as mainly written in Python. This does not model every backend language, contributor skill, or group-wide language policy.
---

# Phono3py

Phono3py is an open-source package for phonon–phonon interaction and related
properties, including lattice thermal conductivity. Its distinct ecosystem
record owns public documentation, issue, pull-request, and mailing-list routes.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PHONO3PY-DOCUMENTATION` | [Phono3py documentation](https://phonopy.github.io/phono3py/) describes phonon–phonon interaction calculations using the supercell approach, including lattice thermal conductivity, phonon lifetime/linewidth, a Python API, BSD-3-Clause licensing, and a contributor listing for Atsushi Togo at NIMS. Accessed 2026-07-13. |
| `SRC-PHONO3PY-REPOSITORY` | [phonopy/phono3py](https://github.com/phonopy/phono3py) is the public source repository. Its README describes Phono3py as a phonon–phonon-interaction package mainly written in Python, displays BSD-3-Clause licensing, and documents issues and pull requests as development routes. Accessed 2026-07-13. |

## Boundary and limitations

This record makes no claim about a complete backend-language inventory,
performance, support, funding, mentoring, admissions, applicant fit, or every
Phono3py contributor, interface, calculator integration, or dependency.
