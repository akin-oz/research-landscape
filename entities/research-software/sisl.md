---
schema_version: 2
entity_type: research-software
id: SW-SISL
name: sisl
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-SISL-REPOSITORY]
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE]
open_source: "yes"
website: https://zerothi.github.io/sisl/
repository_url: https://github.com/zerothi/sisl
license: MPL-2.0
programming_language_ids: [PROGRAMMING-LANGUAGE-PYTHON]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-SISL-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
---

# sisl

sisl is an open-source Python framework for density-functional-theory analysis
and tight-binding calculations. Its separate ecosystem record owns public
source, documentation, support, and contribution routes; this record does not
model every external code, workflow, contributor, or user.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SISL-REPOSITORY` | [zerothi/sisl](https://github.com/zerothi/sisl) describes sisl as an open-source density-functional-theory API framework for post-analysis and tight-binding calculations, displays MPL-2.0 licensing, identifies it as an electronic-structure Python package, and links documentation, issues, discussions, and contribution guidance. Accessed 2026-07-13. |

## Boundary and limitations

Documented interoperability with external software remains prose context because
the graph has no safe dependency predicate. This record makes no claim about
method completeness, accuracy, performance, support, review, funding,
openings, mentoring, admissions, or applicant fit.
