# ADR 0006: Resolve the vNext host reference for university-based research groups

- **Status:** Accepted — 2026-07-12
- **Date:** 2026-07-12

## Context

At proposal time, the vNext schema required every `research-group` record to
have `organization_id`. The metadata contract describes that field as the direct
non-university host, while `institution_id` represents a university host. The
relationship model also permits a Research Group to `belongs_to` a University
or an Organization.

This works for the existing AiiDA slice because PSI is modeled as an
Organization. It does not work cleanly for Anchor Cohort groups whose direct
host is a university: satisfying the required `organization_id` would either
mislabel a University as an Organization or create a prohibited duplicate
Organization record for the same university.

The entity model explicitly says not to create both a University and a generic
Organization record merely to describe the same institution. A schema
workaround would therefore violate canonical ownership.

## Decision

Option 1, **Either host field**, is accepted.

For a reviewed or published vNext `research-group`, exactly one direct host is
required:

- `institution_id` when the direct host resolves to a canonical University;
- `organization_id` when the direct host resolves to a canonical non-university
  Organization.

`department_id` may record an evidenced administrative context, but it is not
a substitute for the direct host. `organization_ids` may record additional
evidenced organizations, but cannot satisfy or repeat the direct-host field.
A draft group may omit its host while evidence is incomplete, but it must not
declare both direct-host fields.

The vNext JSON Schema enforces the field cardinality. Before a group is marked
reviewed or published, canonical review must also verify that the selected ID
resolves to exactly one canonical entity of the required type and that the
group's evidence-bearing direct `belongs_to` assertion, when present, names the
same ID. This is a cross-record semantic check; JSON Schema cannot establish
it from one record alone.

Contributors must not point `organization_id` at a University merely to satisfy
validation and must not duplicate a University as an Organization.

## Consequences

- The PSI AiiDA reference slice remains valid because its host is an
  Organization.
- Candidate groups at university hosts can enter QG1 once their evidence and
  direct-host identity are reviewed; no duplicate institutional entity is
  added.
- A later graph validator can automate the cross-record host-type check, but
  the canonical review rule applies before that automation exists.

## References

- [vNext entity metadata](../architecture/metadata.md)
- [Entity-oriented knowledge model](../architecture/entity-model.md)
- [Relationship model](../architecture/relationships.md)
- [Entity vNext schema](../../schemas/entity-vnext.schema.json)
