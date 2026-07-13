# Entities

`entities/` is the architecture boundary for the repository's first-class knowledge entities. The [AiiDA reference implementation](../docs/reference-implementation.md) is the first reviewed vNext cluster, followed by the [Materials Project vertical slice](../docs/materials-project-vertical-slice.md): both add canonical records incrementally without moving or renaming existing material.

Each child directory is a canonical home for one entity type. Views and country-oriented navigation reference these records rather than duplicate them. `departments/` is included alongside the requested directories because Department is a first-class entity in the model.

The AiiDA cluster contains [aiida-core](research-software/aiida-core.md), [AiiDA Ecosystem](ecosystems/aiida.md), [Giovanni Pizzi](principal-investigators/giovanni-pizzi.md), [Materials Software and Data Group](research-groups/materials-software-and-data-group.md), [Paul Scherrer Institute](organizations/paul-scherrer-institute.md), [Switzerland](countries/switzerland.md), and [Computational Materials Science](research-areas/computational-materials-science.md).

The Materials Project cluster adds [pymatgen](research-software/pymatgen.md), [Materials Project](ecosystems/materials-project.md), [Kristin A. Persson](principal-investigators/kristin-persson.md), [Persson Group](research-groups/persson-group.md), [Lawrence Berkeley National Laboratory](organizations/lawrence-berkeley-national-laboratory.md), and [United States](countries/united-states.md), while reusing the existing Computational Materials Science area.

The OQMD cluster adds [Open Quantum Materials Database](ecosystems/oqmd.md), [Chris Wolverton](principal-investigators/chris-wolverton.md), [Wolverton Research Group](research-groups/wolverton-research-group.md), and [Northwestern University](universities/northwestern-university.md), while reusing the United States country and Computational Materials Science area records.

The AFLOW cluster adds [AFLOW](ecosystems/aflow.md), the [AFLOW framework](research-software/aflow.md), [Stefano Curtarolo](principal-investigators/stefano-curtarolo.md), [Curtarolo Group](research-groups/curtarolo-group.md), and [Duke University](universities/duke-university.md), while reusing the United States country and Computational Materials Science area records.

The Materialyze.AI cluster adds [Shyue Ping Ong](principal-investigators/shyue-ping-ong.md), [Materialyze.AI Lab](research-groups/materialyze-ai-lab.md), [National University of Singapore](universities/national-university-of-singapore.md), [Singapore](countries/singapore.md), and [Materials Informatics](research-areas/materials-informatics.md), while linking to the existing [pymatgen](research-software/pymatgen.md) and Materials Project records.

The Hacking Materials cluster adds [Anubhav Jain](principal-investigators/anubhav-jain.md) and [Hacking Materials](research-groups/hacking-materials.md), reusing the existing Lawrence Berkeley National Laboratory, United States, Computational Materials Science, and Materials Project records.

The THEOS cluster adds [Nicola Marzari](principal-investigators/nicola-marzari.md), [THEOS](research-groups/theos.md), [EPFL](universities/epfl.md), and [Materials Cloud](ecosystems/materials-cloud.md), while reusing the Swiss, PSI, AiiDA, and Computational Materials Science records.

The FAIRmat cluster adds [Claudia Draxl](principal-investigators/claudia-draxl.md), [SOLgroup](research-groups/solgroup.md), [Humboldt-Universität zu Berlin](universities/humboldt-university-berlin.md), [Germany](countries/germany.md), [NOMAD](research-software/nomad.md), and [FAIRmat](ecosystems/fairmat.md), while reusing Computational Materials Science.

The RIKEN Computational Materials Science cluster adds [Seiji Yunoki](principal-investigators/seiji-yunoki.md), the [Computational Materials Science Research Team](research-groups/riken-computational-materials-science-team.md), [RIKEN Center for Computational Science](organizations/riken-center-for-computational-science.md), and [Japan](countries/japan.md), while reusing Computational Materials Science.

The RIKEN Polymeromics cluster adds [Ryo Yoshida](principal-investigators/ryo-yoshida.md), the [Polymeromics Team](research-groups/riken-polymeromics-team.md), [RIKEN TRIP Headquarters](organizations/riken-trip-headquarters.md), and [RadonPy](research-software/radonpy.md), while reusing Japan and Materials Informatics.

The ASE cluster adds [Atomic Simulation Environment](research-software/ase.md), the [ASE Ecosystem](ecosystems/ase.md), [Computational Atomic-scale Materials Design](research-groups/dtu-camd.md), [Technical University of Denmark](universities/technical-university-of-denmark.md), and [Denmark](countries/denmark.md), while reusing Computational Materials Science.

The Quantum ESPRESSO cluster adds [Quantum ESPRESSO](research-software/quantum-espresso.md), the [Quantum ESPRESSO Ecosystem](ecosystems/quantum-espresso.md), [Quantum ESPRESSO Foundation](organizations/quantum-espresso-foundation.md), [Stefano Baroni](principal-investigators/stefano-baroni.md), [SISSA](universities/sissa.md), and [Italy](countries/italy.md), while reusing Nicola Marzari and Computational Materials Science.

