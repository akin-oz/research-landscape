# Frontmatter specification

Every entity Markdown document begins with YAML frontmatter conforming to `schemas/<entity>.schema.json`. Markdown body text explains the record; frontmatter is the machine-readable contract.

## Required common fields

```yaml
schema_version: 1
entity_type: advisor
id: TR-AKU-CSE-ADV-001
name: Example Name
status: draft
created_at: 2026-07-11
updated_at: 2026-07-11
```

Dates use `YYYY-MM-DD`; IDs follow the [stable identifier specification](../data-model/stable-identifiers.md). `aliases`, `external_ids`, `source_ids`, `confidence`, `evidence_window`, and `notes` are optional common fields. Entity documents must not include unrecognized top-level fields.

## Entity extensions

| Type | Required extension fields | Example |
| --- | --- | --- |
| `country` | `country_code` | `country_code: TR` |
| `university` | `country_id` | `country_id: TR` |
| `department` | `university_id` | `university_id: TR-AKU-UNI` |
| `lab` | `organization_id` | `organization_id: TR-AKU-CSE-DEPT` |
| `advisor` | `affiliation_ids` | `affiliation_ids: [TR-AKU-CSE-DEPT]` |
| `program` | `university_id`, `degree_level` | `degree_level: masters` |
| `publication` | `title`, `publication_date`, `publication_type` | `publication_type: article` |

## Examples

```yaml
---
schema_version: 1
entity_type: department
id: TR-AKU-CSE-DEPT
name: Computer Engineering
status: draft
created_at: 2026-07-11
updated_at: 2026-07-11
university_id: TR-AKU-UNI
faculty_id: TR-AKU-ENG-FAC
source_ids: []
---
```

Schemas allow empty relation arrays during drafting, but published records must meet evidence and editorial requirements. Schema validation checks shape, not truth, source quality, uniqueness, or permission to publish.
