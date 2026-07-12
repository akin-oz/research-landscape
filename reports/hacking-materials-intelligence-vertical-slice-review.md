# Hacking Materials intelligence vertical slice review

**Review date:** 2026-07-12

**Scope:** the QG4 enrichment of existing Hacking Materials, Anubhav Jain,
Berkeley Lab, Materials Project, and computational-materials cohort described
in [the vertical-slice document](../docs/hacking-materials-intelligence-vertical-slice.md).

**Outcome:** this fourth Quality Gate 4 slice adds no new entity or relationship
because the group, PI, direct host, research area, and PI-level Materials
Project connection are already canonical. It improves evidence quality and
discoverability with first-party group, handbook, and software-documentation
sources for stated research scope, community software work, collaboration
modality, role categories, process, compute context, and bounded funding
evidence.

## Evidence coverage

| Claim family | Primary evidence used | Review result |
| --- | --- | --- |
| Research, software, and collaboration modality | Hacking Materials group page | Supports stated theory/HPC/AI/data-software scope, named research areas, and collaboration with experimental/autonomous labs. |
| People, alumni, and participation boundary | Hacking Materials group page | Supports displayed role categories, alumni section, and official live-page participation routes—not a current opening or eligibility decision. |
| Process, mentorship, and computing context | Hacking Materials Handbook | Supports separately displayed onboarding/training and professional-development observations for documented communication, graduate-study/writing/presentation guidance, plus compute-resource context; handbook age bounds these claims. |
| Software-specific funding context | AMSET contributors documentation | Supports group-led AMSET development and the stated DOE Early Career context for that software, not a group funding ledger. |
| Publication and career limits | Group page and handbook | Does not establish an internal publication inventory, mentoring outcome, placement rate, or career guarantee. |

All `SRC-*` values are record-local citations resolved in the Hacking Materials
record’s Evidence table. Report-scoped `S122` and `S123` remain source-register
keys and are not used as canonical citation identifiers.

## Integrity review

| Check | Result |
| --- | --- |
| Canonical ownership | Group evidence remains in `RG-HACKING-MATERIALS`; no duplicate lab profile, people registry, project catalog, software catalog, or alumni entities are created. |
| Direct-host rule | Existing `organization_id: ORG-LBNL` and matching `belongs_to` assertion remain unchanged and valid. |
| Materials Project boundary | The existing PI-level associate-director relation remains PI-scoped; group participation in a named research area does not create group-wide ecosystem governance. |
| Software boundary | Group-led AMSET documentation and open-source research-area statements do not establish records or roles for every named tool, package, or contributor. |
| Time boundary | The handbook self-identifies as last updated two years ago; it is retained as dated process evidence, while current opportunities must be rechecked on the live group page. |
| Mentorship and career boundary | Documented process and public alumni content are not generalized into mentoring quality, supervision capacity, placement success, applicant fit, or a current opening. |

## Deliberate non-claims

1. Live participation language is not converted into a claim that a position is
   open, that an applicant is eligible, or that the group can supervise a
   particular person.
2. AMSET’s documentation does not establish a current or group-wide DOE award,
   funding amount, full contributor roster, or every individual’s role.
3. Named research areas and links do not establish project, software,
   collaborator, industry-partner, facility, or funding-programme entities.
4. Handbook guidance, compute-resource discussion, alumni presence, and
   news/achievement updates do not establish mentorship quality, allocation,
   publication quality, placement success, or career outcomes.

## Verification record

On 2026-07-12, a one-off complete-v2-corpus validation is required after this
group enrichment. It must check schema shape and date formats, unique IDs,
relationship target/type compatibility, record-local source resolution,
direct-host target type, matching `belongs_to` assertions, exact-one host
cardinality, changed-document local links, whitespace, and the ADR 0006
University/Organization positive and negative branch cases. No persistent
validator, migration utility, generated view, or architecture change is
introduced before Quality Gate 6.
