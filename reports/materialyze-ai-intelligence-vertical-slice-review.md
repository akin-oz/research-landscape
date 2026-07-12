# Materialyze.AI intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the Quality Gate 4 enrichment of the existing Materialyze.AI Lab,
Shyue Ping Ong, National University of Singapore, Materials Informatics,
pymatgen, and Materials Project cohort described in [the vertical-slice
document](../docs/materialyze-ai-intelligence-vertical-slice.md).

**Outcome:** this eighth Quality Gate 4 slice adds no entity or relationship.
It improves the canonical group record's evidence, documentation, and
discoverability with first-party public information about research themes,
software/open-science context, role categories, and a dated applicant and
onboarding process. Existing PI-level software stewardship remains distinct
from group-wide claims.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Group identity and research scope | NUS faculty profile and Materialyze.AI home page | Supports the NUS-hosted materials-informatics group and stated theory/data/AI/translation pillars; not a complete project inventory. |
| Software and open-science context | Materialyze.AI home page and Join Us post | Supports public open data/API/software context and an advertised contribution surface; not exclusive maintenance, individual roles, licenses, or quality metrics. |
| People boundary | Materialyze.AI Team page | Supports visible research-fellow, postdoctoral, and graduate-student role categories, but mixes NUS/UCSD context and is not a normalized current NUS roster. |
| Application and mentorship boundary | Dated Materialyze.AI Join Us post | Supports a public stated application, onboarding, and mentorship process; not live capacity, an admission decision, funding, or outcome evidence. |
| Funding, collaborations, publications, and outcomes | Reviewed public surfaces | Do not yield a bounded group-level funding ledger, partner graph, publication register, or alumni-outcome evidence. |

All `SRC-*` values are record-local citations resolved in the Materialyze.AI
entity's Evidence table. Report-scoped `S135` through `S137` remain
source-register keys and are not used as canonical citation identifiers.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group facts remain in `RG-MATERIALYZE-AI`; no duplicate lab, roster, project catalog, software catalog, or opportunity feed is introduced. |
| Direct-host rule | Existing `institution_id: UNIVERSITY-NUS` and matching `belongs_to` assertion remain unchanged and valid. |
| Software boundary | Existing PI-level `develops → SW-PYMATGEN` remains the only stewardship relation. The group's public software portfolio is descriptive context, not a maintenance or ownership edge. |
| Cross-site boundary | The public Team page's UCSD references are not converted into a current NUS affiliation, collaboration, or person graph. |
| Opportunity boundary | The public Join Us post is date- and source-bounded; it is not treated as a live vacancy, admissions guarantee, funding promise, or supervision-capacity statement. |
| Missing-evidence boundary | Funding, complete roster, project, partner, publication, mentoring-outcome, and career gaps remain explicit rather than inferred. |

## Deliberate non-claims

1. A public software portfolio and contribution invitation do not establish a
   group-wide pymatgen/Materials Project maintenance, ownership, governance, or
   individual-contributor roster.
2. Public role categories and mixed NUS/UCSD biographies do not establish a
   current NUS headcount, employee status, individual responsibility, or career
   outcome.
3. A dated application process and stated mentorship do not establish a current
   vacancy, admission decision, funding, salary, eligibility, response time,
   supervision capacity, mentoring quality, or placement result.
4. Named research domains, methods, and applications do not establish a
   complete project, collaboration, industry, infrastructure, or publication
   graph.

## Verification record

On 2026-07-12, the complete-v2-corpus validation passed after this enrichment.
It checked schema shape and dates, unique IDs, relationship target/type
compatibility, record-local source resolution, direct-host target type and
matching `belongs_to` assertion, exact-one host cardinality, changed-document
local links, whitespace, and ADR 0006's University/Organization positive and
negative branch cases. The corpus contains 67 v2 entities and 116 relationship
assertions. No persistent validator, generated view, or architecture change is
introduced before Quality Gate 6.
