---
schema_version: 2
entity_type: research-software
id: SW-MATGL
name: Materials Graph Library (MatGL)
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-MATGL-REPOSITORY
  - SRC-MATERIALYZE-SOFTWARE
  - SRC-MATGL-DOCUMENTATION
research_area_ids:
  - AREA-MATERIALS-INFORMATICS
  - AREA-AI-FOR-MATERIALS
  - AREA-MACHINE-LEARNED-POTENTIALS
ecosystem_ids:
  - ECO-MATML
open_source: "yes"
programming_language_ids:
  - PROGRAMMING-LANGUAGE-PYTHON
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-MATGL-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
  - predicate: supports
    target_id: PROBLEM-MATERIALS-PROPERTY-PREDICTION
    source_ids: [SRC-MATGL-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
website: https://matgl.ai/
repository_url: https://github.com/materialyzeai/matgl
license: BSD-3-Clause
---

# Materials Graph Library (MatGL)

MatGL is a distinct open-source graph deep-learning library for materials
science. Its canonical record covers the software artifact, documented
Materialyze.AI collaboration, Python implementation, and potential-related
architectures; it does not turn every architecture, checkpoint, model,
dataset, contributor, or application into a separate graph entity.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-MATGL-REPOSITORY` | [materialyzeai/matgl](https://github.com/materialyzeai/matgl) describes MatGL as a graph deep-learning library for materials science, identifies its first version as a Materialyze.AI and Intel Labs collaboration, documents M3GNet/CHGNet and interatomic-potential development context, reports a BSD-3-Clause license, and shows Python as the primary repository language. Accessed 2026-07-12. |
| `SRC-MATERIALYZE-SOFTWARE` | [Materialyze.AI: Home](https://www.materialyze.ai/) presents MatGL among the lab's open-source codes and describes it as a materials-science graph deep-learning library implementing foundation-potential architectures including TensorNet, CHGNet, and M3GNet. Accessed 2026-07-12. |
| `SRC-MATGL-DOCUMENTATION` | [MatGL documentation](https://matgl.ai/) describes graph deep-learning surrogate models for predicting materials properties, pretrained formation-energy and band-gap models, and property-model usage. Accessed 2026-07-13. |

## Boundary and limitations

This record does not claim that every MatGL model, checkpoint, architecture,
benchmark, dependency, or downstream use has the same accuracy, maturity,
license, or access conditions. Public code and a lab/software association do
not establish an individual maintainer, contributor, support, employment,
mentorship, admissions, or applicant-fit claim.
