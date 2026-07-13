---
schema_version: 2
entity_type: research-software
id: SW-NEQUIP
name: NequIP
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-NEQUIP-REPOSITORY, SRC-NEQUIP-DOCUMENTATION]
research_area_ids: [AREA-AI-FOR-MATERIALS, AREA-MACHINE-LEARNED-POTENTIALS]
open_source: "yes"
website: https://nequip.readthedocs.io/en/latest/
repository_url: https://github.com/mir-group/nequip
license: MIT
programming_language_ids: [PROGRAMMING-LANGUAGE-PYTHON]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-NEQUIP-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
  - predicate: supports
    target_id: PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING
    source_ids: [SRC-NEQUIP-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
    notes: NequIP documentation describes E(3)-equivariant interatomic potentials and training techniques; this assertion is limited to support for the named modeling challenge.
---

# NequIP

NequIP is an open-source package for E(3)-equivariant machine-learning
interatomic potentials. Its separate ecosystem record owns public source,
documentation, integration, and contribution routes; this record does not model
every extension, pretrained model, external package, developer, or user.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-NEQUIP-REPOSITORY` | [mir-group/nequip](https://github.com/mir-group/nequip) identifies NequIP as open-source E(3)-equivariant interatomic-potential code, displays MIT licensing, and provides issue, discussion, tutorial, and contribution routes. Accessed 2026-07-13. |
| `SRC-NEQUIP-DOCUMENTATION` | [NequIP documentation](https://nequip.readthedocs.io/en/latest/introduction/intro.html) describes E(3)-equivariant interatomic potentials, an open-source code for machine learning on atomic systems, configuration and training techniques, its Python API, and developer contribution guidance. Accessed 2026-07-13. |

## Boundary and limitations

Documented integrations and extensions remain prose context because the graph
has no safe dependency predicate. This record makes no claim about model
accuracy, performance, support, review, funding, openings, mentoring,
admissions, or applicant fit.
