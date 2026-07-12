# Architecture status

**Status date:** 2026-07-12

The entity-oriented architecture is implemented and remains frozen for ordinary
content work. Canonical entity ownership, v2 metadata, stable IDs, typed
relationships, view definitions, generated-output boundaries, and public/private
separation are operational.

The only execution-phase contract clarification is accepted ADR 0006, which
resolves the direct University-versus-Organization host reference for reviewed
Research Groups. New entity types, predicates, schema fields, canonical layers,
or changes to these boundaries require an ADR and explicit review; they must not
be introduced as a content workaround.
