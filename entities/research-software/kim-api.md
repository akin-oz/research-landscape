---
schema_version: 2
entity_type: research-software
id: SW-KIM-API
name: KIM API
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-KIM-API-REPOSITORY
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
open_source: "yes"
website: https://openkim.org/kim-api/
repository_url: https://github.com/openkim/kim-api
license: LGPL-2.1-or-later
programming_language_ids:
  - PROGRAMMING-LANGUAGE-CPP
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-CPP
    source_ids: [SRC-KIM-API-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The public KIM API repository identifies C++ as its primary language and describes language-neutral atomistic-simulation interfaces. This is a software implementation relation, not a group-wide language policy or individual skill claim.
---

# KIM API

KIM API is represented as the distinct public system-level library in the
OpenKIM ecosystem. It enables atomistic or molecular simulation programs to
interface with interatomic-model implementations across supported programming
languages; it is not a claim that every OpenKIM model, test, dataset, or client
code is itself a separate canonical software artifact.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-KIM-API-REPOSITORY` | [openkim/kim-api](https://github.com/openkim/kim-api) describes the KIM API package as a system-level library for language-neutral interfaces between atomistic/molecular simulation programs and interatomic-model implementations; it identifies LGPL-2.1-or-later licensing, public pull-request/issue contribution paths, and C++ as the repository's primary language. Accessed 2026-07-13. |

## Boundary and limitations

This record does not model every client code, model, test, driver, database
record, release, dependency, contributor, or user. It makes no claim about
model accuracy, support, review, acceptance, funding, openings, mentoring,
admissions, or applicant fit.
