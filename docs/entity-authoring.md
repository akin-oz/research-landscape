# Entity authoring guide

Canonical entities own reusable public facts exactly once. They live under
`entities/<entity-type>/`, use `schema_version: 2`, and are validated against
[`entity-vnext.schema.json`](../schemas/entity-vnext.schema.json). Reports,
views, recommendations, and legacy pages link to them rather than copying their
facts.

## Before you create an entity

1. Search `entities/` by stable ID, name, alias, website, and external ID.
2. Confirm the object is a first-class type supported by the entity model and
   schema. Do not invent a type to model a convenient detail.
3. Identify the one canonical owner and the smallest public source set needed
   to establish its identity.
4. Prefer a small vertical slice: only add related entities when a precise,
   evidence-backed relationship requires them.

## Required record shape

Use the applicable existing record as the template. A reviewed record needs at
least the common v2 fields, record-local sources, and type-specific required
fields:

```yaml
---
schema_version: 2
entity_type: research-group
id: RG-EXAMPLE
name: Example Research Group
status: reviewed
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
last_review: "YYYY-MM-DD"
confidence: high
source_ids: [SRC-EXAMPLE-HOME]
institution_id: UNIVERSITY-EXAMPLE
relationship_assertions:
  - predicate: belongs_to
    target_id: UNIVERSITY-EXAMPLE
    source_ids: [SRC-EXAMPLE-HOME]
    confidence: high
---
```

Every `SRC-*` value must resolve in a unique row of that record's `## Evidence`
table; a prose mention elsewhere in the file does not resolve it. It is a
record-local citation key, not a global source entity. Each row must include a
public URL and `Accessed YYYY-MM-DD`. Keep the source statement narrow: say
exactly what the page supports and what it does not establish.

## Relationships

Use only predicates in the [relationship model](architecture/relationships.md)
and the schema. An assertion needs a target stable ID, supporting source IDs,
and confidence. Store it once in the documented direction; generated views
derive inverse display links.

Reviewed or published Research Groups must satisfy ADR 0006: choose exactly one
direct host—`institution_id` for a University or `organization_id` for a
non-university Organization—and include exactly one matching `belongs_to`
assertion. A Department may be administrative context only; it is not a second
direct host.

## Evidence and unknowns

- Prefer current, primary institutional, project, repository, funder, or
  publisher records.
- Record access dates and scope in the Evidence table.
- Do not infer current roles, opportunities, funding, language, mentorship,
  contributor status, software quality, or career outcomes from nearby facts.
- Omit unsupported metadata. Unknown is not `no` and never a score of zero.
- Put a bounded interpretation in `reports/`, not in the canonical entity.

## Validation and handoff

Run the onboarding commands, inspect generated diffs, and link any affected
views or reports rather than editing their output. Explain deliberate omissions
in the entity's boundary section or a vertical-slice review. See the
[review process](review-process.md) for the pull-request checklist.
