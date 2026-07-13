---
schema_version: 2
entity_type: research-ecosystem
id: ECO-DEEPMD-KIT
name: DeePMD-kit Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-DEEPMD-REPOSITORY, SRC-DEEPMD-DOCUMENTATION]
ecosystem_kind: open machine-learned-potential and molecular-simulation software ecosystem
website: https://deepmd-kit.readthedocs.io/en/stable/
software_ids: [SW-DEEPMD-KIT]
relationship_assertions:
  - predicate: includes
    target_id: SW-DEEPMD-KIT
    source_ids: [SRC-DEEPMD-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# DeePMD-kit Ecosystem

The DeePMD-kit ecosystem is distinct from its software artifact. Public source,
documentation, installation, issues, pull requests, discussions, and
contribution guidance are discovery routes, not a claim of access, review,
acceptance, mentoring, support, membership, or a complete community roster.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-DEEPMD-REPOSITORY` | [deepmodeling/deepmd-kit](https://github.com/deepmodeling/deepmd-kit) is the public source repository and exposes issues, pull requests, discussions, CI, releases, and contribution guidance. Accessed 2026-07-13. |
| `SRC-DEEPMD-DOCUMENTATION` | [DeePMD-kit documentation](https://deepmd-kit.readthedocs.io/en/stable/) exposes public installation and interface documentation. Accessed 2026-07-13. |

## Boundary and limitations

This record does not enumerate developers, maintainers, reviewers, institutions,
funders, interfaces, models, training data, releases, or users, and does not
infer individual role, contribution frequency, employment, supervision,
mentoring, funding, admissions, or applicant fit.
