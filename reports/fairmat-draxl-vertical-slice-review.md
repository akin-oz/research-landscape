# FAIRmat–Draxl vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed Claudia Draxl / SOLgroup / FAIRmat cohort in
[the vertical-slice document](../docs/fairmat-draxl-vertical-slice.md).

**Outcome:** the slice adds six canonical entities and eight evidence-bearing
relationships. It exercises the accepted University-host branch of ADR 0006,
models NOMAD as distinct software and FAIRmat as a connected infrastructure
ecosystem, and preserves multi-institutional ownership and governance limits.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Draxl’s current University affiliation and group role | Humboldt-Universität zu Berlin profile and SOLgroup page | Supports current professorship, SOLgroup leadership, direct University host, and computational-materials scope. |
| FAIRmat spokesperson role | FAIRmat team page | Supports a current ecosystem-to-PI spokesperson relationship, not a personal ownership claim. |
| FAIRmat and NOMAD distinction | FAIRmat overview and organizational story | Supports FAIRmat as a federated infrastructure that develops NOMAD Laboratory infrastructure, distinct from the software artifact. |
| NOMAD software identity | Public NOMAD repository and official documentation | Supports software purpose, public repository, Apache-2.0 license, API, and documentation. |
| German geographic endpoint | Humboldt University contact material and ISO 3166 `DE` reference | Supports University location normalization and country code. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S35` and `S43`–`S47` remain
source-register keys and are not used as canonical citation identifiers.

## ADR 0006 host review

| Check | Result |
| --- | --- |
| Direct-host cardinality | `RG-SOLGROUP` has `institution_id: UNIVERSITY-HU-BERLIN` and no `organization_id`. |
| Host type | `UNIVERSITY-HU-BERLIN` resolves to one reviewed v2 `university` record. |
| Evidence-bearing relationship | SOLgroup records `belongs_to → UNIVERSITY-HU-BERLIN` using its public group-page evidence. |
| No duplicate Organization | No generic Organization duplicate is created for Humboldt-Universität zu Berlin. |

## Deliberate non-claims

1. FAIRmat's connection to NOMAD does not establish exclusive hosting,
   development, governance, funding, or ownership by FAIRmat or Draxl.
2. The SOLgroup mention of NOMAD and FAIRmat does not establish group-wide
   maintenance or technical stewardship of the software.
3. FAIR-DI, NOMAD CoE, NOMAD HUB, infrastructure providers, and consortium
   participants remain out of scope until each identity and relation is
   separately reviewed.
4. No current opening, supervision, mentoring, admissions, funding, language,
   ranking, or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this
cohort was added. It checked schema shape and date formats, unique IDs,
relationship target/type compatibility, record-local source resolution,
direct-host target type, matching `belongs_to` assertions, exact-one host
cardinality, changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. No generic
validator, automation, migration, or architecture change is introduced in
this Quality Gate 1 slice.
