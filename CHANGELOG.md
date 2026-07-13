# Changelog

All notable changes are documented here. This project follows the principles of [Keep a Changelog](https://keepachangelog.com/) and semantic versioning when releases begin.

## [Unreleased]

### Added

- `discover-problems --language` now narrows the reviewed problem catalog through a documented software `implemented_in` → `supports` → problem path, exposing both sources without treating an implementation language as individual skill, group practice, research fit, or a ranking signal.
- `discover-problems --ecosystem` now narrows the reviewed problem catalog through an explicit ecosystem `includes` → software `supports` → problem path, exposing both sources without treating ecosystem adjacency as a problem relationship or ranking results.
- `discover-problems --software` now narrows the reviewed problem catalog through a software record's direct sourced `supports` assertion; it can be ANDed with `--area` without inferring a problem relationship from software adjacency or ranking results.
- `discover-problems --area` now narrows the reviewed problem catalog through each problem's own sourced controlled-area classification and shows that matching evidence, without inferring problem scope from adjacent graph entities or ranking the results.
- A fourth evidence-bounded Research Problem record for Density-Functional Electronic-Structure Calculation, with independent direct support paths from ABINIT, Quantum ESPRESSO, GPAW, and SIESTA; the discovery path does not compare functionals, numerical methods, software, or problem importance.
- A third evidence-bounded Research Problem record for Machine-Learned Interatomic Potential Modeling, with independent direct support paths from MACE, NequIP, and DeePMD-kit; the discovery path does not compare architectures, training methods, datasets, software, or problem importance.
- A second evidence-bounded Research Problem record for Crystal Symmetry Determination, with a direct Spglib support path, demonstrating independent non-comparative problem discovery without turning documented functionality into a method or importance ranking.
- A first-class, evidence-bounded Research Problem entity contract and Lattice Thermal Conductivity Prediction slice, with a generated public problem index and direct Phono3py support path; it does not rank problem importance or convert a problem into a project.
- A controlled Crystal Symmetry Analysis area with direct Spglib and Atsushi Togo links, exposing topic-first software and PI discovery without inferring group scope or ranking research problems.
- A bounded Spglib ecosystem slice with distinct BSD-3-Clause C software, ecosystem, and language records, exposing a documented current main-developer path without inventing interface dependencies, group-wide language practice, or institutional relationships.
- A bounded Phono3py ecosystem slice with distinct BSD-3-Clause Python software and ecosystem records, exposing direct computational-materials and computational-phonon paths without inventing external-software dependencies, people beyond a contributor listing, or institutional relationships.
- A controlled Computational Phonon Calculations area with direct Phonopy, NIMS group, and Atsushi Togo links, exposing topic-first software, group, and PI discovery without making a research-problem ranking claim.
- A bounded Phonopy–NIMS environment extension with direct developer-maintainer, group, research-institute, and Japan paths, without inventing a university route, mentorship, admissions, or ranking claims.
- A bounded Phonopy ecosystem slice with distinct BSD-3-Clause Python software and ecosystem records, exposing direct computational-materials phonon-calculation paths without inventing contributor, dependency, people, or institutional relationships.
- A bounded Qbox ecosystem slice with distinct GPL-2.0-or-later C++ software and ecosystem records, exposing direct computational-materials and DFT/electronic-structure paths without inventing contributor, dependency, people, or institutional relationships.
- A bounded JDFTx ecosystem slice with distinct GPL-3.0-or-later C++ software and ecosystem records, exposing direct computational-materials and DFT/electronic-structure paths without inventing contributor, dependency, people, or institutional relationships.
- A bounded DFTK/Julia ecosystem slice with distinct MIT-licensed Julia software, ecosystem, and language records, exposing direct computational-materials and DFT/electronic-structure paths without inventing contributor, dependency, people, or institutional relationships.
- A bounded BigDFT ecosystem slice with distinct GPL-2.0-only Fortran software and ecosystem records, exposing direct computational-materials and DFT/electronic-structure paths without inventing suite-dependency, people, or institutional relationships.
- A bounded sisl ecosystem slice with distinct MPL-2.0 Python software and ecosystem records, exposing direct computational-materials and DFT/electronic-structure paths without inventing external-software dependency, people, or institutional relationships.
- A bounded NequIP ecosystem slice with distinct MIT-licensed Python software and ecosystem records, exposing direct AI-for-Materials and machine-learned-potential paths without inventing external-software dependency, people, or institutional relationships.
- A bounded DeePMD-kit ecosystem slice with distinct LGPL-3.0-only Python/C++ software and ecosystem records, exposing direct machine-learned-potential and AI-for-Materials paths without inventing external-software dependency, people, or institutional relationships.
- A bounded FLEUR ecosystem slice with distinct MIT-licensed Fortran software and ecosystem records, exposing direct all-electron DFT, source, test, and contribution evidence without inventing people or institutions.
- A bounded Wannier90 ecosystem slice with distinct LGPL-2.1-or-later Fortran software and ecosystem records, plus direct official developer-group evidence for Giovanni Pizzi and Nicola Marzari without inferring maintenance, ownership, or institutional control.
- A bounded SIESTA ecosystem slice with distinct GPL-3.0-only Fortran software and ecosystem records, exposing direct DFT/electronic-structure, installation, and GitLab contribution evidence without inventing people or institutional ownership.
- A direct, SISSA-CV-backed DFT/electronic-structure classification for Stefano Baroni, with a non-comparative PI discovery query; no other PI is inferred from group or ecosystem adjacency.
- A bounded GPAW ecosystem slice with distinct GPL-3.0-or-later Python software and ecosystem records, directly linking documented CAMD development and ASE-based DFT workflow context without asserting ownership or individual maintenance.
- A controlled Density-Functional Theory and Electronic Structure area, directly classifying ABINIT, CP2K, Quantum ESPRESSO, CAMD, Curtarolo Group, Persson Group, SOLgroup, and Wolverton Group; source-explainable ecosystem, group, and direct-host University queries expose only those paths without defining a universal subject taxonomy or method ranking.
- A bounded ABINIT ecosystem slice with distinct GPLv3 software and ecosystem records, reusing the controlled Fortran path to expose only documented DFT/materials, source-control, and learning/contribution surfaces.
- A bounded CP2K ecosystem slice with separate CP2K software and ecosystem records plus a controlled Fortran language entity; it exposes a source-backed GPL/Fortran contribution route without constructing a people, institution, or complete-community graph.
- A distinct Open Catalyst Project ecosystem record with its official, time-bounded code migration to FAIRChem; AI-for-Materials and machine-learned-potential discovery now exposes that route without conflating legacy OCP and current FAIRChem ownership or maintenance.
- A bounded OpenKIM/University of Minnesota vertical slice with distinct KIM API, ecosystem, PI, and University records; it documents C++ and LGPL-2.1-or-later software evidence while retaining Ellad Tadmor's founding-director context as historical rather than a current development claim.
- A controlled Scientific Software Engineering area with direct group and PI evidence, plus deterministic group, PI, ecosystem, and direct-host university discovery queries that remain non-comparative.
- A Temple University/Axel Kohlmeyer extension to the LAMMPS ecosystem, with independently sourced research-faculty affiliation and core-developer/co-maintainer evidence that avoids making supervision, ownership, or complete-maintainer claims.
- A controlled `discover-software --open-source` facet that AND-filters the software record's directly evidenced `open_source` state alongside area, implementation language, and ecosystem paths.
- A bounded LAMMPS ecosystem slice with distinct software, Sandia National Laboratories, and ecosystem records; it surfaces documented C++ implementation and public GitHub contribution paths without inventing a developer or maintainer roster.
- A bounded Quantum ESPRESSO ecosystem slice with distinct software, Foundation, and ecosystem records; its documented Foundation representative links to Stefano Baroni and Nicola Marzari avoid inferring current maintenance, governance, or contribution-frequency roles.
- A directly source-bounded Materials Informatics classification for RadonPy, based on RIKEN's published “polymer informatics” article listing; the record explicitly avoids generalizing that classification beyond the documented software context.
- An AI for Materials controlled research area with direct, evidence-bounded group and PI links, plus FAIR Chemistry/FAIRChem and UC Berkeley/CEDER/Gerbrand Ceder/CHGNet vertical slices.
- A controlled Machine-Learned Potentials for Materials area with directly supported CHGNet, FAIRChem, and CEDER Group connections plus explainable group, ecosystem, and direct-host university discovery paths.
- A MACE/University of Cambridge vertical slice with canonical United Kingdom, University, PI, and software nodes; the MACE relation is explicitly limited to group-attributed development evidence.
- A reviewed MatGL/Materialyze.AI software path with a bounded NUS-hosted group-development relation and Python implementation evidence, expanding Machine-Learned Potentials discovery without asserting individual roles.
- A named MatML ecosystem node with a single sourced MatGL inclusion, making its documented software-ecosystem context discoverable without inferring unreviewed components or contributors.
- A source-bounded M3GNet publication relation that exposes Shyue Ping Ong's Machine-Learned Potentials for Materials work without inferring an individual MatGL maintenance role.
- A distinct archived M3GNet software record, linked to its paper and Python implementation path, preserving the repository's replacement-by-MatGL boundary without conflating the two artifacts.
- A source-backed software-lifecycle contract, initially surfacing M3GNet's archived state in interactive software discovery while leaving all unobserved lifecycle states explicitly undocumented.
- Bounded AiiDA development-team relations from Giovanni Pizzi and Nicola Marzari to `aiida-core`, allowing open-source PI discovery without claiming maintainer authority, ownership, or ongoing contribution frequency.
- A controlled C++ programming-language entity and sourced implementation paths for AFLOW (C++), NOMAD, RadonPy, MACE, and FAIRChem (Python), with explicit implementation-only boundaries.
- Accepted and implemented ADR 0007: a controlled Python programming-language entity, sourced Research Software `implemented_in` assertions, and an evidence-discovery path for groups with documented development links to Python software.
- Extended the CEDER/CHGNet vertical slice with a sourced Python implementation link, exposing its already documented group-development path in the Python discovery query.
- Accepted and implemented ADR 0008: a bounded public mentorship-process evidence field, two independently reviewed category slices, and a non-comparative discovery query that retains source limitations.
- Extended Hacking Materials' bounded mentorship-process evidence with a separately surfaced professional-development observation for documented research-writing and presentation guidance; it remains historical process evidence, not a quality or outcome signal.
- New explainable discovery paths for AI-for-Materials groups, PIs, ecosystems, and direct-host universities; PIs with licensed open-source software development evidence; and universities directly hosting documented Computational Materials Science groups.
- A `recommend --list` catalog for public query IDs, aliases, titles, and unavailable-dimension status, plus `recommend --query` interactive lookup.
- A public `catalog` command for reviewed Research Area, Country, Research Software, and Programming Language IDs accepted by interactive discovery commands.
- An interactive `discover-groups` command for deterministic AND filtering of reviewed research groups by canonical area, country, software, and programming-language IDs, with every matching path and source ID shown.
- An interactive `discover-pis` command applying the same evidence-first filters to reviewed Principal Investigators, with country matches limited to documented public affiliation paths.
- An interactive `discover-universities` command exposing documented country and direct-host group paths for academic-environment discovery without comparing institutions.
- An interactive `discover-ecosystems` command for source-explainable ecosystem filtering by controlled research area and included research software, without dominance claims.
- An interactive `discover-software` command for source-explainable AND filtering by research area, implementation language, and ecosystem inclusion.
- Ecosystem-path filters for groups, PIs, and direct-host universities, showing the sourced developer → software → ecosystem route without inferring ecosystem membership, ownership, governance, or institutional strength.
- A reproducible review-freshness audit based on canonical `last_review` dates and declared volatile-assertion deadlines.
- A generated research-area discovery coverage matrix showing the current direct group, PI, software, direct-host University, and ecosystem path coverage for each controlled area.

### Changed

- Ecosystem-by-area discovery and generated area coverage now require either direct included-software classification or a connected research group's direct area relation; an individual PI's separate topic portfolio no longer classifies every connected ecosystem.
- Evidence validation now resolves `SRC-*` claims only from unique `## Evidence` table rows and requires a public URL plus a valid ISO access date for each source.
- Ecosystem-by-area recommendations now display both sourced ecosystem-to-entity paths and sourced ecosystem-to-software-to-area paths.

### Notes

- This work is post-v0.3 and is not part of the `v0.3.0` release tag.
- “High mentorship environments” remains unavailable; the new process-evidence query is explicitly non-comparative and does not measure quality or capacity.

## [0.3.0] - 2026-07-12

### Added

- The first production-quality knowledge-graph execution cohort: 67 reviewed v2 canonical entities and 116 evidence-bearing typed relationship assertions.
- Software Ecosystem Mapping and Research Group Intelligence coverage for the reviewed cohort, including direct-host integrity checks.
- Declarative deterministic views: 13 definitions, 10 generated public indexes, and 3 deliberately private contracts.
- Repository validation, migration checks, generated health reporting, deterministic recommendation generation, regression tests, and CI drift checks.
- Explainable evidence-discovery queries that expose predicates, targets, source identifiers, confidence, coverage, limitations, and explicitly unavailable dimensions.
- Contributor onboarding, entity-authoring, review-process, automation, recommendation, quality, migration, and architecture-status guidance.
- Final implementation review and release documentation for the complete QG1–QG10 execution phase.

### Changed

- The roadmap now records the completed v0.3.0 execution release and focuses forward work on evidence-bounded expansion, source/freshness governance, and ethical mentorship evidence.

### Notes

- This release is an integrity-reviewed canonical cohort, not a global census, prestige ranking, admissions prediction, or mentorship ranking.
- Language and comparable mentorship dimensions remain unavailable until governed evidence contracts exist.

## [0.2.0] - 2026-07-11

### Added

- Research Relationship Management (RRM): a Markdown-first, Git-based layer for preparing, documenting, and improving research-related interactions without introducing a CRM, database, or web application.
- Reusable relationship templates for timelines, contact logs, meeting preparation and notes, action items, follow-ups, reading progress, research ideas, application plans, and research-focused email drafts.
- Explicit relationship philosophy, privacy boundaries, lifecycle statuses, archive policy, and automation-readiness rules.
- Prepared, uncontacted relationship records for Adem Tekin, Sadettin Yavuz Uğurlu, and Hande Toffoli. The records link to existing due diligence and intentionally contain no fabricated interaction or application facts.
- Deep due-diligence dossiers for the narrowed three-advisor shortlist, including publication audits, reading plans, meeting preparation, risk analysis, decision gates, and first-contact guidance.

### Changed

- The repository README and Turkey index now link the due-diligence and RRM layers.

### Notes

- RRM interaction records are not public research evidence, relationship-quality scores, admissions predictions, or networking profiles.
- Automation may validate structure and dates in the future, but must not infer intent, send messages, scrape contact data, or turn interactions into evidence automatically.

## [0.1.0] - 2026-07-11

### Added

- Core knowledge model: stable identifiers, entity and relationship contracts, evidence pipeline, frontmatter specification, ADRs, and JSON Schemas.
- Versioned scoring-model contracts under `scoring/v1/`.
- Evidence-bounded Akdeniz University compatibility pilot, including current-roster reconciliation, individual advisor dossiers, comparison, ranked shortlist, and decision report.
- Nationwide Turkey advisor search with 20 evidence-backed potential MSc advisors, research-environment comparison, application tiers, and source register.

### Changed

- Country namespaces now surface published pilot and nationwide reports rather than placeholder-only content.

### Notes

- Compatibility tiers are not prestige rankings or admissions recommendations.
- The scoring model remains a design contract; no universal numeric advisor scores are published.

## [0.0.1] - 2026-07-11

### Added

- Initial repository architecture and documentation framework.
- Research methodology, scoring philosophy, and roadmap.
- Community guidelines, contribution documentation, licensing, and open-source infrastructure.

### Notes

This release establishes the project's engineering and methodological foundations. No university data, advisor evaluations, department reports, or scoring results are included.
