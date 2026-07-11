---
report_type: advisor-due-diligence-meeting-questions
status: evidence-reviewed
evidence_window: public sources accessed 2026-07-11
confidence: mixed
---

# Meeting questions — Hande Toffoli

Use these selectively. They are designed to replace public-record unknowns with direct answers, not to interrogate the advisor.

**Fact — high confidence.** Current sources establish DFT/MD/HPC activity and past supervision, but not an opening or a software-first thesis policy. [METU faculty directory](https://phys.metu.edu.tr/en/faculty) [AVESIS profile](https://avesis.metu.edu.tr/ustunel) **Interpretation — high confidence.** A short, focused question set is the best way to assess fit. **Unknown — high confidence in the limitation:** only the advisor can answer these current-state questions.

## Start with scope

1. I am seeking research advice, not asking for an admission decision today. Given my software architecture background and current move into computational materials, where would you see a credible entry point?
2. Which one or two questions are actively important in your group this year, rather than merely interesting directions from past papers?
3. Would an MSc student realistically have room to make both a scientific and a software/reproducibility contribution on one of them?
4. What would a successful thesis result look like at the end: a physical conclusion, a method, a dataset, a paper, a software artifact, or some combination?

## Establish the science before the tooling

5. Is there a current problem in surface chemistry, molten-alloy catalysis, 2D interfaces, hydrogen materials, or glass/interface modelling that needs better simulation workflow support?
6. For that problem, what is the narrowest scientifically defensible starting system and observable?
7. What assumptions are the highest-risk in the existing calculation: functional, pseudopotential, slab/cell, force field, temperature/ensemble, convergence, or analysis?
8. Is a cross-code or convergence study scientifically useful, or would it be a distraction from the key physics?
9. The 2024 methane-pyrolysis article says future work may integrate ML-assisted techniques. Is that line active, and if so, what data and labels exist now? [Paper](https://doi.org/10.1021/acsaem.3c03235)
10. Is there an appropriate non-confidential analogue of the glass-coating or industry-facing work that a student could study? [EuroCC record](https://eurocc.truba.gov.tr/?page_id=9494)

## Test whether software work will be first-class research

11. Would a versioned, tested workflow/data-provenance layer be part of the evaluated thesis contribution, or only internal support?
12. How do you currently capture calculation inputs, software versions, pseudopotentials/force fields, queue settings, and the code that creates figures?
13. Would you welcome a small schema for simulation runs and results that produces the methods tables/figures automatically?
14. Which tools are actually used now: Quantum ESPRESSO, VASP, LAMMPS, Packmol, OVITO, Python, ASE, pymatgen, notebooks, workflow managers, Git, containers?
15. Is there an existing repository or data location that a student should extend rather than replacing?
16. What tests or reference cases would convince you that an analysis pipeline is scientifically trustworthy?
17. Could code, input files, and derived data be released publicly? If not, what can be released as a clean, synthetic, or reduced example?

## Compute, data, and compliance

18. Which compute resources would the thesis use—local systems, METU systems, TRUBA, or an external project allocation?
19. Are there access, onboarding, quota, VASP-license, security, or export-control constraints?
20. Who owns the raw trajectories, input decks, scripts, and downstream datasets?
21. Does an industry collaboration impose an NDA, embargo, approval, or IP rule that affects thesis writing or open-source release?
22. What timeline should be assumed for a first reproducible result, a scientific result, and a manuscript?

## Supervision and team shape

23. Are you considering new MSc students for the relevant intake, and what prerequisite gaps would need to be closed first?
24. Who would be the day-to-day technical mentor for the physical modelling and for the software work?
25. Would a co-supervisor from materials, chemical engineering, or computer engineering strengthen this project? Who might that be?
26. How often do you normally review simulation choices, code, results, and writing with MSc students?
27. What are the expectations for independent learning, group collaboration, documentation, and research communication?
28. May I speak with a current or recent student about the working process, if that is appropriate and voluntary?

## Authorship, outcome, and international path

29. How are authorship and credit usually assigned when a student builds reusable analysis/software that enables a group paper?
30. What student outcomes or collaboration paths have helped people move toward international PhD environments? What would you recommend building during an MSc for that goal?

## The five answers that determine the decision

Record the answer verbatim to these five:

1. **Live problem:** What exact materials question would I work on?
2. **Scientific deliverable:** What result would make it a thesis rather than tooling?
3. **Software status:** Is the artifact explicitly credited, reviewed, and permitted to be released?
4. **Supervision/capacity:** Who mentors what, and is there a slot?
5. **Constraints:** What compute, license, data, and IP boundaries apply?

No current public source answers all five. That is why a good conversation is necessary.

## Questions not to ask in the first meeting

These questions either turn a research conversation into an admissions transaction or ask the advisor to promise facts that are not yet knowable.

| Avoid | Why it weakens the conversation | Better move |
| --- | --- | --- |
| “Will you admit me / fund me?” | It asks for a formal decision before scientific fit and programme process are understood. | Ask whether a short research-direction conversation and a later formal application would be appropriate. |
| “Can you guarantee a PhD at KTH, Chalmers, ETH, EPFL, or TU Delft?” | No responsible advisor can guarantee another institution’s decision. | Ask what skills, outputs, collaborations, and references a strong MSc should build for international doctoral applications. |
| “Can I build Materials Atlas as my thesis?” | It makes the candidate’s product, rather than the advisor’s scientific question, the centre of the meeting. | Ask whether a small provenance/data pattern from it would solve a specific active simulation problem. |
| “May I have the industry data/code?” | It assumes access and may create unnecessary IP discomfort. | Ask whether a non-confidential student-sized analogue exists and what release boundaries apply. |
| “Do you use Python / GitHub?” | A binary tooling question reveals little about the actual research workflow. | Ask which tools, data locations, scripts, checks, and handoffs are used on the candidate project. |
| “Can I get a recommendation letter after the MSc?” | It requests a future favor before any work relationship exists. | Ask how students normally develop publishable work, presentations, and references. |
