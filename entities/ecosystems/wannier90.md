---
schema_version: 2
entity_type: research-ecosystem
id: ECO-WANNIER90
name: Wannier90 Ecosystem
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-WANNIER90-REPOSITORY
  - SRC-WANNIER90-FEATURES
  - SRC-WANNIER90-SUPPORT
ecosystem_kind: open electronic-structure and Wannier-functions software ecosystem
website: https://wannier.org/
software_ids:
  - SW-WANNIER90
principal_investigator_ids:
  - PI-GIOVANNI-PIZZI
  - PI-NICOLA-MARZARI
relationship_assertions:
  - predicate: includes
    target_id: SW-WANNIER90
    source_ids: [SRC-WANNIER90-REPOSITORY, SRC-WANNIER90-FEATURES]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: PI-GIOVANNI-PIZZI
    role: developer-group-member
    source_ids: [SRC-WANNIER90-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The official repository lists Giovanni Pizzi in the Wannier90 Developer Group. This does not establish exclusive ownership, a maintainer assignment, review authority, employment, or contribution frequency.
  - predicate: connects
    target_id: PI-NICOLA-MARZARI
    role: developer-group-member
    source_ids: [SRC-WANNIER90-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
    notes: The official repository lists Nicola Marzari in the Wannier90 Developer Group. This does not establish exclusive ownership, a maintainer assignment, review authority, employment, or contribution frequency.
---

# Wannier90 Ecosystem

The Wannier90 ecosystem is modeled separately from the Wannier90 code. It
records a bounded public developer-group connection, source, issue, contribution,
documentation, tutorial, and support context without creating a complete
community, institutional, funding, or interface graph.

## Contribution and learning surfaces

Wannier90 publishes a GitHub repository, issue and contribution guidance,
developer documentation, user guide, tutorial, and support material. Its public
project pages identify GitHub as the development location and describe CI
context. These are transparent learning and contribution routes, not a promise
of access, acceptance, review, response, support, mentoring, or membership.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-WANNIER90-REPOSITORY` | [wannier-developers/wannier90](https://github.com/wannier-developers/wannier90) is the official source repository, links contribution and issue guidance, and lists Giovanni Pizzi and Nicola Marzari in the Wannier90 Developer Group. Accessed 2026-07-13. |
| `SRC-WANNIER90-FEATURES` | [Wannier90 features](https://wannier.org/features/) describes GitHub-managed development, continuous integration, contribution context, and electronic-properties-of-materials scope. Accessed 2026-07-13. |
| `SRC-WANNIER90-SUPPORT` | [Wannier90 support](https://wannier.org/support/) links current user-guide, tutorial, source-documentation, and past tutorial/event material. Accessed 2026-07-13. |

## Boundary and limitations

This record does not enumerate every developer, maintainer, reviewer,
contributor, institution, funder, interface, workflow, library, release, test,
event, or user. It does not infer individual role beyond the documented
Developer Group listing, review authority, contribution frequency, employment,
support, supervision, mentoring, funding, admissions, or applicant fit.
