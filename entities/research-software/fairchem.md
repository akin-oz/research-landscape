---
schema_version: 2
entity_type: research-software
id: SW-FAIRCHEM
name: FAIRChem
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-FAIRCHEM-DOCUMENTATION
  - SRC-FAIRCHEM-REPOSITORY
research_area_ids:
  - AREA-AI-FOR-MATERIALS
ecosystem_ids:
  - ECO-FAIR-CHEM
open_source: "yes"
website: https://fair-chem.github.io/
repository_url: https://github.com/facebookresearch/fairchem
license: MIT
---

# FAIRChem

FAIRChem is the distinct open-source software artifact in the FAIR Chemistry
slice. Its public documentation describes machine-learning models for materials
science and quantum chemistry, including materials and catalysis application
surfaces. The separate ecosystem record owns the broader research-community
context; this record does not turn every FAIR Chemistry dataset, model, demo,
or application into a separate software entity.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-FAIRCHEM-DOCUMENTATION` | [FAIR Chemistry Documentation](https://fair-chem.github.io/) describes FAIRChem as machine-learning models for materials science and quantum chemistry, including materials and heterogeneous-catalysis applications, and links its public source repository. Accessed 2026-07-12. |
| `SRC-FAIRCHEM-REPOSITORY` | [facebookresearch/fairchem](https://github.com/facebookresearch/fairchem) identifies `fairchem` as FAIR Chemistry's centralized repository for data, models, demos, and application efforts for materials science and quantum chemistry, and states that the code is available under the MIT License. Accessed 2026-07-12. |

## Boundary and limitations

This record does not claim that every model, checkpoint, dataset, application,
or chemistry domain has the same license, maturity, performance, or access
conditions. In particular, model/checkpoint licenses and gated-model access
can vary by application area. Public code and contribution surfaces do not
establish a contributor role, review entitlement, support guarantee, opening,
mentorship, admission, or applicant fit.
