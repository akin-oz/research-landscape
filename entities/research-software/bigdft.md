---
schema_version: 2
entity_type: research-software
id: SW-BIGDFT
name: BigDFT
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-BIGDFT-PROJECT, SRC-BIGDFT-LICENSE, SRC-BIGDFT-PACKAGE]
research_area_ids: [AREA-COMPUTATIONAL-MATERIALS-SCIENCE, AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE]
open_source: "yes"
website: https://bigdft.org/
repository_url: https://gitlab.com/l_sim/bigdft-suite
license: GPL-2.0-only
programming_language_ids: [PROGRAMMING-LANGUAGE-FORTRAN]
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-FORTRAN
    source_ids: [SRC-BIGDFT-PACKAGE]
    confidence: high
    evidence_window: 2026-07
---

# BigDFT

BigDFT is an open-source DFT code for ab-initio atomistic simulation. Its
separate ecosystem record owns public documentation, tutorial, GitLab, and
developer routes; this record does not model every suite package, dependency,
integration, contributor, or user.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-BIGDFT-PROJECT` | [BigDFT project site](https://bigdft.org/index.html) describes BigDFT as open-source software for materials and nanoscale systems and as a DFT code for ab-initio atomistic simulation. Accessed 2026-07-13. |
| `SRC-BIGDFT-LICENSE` | [BigDFT-suite license documentation](https://bigdft-suite.readthedocs.io/en/latest/overview/license.html) identifies the `bigdft` package as GPLv2. Accessed 2026-07-13. |
| `SRC-BIGDFT-PACKAGE` | [BigDFT-suite package documentation](https://bigdft-suite.readthedocs.io/en/latest/overview/package.html) identifies `bigdft` as core electronic-structure routines and documents `futile` as a Fortran library extensively used in BigDFT packages. Accessed 2026-07-13. |

## Boundary and limitations

Suite composition and external integrations remain prose context because the
graph has no safe dependency predicate. This record makes no claim about
performance, correctness, support, funding, openings, mentoring, admissions,
or applicant fit.
