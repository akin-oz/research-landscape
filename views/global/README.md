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

The [AiiDA reference implementation](../../docs/reference-implementation.md), [ASE–DTU CAMD vertical slice](../../docs/ase-dtu-vertical-slice.md), [LAMMPS ecosystem vertical slice](../../docs/lammps-ecosystem-intelligence-vertical-slice.md), [Open Catalyst Project vertical slice](../../docs/open-catalyst-project-vertical-slice.md), [OpenKIM–University of Minnesota vertical slice](../../docs/openkim-umn-vertical-slice.md), [Materials Project vertical slice](../../docs/materials-project-vertical-slice.md), [OQMD–Wolverton vertical slice](../../docs/oqmd-wolverton-vertical-slice.md), [AFLOW–Curtarolo vertical slice](../../docs/aflow-curtarolo-vertical-slice.md), [Materialyze.AI–NUS vertical slice](../../docs/materialyze-ai-vertical-slice.md), [MACE–Cambridge vertical slice](../../docs/mace-cambridge-vertical-slice.md), [Quantum ESPRESSO ecosystem vertical slice](../../docs/quantum-espresso-ecosystem-intelligence-vertical-slice.md), [THEOS–EPFL / Materials Cloud vertical slice](../../docs/theos-vertical-slice.md), and [FAIRmat–Draxl vertical slice](../../docs/fairmat-draxl-vertical-slice.md) supply reviewed canonical entities across multiple software-ecosystem chains. The Open Catalyst record keeps its source-documented deprecation and code migration visible rather than treating a public legacy project as a current ecosystem-completeness claim.
