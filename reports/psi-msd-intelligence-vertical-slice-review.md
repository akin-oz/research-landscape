# PSI Materials Software and Data intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the Quality Gate 4 enrichment of the existing Materials Software and
Data Group, Giovanni Pizzi, PSI, aiida-core, AiiDA ecosystem, and Computational
Materials Science cohort described in [the vertical-slice
document](../docs/psi-msd-intelligence-vertical-slice.md).

**Outcome:** this eleventh Quality Gate 4 slice adds no entity or relationship.
It improves discoverability of first-party PSI evidence about software/data
research, open-science platforms, role categories, publications, and project/
opportunity navigation while keeping those public displays from becoming a
second graph or a set of inferred opportunities.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Research and open-science context | PSI MSD group page | Supports simulation/spectroscopy algorithms, AiiDA, AiiDAlab, Materials Cloud, high-throughput workflows, interfaces, data, and autonomous-lab aspirations; not a complete program inventory. |
| Software boundary | PSI MSD page and existing AiiDA relation | Supports existing shared aiida-core development plus broad open-source context; not every code's identity, ownership, license, governance, or maintainer roster. |
| People and publication boundary | PSI MSD page | Supports visible role categories and a publication list; not a complete workforce, attribution, productivity, quality, or career-outcome record. |
| Project, funding, infrastructure, and opportunity boundary | PSI MSD page | Supports navigation to PSI project/software/opening surfaces; not stable project/funder identities, capacity, service access, or live opportunities. |
| Mentorship and outcomes | Reviewed PSI surfaces | Do not establish supervision practice, mentoring quality, or alumni outcome evidence. |

All `SRC-*` values are record-local citations resolved in the MSD entity's
Evidence table. Existing PSI/AiiDA sources are reused rather than duplicated.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group facts remain in `RG-PSI-MSD`; no duplicate AiiDA, Materials Cloud, roster, code catalog, project, funding, or opportunity store is introduced. |
| Direct-host rule | Existing `organization_id: ORG-PSI` and matching `belongs_to` assertion remain unchanged and valid. |
| Software boundary | Existing shared `develops → SW-AIIDA-CORE` remains the precise evidence-bearing edge. Other public software statements remain context until separately reviewed. |
| Scope boundary | PSI links and displays are not converted into claims about team membership, current projects, funding, availability, access, or outcomes. |
| Missing-evidence boundary | Programming stack, complete roster, project/funding, partner, mentoring, and career gaps remain explicit rather than inferred. |

## Deliberate non-claims

1. A current group display does not establish a complete workforce, role history,
   responsibility map, supervision structure, or career path.
2. A publication list does not establish a complete bibliography, individual
   authorship, research quality, productivity, or impact measure.
3. Mentions of projects, platforms, simulation services, and autonomous labs do
   not establish a stable project/funder graph, infrastructure deployment,
   allocation, availability, user access, or acceptance promise.
4. AiiDA/AiiDAlab/Materials Cloud references do not establish group-wide or
   exclusive ownership, governance, licensing, or every contributor's role.

## Verification record

On 2026-07-12, the complete-v2-corpus validation passed after this enrichment.
It checked schema shape and dates, unique IDs, relationship target/type
compatibility, record-local source resolution, direct-host target type and
matching `belongs_to` assertion, exact-one host cardinality, changed-document
local links, whitespace, and ADR 0006's University/Organization positive and
negative branch cases. The corpus contains 67 v2 entities and 116 relationship
assertions. No persistent validator, generated view, or architecture change is
introduced before Quality Gate 6.
