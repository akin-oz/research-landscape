---
schema_version: 2
entity_type: research-software
id: SW-MACE
name: MACE
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-MACE-REPOSITORY
  - SRC-MACE-DOCUMENTATION
research_area_ids:
  - AREA-MACHINE-LEARNED-POTENTIALS
open_source: "yes"
website: https://mace-docs.readthedocs.io/
repository_url: https://github.com/ACEsuit/mace
license: MIT
programming_language_ids:
  - PROGRAMMING-LANGUAGE-PYTHON
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-MACE-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The project-owned repository documents Python >= 3.9, pip installation, and Python entry points for the MACE reference implementation. This does not classify the separately named JAX implementation or establish a group-wide language policy or individual skill.
---

# MACE

MACE is a distinct open-source research-software artifact for machine-learning
interatomic potentials with higher-order equivariant message passing. The
record keeps software identity, technical scope, and license separate from the
public University affiliation and the bounded group-attributed development
evidence recorded on the PI node.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-MACE-REPOSITORY` | [ACEsuit/mace](https://github.com/ACEsuit/mace) describes MACE as fast and accurate machine-learning interatomic potentials with higher-order equivariant message passing, identifies the reference implementation as developed by named contributors and the group of Gábor Csányi, and states that the code is distributed under the MIT License. Accessed 2026-07-12. |
| `SRC-MACE-DOCUMENTATION` | [MACE documentation: Introduction](https://mace-docs.readthedocs.io/en/latest/guide/intro.html) describes MACE as machine-learning interatomic potentials with higher-order equivariant message passing. Accessed 2026-07-12. |

## Boundary and limitations

This record does not represent every MACE checkpoint, foundation model,
dataset, dependency, application, user, contributor, or organisation. The
Python relation is limited to the reviewed reference implementation; it does
not classify the separately named JAX implementation, establish a group-wide
language policy, or identify an individual's skill. The record does not assert
model performance, support availability, review entitlement, employment,
mentorship, admissions, or applicant fit.
