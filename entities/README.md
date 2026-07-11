# Entities

`entities/` is the architecture boundary for the repository's first-class knowledge entities. The [AiiDA reference implementation](../docs/reference-implementation.md) is the first reviewed vNext cluster: it adds canonical records incrementally without moving or renaming existing material.

Each child directory is a canonical home for one entity type. Views and country-oriented navigation reference these records rather than duplicate them. `departments/` is included alongside the requested directories because Department is a first-class entity in the model.

The reference cluster contains [aiida-core](research-software/aiida-core.md), [AiiDA Ecosystem](ecosystems/aiida.md), [Giovanni Pizzi](principal-investigators/giovanni-pizzi.md), [Materials Software and Data Group](research-groups/materials-software-and-data-group.md), [Paul Scherrer Institute](organizations/paul-scherrer-institute.md), [Switzerland](countries/switzerland.md), and [Computational Materials Science](research-areas/computational-materials-science.md).
