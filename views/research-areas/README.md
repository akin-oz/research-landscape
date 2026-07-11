# Research areas view

The research-areas view organizes entities around controlled subject concepts. A research-area entity is reusable: a PI, group, publication, project, software artifact, and ecosystem can all refer to the same stable research-area ID.

## Intended query

```yaml
view_id: research-areas/<research-area-id>
scope:
  entity_types:
    - principal-investigator
    - research-group
    - research-software
    - project
    - publication
filters:
  all:
    - path: research_area_ids
      intersects: [<research-area-id>]
```

Hierarchical areas can be resolved through a documented `parent_id` relationship. For example, Materials Informatics, Scientific Software, and AI should be controlled concepts with clear scope notes rather than loosely matched phrases in prose.

## Presentation rules

- Show the relationship type—such as `researches`, `is_about`, `uses`, or `develops`—where it changes the meaning of inclusion.
- Do not imply that every group connected to a broad area has the same methods, software culture, or degree opportunities.
- Keep an entity's detailed explanation and evidence in its canonical record; this view provides links and facets only.
- Treat a missing research-area relation as unknown until a contributor adds sourced metadata. It is not proof of absence.

This view is the preferred starting point for combinations such as "Materials Informatics + Python" or "AI + Scientific Software," which can then be narrowed with the personal filtering contract.
