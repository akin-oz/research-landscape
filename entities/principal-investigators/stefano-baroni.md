---
schema_version: 2
entity_type: principal-investigator
id: PI-STEFANO-BARONI
name: Stefano Baroni
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-SISSA-BARONI-CV
  - SRC-SISSA-BARONI-PROFILE
  - SRC-QEF-ABOUT
affiliation_ids:
  - UNIVERSITY-SISSA
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
website: https://people.sissa.it/~baroni/
relationship_assertions:
  - predicate: affiliated_with
    target_id: UNIVERSITY-SISSA
    source_ids: [SRC-SISSA-BARONI-PROFILE]
    confidence: high
    evidence_window: 2026-07
  - predicate: works_on
    target_id: AREA-COMPUTATIONAL-MATERIALS-SCIENCE
    source_ids: [SRC-SISSA-BARONI-CV]
    confidence: high
    evidence_window: 2026-07
    notes: The public SISSA CV describes Baroni's theoretical-condensed-matter and quantum-simulation work. This is an area connection, not a complete research, affiliation, supervision, or availability profile.
---

# Stefano Baroni

Stefano Baroni is represented for a current SISSA affiliation, documented
computational-materials research connection, and historical Quantum ESPRESSO
project/Foundation context. The record deliberately does not manufacture a
maintainer assignment or contribution-frequency claim.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SISSA-BARONI-CV` | [SISSA: Stefano Baroni curriculum vitae](https://people.sissa.it/~baroni/CV%20GG.pdf) describes his theoretical condensed-matter and quantum-simulation profile, identifies him as the initiator of the Quantum ESPRESSO project and founding director of the Quantum ESPRESSO Foundation, and notes that the document was updated in April 2024. Accessed 2026-07-12. |
| `SRC-SISSA-BARONI-PROFILE` | [SISSA Condensed Matter Theory: Stefano Baroni](https://cm.sissa.it/people/stefano-baroni) identifies him as a Full Professor with SISSA Condensed Matter Theory and describes quantum-simulation methods and materials-related research interests. Accessed 2026-07-12. |
| `SRC-QEF-ABOUT` | [Quantum ESPRESSO Foundation: About](https://foundation.quantum-espresso.org/about/) lists SISSA (Stefano Baroni) among representative members. Accessed 2026-07-12. |

## Boundary and limitations

The historical initiator and founding-director evidence does not establish a
current coding, maintainer, governance, release, or contribution-frequency
role. The SISSA affiliation does not establish supervision, mentoring, funding,
admissions, or applicant fit.
