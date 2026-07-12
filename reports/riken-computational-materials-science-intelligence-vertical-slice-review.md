# RIKEN Computational Materials Science intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the Quality Gate 4 enrichment of the existing Computational Materials
Science Research Team, Seiji Yunoki, RIKEN Center for Computational Science,
and Computational Materials Science cohort described in [the vertical-slice
document](../docs/riken-computational-materials-science-intelligence-vertical-slice.md).

**Outcome:** this tenth Quality Gate 4 slice adds no entity or relationship. It
makes first-party group evidence more discoverable: numerical-method research,
quantum/HPC context, public people roles, representative papers, annual reports,
and job-navigation context. It keeps generic and incomplete page material from
becoming a people roster, software registry, project catalog, funding record,
or opportunity feed.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Research and methods | RIKEN Computational Materials Science Research Team page | Supports QMC/tensor-network/quantum-algorithm and classical-supercomputer scope; not a complete research or project inventory. |
| Software boundary | Same RIKEN page | Supports technical software-application context only; it does not supply a stable code identity, repository, license, or maintainer evidence. |
| People and publication boundary | Same RIKEN page | Supports displayed role categories, representative papers, and report links; not a complete personnel, bibliography, attribution, or metric record. |
| Infrastructure and opportunity boundary | Same RIKEN page | Supports historical large simulation and generic job navigation; not current access, allocation, vacancy, degree, or team-specific opportunity evidence. |
| Funding, collaboration, mentorship, and outcomes | Reviewed RIKEN surfaces | Do not establish a group-level funder/partner graph, mentoring practice, or career-outcome record. |

All `SRC-*` values are record-local citations resolved in the Computational
Materials Science Research Team entity's Evidence table. The slice reuses
existing source-register entries rather than creating a second source catalogue.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group evidence remains in `RG-RIKEN-COMPUTATIONAL-MATERIALS-SCIENCE`; no duplicate team, people, code, paper, project, funding, or opportunity record is introduced. |
| Direct-host rule | Existing `organization_id: ORG-RIKEN-CCS` and matching `belongs_to` assertion remain unchanged and valid. |
| Software boundary | A described QMC application is not turned into a Research Software entity or an individual/group maintainer relationship without identity and provenance evidence. |
| Scale boundary | Historical K-computer results do not establish current Fugaku allocation, access, infrastructure capacity, or a user-service promise. |
| Opportunity boundary | Generic RIKEN/R-CCS job and education navigation is not represented as a team vacancy, internship, degree route, eligibility, or admission path. |
| Missing-evidence boundary | Funding, partners, complete personnel, project, software, mentoring, and career gaps remain explicit rather than inferred. |

## Deliberate non-claims

1. A team-page people list does not establish a complete current workforce,
   headcount, employment status, individual contribution, or supervision map.
2. A representative-paper list and annual reports do not establish a complete
   bibliography, publication quality, productivity, or individual attribution.
3. A software-application and historical simulation description do not identify
   an open-source code, repository, license, maintenance role, ecosystem, or
   current infrastructure access.
4. Generic RIKEN career and education links do not establish live openings,
   funding, admissions, language, supervision, mentoring, or career outcomes.

## Verification record

On 2026-07-12, the complete-v2-corpus validation passed after this enrichment.
It checked schema shape and dates, unique IDs, relationship target/type
compatibility, record-local source resolution, direct-host target type and
matching `belongs_to` assertion, exact-one host cardinality, changed-document
local links, whitespace, and ADR 0006's University/Organization positive and
negative branch cases. The corpus contains 67 v2 entities and 116 relationship
assertions. No persistent validator, generated view, or architecture change is
introduced before Quality Gate 6.
