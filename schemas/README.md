# Schemas

These JSON Schema Draft 2020-12 contracts validate YAML frontmatter after YAML is parsed to JSON. Every first-class entity has a schema; common fields live in `common.schema.json`. Schema shape is deliberately separate from evidence and semantic validation.

`entity-vnext.schema.json` is the forward-looking contract for the new entity-oriented `entities/` namespace. It adds standardized filter metadata and typed relationship assertions without changing, moving, or invalidating the existing v1 records. It will become enforceable only in a later Knowledge Graph Layer milestone.
