---
report_type: advisor-due-diligence-meeting-preparation
status: evidence-reviewed
evidence_window: public sources accessed 2026-07-11
confidence: mixed
---

# Meeting preparation — Hande Toffoli

## The purpose of the first meeting

Ask for **research advice**, not admission, funding, or a supervision commitment. The useful question is: *“Could a software-engineering-led MSc project make a real, publishable contribution to one of your active computational-materials questions?”*

**Fact — high confidence.** The public evidence supports a conversation about DFT/QE, MD/LAMMPS, surface and energy materials, HPC, and materials-industry work: [public QE course](https://acikders.ulakbim.gov.tr/course/view.php?id=35&lang=en), [graduate simulations course](https://catalog2.metu.edu.tr/course/PHYS518/2300518), [2024 AIMD study](https://doi.org/10.1021/acsaem.3c03235), [2024 LAMMPS study](https://doi.org/10.3390/lubricants12020046), and [2025 Şişecam EuroCC proof of concept](https://eurocc.truba.gov.tr/?page_id=9494).

**Unknown.** No public source tells us which of these strands will be active, funded, or open to a new MSc student. Do not arrive with a project presented as an assumed vacancy.

## Ten-minute pre-meeting brief

1. **One sentence of fit.** “I build durable software systems and want to apply that skill to reproducible computational materials—especially DFT/MD campaign provenance, validation, and analysis.”
2. **One paper-specific observation.** The 2024 methane-pyrolysis study used event-by-event AIMD analysis, not only static barriers; ask whether its planned ML-assisted follow-on needs a robust data/trajectory layer. [Paper](https://doi.org/10.1021/acsaem.3c03235)
3. **One software-specific observation.** The 2024 tribology paper exposes a fully parameterized LAMMPS protocol. Ask whether simulation inputs, convergence records, and analysis outputs are presently organized for reuse across students. [Paper](https://doi.org/10.3390/lubricants12020046)
4. **One current-environment observation.** The active EUROCC3 record and completed Şişecam proof of concept make it reasonable to ask about TRUBA workflows, collaboration boundaries, and industry-IP constraints. [METU project record](https://ak.metu.edu.tr/tr/node/15) [EuroCC PoC](https://eurocc.truba.gov.tr/?page_id=9494)
5. **One bounded offer.** “I can build a small, documented, testable artifact around a real physical question; I do not want to build a generic platform detached from a thesis result.”

## Read before contacting

Read these in order; do not skim twenty abstracts.

1. [2024 methane-pyrolysis AIMD paper](https://doi.org/10.1021/acsaem.3c03235): understand the event classification, the VASP/AIMD protocol, its stated ML-assisted outlook, and TRUBA acknowledgement.
2. [2024 graphene/Au LAMMPS paper](https://doi.org/10.3390/lubricants12020046): understand the model assumptions, force fields, finite-temperature protocol, and why reproducibility needs more than one input file.
3. [2023 Pt/Au Quantum ESPRESSO paper](https://doi.org/10.3390/molecules28237928): understand a tractable reaction-pathway calculation and its documented computational choices.
4. [QE course](https://acikders.ulakbim.gov.tr/course/view.php?id=35&lang=en): work through enough of the hands-on material to use the vocabulary accurately.
5. [EuroCC/Şişecam proof of concept](https://eurocc.truba.gov.tr/?page_id=9494): prepare a neutral question about whether a student-facing, non-confidential analogue could be useful.

The fuller annotated list is in [reading-list.md](reading-list.md).

## Five thesis concepts to offer as hypotheses, not proposals to impose

| Concept | A real research question it could serve | Software contribution | Minimum viability evidence to request | Boundary / risk |
| --- | --- | --- | --- | --- |
| 1. **Provenance-first DFT/MD campaign layer** | Can an experiment/simulation campaign be made auditable across structures, parameters, software versions, compute runs, and derived figures? | A schema-backed run manifest, validators, immutable run IDs, and automatically generated methods tables for a *small active project*. | One active system, permitted data, and agreement that provenance is assessed as thesis work. | Avoid becoming a generic lab-management product; data may be confidential. |
| 2. **Convergence and uncertainty harness for surface calculations** | Which conclusions in a selected adsorption/reaction study are robust to cutoff, k-point, slab, vacuum, smearing, and functional choices? | Reproducible sweep specification, result parser, regression tests, and uncertainty report for QE first; VASP only if licensed. | A narrow target system and accepted convergence criteria from the advisor. | VASP licensing and compute budgets; do not promise cross-code equivalence. |
| 3. **AIMD trajectory/event analysis for molten-alloy chemistry** | Can dissociation events and local descriptors be classified reproducibly enough to support later screening? | Data model and analysis pipeline for trajectories/events, with traceable feature calculations and benchmarked labels. | Whether the 2024 molten-metal line is still active, and whether trajectories can be shared. [Paper context](https://doi.org/10.1021/acsaem.3c03235) | The paper’s ML outlook is future work, not confirmation of an available ML thesis. |
| 4. **Reproducible LAMMPS benchmark for 2D interfaces or nanocomposites** | Do force-field/model choices change a selected friction, mechanical, or nanocomposite result enough to affect interpretation? | Container/environment specification where feasible, input validation, analysis notebooks/scripts, and a transparent benchmark report. | An advisor-approved observable and permitted force-field/data choices. [LAMMPS paper](https://doi.org/10.3390/lubricants12020046) | A benchmark alone is not a thesis unless it answers a scientific question. |
| 5. **Computational screening record for glass/interface chemistry** | Can candidate surface/passivation/precursor calculations be organized into a decision-ready, reproducible screening set? | A small domain ontology, provenance-aware results store, and evidence-to-figure pipeline. | Confirmation that a non-confidential version of the current materials-discovery work is possible. [EuroCC PoC](https://eurocc.truba.gov.tr/?page_id=9494) | Industry IP may preclude code/data release; do not assume the Şişecam project is a student opening. |

**Interpretation — high confidence.** Concepts 1–4 are the best bridge to the candidate’s profile because they make software quality answer a materials question. Concept 5 has high topical relevance but the greatest IP risk.

## What a good first conversation sounds like

The candidate should be able to say:

> I noticed that your recent work spans both Quantum ESPRESSO/VASP and LAMMPS, and that your public training materials make the computational setup explicit. I am interested in making a small active simulation campaign more reproducible and analyzable—not in building tooling for its own sake. Which live question would benefit from that, and what would count as a publishable scientific result rather than support work?

Then pause. Let the advisor define the science. A concrete reply naming a system, question, data boundary, and expected method is more valuable than a broad encouraging reply.

## Conversation strategy for an in-person visit

### Opening — 60 seconds

> I am a senior software engineer learning the computational-materials foundations needed to contribute responsibly. I am here for advice, not an admission decision. I would like to understand whether a small, software-enabled MSc project could make a real contribution to one of your active DFT/MD questions.

### Research discussion — lead with evidence, not a product

Start from one paper already read in full: the AIMD methane-pyrolysis work, the LAMMPS graphene/Au study, or the QE surface-reaction paper. State one methodological observation and ask which *current* question has an analogous bottleneck. Do not claim that the paper’s future ML note, industry work, or public teaching material is automatically an open student project.

### Explain the software-engineering background

> My value is usually in making complex systems repeatable, testable, and understandable to their next maintainer. In this context I would apply that to a narrowly defined physics question: run metadata, input validation, convergence records, analysis, and a reproducible result—not to a generic platform.

### Introduce Materials Atlas and Research Landscape briefly

> Materials Atlas and Research Landscape are small open projects that taught me to model sources, assumptions, and stable metadata carefully. I do not expect them to become your group’s project. I mention them only because the same habits may help make a simulation campaign easier to reproduce and audit.

If the advisor shows interest, offer a one-page example of a run manifest or data contract. Otherwise move back to the advisor’s active research question immediately.

### Ask for guidance rather than an offer

> What would you recommend I reproduce, read, or build over the next few months to test whether I could contribute meaningfully to one of these directions?

End by seeking one bounded next action—one paper, a small replication, a brief feasibility note, or a later conversation—not a vague promise of supervision.

## Meeting structure (25–30 minutes)

| Minutes | Goal |
| ---: | --- |
| 0–3 | Introduce the target direction and explicitly state that this is a request for research advice, not admission. |
| 3–8 | Discuss one paper-specific observation and one current-work observation. |
| 8–16 | Ask which current question could support an MSc-sized, code-plus-science contribution. |
| 16–23 | Test capacity, co-supervision, compute/data/IP, authorship, and whether code can be credited. |
| 23–30 | Agree on one small follow-up: a paper, mini-task, feasibility note, or referral. Do not seek a vague promise. |

## Bring / do not bring

Bring a one-page technical brief with: two relevant public projects (Materials Atlas and Research Landscape), a link to a small well-documented code sample, a diagram of the proposed evidence/provenance layer, and one paragraph each on QE/LAMMPS learning already completed.

Do not bring a long portfolio, a ranking report about the advisor, an admission ultimatum, a speculative claim that the group is “AI-driven,” or a request for confidential data before a project scope exists.

## Hard gates after the meeting

Proceed only if all or almost all answers are affirmative:

- There is a live, MSc-sized research question—not just a desire for cleaner code.
- A software artifact is named in the thesis plan and has authorship/assessment expectations.
- The advisor or a named co-supervisor owns the physics/materials question.
- Access to suitable compute/software/data is realistic.
- IP, data sharing, and public-release expectations are clear before implementation.
- The expected supervision cadence and student capacity fit the applicant’s experience level.

If these are not met, the conversation can still be valuable research advice, but it is not yet an application target.
