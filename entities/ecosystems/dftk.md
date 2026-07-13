---
schema_version: 2
entity_type: research-ecosystem
id: ECO-DFTK
name: DFTK Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-DFTK-REPOSITORY, SRC-DFTK-DOCUMENTATION]
ecosystem_kind: open plane-wave density-functional-theory software ecosystem
website: https://docs.dftk.org/
software_ids: [SW-DFTK]
relationship_assertions:
  - predicate: includes
    target_id: SW-DFTK
    source_ids: [SRC-DFTK-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# DFTK Ecosystem

The DFTK ecosystem records public source, documentation, tutorial, issue, and
pull-request routes without asserting a complete contributor, institution,
funding, maintainer, or support graph.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-DFTK-REPOSITORY` | [JuliaMolSim/DFTK.jl](https://github.com/JuliaMolSim/DFTK.jl) provides public source, issues, pull requests, tutorials, and contribution guidance. Accessed 2026-07-13. |
| `SRC-DFTK-DOCUMENTATION` | [DFTK installation documentation](https://docs.dftk.org/stable/guide/installation/) documents Julia package installation, tutorials, and developer setup. Accessed 2026-07-13. |

## Boundary and limitations

Public routes do not establish access, acceptance, review, response, support,
mentoring, membership, individual role, funding, admissions, or applicant fit.
