# Persson Group intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG4 enrichment of the existing Persson Group, Kristin Persson,
LBNL, Materials Project, and pymatgen canonical cohort described in [the
vertical-slice document](../docs/persson-group-intelligence-vertical-slice.md).

**Outcome:** this first Quality Gate 4 slice adds no new entity or relationship
because the needed group/PI/host/ecosystem records already exist. It instead
raises the group record’s evidence quality and discoverability with four new
first-party evidence sources, alongside the existing research and software
sources, covering people categories, publication surface, role-specific
guidance, awards, and selected public alumni outcomes.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Research and infrastructure | Persson Group research page | Supports DFT/MD/HPC/ML/NLP themes, Materials Project expansion, battery/synthesis/symmetry work, and experimental-collaboration statement. |
| Software maturity and open source | Persson Group software page | Supports prompt code-publication intent and Materials Project GitHub project context without assigning unverified individual/group maintenance. |
| People roles and alumni | Persson Group people page | Supports public PI, postdoctoral, graduate, staff, undergraduate, visitor, and alumni categories and selected stated alumni destinations. |
| Publication and award surface | Group publications and news pages | Supports chronological continuing publications and bounded dated awards/recognition. |
| Mentorship and opportunity boundary | Group open-positions page | Supports one specific 2024 intern role’s weekly and one-to-one guidance; page displays no postdoctoral/staff openings and is not used as a current-availability claim. |
| Funding and collaboration limits | All reviewed group pages | No reliable group-level funding ledger, industry collaboration roster, or comprehensive partner roster is established. |

All `SRC-*` values are record-local citations resolved in the Persson Group
record’s Evidence table. Report-scoped `S112` through `S115` remain source-
register keys and are not used as canonical citation identifiers.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group-level evidence remains in `RG-PERSSON-GROUP`; no duplicate lab profile or person roster is created. |
| Direct-host rule | Existing `organization_id: ORG-LBNL` and matching `belongs_to` assertion remain unchanged and valid. |
| Software-role boundary | The group’s Materials Project and open-source practice does not establish a group-level pymatgen development/maintenance/usage relation; no such edge is added. |
| Mentorship boundary | Weekly updates and one-to-one guidance are limited to a dated undergraduate intern role, not generalized to all members or applicants. |
| Career-outcome boundary | Individual alumni biographies are examples of public outcomes, not a placement rate or causal claim. |
| Opportunity boundary | A dated 2024 listing and current page headings are not presented as a live opening, admission route, or hiring promise. |

## Deliberate non-claims

1. The group’s public people page is not treated as a complete current roster,
   employment record, or a basis for bulk person-entity creation.
2. Open-source project listings do not establish ownership, code review,
   maintenance, contributor rights, or licensing for every project or person.
3. Research themes and experimental collaboration do not establish a complete
   collaboration/industry network, funding source, facility allocation, or
   project portfolio.
4. Awards, alumni destinations, and a role-specific guidance statement do not
   establish mentorship quality, career outcomes, applicant fit, or guaranteed
   access to opportunities.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation passed after this group
enrichment. It checked schema shape and date formats, unique IDs, relationship
target/type compatibility, record-local source resolution, direct-host target
type, matching `belongs_to` assertions, exact-one host cardinality,
changed-document local links, whitespace, and the ADR 0006 University/
Organization positive and negative branch cases. No persistent validator,
migration utility, generated view, or architecture change is introduced before
Quality Gate 6.
