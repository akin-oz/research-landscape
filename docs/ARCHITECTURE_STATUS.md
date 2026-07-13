# Architecture status

**Status date:** 2026-07-13

The entity-oriented architecture is implemented and remains frozen for ordinary
content work. Canonical entity ownership, v2 metadata, stable IDs, typed
relationships, view definitions, generated-output boundaries, and public/private
separation are operational.

Accepted ADR 0006 resolves the direct University-versus-Organization host
reference for reviewed Research Groups. Accepted ADR 0007 adds the bounded
Programming Language entity and Research Software `implemented_in` contract.
Accepted ADR 0008 adds bounded public mentorship-process evidence without a
score or comparative claim. Accepted ADR 0009 adds the bounded Research Problem
entity and software `supports` contract. Accepted ADR 0010 keeps comparative
Research Problem outputs unavailable until a versioned, stakeholder-scoped,
evidence- and ethics-governed evaluation model is accepted. New entity types,
predicates, schema fields, canonical layers, or changes to these boundaries
require an ADR and explicit review; they must not be introduced as a content
workaround.
