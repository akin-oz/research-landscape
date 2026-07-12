# Quantum ESPRESSO ecosystem-intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** a Quality Gate 3 canonicalization of the existing Quantum ESPRESSO
discovery trail into software, ecosystem, Foundation organization, and bounded
PI context.

**Outcome:** the slice adds six canonical entities and six evidence-bearing
relationships. It is intentionally narrower than a full community census: the
sources establish public software, Foundation, representative-member, direct
SISSA affiliation, and contribution surfaces, but not an exhaustive
institution, contributor, funding, or governance graph.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Software purpose and license | Official Quantum ESPRESSO home page and QEF GitLab repository | Supports the DFT/plane-wave/pseudopotential materials-modelling scope and GPL-2.0-or-later source distribution. |
| Community and contribution path | Official forum, developers' manual, and GitLab repository | Supports public user/developer discussion, issue, merge-request, and software-extension paths. |
| Foundation context | Quantum ESPRESSO Foundation's official About page | Supports the Foundation's stated roles and its representative-member listing. |
| Baroni context | Current SISSA profile, public SISSA CV, and Foundation About page | Supports current SISSA affiliation plus historical project initiator/founding-director and representative-member context, not current Quantum ESPRESSO operational roles. |
| Marzari context | Foundation About page plus existing reviewed PI record | Supports the ecosystem's representative-member connection without duplicating or modifying Marzari's independently owned facts. |

## Relationship review

| Check | Result |
| --- | --- |
| Ecosystem software inclusion | `ECO-QUANTUM-ESPRESSO → includes → SW-QUANTUM-ESPRESSO` is supported by the official project and its central source repository. |
| Foundation connection | `ECO-QUANTUM-ESPRESSO → connects → ORG-QUANTUM-ESPRESSO-FOUNDATION` records the Foundation's stated project roles, not a complete legal or financial graph. |
| PI connections | The two ecosystem-to-PI edges are limited to Foundation representative membership; Baroni's separate historical initiator/founding-director evidence is noted without creating a current `develops` edge. |
| Direct affiliation path | `PI-STEFANO-BARONI → affiliated_with → UNIVERSITY-SISSA → located_in → COUNTRY-IT` uses current SISSA profile and institutional location evidence. |
| No duplicated ownership | Software facts remain in the software record, Foundation facts in the organization record, and person-specific evidence in each PI record. |

## Deliberate non-claims

1. The public repository, community pages, issues, merge requests, developer
   manual, and mailing lists do not identify every maintainer, reviewer,
   contributor, employer, host, funder, or partner.
2. The Foundation's objectives do not establish a current legal location,
   board, membership, sponsorship, funding, or operational authority beyond
   what its public page states.
3. Baroni's historical project-initiator and founding-director context does
   not establish current coding, maintenance, governance, supervision,
   mentoring, or availability beyond the separately documented SISSA
   affiliation.
4. The slice makes no claim about performance, admissions, openings, language,
   funding, rank, or applicant fit.

## Verification record

The slice is accepted only when the canonical validator, deterministic view
and recommendation drift checks, and repository regression suite pass after
regeneration. It introduces no architecture, schema, generator, or scoring
change.
