# ABINIT ecosystem vertical slice review

**Review date:** 2026-07-13

**Scope:** a bounded ABINIT canonicalization of the software suite and its
ecosystem contribution surface, reusing the controlled Fortran language.

**Outcome:** the slice adds two canonical entities and two evidence-bearing
relationships. Software, ecosystem, and language facts retain separate
ownership; no person, institution, consortium, or funding graph is inferred.

## Evidence coverage

| Claim family | Primary evidence | Review result |
| --- | --- | --- |
| Software purpose and license | ABINIT presentation and license pages | Supports DFT/materials scope and GNU GPLv3 distribution. |
| Fortran implementation | ABINIT development overview | Supports a bounded Fortran90 implementation relation. |
| Public development surface | ABINIT home, Git, and development pages | Supports packages, learning routes, Git/GitLab, testing, and a worldwide-open contribution philosophy. |

## Relationship review

| Check | Result |
| --- | --- |
| Ecosystem inclusion | `ECO-ABINIT → includes → SW-ABINIT` is backed by the project's public home. |
| Language implementation | `SW-ABINIT → implemented_in → PROGRAMMING-LANGUAGE-FORTRAN` is backed by the developer overview. |
| Area metadata | The software record's Computational Materials Science classification is limited to the published DFT/molecules/periodic-solids materials scope. |
| Ownership separation | Software facts remain in ABINIT, ecosystem learning/contribution facts in its ecosystem record, and language identity in Fortran. |

## Deliberate non-claims

1. The sources do not establish a full ABINIT maintainer, contributor,
   institution, consortium, funding, package, or user roster.
2. Public source-control, documentation, and forum routes do not establish
   current access, support, review rights, employment, mentoring, or capacity.
3. The slice makes no claim about performance, correctness, project activity,
   admissions, opportunities, or applicant outcomes.

## Verification record

Acceptance requires clean canonical validation, deterministic view and
recommendation checks after regeneration, and regression coverage of the
four-criterion ABINIT discovery path. This introduces no schema, generator, or
scoring-model change.
