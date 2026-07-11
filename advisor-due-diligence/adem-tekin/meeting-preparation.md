---
report_type: advisor-meeting-preparation
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: high
---

# Meeting preparation — Adem Tekin

## Meeting objective

Do not try to secure admission in this conversation. The objective is to answer one question:

> Is there a scientifically meaningful, well-supervised thesis at the intersection of transparent CSP, computational materials, and production-quality scientific software?

The meeting should be treated as mutual due diligence. Bring enough technical preparation to make the discussion useful, but leave room for the advisor to define the scientifically important problem.

## 90-second briefing to know cold

**Fact:** The group combines global optimization, crystal-structure prediction, periodic DFT, AI/ML-supported materials design, high-accuracy force fields and molecular dynamics. It currently lists PNcsp, CASPESA and work on hydrogen storage, CO₂ capture, catalysts and perovskites. [UHEM group page](https://uhem.itu.edu.tr/en/our-center/research-groups/theoretical-chemistry-and-computational-design-of-energy-materials)

**Fact:** PNcsp+ expands a periodic-number similarity CSP scheme by retrieving analogous prototypes from a materials database and ranking candidates with MACE, M3GNet, and ALIGNN-FF. The paper evaluates this on CSPBench and releases implementation data/code. [PNcsp+ paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/) · [PNcsp+ repository](https://github.com/tccdem/PNcsp_Plus)

**Fact:** The active-project record includes PNcsp+ development, testing PNcsp on complex systems, PN phase-map exceptions, LLM-assisted crystal generation, and a 2026–29 binary-compound design project. [ITU project record](https://research.itu.edu.tr/en/persons/tekinad/)

**Interpretation — high confidence:** The candidate should enter through the **software-validation boundary**: reproducible data intake, benchmarking, physical validation handoff, and transparent provenance. This serves a live scientific programme and makes the engineering contribution academically legible.

## What to read before entering the room

Read the first three items in [reading-list.md](reading-list.md) fully. Be able to explain in plain language:

1. Why prototype retrieval based on periodic-number proximity is useful and interpretable.
2. Why ranking with ML potentials is not equivalent to DFT validation.
3. Why performance needs a benchmark protocol, structured data provenance, explicit failure analysis, and reproducible environments.

Prepare one page with:

- one diagram of a proposed pipeline: **formula → candidate prototypes → ML ranking → DFT/relaxation → stability/property checks → provenance-rich report**;
- one small, real engineering example from your work (tests, API/version migration, observability, reproducibility, data schema, or deployment); and
- a link or short demo of Materials Atlas only if it is stable enough to discuss without a long product presentation.

## Current research hooks

| Hook | Direct evidence | A good research—not sales—entry point |
| --- | --- | --- |
| PNcsp+ | The 2026 paper combines PN-similarity prototype generation with MACE/M3GNet/ALIGNN-FF ranking and supports optional relaxation. [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/) | “Which benchmark failures are scientifically most informative: low-symmetry systems, metastability, molecular components, or out-of-distribution chemistry?” |
| PN phase maps / binary compounds | ITU lists CDBC through 2029 plus 2025–26 PNcsp/phase-map projects. [projects](https://research.itu.edu.tr/en/persons/tekinad/) | “Could a thesis produce a versioned, auditable phase-map data model and benchmark corpus that identifies where PN similarity succeeds or fails?” |
| Perovskite screening | The group combines DFT and ML for stability/band-gap screening; the 2025 study publishes code/data. [PCCP full text](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b) | “How should predicted candidates be triaged and recorded so downstream DFT and experimental partners can assess confidence?” |
| Force fields / FFCASP | FFCASP is a parallel CSP method; NICE-FF automates force-field parameterisation and integrates with it. [FFCASP](https://doi.org/10.1021/acs.jctc.0c01197) · [NICE-FF](https://research.itu.edu.tr/en/publications/nice-ff-a-non-empirical-intermolecular-consistent-and-extensible-/) | “Where does force-field/candidate uncertainty most affect published conclusions, and can a workflow expose it rather than hide it?” |
| HPC/data infrastructure | Published work acknowledges UHEM/TRUBA; PNcsp+ documents local OQMD plus optional MP/MPDS sources. [PCCP paper](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b) · [PNcsp+ README](https://github.com/tccdem/PNcsp_Plus) | “What is the current bottleneck—database access, model execution, scheduler orchestration, or validation cost?” |

## Five realistic thesis hypotheses

These are **discussion starters**, not proposals to impose. Each has a scientific question, a software deliverable, and a validation condition. None should begin until the advisor identifies the one that advances a current group problem.

### 1. Reproducible and uncertainty-aware PNcsp+ benchmark suite

**Question:** Under which chemical-system classes, database versions, neighbour orders, and ML calculators does PNcsp+ reliably recover physically relevant structures—and where does it fail?

**Build:** A versioned benchmark harness around the published CSPBench protocol; pinned environment, data manifests, deterministic run records, structured output schema, baseline comparison, regression tests, and a result dashboard generated from machine-readable artifacts.

**Scientific value:** Converts a headline accuracy into a failure map across compositional complexity, symmetry, data-source availability, and relaxation mode. The current paper already exposes the components—prototype retrieval, GNN ranking, optional relaxation, StructureMatcher evaluation—so this extends rather than replaces the science. [PNcsp+ methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/)

**Validation:** Reproduce a documented subset of published results, pre-register a held-out subset, and compare predicted candidates after a common DFT-relaxation protocol.

**Risk to resolve:** “Benchmark” must not become only CI plumbing. The thesis needs a falsifiable finding about retrieval/ranking behaviour.

### 2. FAIR provenance layer for DFT–ML material-screening workflows

**Question:** Can a materials candidate remain interpretable after it travels from database record through heuristic filtering, ML prediction, DFT validation, and report?

**Build:** Python package plus JSON/JSON-LD-like provenance records for composition, source database/version/license, structure identifier, code/model/version, hyperparameters, resource request, computed properties, uncertainty, and decision/rejection reason. Include exportable human-readable reports.

**Scientific value:** In the 2025 perovskite study, thousands of candidates move through tolerance factors, DFT datasets, gradient boosting, and selected DFT checks. The proposed work makes this decision chain inspectable and reusable. [perovskite methods](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b)

**Validation:** Reconstruct one published screen from its released code/data; audit a sample of candidates end-to-end; measure whether a second researcher can reproduce the candidate table and explain exclusions.

**Risk to resolve:** Data licenses/API terms for OQMD, Materials Project, MPDS, and project-generated structures must be agreed before release.

### 3. Hybrid ML-potential → DFT triage with calibrated escalation

**Question:** When should PNcsp+ trust a fast ML-potential ranking, relax candidates, or escalate to DFT so that compute budget is spent where it changes the scientific conclusion?

**Build:** A Python orchestration layer using documented calculators (MACE/M3GNet/ALIGNN-FF), consensus/disagreement metrics, failure logging, scheduler adapters, and a queue that emits reproducible DFT input bundles.

**Scientific value:** Rather than chasing generic “better AI,” this tests a decision policy against physical outcomes: structure match, space group, stability/ranking changes after relaxation, and compute cost. [PNcsp+](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/)

**Validation:** Compare fixed top-*n* ranking with an uncertainty/escalation policy on a held-out corpus; report accuracy, wall time, CPU/GPU use, and cases where the policy is unsafe.

**Risk to resolve:** The advisor must define acceptable calculators and access to DFT/HPC resources; no validity claim should rely solely on ML potential agreement.

### 4. Data-quality and exception discovery for periodic-number phase maps

**Question:** Which apparent PN-phase-map exceptions are chemistry, which are database coverage artefacts, and which arise from prototype or symmetry matching choices?

**Build:** A typed data-quality pipeline that detects duplicate/ambiguous prototypes, missing metadata, inconsistent formula normalisation, and provenance conflicts; pair it with an interactive exception review notebook and a curated, citable exception set.

**Scientific value:** The group has a named 2025–26 project on PN-based phase-map exceptions. This turns data hygiene into a testable source of materials insight rather than a generic cleanup task. [ITU projects](https://research.itu.edu.tr/en/persons/tekinad/)

**Validation:** Manually adjudicate a blinded sample with group experts; compare conclusions before/after data corrections; validate a subset with DFT or literature-backed structures.

**Risk to resolve:** Human adjudication criteria and data-source rights must be written down at the start.

### 5. Open candidate-to-publication workflow for lead-free perovskites

**Question:** Can a transparent workflow preserve the physical assumptions needed to turn a large composition screen into a defensible, small candidate set?

**Build:** Reusable Python workflow from elemental descriptors and initial structural assumptions through DFT (Quantum Espresso/GPAW-style inputs where permitted), model training, uncertainty/error reporting, candidate cards, and experimental-handoff data packages.

**Scientific value:** The existing screen already uses DFT-generated stability/band-gap data, gradient boosting, cross-validation and a small DFT validation sample. The new contribution would expose out-of-domain risk, phase assumptions, and reproducible candidate selection. [perovskite study](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b)

**Validation:** Use nested/temporal or compositional hold-out tests, independent DFT re-computation, and—only if a partner agrees—an experimental feedback loop.

**Risk to resolve:** Do not market predicted candidates as experimentally realised materials. The published work itself is computational screening.

## Collaboration ideas to mention, briefly

- **Software-engineering contribution to PNcsp+:** tests, well-defined data contracts, package/release design, benchmark reproducibility, and user-facing documentation.
- **HPC orchestration:** useful only if the group identifies a real scheduler, data-transfer, or repeated-run bottleneck.
- **Materials Atlas:** offer it as an experiment in provenance-rich materials records and reading pathways, not as an unrelated product. Ask whether a small PNcsp+ benchmark/candidate dataset would be useful to the group.
- **Research Landscape:** mention once as evidence of structured research-data thinking. Do not ask the advisor to evaluate it or devote meeting time to it.

## Conversation plan for an in-person visit

### Opening — 60 seconds

“Thank you for meeting me. I have spent the last decade building software systems, and I am deliberately moving toward scientific software for computational materials. I read the PNcsp+ work and the perovskite screening paper because I was struck by the combination of interpretable chemistry, ML acceleration, and a real computational validation path. I am not here to ask for admission today; I would value your advice on where software work can make a scientifically original contribution in this area.”

### Research discussion — 10 minutes

1. State one specific observation: PNcsp+ makes a chemical-similarity prior explicit, while the ML potential is a ranking layer.
2. Ask one question about failure modes, not features: “Which class of systems is currently hardest or most scientifically revealing?”
3. Offer one bounded engineering hypothesis: a reproducible benchmark/provenance/escalation workflow, then invite correction.
4. Ask what would count as a thesis-level scientific result rather than “better code.”

### Introduce the software background — 90 seconds

“My strongest contribution is not simply writing scripts. It is turning a research workflow into something another person can run, inspect, test, and extend: explicit data contracts, reproducible environments, automated validation, documentation, and careful change management. I would want those practices to serve a materials question and be evaluated by scientific outcomes.”

### Introduce Materials Atlas — 45 seconds

“I am building Materials Atlas as a transparent, source-linked way of organizing materials knowledge. I see its relevance here only if it can make computational candidates and their provenance easier to inspect—for example, a small benchmark/candidate record with methods, inputs, and validation status. Would that be useful, or would it distract from the group’s current needs?”

### Ask for guidance, not admission — 30 seconds

“Given the group’s current projects, what would you recommend I learn or reproduce over the next few months to find out whether I can make a meaningful contribution? If there is a suitable direction, I would be grateful for a later conversation about a formal graduate path.”

## What success looks like after the meeting

Leave with written answers to these five points:

1. One named scientific problem and why it matters now.
2. A candidate contribution bounded to a real codebase/dataset/workflow.
3. A proposed validation standard (benchmark, DFT, literature, experimental partner, or all of these).
4. A supervision cadence and decision-maker for technical review.
5. Agreement on ownership, licensing, authorship, and whether a software artifact can be a named thesis output.

If these remain vague, the topic fit is real but the supervisory fit is unproven.
