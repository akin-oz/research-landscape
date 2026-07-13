# CP2K ecosystem vertical slice review

**Review date:** 2026-07-13

**Scope:** a bounded CP2K canonicalization covering software, ecosystem, and
controlled implementation-language identity.

**Outcome:** the slice adds three canonical entities and two evidence-bearing
relationships. It preserves the separation between CP2K as software and CP2K
as an ecosystem contribution surface, while adding no unsupported people or
institutional context.

## Evidence coverage

| Claim family | Primary evidence | Review result |
| --- | --- | --- |
| Software purpose and implementation | Public `cp2k/cp2k` repository | Supports quantum-chemistry/solid-state/atomistic-simulation scope, GPL-2.0 repository license, public source access, and Fortran 2008 implementation. |
| Open distribution | Official CP2K download page | Supports GPL availability, releases, Git development versions, and documented installation paths. |
| Contribution process | Official CP2K development guide | Supports fork, pull-request, test, CI, and integration guidance. |
| Language identity | ISO/IEC 1539-1:2023 | Supports the controlled Fortran language entity only. |

## Relationship review

| Check | Result |
| --- | --- |
| Software ecosystem inclusion | `ECO-CP2K → includes → SW-CP2K` is backed by official CP2K software and download sources. |
| Language implementation | `SW-CP2K → implemented_in → PROGRAMMING-LANGUAGE-FORTRAN` is backed by the repository's explicit Fortran 2008 description. |
| Area metadata | CP2K's software record has the bounded Computational Materials Science classification from its materials/periodic atomistic-simulation description. |
| No duplicated ownership | Software facts remain in CP2K; contribution and community surfaces remain in its ecosystem record; the language record owns only language identity. |

## Deliberate non-claims

1. The public project sources do not establish a complete CP2K developer,
   maintainer, reviewer, institution, funder, package, library, method, or
   user graph.
2. A public pull-request and CI path does not establish acceptance, review
   rights, support, employment, mentoring, supervision, or availability.
3. The slice makes no claim about technical performance, scientific quality,
   project activity, funding, openings, admissions, or applicant outcomes.

## Verification record

Acceptance requires clean canonical validation, deterministic generated output
and recommendation checks, and regression coverage of the four-criterion
software-discovery path. The slice introduces no schema, generator, or scoring
model change.
