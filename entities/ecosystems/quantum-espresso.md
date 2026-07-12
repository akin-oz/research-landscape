---
schema_version: 2
entity_type: research-ecosystem
id: ECO-QUANTUM-ESPRESSO
name: Quantum ESPRESSO Ecosystem
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-QE-HOME
  - SRC-QE-REPOSITORY
  - SRC-QE-FORUM
  - SRC-QE-DEVELOPERS-MANUAL
  - SRC-QEF-ABOUT
  - SRC-SISSA-BARONI-CV
ecosystem_kind: open-source electronic-structure software ecosystem
website: https://www.quantum-espresso.org/
software_ids:
  - SW-QUANTUM-ESPRESSO
organization_ids:
  - ORG-QUANTUM-ESPRESSO-FOUNDATION
principal_investigator_ids:
  - PI-NICOLA-MARZARI
  - PI-STEFANO-BARONI
relationship_assertions:
  - predicate: includes
    target_id: SW-QUANTUM-ESPRESSO
    source_ids: [SRC-QE-HOME, SRC-QE-REPOSITORY]
    confidence: high
    evidence_window: 2026-07
  - predicate: connects
    target_id: ORG-QUANTUM-ESPRESSO-FOUNDATION
    role: project-foundation
    source_ids: [SRC-QEF-ABOUT]
    confidence: high
    evidence_window: 2026-07
    notes: The Foundation publicly states its support, community, copyright, open-source-protection, training, and official-voice roles. This does not establish every legal, financial, or operational relationship.
  - predicate: connects
    target_id: PI-NICOLA-MARZARI
    role: representative-member
    source_ids: [SRC-QEF-ABOUT]
    confidence: high
    evidence_window: 2026-07
    notes: The Foundation lists EPFL (Nicola Marzari) among representative members. This does not assert a Quantum ESPRESSO coding, maintenance, governance, employment, or contribution-frequency role.
  - predicate: connects
    target_id: PI-STEFANO-BARONI
    role: representative-member-and-historical-project-initiator
    source_ids: [SRC-QEF-ABOUT, SRC-SISSA-BARONI-CV]
    confidence: high
    evidence_window: 2026-07
    notes: Foundation representative-member evidence and Baroni's historical initiator/founding-director evidence do not establish a current maintainer, coding, governance, employment, or contribution-frequency role.
---

# Quantum ESPRESSO Ecosystem

The Quantum ESPRESSO ecosystem is modeled separately from the software suite.
It captures the public Foundation context, documented representative-member
links, and user/developer contribution surfaces without turning a global
community into a closed roster of people, institutions, or projects.

## Purpose, scientific scope, and contribution surfaces

The project describes Quantum ESPRESSO as open-source software for
electronic-structure calculations and nanoscale materials modelling. Its public
GitLab repository, developers' manual, forum, mailing lists, issue tracker, and
merge-request routes provide documented entry points for use and contribution.
They are learning and contribution surfaces—not promises of review, acceptance,
support, account access, or mentoring.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-QE-HOME` | [Quantum ESPRESSO](https://www.quantum-espresso.org/) describes the integrated open-source suite, its density-functional-theory, plane-wave, and pseudopotential basis, and its worldwide developer community. Accessed 2026-07-12. |
| `SRC-QE-REPOSITORY` | [QEF/q-e](https://gitlab.com/QEF/q-e) is the public source repository; its README identifies the suite and GPL version 2-or-later distribution. Accessed 2026-07-12. |
| `SRC-QE-FORUM` | [Quantum ESPRESSO Users Forum](https://www.quantum-espresso.org/forum/) identifies the users' mailing list/forum, developer mailing list, GitLab issues for problems, and GitLab merge requests for bug fixes. Accessed 2026-07-12. |
| `SRC-QE-DEVELOPERS-MANUAL` | [Quantum ESPRESSO Developers' Manual](https://www.quantum-espresso.org/developers-manual/) identifies the manual's audience as people who want to understand, modify, customize, add to, extend, improve, or clean up Quantum ESPRESSO. Accessed 2026-07-12. |
| `SRC-QEF-ABOUT` | [Quantum ESPRESSO Foundation: About](https://foundation.quantum-espresso.org/about/) states the Foundation's objectives and lists representatives from SISSA (Stefano Baroni), EPFL (Nicola Marzari), ICTP, the Oden Institute, University of North Texas, and CINECA. Accessed 2026-07-12. |
| `SRC-SISSA-BARONI-CV` | [SISSA: Stefano Baroni curriculum vitae](https://people.sissa.it/~baroni/CV%20GG.pdf) identifies Baroni as Quantum ESPRESSO project initiator and the Foundation's founding director, while marking the CV as updated in April 2024. Accessed 2026-07-12. |

## Boundary and limitations

This record does not enumerate every developer, user, representative,
institution, contributor, module, pseudopotential, interface, dependency,
publication, funding source, event, or partner. It does not infer current
maintenance, code-review authority, ongoing contribution frequency,
employment, supervision, mentoring, admission, funding, language, or applicant
fit from public community and Foundation material.
