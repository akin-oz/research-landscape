# AFLOW ecosystem-intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG3 enrichment of the existing AFLOW, Curtarolo Group, Stefano
Curtarolo, Duke, and 2023 `aflow++` publication cohort described in [the
vertical-slice document](../docs/aflow-ecosystem-intelligence-vertical-slice.md).

**Outcome:** this fourth Quality Gate 3 slice adds one canonical publication and
three evidence-bearing relationships. It makes the AFLOW software ecosystem
more intelligible through source-backed contributor, installation,
documentation, and API-user context, while retaining the existing framework/
ecosystem distinction and strict funding and maintenance boundaries.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| AFLOW purpose and contributor context | AFLOW framework documentation | Supports high-throughput DFT/data-informatics purpose and a bounded Stefano Curtarolo contributor connection. |
| User journey and learning surfaces | AFLOW installation and AFLUX/REST documentation | Supports public source, installation, code documentation, property-based query, and data-download routes. |
| Group, institution, and role context | Existing Curtarolo Group and Duke evidence | Preserves independently reviewed group-level framework development and PI/group/University relationships. |
| Key technical reference | Duke Scholars `aflow++` record | Supports the 25 January 2023 date, DOI, Stefano Curtarolo authorship, and framework subject. |
| Funding boundary | Official technical/public sources reviewed for this slice | No current or historical programme identity plus direct AFLOW award evidence supports a typed funding relationship. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S89` through `S93` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Ecosystem contributor connection | `ECO-AFLOW` records `connects → PI-STEFANO-CURTAROLO` with role `contributor`, supported by the official framework documentation. |
| Publication authorship | `PUB-AFLOW-PLUS-PLUS-2023` records `authored_by → PI-STEFANO-CURTAROLO` using the publication author list. |
| Publication software description | `PUB-AFLOW-PLUS-PLUS-2023` records `describes → SW-AFLOW` using the article's stated technical subject. |
| Existing framework development | The existing Curtarolo Group → AFLOW `develops` edge remains group-level and does not become a duplicate PI maintenance assertion. |
| No unsupported funding edge | No funding relation is fabricated from publication acknowledgements, institutional association, or source availability. |

## Contract limitations surfaced, not changed

1. `programming_language_ids` cannot be populated until a canonical Programming
   Language entity type and namespace are approved.
2. The schema has no canonical Community, dependency, API endpoint, database,
   workflow, package, or contributor-role entity type, so these documented
   components are not converted into speculative graph nodes.
3. The documented `connects` predicate does not accept a Research Ecosystem
   target. Related ecosystems therefore remain cross-reference candidates rather
   than unsupported typed relations.
4. A contributor list is not a maintainer, governance, or current funding
   contract, so it is modeled only as a bounded ecosystem connection.

## Deliberate non-claims

1. Public source, installation, API, and documentation paths do not establish
   individual review, acceptance, mentorship, employment, governance, result
   quality, or support commitments.
2. The 2023 publication does not establish current versions, capabilities,
   affiliations, maintainer roles, or a complete author graph.
3. No AFLOW consortium membership, funding, or ownership inference is made from
   the existing group or PI context.
4. No career placement, opening, supervision, admissions, language, ranking,
   or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this cohort
was added. It checked schema shape and date formats, unique IDs, relationship
target/type compatibility (including `authored_by` and `describes`), record-
local source resolution, direct-host target type, matching `belongs_to`
assertions, exact-one host cardinality, changed-document local links,
whitespace, and the ADR 0006 University/Organization positive and negative
branch cases. No persistent validator, migration utility, generated view, or
architecture change is introduced before Quality Gate 6.
