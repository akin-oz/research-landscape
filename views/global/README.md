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

The current Materials Project, AiiDA, Materials Cloud, NOMAD, AFLOW, ASE, Quantum ESPRESSO, and LAMMPS material in the repository is a useful discovery trail. Its source register and dossiers remain the evidence boundary until matching canonical entities are created.
