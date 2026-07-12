# LAMMPS ecosystem-intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** a Quality Gate 3 canonicalization of the existing LAMMPS discovery
trail into software, ecosystem, and source-bounded Sandia organizational
context.

**Outcome:** the slice adds three canonical entities and four evidence-bearing
relationships. It captures the public software, C++ implementation, GPLv2,
GitHub contribution, and original-Sandia-development paths without claiming a
complete developer or governance graph.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Software scope and license | Official LAMMPS documentation and public GitHub repository | Supports classical MD for materials modelling, parallel/extensible design, and GPLv2 distribution. |
| Implementation and contribution | Public GitHub repository plus official developer/contribution documentation | Supports C++ implementation context, public GitHub workflow, contribution requirements, tests, and review path. |
| Sandia connection | Official LAMMPS sources plus Sandia's official About page | Supports original Sandia development and a sourced Organization-to-country endpoint. |

## Relationship review

| Check | Result |
| --- | --- |
| Ecosystem software inclusion | `ECO-LAMMPS → includes → SW-LAMMPS` is sourced by official documentation and central public repository. |
| Original-development context | `ECO-LAMMPS → connects → ORG-SANDIA-NATIONAL-LABORATORIES` uses only original-development language and explicitly excludes exclusive-current-role claims. |
| C++ implementation | `SW-LAMMPS → implemented_in → PROGRAMMING-LANGUAGE-CPP` is backed by the repository's primary-language declaration and C++ developer documentation. |
| Person graph boundary | Only the independently reviewed Temple–Kohlmeyer record is now connected; all other public developer/team material remains outside the graph until separately reviewed. |

## Deliberate non-claims

1. Public source code, pull requests, tests, forums, and contribution guidance
   do not establish individual review, acceptance, support, mentorship,
   employment, or governance roles.
2. Original Sandia development does not establish exclusive current ownership,
   hosting, funding, staffing, or project governance.
3. No performance, opening, admissions, funding, rank, language, or applicant
   fit claim is made.

## Verification record

The slice is accepted only when canonical validation, deterministic view and
recommendation drift checks, and the repository regression suite pass after
regeneration. It introduces no architecture, schema, generator, or scoring
change.