The LAMMPS cluster adds [LAMMPS](research-software/lammps.md), the [LAMMPS Ecosystem](ecosystems/lammps.md), and [Sandia National Laboratories](organizations/sandia-national-laboratories.md), while reusing the United States, Computational Materials Science, and C++ records.

The OpenKIM cluster adds [KIM API](research-software/kim-api.md), the [OpenKIM Ecosystem](ecosystems/openkim.md), [Ellad Tadmor](principal-investigators/ellad-tadmor.md), and [University of Minnesota](universities/university-of-minnesota.md), while reusing the United States, Computational Materials Science, and C++ records. Tadmor's ecosystem relation is explicitly historical founding-director context rather than a current software-development claim.

The Open Catalyst Project extension adds the distinct [Open Catalyst Project](ecosystems/open-catalyst-project.md) ecosystem, with an evidence-bounded successor route to the existing [FAIRChem](research-software/fairchem.md) software record. It preserves the Open Catalyst Project organization's documented deprecation and code migration instead of treating current FAIRChem scope as historical-project ownership.

The CP2K cluster adds [CP2K](research-software/cp2k.md), the [CP2K Ecosystem](ecosystems/cp2k.md), and the controlled [Fortran](programming-languages/fortran.md) language record. It makes no person, institution, or complete-project-community claim.

The ABINIT cluster adds [ABINIT](research-software/abinit.md) and the [ABINIT Ecosystem](ecosystems/abinit.md), while reusing the controlled Fortran and Computational Materials Science records. It makes no person, institution, consortium, or complete-project-community claim.

The Density-Functional Theory and Electronic Structure area extension adds the controlled [area record](research-areas/density-functional-theory-and-electronic-structure.md) and directly classifies existing ABINIT, CP2K, Quantum ESPRESSO, CAMD, Curtarolo Group, Persson Group, SOLgroup, and Wolverton Research Group records. Their separately owned ecosystems and direct-host Universities become discoverable through existing evidence-bearing paths.

The Temple–Kohlmeyer–LAMMPS extension adds [Axel Kohlmeyer](principal-investigators/axel-kohlmeyer.md) and [Temple University](universities/temple-university.md), while reusing the LAMMPS, United States, and Computational Materials Science records.

The Scientific Software Engineering area extension adds the controlled [Scientific Software Engineering](research-areas/scientific-software-engineering.md) record and directly classifies the existing Materials Software and Data Group, Hacking Materials, THEOS, and Axel Kohlmeyer records without duplicating their software or host facts.

The NCCR MARVEL funding cluster adds the [Swiss National Science Foundation](organizations/swiss-national-science-foundation.md) and [NCCR MARVEL](funding/nccr-marvel.md), while adding only an evidence-bounded historical funding-program connection to the existing [Materials Cloud](ecosystems/materials-cloud.md) and reusing Switzerland.

The NoMaD Laboratory project cluster adds the [Max Planck Society](organizations/max-planck-society.md) and [The Novel Materials Discovery Laboratory](projects/nomad-laboratory-coe.md), while reusing Germany, Computational Materials Science, and the historical [NOMAD](research-software/nomad.md) software connection.

The Northwestern MSE department cluster adds the [Department of Materials Science and Engineering](departments/northwestern-materials-science-engineering.md) as administrative context for the existing [Wolverton Research Group](research-groups/wolverton-research-group.md), while preserving Northwestern University as that group's direct host.

The Horizon 2020 funding cluster adds the [European Commission](organizations/european-commission.md) and [Horizon 2020 — Research Infrastructures](funding/horizon-2020-research-infrastructures.md), while connecting them to the existing completed [NoMaD Laboratory project](projects/nomad-laboratory-coe.md).

The FAIRmat users-meeting cluster adds the [Eighth FAIRmat Users Meeting](conferences/fairmat-users-meeting-2026.md), while connecting it to the existing FAIRmat ecosystem, Computational Materials Science area, and Germany location endpoint.

The AiiDA ecosystem-intelligence cluster adds the [AiiDA 1.0 publication](publications/aiida-1-0.md), enriches the [AiiDA Ecosystem](ecosystems/aiida.md) and [aiida-core](research-software/aiida-core.md) with source-backed architecture, community, contribution, user-journey, and NCCR MARVEL support context, and reuses the existing PSI, THEOS, Giovanni Pizzi, and Materials Cloud records.

The Materials Project ecosystem-intelligence cluster adds the [2013 pymatgen publication](publications/pymatgen-2013.md), enriches the [Materials Project](ecosystems/materials-project.md) and [pymatgen](research-software/pymatgen.md) with source-backed data-production architecture, API user-journey, and public contribution context, and reuses the existing LBNL, Persson Group, Kristin Persson, Shyue Ping Ong, and Anubhav Jain records.

The NOMAD ecosystem-intelligence cluster adds the [2023 NOMAD publication](publications/nomad-joss-2023.md), enriches [NOMAD](research-software/nomad.md) and [FAIRmat](ecosystems/fairmat.md) with source-backed architecture, data-management user-journey, extension, contribution, and NFDI-funding-boundary context, and reuses existing Claudia Draxl, SOLgroup, NoMaD Laboratory CoE, Horizon 2020, and Users Meeting records.

