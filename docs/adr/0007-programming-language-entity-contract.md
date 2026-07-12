# ADR 0007: Decide whether Programming Language becomes a v2 canonical entity

- **Status:** Proposed — awaiting explicit architecture approval
- **Date:** 2026-07-12

## Context

The public recommendation model deliberately leaves the “Python-heavy research
groups” query unavailable. Its stated prerequisite is a governed Programming
Language entity contract plus sourced software-to-language relations.

The current v2 metadata schema contains a forward-looking
`programming_language_ids` field, but `programming-language` is not an allowed
v2 `entity_type`, no `entities/programming-languages/` canonical namespace
exists, and the relationship vocabulary has no evidence-bearing
software-to-language predicate. The older `programming-language.schema.json`
does not resolve that v2 gap. Adding a directory, an ad hoc free-text value, or
an unsupported relationship would violate canonical ownership and the frozen
architecture.

## Decision requested

Approve or reject this minimal v2 extension:

1. Add `programming-language` to the v2 entity-type contract, with canonical
   records in `entities/programming-languages/`.
2. Add a controlled `Research Software --implemented_in--> Programming
   Language` relationship assertion. Each assertion retains its own source ID
   and confidence; generated views derive inverse displays instead of storing
   a second edge.
3. Treat `programming_language_ids` as an optional convenience facet only when
   it is consistent with evidence-bearing `implemented_in` assertions. It must
   not become an unsourced duplicate relation.
4. Enable a language-based discovery query only after at least two independent
   reviewed software-to-language vertical slices demonstrate the contract.

The extension is limited to publicly documented implementation languages. It
does not infer a group’s working language, required applicant skills, Python
proficiency, mentoring practice, hiring, or admissions outcome from a software
relationship.

## Alternatives considered

### Keep the query unavailable

This preserves current architecture and remains correct if maintaining
language-level evidence is not worth its ongoing review cost. It leaves an
important software-engineer discovery question unanswered.

### Use prose or repository-topic tags

Rejected. Prose cannot support deterministic filters; repository topics and
file extensions can be incomplete, generated, or misleading. They would also
produce no canonical language owner.

### Reuse the legacy language schema without a v2 contract

Rejected. It would create a parallel schema and migration path, contrary to
the entity-oriented v2 architecture.

### Use `programming_language_ids` without typed assertions

Rejected. A software-to-language claim is material relationship evidence and
needs its own source and confidence once v2 relationship assertions exist.

## Consequences if approved

- Contributors gain a single canonical owner for programming-language
  concepts and evidence-backed software implementation links.
- The validator, entity-authoring guide, relationship model, views, and
  recommendation model need a versioned, tested implementation.
- Existing records are not bulk-migrated. The first implementation must be a
  small evidence-bounded vertical slice, reviewed before any language-based
  recommendation is published.
- `python-heavy-research-groups` remains unavailable until the required
  evidence coverage exists; approval alone creates no recommendation.

## Approval record

No implementation may proceed from this ADR while its status is Proposed.
Approval must explicitly confirm the entity type, canonical namespace,
predicate, evidence rule, and vertical-slice threshold above.

## References

- [Architecture status](../ARCHITECTURE_STATUS.md)
- [Entity-oriented knowledge model](../architecture/entity-model.md)
- [Relationship model](../architecture/relationships.md)
- [Evidence recommendations](../../reports/generated/evidence-recommendations.md)
- [Entity v2 schema](../../schemas/entity-vnext.schema.json)
