---
schema_version: 2
entity_type: research-ecosystem
id: ECO-OPENKIM
name: OpenKIM Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-KIM-API-REPOSITORY
  - SRC-UMN-TADMOR-CV
  - SRC-OPENKIM-UPDATE
ecosystem_kind: open interatomic-model and atomistic-simulation infrastructure ecosystem
website: https://openkim.org/
software_ids:
  - SW-KIM-API
principal_investigator_ids:
  - PI-ELLAD-TADMOR
relationship_assertions:
  - predicate: includes
    target_id: SW-KIM-API
    source_ids: [SRC-KIM-API-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: PI-ELLAD-TADMOR
    role: founding-director
    source_ids: [SRC-UMN-TADMOR-CV]
    confidence: high
    evidence_window: historical-to-2026-07
    notes: Tadmor's CV identifies him as OpenKIM's Founding Director. This historical role does not establish current coding, maintenance, review, governance, contribution frequency, or support assignment.
---

# OpenKIM Ecosystem

The OpenKIM ecosystem is modeled separately from the KIM API library. It
captures the public interatomic-model infrastructure, the API software path,
and a bounded founding-director connection without turning an open, distributed
project into an exhaustive people, model, client-code, funding, or partner
graph.

## Purpose and contribution surfaces

The public KIM API project describes standard interfaces between atomistic
simulation programs and interatomic-model implementations, with public source,
issues, and pull-request contribution routes. OpenKIM updates describe active
API and developer-platform work for model and test development. These are
learning and contribution surfaces, not promises of review, acceptance,
support, account access, or mentoring.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-KIM-API-REPOSITORY` | [openkim/kim-api](https://github.com/openkim/kim-api) describes the KIM API package, its atomistic-simulation interface purpose, public contribution paths, LGPL-2.1-or-later license, and relationship to the wider KIM project. Accessed 2026-07-13. |
| `SRC-UMN-TADMOR-CV` | [University of Minnesota: Ellad Tadmor curriculum vitae](https://dept.aem.umn.edu/~tadmor/Biography/tadmor-cv.pdf) identifies Tadmor as Founding Director of OpenKIM and describes the project's curated interatomic-model repository, API, and testing/curation workflow. Accessed 2026-07-13. |
| `SRC-OPENKIM-UPDATE` | [OpenKIM: KIM Quarterly Update](https://openkim.org/news/2025-01-31/) documents ongoing KIM API and developer-platform work, model/test development resources, and community discussion routes. Accessed 2026-07-13. |

## Boundary and limitations

This record does not enumerate every model, test, driver, client software,
developer, contributor, institution, funder, event, or partner. It does not
infer model reliability, current maintenance, review authority, contribution
frequency, employment, supervision, mentoring, admissions, funding, language,
or applicant fit.