The AFLOW ecosystem-intelligence cluster adds the [2023 aflow++ publication](publications/aflow-plus-plus-2023.md), enriches the [AFLOW ecosystem](ecosystems/aflow.md) and [AFLOW framework](research-software/aflow.md) with source-backed contributor, installation, documentation, and API user-journey context, and reuses the existing Curtarolo Group, Stefano Curtarolo, and Duke records.

The ASE ecosystem-intelligence cluster adds the [2017 ASE publication](publications/ase-2017.md), enriches the [Atomic Simulation Environment](research-software/ase.md) and [ASE Ecosystem](ecosystems/ase.md) with source-backed calculator architecture, Python/CLI/GUI user-journey, GitLab contribution, and community-support context, and reuses the existing CAMD and DTU records.

The OQMD ecosystem-intelligence cluster adds the [2015 OQMD publication](publications/oqmd-2015.md), enriches the [Open Quantum Materials Database](ecosystems/oqmd.md) with source-backed REST/OPTIMADE, download, provenance, and citation context, and reuses the existing Wolverton Group, Chris Wolverton, and Northwestern records without inventing an OQMD backend-software entity.

The Materials Cloud ecosystem-intelligence cluster adds the [2020 Materials Cloud publication](publications/materials-cloud-2020.md), enriches [Materials Cloud](ecosystems/materials-cloud.md) with source-backed research-cycle, moderated data-deposition, Archive-architecture, and historical-funding-boundary context, and reuses existing AiiDA, THEOS, Nicola Marzari, Giovanni Pizzi, and NCCR MARVEL records.

The first Research Group Intelligence cluster enriches the [Persson Group](research-groups/persson-group.md) with evidence-bounded themes, people categories, software practice, publication, role-specific guidance, and selected alumni-outcome context while reusing its existing LBNL, Materials Project, pymatgen, and Kristin Persson records.

The second Research Group Intelligence cluster enriches the [Wolverton Research Group](research-groups/wolverton-research-group.md) with evidence-bounded themes, methods, OQMD stewardship, people categories, news, and selected alumni-outcome context while preserving its existing Northwestern, Department, OQMD, and Chris Wolverton records.

The third Research Group Intelligence cluster enriches the [Curtarolo Group](research-groups/curtarolo-group.md) with evidence-bounded research programs, AFLOW’s public software surface, people categories, publication pattern, seminar context, and selected alumni-outcome examples while preserving its existing Duke, AFLOW, and Stefano Curtarolo records.

The fourth Research Group Intelligence cluster enriches [Hacking Materials](research-groups/hacking-materials.md) with evidence-bounded community-software, collaboration, people, process, computing, software-funding, and participation-route context while preserving its existing Berkeley Lab, Materials Project, and Anubhav Jain records.

The fifth Research Group Intelligence cluster enriches [THEOS](research-groups/theos.md) with evidence-bounded research programs, shared open-source infrastructure, education/outreach, and student-project discovery context while preserving its existing EPFL, AiiDA, Materials Cloud, and Nicola Marzari records.

The sixth Research Group Intelligence cluster enriches [SOLgroup](research-groups/solgroup.md) with evidence-bounded research programs, `exciting`/CELL development, open-source context, people/archive, publication, student-topic, and GraFOx-partnership context while preserving its existing Humboldt, FAIRmat, NOMAD, and Claudia Draxl records.

The seventh Research Group Intelligence cluster enriches [DTU CAMD](research-groups/dtu-camd.md) with evidence-bounded section leadership, CAMPOS/ASE software, Python-interface/GPL context, technical programs, sub-group project routes, and limited funding context while preserving its existing DTU and ASE records.

The eighth Research Group Intelligence cluster enriches [Materialyze.AI Lab](research-groups/materialyze-ai-lab.md) with evidence-bounded theory/data/AI themes, public software and open-science context, role categories, and a dated applicant/onboarding surface while preserving the distinct PI-level pymatgen and Materials Project records.

The ninth Research Group Intelligence cluster enriches the [RIKEN Polymeromics Team](research-groups/riken-polymeromics-team.md) with evidence-bounded polymer data, automated MD/first-principles, foundation-model, Sim2Real, autonomous-discovery, people, and selected-publication context while preserving the shared RadonPy relationship and RIKEN TRIP direct host.

The tenth Research Group Intelligence cluster enriches the [RIKEN Computational Materials Science Research Team](research-groups/riken-computational-materials-science-team.md) with evidence-bounded numerical-method, quantum/HPC, people, representative-publication, and report-navigation context while preserving its R-CCS direct host and avoiding unsupported software or opportunity records.

The eleventh Research Group Intelligence cluster enriches the [PSI Materials Software and Data Group](research-groups/materials-software-and-data-group.md) with evidence-bounded software/data, open-science, people, publication, and project-navigation context while preserving its shared AiiDA relationship and PSI direct host.
