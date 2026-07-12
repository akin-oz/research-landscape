# Horizon 2020–NoMaD funding vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed European Commission / Horizon 2020 Research
Infrastructures / NoMaD Laboratory funding cohort in
[the vertical-slice document](../docs/horizon-2020-nomad-funding-vertical-slice.md).

**Outcome:** this fourth Quality Gate 2 slice adds two canonical entities and
two evidence-bearing relationships. It completes a dated funding path to the
existing completed project while maintaining the distinction between a funder,
programme, project, coordinator, and software artifact.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| European Commission identity and role | European Commission About page | Supports the Commission as the EU executive body and its funding-programme management role. |
| Horizon 2020 identity and period | European Commission Horizon 2020 page | Supports Horizon 2020 as the 2014–2020 EU research and innovation funding programme, now ended. |
| Project-specific funding relation | European Commission CORDIS NoMaD project record | Supports NoMaD grant 676580 as funded under Horizon 2020 Excellent Science — Research Infrastructures with 2015–2018 dates. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S61`, `S67`, and `S68` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Funder endpoint | `FUND-H2020-RESEARCH-INFRASTRUCTURES.funder_organization_id` resolves to reviewed `ORG-EUROPEAN-COMMISSION`. |
| Administration assertion | `ORG-EUROPEAN-COMMISSION` records `administers → FUND-H2020-RESEARCH-INFRASTRUCTURES` with official Commission evidence. |
| Funding assertion | The programme records `funds → PROJ-NOMAD-LABORATORY-COE` with CORDIS evidence and the project’s 2015–2018 dates. |
| Project index | The existing project records `funding_program_ids: [FUND-H2020-RESEARCH-INFRASTRUCTURES]` without duplicating the canonical `funds` assertion. |
| One-way storage | No inverse `administers` or `funds` assertion is added to the target record. |

## Deliberate non-claims

1. The completed Horizon 2020 programme and completed NoMaD grant do not
   establish a present funding call, current eligibility, or current NOMAD
   financial support.
2. The Commission record is not an exhaustive graph of EU agencies,
   institutions, countries, funding programmes, or direct grant managers.
3. No programme-wide portfolio, budget, beneficiary, call, co-funder, or award
   record is created from the project fact sheet.
4. No current opening, supervision, mentoring, admissions, language, ranking,
   or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this
cohort was added. It checked schema shape and date formats, unique IDs,
relationship target/type compatibility (including `funds`), record-local source
resolution, direct-host target type, matching `belongs_to` assertions,
exact-one host cardinality, changed-document local links, whitespace, and the
ADR 0006 University/Organization positive and negative branch cases. No
persistent validator, migration utility, generated view, or architecture
change is introduced before Quality Gate 6.
