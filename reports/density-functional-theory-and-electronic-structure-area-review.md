# Density-Functional Theory and Electronic Structure area review

**Review date:** 2026-07-13

**Scope:** a controlled research-area increment connecting only existing
ABINIT, CP2K, Quantum ESPRESSO, CAMD, Curtarolo Group, Persson Group, SOLgroup,
and Wolverton Research Group records where their own sources explicitly
describe DFT or electronic-structure calculations.

**Outcome:** the increment adds one canonical area entity, three direct
software classifications, and five direct group classifications. Existing
ecosystem inclusion, ecosystem-to-group, and direct-host paths make the area
discoverable through six ecosystems and four Universities without adding people or institutional
relationships.

## Evidence coverage

| Claim family | Primary evidence | Review result |
| --- | --- | --- |
| Area identity | Official ABINIT, CP2K, and Quantum ESPRESSO descriptions | Supports the common, bounded DFT/electronic-structure discovery concept. |
| ABINIT classification | ABINIT presentation | Supports DFT electronic-structure calculations for molecules and periodic solids. |
| CP2K classification | CP2K public repository | Supports DFT methods inside the documented quantum-chemistry and solid-state package. |
| Quantum ESPRESSO classification | Quantum ESPRESSO public home | Supports electronic-structure and DFT scope for nanoscale materials modelling. |
| Group classifications | Five first-party group research/development pages | Support record-local DFT or electronic-structure scope for CAMD, Curtarolo, Persson, SOLgroup, and Wolverton. |

## Relationship and discovery review

| Check | Result |
| --- | --- |
| Direct ownership | Each classification remains software-record metadata supported by that software record's own evidence. |
| Ecosystem traversal | Existing `includes` relations yield `ECO-ABINIT`, `ECO-CP2K`, and `ECO-QUANTUM-ESPRESSO`; existing `connects` relations yield ASE via CAMD, Materials Project via Persson Group, and OQMD via Wolverton Group. Every route displays its source identifiers. |
| Group and direct-host traversal | Five sourced group `works_on` relations and four existing direct-host University paths yield non-comparative group and University queries. Persson Group remains visible only at group level because its direct host is an Organization. |
| No inferred people | No PI, organization, or funding relation is created. |
| Public query | Source-explainable ecosystem, group, and University recommendation queries plus dynamic software discovery expose the area. |

## Deliberate non-claims

1. This is not a universal definition of electronic structure, DFT, quantum
   chemistry, solid-state physics, or computational materials science.
2. It does not classify adjacent software, machine-learned potentials,
   workflows, datasets, people, or institutions without record-local evidence.
3. It makes no claim about method superiority, accuracy, performance,
   maintenance, availability, support, funding, admissions, mentoring, or fit.

## Verification record

Acceptance requires clean validation, deterministic generation and
recommendation checks, and regressions for exact software, ecosystem, and
coverage paths. This increment changes no schema or generator contract.
