# Entities

`entities/` is the architecture boundary for the repository's first-class knowledge entities. The [AiiDA reference implementation](../docs/reference-implementation.md) is the first reviewed vNext cluster, followed by the [Materials Project vertical slice](../docs/materials-project-vertical-slice.md): both add canonical records incrementally without moving or renaming existing material.

Each child directory is a canonical home for one entity type. Views and country-oriented navigation reference these records rather than duplicate them. `departments/` is included alongside the requested directories because Department is a first-class entity in the model.

The AiiDA cluster contains [aiida-core](research-software/aiida-core.md), [AiiDA Ecosystem](ecosystems/aiida.md), [Giovanni Pizzi](principal-investigators/giovanni-pizzi.md), [Materials Software and Data Group](research-groups/materials-software-and-data-group.md), [Paul Scherrer Institute](organizations/paul-scherrer-institute.md), [Switzerland](countries/switzerland.md), and [Computational Materials Science](research-areas/computational-materials-science.md).

The Materials Project cluster adds [pymatgen](research-software/pymatgen.md), [Materials Project](ecosystems/materials-project.md), [Kristin A. Persson](principal-investigators/kristin-persson.md), [Persson Group](research-groups/persson-group.md), [Lawrence Berkeley National Laboratory](organizations/lawrence-berkeley-national-laboratory.md), and [United States](countries/united-states.md), while reusing the existing Computational Materials Science area.
