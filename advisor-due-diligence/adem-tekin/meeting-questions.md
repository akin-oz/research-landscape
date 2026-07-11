---
report_type: advisor-meeting-questions
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: high
---

# Questions for a meeting with Adem Tekin

These are research questions designed to resolve documented unknowns. They are not an interrogation script. Choose 6–8 based on the direction the conversation takes; listen to the answer and ask one follow-up.

## Highest-information questions

### 1. Research direction and problem choice

1. “Among PNcsp+, phase-map exceptions, binary compounds, and perovskite screening, which problem is scientifically most urgent for a new student to work on now?”
2. “Where does the present workflow fail in a way that could change a materials conclusion—not just make the code inconvenient?”
3. “For complex or multicomponent systems, what do you regard as the decisive limitation: prototype coverage, data quality, ML-potential ranking, relaxation cost, or physical validation?”
4. “How do you decide that a predicted structure is a publishable candidate rather than only a useful hypothesis?”
5. “What outcome would make you say that a software-heavy MSc thesis made a genuine scientific contribution?”

**Why these questions are grounded:** public projects explicitly concern PNcsp+ development, complex systems, phase-map exceptions, LLM crystal generation, and binary-compound design. [ITU projects](https://research.itu.edu.tr/en/persons/tekinad/)

### 2. Software as research

6. “PNcsp+ already exposes database choice, ML calculator choice, optional relaxation, and candidate checks. Which of those interfaces is scientifically fragile or currently hardest to reproduce?”
7. “Would a project that adds benchmark reproducibility, test coverage, provenance records, and a clear DFT escalation policy be useful to the group? What new scientific analysis would it need to include?”
8. “What coding standards, review practices, or repository conventions do students use in the group today?”
9. “Is the public code intended for outside contributors? If so, how are licensing, authorship, maintainership, and release decisions handled?”
10. “Which data sources can a student reliably use and redistribute—OQMD, Materials Project, MPDS, group-generated data—and what restrictions matter?”
11. “Which part of a workflow should be exposed as an open artifact, and which part must remain internal because of data, project, or partner constraints?”

**Why these questions matter:** PNcsp+ is public Python code and is labelled as under active development; the public tree does not establish a license, release, CI, test, or governance policy. Those are facts to clarify, not assumptions to criticize. [PNcsp+ README](https://github.com/tccdem/PNcsp_Plus) · [public tree](https://api.github.com/repos/tccdem/PNcsp_Plus/git/trees/main?recursive=1)

### 3. Validation and scientific rigor

12. “In the perovskite screen, what were the most important differences between ML predictions and later DFT checks, and what is the next validation step?”
13. “Would you prefer uncertainty/calibration work, a benchmark study, or a direct new-chemistry application? Why?”
14. “What fraction of a thesis should be spent on method validation versus a materials discovery application?”
15. “Who would review the DFT, crystallographic, and materials-science parts if the student’s original strength is software architecture?”
16. “Could an experimental partner or independent calculation serve as a predefined external check for a candidate set?”

**Why these questions are grounded:** the 2025 perovskite paper trains gradient-boosting models on DFT data and DFT-checks 20 selected predicted candidates; it does not claim experimental confirmation of all screening hits. [PCCP full text](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b)

### 4. Mentorship and group operation

17. “How do you usually turn a broad computational question into the first 90-day plan for an MSc student?”
18. “How often do you meet individual MSc and PhD students, and who gives day-to-day feedback on code and simulations?”
19. “Can I speak with one current student and one recent graduate about how a computational project is scoped and reviewed?”
20. “How do you decide first authorship when a student contributes research software, a benchmark, and scientific analysis?”
21. “What are examples of students who began with one topic and successfully changed scope when results contradicted the initial plan?”
22. “What does a successful MSc graduate from your group normally leave with: a paper, code artifact, data set, thesis, or some combination?”

**Why these questions are grounded:** repeated thesis-to-paper paths are positive evidence, but public sources do not reveal cadence, authorship policy, or alumni outcomes. [ITU thesis record](https://akademi.itu.edu.tr/en/tekinad/Thesis) · [UHEM roster](https://uhem.itu.edu.tr/en/our-center/research-groups/theoretical-chemistry-and-computational-design-of-energy-materials)

### 5. Career and international path

23. “For a student aiming eventually at a computational-materials PhD abroad, which skill signal matters most: physics/chemistry depth, a rigorous paper, a maintained research-software artifact, HPC experience, or external collaboration?”
24. “Which international collaborators or schools are most natural for a student working on transparent CSP or materials-data methods today?”
25. “What evidence would you need before writing a strong PhD reference for a student coming from industry?”
26. “Would you recommend an MSc thesis that builds a public, citable software/data artifact, and under what conditions would that strengthen—not dilute—a PhD application?”

**Evidence context:** Germany/Denmark training, Europe-linked collaborators and a Horizon project support a credible international frame, but public records do not establish current placement results or reference practices. [career profile](https://akademi.itu.edu.tr/en/tekinad/Adem-Tekin/) · [PEROSOLAR](https://web.itu.edu.tr/~tekinad/?news=horizon-2020-grant-perosolar)

## Questions to ask only if the conversation is receptive

- “Would a carefully bounded Materials Atlas component—provenance cards for a public benchmark/candidate set—help the group, or should it remain separate?”
- “Would a small reproducibility pull request to PNcsp+ be a sensible pre-MSc trial, and what issue would be most useful?”
- “Would it be useful for me to reproduce one figure/table from PNcsp+ or the perovskite study before we discuss a project?”
- “If I need to close gaps in DFT, Python scientific computing, and crystallography, what order would you recommend?”

## Questions not to ask

Avoid these in the first meeting because they are admission-transactional, premature, or force the advisor to predict facts they cannot responsibly promise.

| Do not ask | Why it weakens the conversation | Better move |
| --- | --- | --- |
| “Can you accept me?” | It turns a research discussion into a binary administrative request before mutual fit is established. | Ask what preparation would demonstrate fit. |
| “Will you guarantee funding/admission/a recommendation?” | These depend on formal processes, future resources, and observed work. | Ask what current projects and funding routes are realistically open, and what milestones are needed. |
| “Can I use your name for KTH/ETH/EPFL?” | It is premature and treats a relationship as a credential. | Ask what research outputs would make a future reference credible. |
| “Can I work remotely and only write code?” | It implies scientific engagement is optional. | Ask which physical/materials validation responsibilities a software-focused student should own. |
| “Can I turn Materials Atlas into my thesis?” | It asks the group to adopt an external product without showing a scientific question. | Offer a small research-aligned provenance/benchmark use case. |
| “What is your h-index / how famous is the group?” | It produces little decision-useful evidence and signals prestige-shopping. | Ask about a current failure mode, project, or student outcome. |
| “How fast can I publish?” | It encourages a quantity frame. | Ask what validates a result and what publication-quality means for the project. |
| “Will I get a paper if I fix the repository?” | Authorship cannot be pre-bartered. | Ask how the group defines scholarly contribution for software. |
| “Can I apply with an industry CV without learning materials science?” | It overvalues prior experience and devalues the disciplinary transition. | State the learning plan and ask for the most important conceptual gaps. |

## A concise sequencing script

1. Start with the research observation: “The PN approach makes the chemical prior unusually interpretable.”
2. Ask one failure-mode question.
3. Describe one software-strength example in non-commercial language.
4. Offer one bounded research hypothesis.
5. Ask about validation and supervision.
6. Ask what to reproduce/read next.
7. End with a request for advice, not a slot.

## Evidence checklist to complete during the meeting

Mark each as **answered / partly answered / not answered** immediately after the conversation.

- [ ] Named current problem and scientific importance
- [ ] Clear source code/data boundary and permissible contribution area
- [ ] Expected validation route
- [ ] Individual and technical mentorship cadence
- [ ] Current student contact offered
- [ ] Authorship / licensing / public-release policy explained
- [ ] Funding and equipment/HPC access described without promises
- [ ] First 90-day learning/reproduction task agreed
- [ ] A follow-up date or decision milestone agreed

If fewer than seven items are answered, schedule a second technical conversation before treating topical fit as a final supervision decision.
