# SIESTA ecosystem vertical slice review

**Review date:** 2026-07-13

**Scope:** a bounded SIESTA canonicalization covering software, ecosystem, and
the existing controlled Fortran and DFT/Electronic Structure paths.

**Outcome:** the slice adds two canonical entities and two evidence-bearing
relationships. It preserves the separation between SIESTA as software and the
SIESTA ecosystem as a public contribution and learning surface, while adding no
unsupported people or institutions.

## Evidence coverage

| Claim family | Primary evidence | Review result |
| --- | --- | --- |
| Software purpose and licensing | Official `siesta-project/siesta` repository | Supports first-principles materials DFT scope, public source access, and GNU GPLv3 display. |
| Electronic-structure and implementation scope | Official SIESTA reference manual | Supports Kohn-Sham density-functional electronic-structure calculations and Fortran 2003 implementation. |
| Installation and learning | Official quick-install guidance | Supports conda/source installation, build requirements, and serial/parallel context. |
| Contribution process | Official contributing guide | Supports GitLab forks, upstream synchronization, and merge-request workflow. |

## Relationship review

| Check | Result |
| --- | --- |
| Software ecosystem inclusion | `ECO-SIESTA → includes → SW-SIESTA` is backed by the official SIESTA repository. |
| Language implementation | `SW-SIESTA → implemented_in → PROGRAMMING-LANGUAGE-FORTRAN` is backed by the manual's explicit Fortran 2003 statement. |
| Area metadata | SIESTA's software record has bounded Computational Materials Science and DFT/Electronic Structure classifications from direct official code and reference-manual descriptions. |
| No duplicated ownership | Software facts remain in SIESTA; contribution and learning context remains in its ecosystem record; the language record owns only language identity. |

## Deliberate non-claims

1. The official project material does not establish a complete SIESTA
   developer, maintainer, reviewer, institution, funder, package, extension,
   dependency, method, or user graph.
2. A GitLab fork and merge-request route does not establish access, acceptance,
   review rights, response, support, employment, mentoring, supervision, or
   availability.
3. The slice makes no claim about technical performance, scientific quality,
   project activity, funding, openings, admissions, or applicant outcomes.

## Verification record

Acceptance requires clean canonical validation, deterministic generated output
and recommendation checks, and regression coverage of the four-criterion SIESTA
software-discovery path. The slice introduces no schema, generator, or scoring
model change.
