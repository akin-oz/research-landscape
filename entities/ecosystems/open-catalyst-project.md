---
schema_version: 2
entity_type: research-ecosystem
id: ECO-OPEN-CATALYST-PROJECT
name: Open Catalyst Project
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-OCP-OVERVIEW
  - SRC-OCP-MIGRATION
  - SRC-FAIRCHEM-CATALYST-DATASETS
ecosystem_kind: public catalysis-AI data, challenge, and open-code ecosystem with a documented code migration
website: https://opencatalystproject.org/
software_ids:
  - SW-FAIRCHEM
relationship_assertions:
  - predicate: includes
    target_id: SW-FAIRCHEM
    source_ids: [SRC-OCP-MIGRATION]
    confidence: high
    evidence_window: historical-to-2026-07
    notes: The Open-Catalyst-Project organization is explicitly deprecated and states that all code development moved to Fair-Chem, with the ocp ML-model repository now in fairchem.core. This records the documented successor software route, not an assertion that all FAIRChem scope, contributors, models, data, or governance belong to Open Catalyst Project.
---

# Open Catalyst Project

Open Catalyst Project is represented as a distinct public ecosystem for
AI-assisted heterogeneous-catalysis research, datasets, challenge, and
historical open-code surface. It is not merged into the FAIRChem software
record: the project's own public GitHub organization explicitly documents a
code-development migration to Fair-Chem and `fairchem.core`.

The explicit `includes` path therefore exposes a verifiable successor software
route while retaining Open Catalyst Project's independently named project,
dataset, demo, leaderboard, and challenge context. It does not reverse the
relationship or turn FAIRChem's wider materials and chemistry scope into an
Open Catalyst Project ownership, membership, or governance claim.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-OCP-OVERVIEW` | [Open Catalyst Project](https://opencatalystproject.org/) describes a FAIR at Meta and Carnegie Mellon chemical-engineering collaboration using AI to model and discover catalysts; it identifies public OC20/OC22 datasets, baseline models and code, a leaderboard, and an evaluation-server route. Accessed 2026-07-13. |
| `SRC-OCP-MIGRATION` | [Open-Catalyst-Project GitHub organization](https://github.com/Open-Catalyst-Project) identifies the organization as deprecated and states that code development moved to Fair-Chem, with the `ocp` ML-model repository now in `fairchem.core`; it directs users to current FAIR Chemistry documentation for OCP/ODAC datasets, the OCP API, CatTsunami, and AdsorbML. Accessed 2026-07-13. |
| `SRC-FAIRCHEM-CATALYST-DATASETS` | [FAIR Chemistry: catalyst datasets](https://fair-chem.github.io/summary-3/) identifies its catalyst-dataset documentation as covering Open Catalyst Project datasets for training and evaluating machine-learning models in heterogeneous catalysis, including OC20 and OC22. Accessed 2026-07-13. |

## Boundary and limitations

This record does not create a dataset, model, benchmark, demo, leaderboard,
API, challenge, publication, person, group, Meta, CMU, funder, or host entity.
It does not infer a complete contributor, institutional, licensing, model,
evaluation, or governance graph. Public data, code, leaderboard, and
evaluation-server routes do not establish current maintenance, support,
review, access, employment, mentorship, funding, admissions, or applicant fit.
