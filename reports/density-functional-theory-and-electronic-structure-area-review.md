# Density-Functional Theory and Electronic Structure area review

**Review date:** 2026-07-13

**Scope:** a controlled research-area increment connecting only existing
ABINIT, CP2K, GPAW, Quantum ESPRESSO, CAMD, Curtarolo Group, Persson Group,
SOLgroup, Wolverton Research Group, and Stefano Baroni records where their own
sources explicitly describe DFT or electronic-structure calculations.

**Outcome:** the increment adds one canonical area entity, four direct software
classifications, five direct group classifications, and one direct PI
classification. Existing ecosystem inclusion, ecosystem-to-group, and
direct-host paths make the area discoverable through seven ecosystems and four
Universities without adding institutional relationships.

## Evidence coverage

| Claim family | Primary evidence | Review result |
| --- | --- | --- |
| Area identity | Official ABINIT, CP2K, and Quantum ESPRESSO descriptions | Supports the common, bounded DFT/electronic-structure discovery concept. |
| ABINIT classification | ABINIT presentation | Supports DFT electronic-structure calculations for molecules and periodic solids. |
| CP2K classification | CP2K public repository | Supports DFT methods inside the documented quantum-chemistry and solid-state package. |
| GPAW classification | GPAW official documentation | Supports DFT Python-code scope based on PAW and ASE. |
| Quantum ESPRESSO classification | Quantum ESPRESSO public home | Supports electronic-structure and DFT scope for nanoscale materials modelling. |
| Group classifications | Five first-party group research/development pages | Support record-local DFT or electronic-structure scope for CAMD, Curtarolo, Persson, SOLgroup, and Wolverton. |
| PI classification | Stefano Baroni's SISSA CV | Supports a person-level DFT/electronic-structure scope relation. |

## Relationship and discovery review

| Check | Result |
| --- | --- |
| Direct ownership | Each classification remains software-record metadata supported by that software record's own evidence. |
| Ecosystem traversal | Existing `includes` relations yield `ECO-ABINIT`, `ECO-CP2K`, `ECO-GPAW`, and `ECO-QUANTUM-ESPRESSO`; existing `connects` relations yield ASE via CAMD, Materials Project via Persson Group, and OQMD via Wolverton Group. Every route displays its source identifiers. |
| Group and direct-host traversal | Five sourced group `works_on` relations and four existing direct-host University paths yield non-comparative group and University queries. Persson Group remains visible only at group level because its direct host is an Organization. |
| PI traversal | Baroni's direct `works_on` relation yields a non-comparative PI query. No other PI is inferred from a group, ecosystem, publication, or adjacent software record. |
| Public query | Source-explainable ecosystem, group, PI, and University recommendation queries plus dynamic software discovery expose the area. |

## Deliberate non-claims

1. This is not a universal definition of electronic structure, DFT, quantum
   chemistry, solid-state physics, or computational materials science.
2. It does not classify adjacent software, machine-learned potentials,
   workflows, datasets, people, or institutions without record-local evidence.
3. It makes no claim about method superiority, accuracy, performance,
   maintenance, availability, support, funding, admissions, mentoring, or fit.

## Verification record

Acceptance requires clean validation, deterministic generation and
recommendation checks, and regressions for exact software, ecosystem, PI, and
coverage paths. This increment changes no schema or generator contract.
