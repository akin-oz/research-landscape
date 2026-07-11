# ADR 0003: Assign immutable project IDs and retain external IDs separately

- **Status:** Accepted
- **Date:** 2026-07-11

## Context

Names, affiliations, and external-provider coverage change. URLs and display names cannot safely serve as primary keys.

## Decision

Use immutable, human-reviewable project IDs with controlled segments. Store ORCID, ROR, DOI, OpenAlex, and other identifiers in `external_ids`.

## Consequences

Records remain linkable through change and can reconcile with external systems. An allocator and collision validator are required before large-scale ingestion.
