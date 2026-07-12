# ADR 0008: Decide whether to model public mentorship-process evidence in v2

- **Status:** Accepted — 2026-07-12
- **Date:** 2026-07-12

## Context

Research Landscape correctly refuses to rank “high-mentorship environments.”
Some current group records contain narrowly scoped public process material—for
example, a handbook, onboarding description, or training route—but the v2
graph has no controlled, evidence-bearing representation for it. Leaving this
material solely in prose preserves caution but prevents an applicant from
discovering documented process evidence systematically. Reusing affiliations,
software links, volatile assertions, or a free-text tag would misrepresent the
claim and duplicate unsupported meaning.

The methodology now defines the allowed public, aggregate evidence and its
privacy boundary in [Mentorship-process evidence](../../methodology/metrics/mentorship.md).
It does not authorize a score, a personality assessment, or a public claim
that one environment is better than another.

## Decision

The approved minimal v2 extension is:

1. Add an optional `mentorship_process_evidence` field for Research Group,
   Department, University, and Organization records. Each observation contains
   a controlled category, source IDs, a bounded scope, an evidence window or
   review date, confidence, and a required limitation.
2. Permit only these initial categories: `written-expectations`,
   `onboarding-training`, `supervision-process`, `professional-development`,
   and `aggregate-outcomes`.
3. Do not add a mentorship score, ordinal rating, personal-testimonial field,
   or a claim of supervision capacity. Any future public query is titled
   “entities with documented mentorship-process evidence,” displays the
   category and limitations, and remains a discovery result rather than a
   comparison.
4. Require two independently reviewed vertical slices with different evidence
   categories before enabling that query. A self-published group handbook is
   valid scoped process evidence, but it cannot alone establish effectiveness
   or comparative quality.

## Alternatives considered

### Keep the current query unavailable indefinitely

This is safe and remains the correct choice if an evidence contract cannot be
maintained. It leaves a core diligence question non-discoverable even where a
public, bounded process statement exists.

### Add a mentorship score or use testimonials

Rejected. Individual experiences are private, context-sensitive, and often
not comparable; a score would turn uneven evidence into a harmful ranking.

### Encode process evidence as an existing relationship or volatile assertion

Rejected. None of the current predicates describes a supervision process, and
volatile assertions model availability/activity states rather than evidence
observations. Reuse would make the graph semantically inaccurate.

### Store a free-text tag in a view or report

Rejected. It has no canonical owner, evidence contract, source-level review,
or deterministic query semantics.

## Consequences if approved

- Maintainers can record bounded public process evidence once, at the entity
  that owns its scope, with explicit source and limitation metadata.
- The schema, validator, entity-authoring guide, privacy guidance, and
  recommendation renderer require a versioned, tested implementation.
- Existing prose is not bulk-migrated. Initial vertical slices must preserve
  their original time/scope limitations and demonstrate that no personal or
  sensitive data is introduced.
- “High mentorship environments” remains unavailable; approval enables only a
  future evidence-discovery path after the coverage gate is met.

## Approval record

The user approved this ADR on 2026-07-12, confirming the allowed entity
scopes, categories, source/limitation requirements, prohibition on scoring,
and vertical-slice threshold.

## References

- [Mentorship-process evidence](../../methodology/metrics/mentorship.md)
- [Ethics policy](../ethics.md)
- [Entity authoring guide](../entity-authoring.md)
- [Evidence recommendations](../../reports/generated/evidence-recommendations.md)
- [Architecture status](../ARCHITECTURE_STATUS.md)
