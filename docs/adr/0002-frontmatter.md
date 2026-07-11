# ADR 0002: Use YAML frontmatter as the entity interchange boundary

- **Status:** Accepted
- **Date:** 2026-07-11

## Context

The project needs machine-readable metadata without losing the context and review ergonomics of Markdown.

## Decision

Require YAML frontmatter for every entity document and validate it with versioned JSON Schemas. Keep evidence narrative and editorial rationale in the body.

## Consequences

Static tooling can validate and index records, while humans can review a single file. YAML parsing and schema validation become required future CI capabilities.
