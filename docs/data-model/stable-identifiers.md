# Stable identifiers

Research Landscape IDs are immutable, opaque enough to survive display-name changes, and readable enough for editorial review. They are internal identifiers, not replacements for ROR, ORCID, DOI, OpenAlex, or funder IDs; external identifiers are stored separately and may be absent.

## Format

`<country>-<institution>-<unit>-<type>-<sequence>`

Segments are uppercase ASCII letters and digits separated by hyphens. The country segment is ISO 3166-1 alpha-2 where applicable. Institution and unit codes are project-assigned abbreviations. Type codes are controlled: `UNI`, `FAC`, `DEPT`, `GRP`, `ADV`, `PROG`, `PUB`, `FUND`, `AREA`, `LANG`, `SW`, and `DATA`.

Examples: `TR-AKU-CSE-ADV-001`, `TR-AKU-MSE-DEPT`, `TR-AKU-UNI`, and `AREA-COMPUTER-VISION`. Global concepts may omit a country or institution segment, while retaining their type code.

## Allocation rules

1. Allocate an ID once an entity is sufficiently evidenced to create a draft record.
2. Never encode a mutable name, title, rank, or score in an ID.
3. Never reuse an ID, including after retirement or deletion of a draft.
4. Record aliases and external IDs for reconciliation; do not create a duplicate merely because a name changes.
5. Maintain a future ID registry generated from frontmatter to detect collisions.

The JSON Schema permits project IDs structurally; semantic uniqueness and segment allocation are repository validation responsibilities.
