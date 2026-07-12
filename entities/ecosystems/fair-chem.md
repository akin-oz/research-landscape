---
schema_version: 2
entity_type: research-ecosystem
id: ECO-FAIR-CHEM
name: FAIR Chemistry
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-FAIRCHEM-DOCUMENTATION
  - SRC-FAIRCHEM-REPOSITORY
ecosystem_kind: AI atomistic-simulation and chemistry ecosystem
website: https://fair-chem.github.io/
software_ids:
  - SW-FAIRCHEM
relationship_assertions:
  - predicate: includes
    target_id: SW-FAIRCHEM
    source_ids: [SRC-FAIRCHEM-DOCUMENTATION, SRC-FAIRCHEM-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: FAIR Chemistry documentation and its central public repository identify FAIRChem as the software surface; this does not assert every model, dataset, or collaborator is represented here.
---

# FAIR Chemistry

FAIR Chemistry is represented as an AI-for-materials and atomistic-simulation
ecosystem, distinct from its `fairchem` software repository. The reviewed
public surface connects machine-learning models, documentation, source code,
and material/catalyst application domains. It provides a clear discovery route
for AI-for-Materials software without manufacturing a people, funder, host, or
complete collaborator graph.

Open Catalyst Project's separately reviewed ecosystem record now owns its
historical project, dataset, challenge, and code-migration context. This record
remains the distinct current FAIRChem software-ecosystem surface; it does not
absorb Open Catalyst Project's independently bounded history or imply that all
FAIRChem scope belongs to that project.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-FAIRCHEM-DOCUMENTATION` | [FAIR Chemistry Documentation](https://fair-chem.github.io/) presents machine-learning models for materials science and quantum chemistry, with application surfaces for heterogeneous catalysis and inorganic materials, and links the public GitHub repository. Accessed 2026-07-12. |
| `SRC-FAIRCHEM-REPOSITORY` | [facebookresearch/fairchem](https://github.com/facebookresearch/fairchem) identifies `fairchem` as FAIR Chemistry's centralized public repository for data, models, demos, and application efforts for materials science and quantum chemistry under the MIT License. Accessed 2026-07-12. |

## Boundary and limitations

This record does not identify every team member, contributor, partner,
institution, publication, model, dataset, benchmark, funding source, or
application. It does not treat a model's stated performance as a universal
research-quality claim, or its public repository as a promise of access,
support, review, employment, mentorship, admissions, or fit.
