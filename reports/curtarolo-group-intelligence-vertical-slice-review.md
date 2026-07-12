# Curtarolo Group intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG4 enrichment of the existing Curtarolo Group, Stefano
Curtarolo, Duke University, AFLOW framework/ecosystem, and
computational-materials cohort described in [the vertical-slice
document](../docs/curtarolo-group-intelligence-vertical-slice.md).

**Outcome:** this third Quality Gate 4 slice adds no new entity or relationship
because the group, PI, direct host, research area, AFLOW framework, and AFLOW
ecosystem are already canonical. It improves evidence quality and
discoverability with three new first-party group sources for named research
programs, public software/learning surfaces, publication pattern, visible role
categories, and selected public alumni examples.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Research programs and methods | Curtarolo Group research page | Supports named materials programs and DFT, thermodynamics, ML, structural-analysis, disorder-modelling, and high-throughput context. |
| AFLOW and public software surface | Curtarolo Group home and AFLOW pages | Supports group-level AFLOW development, public source/binary/web/API/workshop surfaces, and open-source statement. |
| People roles and alumni | Curtarolo Group people page | Supports displayed research-professor, postdoctoral, graduate, visiting-graduate, adjunct, scientific-editor, and selected alumni information. |
| Publication and seminar surface | Curtarolo Group publications and home pages | Supports a chronological dated publication page and public virtual-seminar context. |
| Funding, collaboration, and mentorship limits | All reviewed group sources | Does not establish a group funding ledger, partner inventory, industry-collaboration graph, or mentoring-process evidence. |

All `SRC-*` values are record-local citations resolved in the Curtarolo Group
record’s Evidence table. Report-scoped `S119` through `S121` remain
source-register keys and are not used as canonical citation identifiers.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group evidence remains in `RG-CURTAROLO-GROUP`; no duplicate lab profile, people registry, publication database, or alumni entities are created. |
| Direct-host rule | Existing `institution_id: UNIVERSITY-DUKE` and matching `belongs_to` assertion remain unchanged and valid. |
| AFLOW boundary | Group-level development and public open-source surface do not establish individual maintenance, exclusive ownership, governance, or every member’s software role. |
| People boundary | The displayed people page is treated as a public role surface, not a complete roster, headcount, employment record, or bulk-entity source. |
| Mentorship and opportunity boundary | Seminars, schools, courses, and workshop materials are not generalized into mentoring quality, admissions, hiring, or supervision-capacity claims. |
| Career-outcome boundary | Selected alumni roles are examples of publicly stated outcomes, not a rate, causal claim, or guarantee. |

## Deliberate non-claims

1. The visual presence of funder logos does not establish a group grant, award,
   funding-program relationship, award amount, or current funding status.
2. Public AFLOW source, binaries, APIs, and workshops do not establish a
   complete programming stack, release practice, code-review process,
   maintainer roster, or service-level commitment.
3. Adjunct affiliations and a visiting-graduate entry do not establish an
   international or industry collaboration network.
4. Publications, seminars, workshops, and selected alumni examples do not
   establish group productivity, mentorship quality, placement success,
   applicant fit, or current opportunities.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation is required after this
group enrichment. It must check schema shape and date formats, unique IDs,
relationship target/type compatibility, record-local source resolution,
direct-host target type, matching `belongs_to` assertions, exact-one host
cardinality, changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. No persistent
validator, migration utility, generated view, or architecture change is
introduced before Quality Gate 6.
