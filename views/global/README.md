# Global view

The global view is the cross-border discovery surface for the knowledge graph. It starts from entity type, research area, software, ecosystem, or relationship—not from a country directory—and then exposes country as one filter among many.

It must not present a universal "best in the world" list. A global view can show documented connections and evidence coverage; any score must use the [scoring architecture](../../docs/scoring.md) and state its model and coverage.

## Intended query

```yaml
view_id: global
scope:
  entity_types:
    - principal-investigator
    - research-group
    - university
    - research-software
    - research-ecosystem
filters:
  all:
    - path: status
      in: [reviewed, published]
facets:
  - entity_type
  - research_area_ids
  - ecosystem_ids
  - resolved_country
  - software_ids
```

`resolved_country` is a relationship traversal to the Country record. It is not a second country field copied into every person, group, or software page.

## Inclusion and presentation

- Link each result to its canonical record and display only concise, declared metadata.
- Keep `draft`, `retired`, low-confidence, and stale records visibly distinguishable rather than turning their absence into a negative judgment.
- Present source coverage and last-review information alongside any derived result.
- Do not infer current supervision, openings, language, funding access, or mentorship from geography.

The [AiiDA reference implementation](../../docs/reference-implementation.md) and [Materials Project vertical slice](../../docs/materials-project-vertical-slice.md) now supply reviewed canonical entities for two software-ecosystem chains, including [AiiDA Ecosystem](../../entities/ecosystems/aiida.md) and [Materials Project](../../entities/ecosystems/materials-project.md). Materials Cloud, NOMAD, AFLOW, ASE, Quantum ESPRESSO, and LAMMPS material remain useful discovery trails until matching canonical entities are created; their source registers and dossiers retain their existing evidence boundaries.
