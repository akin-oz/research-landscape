---
schema_version: 2
entity_type: research-software
id: SW-DEEPMD-KIT
name: DeePMD-kit
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-DEEPMD-REPOSITORY, SRC-DEEPMD-DOCUMENTATION]
research_area_ids: [AREA-AI-FOR-MATERIALS, AREA-MACHINE-LEARNED-POTENTIALS]
open_source: "yes"
website: https://deepmd-kit.readthedocs.io/en/stable/
repository_url: https://github.com/deepmodeling/deepmd-kit
license: LGPL-3.0-only
programming_language_ids: [PROGRAMMING-LANGUAGE-PYTHON, PROGRAMMING-LANGUAGE-CPP]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-DEEPMD-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-CPP
    source_ids: [SRC-DEEPMD-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# DeePMD-kit

DeePMD-kit is a distinct deep-learning package for interatomic potential-energy
and force-field models and molecular dynamics. Its ecosystem record owns public
source, installation, issue, contribution, and documentation routes; this
record does not model every backend, interface, package, model, user, or result.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-DEEPMD-REPOSITORY` | [deepmodeling/deepmd-kit](https://github.com/deepmodeling/deepmd-kit) describes a Python/C++ package for deep-learning interatomic potential-energy/force-field models and molecular dynamics, identifies GNU LGPLv3 licensing, and links contribution guidance. Accessed 2026-07-13. |
| `SRC-DEEPMD-DOCUMENTATION` | [DeePMD-kit documentation](https://deepmd-kit.readthedocs.io/en/stable/) provides public installation and Python/C++ interface documentation. Accessed 2026-07-13. |

## Boundary and limitations

The repository documents interfaces with several external simulation packages;
these remain prose context because the current graph has no safe dependency
predicate. This record makes no claim about model accuracy, performance,
support, review, funding, openings, mentoring, admissions, or applicant fit.
