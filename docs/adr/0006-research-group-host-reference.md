# ADR 0006: Resolve the vNext host reference for university-based research groups

- **Status:** Proposed — approval required before university-hosted group migration
- **Date:** 2026-07-12

## Context

The vNext schema requires every `research-group` record to have
`organization_id`. The metadata contract describes that field as the direct
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

No schema workaround is selected in this ADR.

Quality Gate 1 must not create university-hosted Research Group records until
an approved decision reconciles the schema, metadata semantics, and
relationship model. Contributors must not point `organization_id` at a
University merely to satisfy validation and must not duplicate a University as
an Organization.

## Options requiring approval

1. **Either host field.** Make `organization_id` or `institution_id` the
   required direct-host reference for `research-group`, with a precise
   cardinality and validation rule.
2. **Broaden `organization_id`.** Allow it to resolve to a University, then
   revise the metadata semantics and migration guidance consistently.
3. **Introduce a versioned host abstraction.** Define a new normalized host
   reference only if the additional concept is justified against the simplicity
   and 50,000-entity scale constraints.

Any approved option must preserve existing v2 records, define target-type
validation, and provide a deliberate migration path for future university-hosted
groups.

## Consequences

- The PSI AiiDA reference slice remains valid because its host is an
  Organization.
- Candidate groups at university hosts remain in legacy discovery material
  until this contract is approved; no duplicate institutional entity is added.
- Future graph validation must enforce the approved host-type rule instead of
  validating ID shape alone.

## References

- [vNext entity metadata](../architecture/metadata.md)
- [Entity-oriented knowledge model](../architecture/entity-model.md)
- [Relationship model](../architecture/relationships.md)
- [Entity vNext schema](../../schemas/entity-vnext.schema.json)
