# RIKEN Polymeromics intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the Quality Gate 4 enrichment of the existing Polymeromics Team,
Ryo Yoshida, RIKEN TRIP, Materials Informatics, and RadonPy cohort described in
[the vertical-slice document](../docs/riken-polymeromics-intelligence-vertical-slice.md).

**Outcome:** this ninth Quality Gate 4 slice adds no entity or relationship. It
makes existing first-party group evidence easier to discover and review:
automation-centered polymer research, a bounded public people surface, selected
publications, and the existing shared RadonPy connection. It does not convert
web-page lists into canonical people, publications, projects, or funding.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Research and methods | RIKEN Polymeromics Team page | Supports polymer database, foundation-model, automated MD/first-principles, Sim2Real, and autonomous-discovery scope; not a complete project inventory. |
| Software and open-source boundary | RIKEN Team page plus existing RadonPy record | Supports the existing bounded group-to-RadonPy relation and public code link; not individual or exclusive maintenance/governance. |
| People boundary | RIKEN Team page | Supports a named Team Director and displayed research-/visiting-scientist role categories; not an exhaustive employment or student/postdoc record. |
| Publication boundary | RIKEN Team page | Supports a selected publication surface, explicitly including work marked as outside RIKEN; not a complete group bibliography or metric. |
| Funding, collaborations, mentoring, and outcomes | Reviewed RIKEN surfaces | Do not establish a funding ledger, partner graph, supervision practice, opportunity, or alumni-outcome record. |

All `SRC-*` values are record-local citations resolved in the Polymeromics Team
entity's Evidence table. The slice uses existing source-register entries rather
than duplicating a new source catalogue.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group evidence remains in `RG-RIKEN-POLYMEROMICS`; no duplicate team, roster, publication database, project catalog, or funding store is introduced. |
| Direct-host rule | Existing `organization_id: ORG-RIKEN-TRIP` and matching `belongs_to` assertion remain unchanged and valid. |
| Software boundary | Existing shared `develops → SW-RADONPY` remains the sole team software edge. Public links and research themes are not expanded into individual roles or an ecosystem claim. |
| Personnel/publication boundary | Public display names and selected citations are not converted into people or publication records, attribution claims, or quantitative signals. |
| Missing-evidence boundary | Funding, partner, project, opportunity, mentorship, and career gaps remain explicit rather than inferred. |

## Deliberate non-claims

1. The current people display does not establish a complete current workforce,
   headcount, employment status, responsibility map, or student/postdoc route.
2. A selected-publication page does not establish a complete bibliography,
   individual contribution, publication quality, group productivity, or current
   RIKEN affiliation for entries explicitly marked as external work.
3. Automation, data, AI, and robotics descriptions do not establish a deployed
   facility, hardware/robot access, project membership, funding, or operational
   capacity.
4. The existing RadonPy relation does not establish exclusive ownership,
   governance, license responsibility, a maintainer roster, or every member's
   software role.

## Verification record

On 2026-07-12, the complete-v2-corpus validation passed after this enrichment.
It checked schema shape and dates, unique IDs, relationship target/type
compatibility, record-local source resolution, direct-host target type and
matching `belongs_to` assertion, exact-one host cardinality, changed-document
local links, whitespace, and ADR 0006's University/Organization positive and
negative branch cases. The corpus contains 67 v2 entities and 116 relationship
assertions. No persistent validator, generated view, or architecture change is
introduced before Quality Gate 6.
