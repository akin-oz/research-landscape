# NoMaD Laboratory project vertical slice review

**Review date:** 2026-07-12

**Scope:** the reviewed Max Planck Society / NoMaD Laboratory / NOMAD project
cohort in [the vertical-slice document](../docs/nomad-laboratory-project-vertical-slice.md).

**Outcome:** this second Quality Gate 2 slice adds two canonical entities and
four evidence-bearing relationships. It introduces a completed Project record,
the organization-level coordinator, and historical project-to-software and
project-to-area connections without converting historical work into current
maintainer or governance claims.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Project identity, dates, and coordinator | European Commission CORDIS project record | Supports completed NoMaD grant 676580, 2015-11-01 through 2018-10-31 dates, and Max-Planck-Gesellschaft coordination. |
| Project research and tooling scope | CORDIS project record | Supports computational-materials-science data infrastructure and project-developed NOMAD tools. |
| Historical NOMAD relation | NOMAD CoE history | Supports the 2015–2018 NOMAD Laboratory CoE substantially extending NOMAD. |
| Organization identity and Germany endpoint | Max Planck Society organization page and CORDIS | Supports MPG as an independent research organization and its bounded German project context. |

All `SRC-*` values are record-local citations resolved in their subject
record's Evidence table. Report-scoped `S61` through `S63` remain source-
register keys and are not used as canonical citation identifiers.

## Relationship review

| Check | Result |
| --- | --- |
| Project host endpoint | `PROJ-NOMAD-LABORATORY-COE.host_organization_id` resolves to reviewed `ORG-MPG`. |
| Coordinator assertion | The project records `involves → ORG-MPG` with `coordinator` role and CORDIS evidence. |
| Software assertion | The project records a dated, historical `develops → SW-NOMAD` assertion supported by CORDIS and the NOMAD CoE history. |
| Area assertion | The project records `works_on → AREA-COMPUTATIONAL-MATERIALS-SCIENCE` with CORDIS evidence. |
| Location assertion | `ORG-MPG` records a bounded `located_in → COUNTRY-DE` relationship using the project-coordinator evidence. |
| One-way storage | No inverse project, software, area, or country assertion is added to target records. |

## Deliberate non-claims

1. The 2015–2018 project relation does not establish current NOMAD maintenance,
   governance, funding, services, or Max Planck Society ownership of every
   NOMAD component.
2. CORDIS lists a coordinated project, not an exhaustive canonical graph of
   every partner, person, work package, publication, or output; those records
   are not created here.
3. The historical project is not treated as evidence of an ongoing relationship
   with the current FAIRmat ecosystem or current NOMAD CoE.
4. No current opening, funding availability, supervision, mentoring,
   admissions, language, ranking, or applicant-fit claim is made.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this
cohort was added. It checked schema shape and date formats, unique IDs,
relationship target/type compatibility (including `involves`), record-local
source resolution, direct-host target type, matching `belongs_to` assertions,
exact-one host cardinality, changed-document local links, whitespace, and the
ADR 0006 University/Organization positive and negative branch cases. No
persistent validator, migration utility, generated view, or architecture
change is introduced before Quality Gate 6.
