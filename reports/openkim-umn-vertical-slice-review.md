# OpenKIM–University of Minnesota vertical slice review

**Review date:** 2026-07-13

**Scope:** a bounded canonicalization of KIM API, the OpenKIM ecosystem, Ellad
Tadmor's direct University of Minnesota affiliation, and a historical
founding-director connection.

**Outcome:** the slice adds four canonical entities and six evidence-bearing
relationships. It distinguishes the KIM API software artifact from the broader
OpenKIM ecosystem and preserves the difference between current affiliation and
historical project leadership.

## Evidence coverage

| Claim family | Primary evidence | Review result |
| --- | --- | --- |
| KIM API purpose and implementation | Public `openkim/kim-api` repository | Supports the atomistic/interatomic-model interface role, LGPL-2.1-or-later distribution, public contribution surfaces, and C++ implementation metadata. |
| Ecosystem and contribution context | KIM API repository and OpenKIM quarterly update | Supports a distinct ecosystem with public developer, model, and test surfaces, not a complete community or governance graph. |
| Tadmor and UMN context | UMN profile | Supports current professor affiliation and a bounded atomic-scale materials-modelling relation. |
| Founding-director context | Tadmor public CV | Supports a historical OpenKIM Founding Director role. It does not support a present `develops` or `maintains` relation. |

## Relationship review

| Check | Result |
| --- | --- |
| Ecosystem software inclusion | `ECO-OPENKIM → includes → SW-KIM-API` is backed by the public KIM API project source. |
| Historical person context | `ECO-OPENKIM → connects → PI-ELLAD-TADMOR` has role `founding-director` and an explicitly historical evidence window. |
| Affiliation path | `PI-ELLAD-TADMOR → affiliated_with → UNIVERSITY-UMN → located_in → COUNTRY-US` is limited to the published UMN affiliation and location context. |
| Direct metadata paths | KIM API carries sourced Computational Materials Science, C++, LGPL-2.1-or-later, and open-source metadata; these do not generalize to all OpenKIM components. |
| No duplicated ownership | Software, ecosystem, PI, and University evidence remain in their respective canonical records. |

## Deliberate non-claims

1. The reviewed sources do not establish a complete OpenKIM contributor,
   maintainer, governance, funder, partner, model, test, client-code, or
   institutional-host roster.
2. Historical founding-director context does not establish current coding,
   maintenance, review, governance, support, employment, supervision, or
   availability.
3. The slice makes no statement about model accuracy, software performance,
   service availability, admissions, funding, mentoring, programme fit, or
   applicant outcomes.

## Verification record

Acceptance requires a clean canonical validation, deterministic view and
recommendation drift checks after regeneration, and the repository regression
suite. This slice introduces no schema, generator, or scoring-model change.
