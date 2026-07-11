# ADR 0001: Model the repository as a document-backed knowledge graph

- **Status:** Accepted
- **Date:** 2026-07-11

## Context

Thousands of research entities and cross-cutting relationships cannot be maintained as isolated narrative reports.

## Decision

Use Markdown entity documents with schema-validated YAML metadata and stable ID references. Treat frontmatter records and typed relationships as the canonical graph representation; reports are derived views.

## Consequences

The repository remains reviewable in Git and usable without a database, while future tooling can parse it into indexes, APIs, and graph stores. Contributors must follow stricter metadata rules.
