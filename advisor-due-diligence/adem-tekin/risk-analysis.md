---
report_type: advisor-risk-analysis
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: high
---

# Risk analysis — Adem Tekin

## Overall risk posture

**Interpretation — high confidence:** The main risk is not lack of topic fit. It is allowing a strong software/materials intersection to become an ill-defined “make the code better” assignment without a scientific question, validation plan, ownership agreement, and regular technical supervision.

This profile has strong upside and manageable risks **if** those conditions are explicitly agreed. It is not suitable for a candidate who wants a guaranteed, narrowly defined software-engineering role with no commitment to materials theory, DFT/ML validation, or published scientific analysis.

## SWOT

| Dimension | Evidence-led assessment | Confidence |
| --- | --- | --- |
| **Strengths** | Public Python research software (PNcsp/PNcsp+), algorithm papers (FFCASP/NICE-FF), current CSP/ML projects, HPC-linked work, and a graduate course in scientific software are all directly documented. [PNcsp+](https://github.com/tccdem/PNcsp_Plus) · [ITU projects](https://research.itu.edu.tr/en/persons/tekinad/) · [HBM 801](https://ninova.itu.edu.tr/en/courses/institute-of-informatics/13508/hbm-801/form) | High |
| **Strengths** | Research has a credible physical-validation ladder: candidate generation → ML/force-field screening → DFT/relaxation → convex hull/AIMD or property checks. [PNcsp+](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/) · [borohydrides](https://research.itu.edu.tr/en/publications/hydrogen-storage-in-trimetallic-borohydrides-a-crystal-structure-/) | High |
| **Strengths** | Repeat student-thesis-to-paper pathways provide a positive, though incomplete, mentoring signal. [theses](https://akademi.itu.edu.tr/en/tekinad/Thesis) · [Samet Demir profile](https://sametd.github.io/) | Medium/high |
| **Weaknesses** | The public PNcsp+ software presents as active research code rather than a fully evidenced mature RSE product: no visible license/release/test/CI/governance surface in the public tree. [repository](https://github.com/tccdem/PNcsp_Plus) · [tree](https://api.github.com/repos/tccdem/PNcsp_Plus/git/trees/main?recursive=1) | High for the public-repository observation; not evidence about private practice |
| **Weaknesses** | The group spans CSP, energy materials, perovskites, force fields, biomolecular systems and drug delivery. Breadth creates opportunity, but an incoming student can drift from the chosen software/materials intersection. [group scope](https://uhem.itu.edu.tr/en/our-center/research-groups/theoretical-chemistry-and-computational-design-of-energy-materials) | High |
| **Opportunities** | Current PNcsp+, phase-map-exception, LLM crystal-generation and binary-compound projects create a window for reproducibility, benchmarking, provenance, package design and data-quality work that directly serves active science. [ITU projects](https://research.itu.edu.tr/en/persons/tekinad/) | High |
| **Opportunities** | Materials Atlas can become useful as a small provenance/knowledge artifact for a real benchmark or candidate data set, leveraging the group’s OQMD/MP/MPDS-style workflow. [PNcsp+ README](https://github.com/tccdem/PNcsp_Plus) | Medium |
| **Threats** | Database access, version drift, licensing and HPC configuration can undermine reproducibility and public artifact release. PNcsp+ itself documents local OQMD dependence and optional external data sources. [README](https://github.com/tccdem/PNcsp_Plus) | High |
| **Threats** | 2025–26 BAP project end dates do not establish funding beyond those dates; external grants and student allocation are not publicly specified. [ITU projects](https://research.itu.edu.tr/en/persons/tekinad/) | Medium/high |

## Green flags

### 1. A real method-development record

**Fact:** FFCASP is a published massively parallel CSP algorithm; PNcsp/PNcsp+ are public implementations; NICE-FF builds a parameterisation pipeline and integrates it into CSP. [FFCASP](https://doi.org/10.1021/acs.jctc.0c01197) · [PNcsp](https://github.com/tccdem/PNcsp) · [NICE-FF](https://research.itu.edu.tr/en/publications/nice-ff-a-non-empirical-intermolecular-consistent-and-extensible-/)

**Why it is green:** A software engineer can plausibly make a scholarly contribution because tools, not just downstream simulations, are already part of the group’s publication record.

**Confidence:** High.

### 2. Current, specific research momentum

**Fact:** ITU lists 5 active projects including CDBC through 2029 and several 2025–26 projects directly concerned with PNcsp/phase maps/LLM crystal generation. [ITU research profile](https://research.itu.edu.tr/en/persons/tekinad/)

**Why it is green:** The candidate would have concrete conversations to join. The live projects reduce the risk of inventing a thesis around stale interests.

**Confidence:** High for project existence; medium for actual available student slots.

### 3. Evidence of student continuity

**Fact:** The thesis record maps Samet Demir from MSc through PhD work in the group, and the public publication record connects him to FFCASP and later materials work. Gözde İniş Demir and Cem Oran show comparable thesis-to-method-publication continuity. [ITU theses](https://akademi.itu.edu.tr/en/tekinad/Thesis) · [Samet’s profile](https://sametd.github.io/) · [PNcsp+](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/)

**Why it is green:** It is evidence that a student can develop a multi-year computational-method trajectory rather than being confined to a one-off calculation.

**Confidence:** Medium/high; it does not substitute for talking to current/former students.

### 4. HPC and international interfaces

**Fact:** Published studies acknowledge UHEM/TRUBA; Tekin’s profile documents Germany/Denmark research experience, a Horizon project, and international coauthors in recent work. [PCCP study](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b) · [career record](https://akademi.itu.edu.tr/en/tekinad/Adem-Tekin/) · [PNcsp+](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/)

**Why it is green:** The research environment is not isolated from computational infrastructure or international methods communities.

**Confidence:** High for those connections; medium for translating them into future placements.

### 5. A legible gap for a senior engineer

**Fact:** PNcsp+ has public runnable code, data, requirements and examples, but the public software surface lacks visible releases, test directories, CI workflows, governance and licensing. [PNcsp+ repository](https://github.com/tccdem/PNcsp_Plus)

**Why it is green:** The gap is valuable only because it can be connected to scientific questions: benchmark correctness, data provenance, model-selection risk, or publication-reproducibility. A mature engineer can add unusually high leverage.

**Confidence:** High for opportunity; conditional on advisor support for open and maintained outputs.

## Red flags / questions that could reverse the recommendation

### 1. Software may be treated as service work rather than research

**Fact:** Published papers prove that software methods can be scholarly in this group; they do not specify how a new student’s maintenance or infrastructure work is credited. [FFCASP](https://doi.org/10.1021/acs.jctc.0c01197) · [PNcsp+](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/)

**Risk interpretation — high confidence:** If the advisor cannot name a scientific hypothesis, evaluation metric, and authorship path for the software work, decline a software-first thesis scope. A refactor without a research result is not enough for the candidate’s long-term goal.

**Test in meeting:** Ask what would count as a publishable scientific result from a benchmark/provenance/orchestration project and who would technically review it.

### 2. Public repository maturity may not support an open thesis artifact

**Fact:** PNcsp+ declares active development and invites bugs, but its public tree does not visibly establish licensing, release, CI, test or governance practices. [README](https://github.com/tccdem/PNcsp_Plus) · [public tree](https://api.github.com/repos/tccdem/PNcsp_Plus/git/trees/main?recursive=1)

**Risk interpretation — medium/high confidence:** A candidate could inherit hidden technical debt or be unable to release their contribution. This is remediable, but only with an explicit agreement on repository ownership, license, maintainer role, scope, and review process.

**Test in meeting:** Ask whether an external contribution can be accepted, licensed, released and cited; ask whether tests/CI/documentation can be explicit thesis deliverables.

### 3. Data access and reproducibility can become the real bottleneck

**Fact:** PNcsp+ documentation says its default configuration scans a local OQMD instance and supports OQMD/MP/MPDS; the pipeline depends on data availability and model dependencies. [PNcsp+ README](https://github.com/tccdem/PNcsp_Plus)

**Risk interpretation — high confidence:** A thesis could stall on data mirrors, credentials, version changes, source licenses, or HPC environments rather than the scientific question.

**Test in meeting:** Before committing, obtain a minimal reproducible environment, data-access plan, compute allocation path, and a small smoke-test target that can run locally or on shared infrastructure.

### 4. The field transition is substantial

**Fact:** The candidate has strong software experience but needs to develop crystallography, thermodynamics, DFT, materials stability, error analysis and the limits of ML potentials. The group’s publications use these concepts deeply. [PNcsp+](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/) · [borohydrides](https://research.itu.edu.tr/en/publications/hydrogen-storage-in-trimetallic-borohydrides-a-crystal-structure-/)

**Risk interpretation — high confidence:** Senior software experience accelerates engineering judgement but does not replace scientific apprenticeship. A programme that offers no structured domain learning would be a poor fit.

**Test in meeting:** Request a 90-day learning plan, reading/reproduction task, and named person for scientific code review.

### 5. Breadth can cause scope drift

**Fact:** Public group scope includes energy materials, CSP, theoretical chemistry, force fields, molecular dynamics and drug delivery. [group page](https://uhem.itu.edu.tr/en/our-center/research-groups/theoretical-chemistry-and-computational-design-of-energy-materials)

**Risk interpretation — medium confidence:** A project may be redirected to a convenient but less aligned application. The candidate should choose a thesis statement with a non-negotiable core: *transparent/reproducible CSP or materials screening plus physical validation*.

**Test in meeting:** Ask for a one-sentence thesis question, a “not in scope” list, and criteria for saying no to adjacent work.

### 6. Mentoring quality has positive proxies but incomplete direct evidence

**Fact:** Theses and recurring student authorship are public; meeting cadence, student load, conflict handling, alumni locations and student feedback are not. [thesis record](https://akademi.itu.edu.tr/en/tekinad/Thesis)

**Risk interpretation — high confidence:** Do not convert publication continuity into a blanket claim about mentorship quality.

**Test in meeting:** Speak privately with at least one current and one former student. Ask concrete questions about feedback latency, research autonomy, authorship, project changes, and whether software work was recognised.

### 7. Future international PhD leverage is plausible, not guaranteed

**Fact:** Tekin has German and Danish training/postdoctoral experience; recent work has international collaborators and a previous Horizon project. [career profile](https://akademi.itu.edu.tr/en/tekinad/Adem-Tekin/) · [PEROSOLAR](https://web.itu.edu.tr/~tekinad/?news=horizon-2020-grant-perosolar)

**Unknown:** There is no public alumni-placement ledger or public evidence of current reference-writing practice for KTH, Chalmers, ETH, EPFL or TU Delft.

**Risk interpretation — medium confidence:** The environment can help create a strong application, but it will do so only through demonstrable research outputs, domain depth, and credible letters—not by association alone.

## Mitigation plan before any formal application

| Risk | Required mitigation | Evidence of success |
| --- | --- | --- |
| Vague software scope | Write a 1–2 page research note with hypothesis, datasets, baselines, validation and artifact scope. | Advisor can state what scientific question the code answers. |
| No data/compute path | Reproduce one small PNcsp+ or perovskite workflow with documented inputs. | A clean run record that another group member can repeat. |
| Unclear authorship/release | Discuss authorship, license, code ownership, and publication strategy before major implementation. | Written summary from the meeting/email, not a verbal assumption. |
| Insufficient domain preparation | Complete the first reading list and a small DFT/CSP exercise. | Candidate can explain why a predicted structure needs physical validation. |
| Uncertain mentorship fit | Speak to current and former students. | Consistent reports on cadence and project ownership. |
| Scope drift | Define primary thesis question and two explicit exclusions. | A 90-day plan signed off by advisor/student. |

## Decision-triggering red flags

Pause or decline if any of the following occur:

1. The proposed work is “improve the code” with no scientific hypothesis or validation plan.
2. The candidate is asked to make substantial code contributions with no clarity on ownership, authorship, or ability to cite/release the work.
3. No one can provide a reproducible data/compute path for the first milestone.
4. The advisor cannot identify how often the student will receive research and technical feedback.
5. Current/former students independently describe persistent lack of feedback, unclear authorship, or unbounded topic changes.

## Conditional green-light criteria

Proceed if the meeting establishes all of the following:

1. A live group problem—not a speculative side project—needs the proposed software/research work.
2. The work has a measurable physical or methodological validation route.
3. Software artifact, data, paper and thesis contributions are explicitly connected.
4. The candidate can learn domain fundamentals with regular feedback from a named person.
5. The software can be made reusable/open where legally and scientifically appropriate.

**Final interpretation — high confidence:** This is a high-upside opportunity for the specified candidate profile, but it should be chosen as a *research apprenticeship with engineering leverage*, not as an industry-style software job embedded in a lab.
