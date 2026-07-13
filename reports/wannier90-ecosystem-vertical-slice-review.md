# Wannier90 ecosystem vertical slice review

**Review date:** 2026-07-13

**Scope:** a bounded Wannier90 canonicalization covering software, ecosystem,
controlled language/area paths, and two directly sourced developer-group
relations to existing PI records.

**Outcome:** the slice adds two canonical entities and six evidence-bearing
relationships. It distinguishes Wannier90 software, its ecosystem participation
surface, and two source-bounded PI development relations without creating a
complete people, institutional, or related-software graph.

## Evidence coverage

| Claim family | Primary evidence | Review result |
| --- | --- | --- |
| Software scope and licensing | Official `wannier-developers/wannier90` repository and project features page | Supports open electronic-properties-of-materials scope, public source/contribution context, and LGPL-2.1-or-later licensing. |
| Implementation | Official library-mode documentation | Supports a Fortran library interface and C interoperability context. |
| Developer group | Official repository | Directly lists Giovanni Pizzi and Nicola Marzari in the Wannier90 Developer Group. |
| Learning and support | Official support page | Supports user-guide, tutorial, source-documentation, and event-material routes. |

## Relationship review

| Check | Result |
| --- | --- |
| Software ecosystem inclusion | `ECO-WANNIER90 → includes → SW-WANNIER90` is backed by official repository and project-feature material. |
| Language implementation | `SW-WANNIER90 → implemented_in → PROGRAMMING-LANGUAGE-FORTRAN` is backed by the official Fortran library-interface documentation. |
| PI development paths | `PI-GIOVANNI-PIZZI` and `PI-NICOLA-MARZARI` each have a direct `develops → SW-WANNIER90` assertion from the official Developer Group listing. |
| Ecosystem PI paths | Ecosystem `connects` relations repeat the same direct, role-bounded Developer Group evidence without claiming current maintenance or governance. |
| No duplicated ownership | Software facts remain in Wannier90; public participation context remains in its ecosystem record; PI records own their individual development paths. |

## Deliberate non-claims

1. The sources do not establish a complete Wannier90 developer, maintainer,
   reviewer, institution, funder, interface, workflow, method, or user graph.
2. A Developer Group listing does not establish exclusive ownership, current
   maintenance, review rights, contribution frequency, employment, support,
   mentoring, supervision, or availability.
3. The slice makes no claim about technical performance, scientific quality,
   project activity, funding, openings, admissions, or applicant outcomes.

## Verification record

Acceptance requires clean canonical validation, deterministic generated output
and recommendation checks, and regression coverage of the four-criterion
Wannier90 software-discovery path and bounded PI development assertions. The
slice introduces no schema, generator, or scoring-model change.
