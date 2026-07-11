---
report_type: advisor-decision-recommendation
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: high
---

# Decision — whether to pursue Adem Tekin as a supervisor

## Recommendation

**Recommendation — high confidence, conditional:** Contact and visit Prof. Adem Tekin early. I would personally recommend pursuing a serious research conversation and, if the decision gates below are met, an MSc under his supervision. The public evidence makes this an unusually strong fit for a candidate whose goal is to make **scientific software itself** a visible contribution to computational materials research.

**Not a blanket recommendation:** Do not decide solely from topical fit. The MSc recommendation becomes a “yes” only after confirming supervision cadence, a thesis-level scientific question, ownership/authorship, data/compute access, and at least one current/former student reference.

## Evidence-based compatibility matrix

| Dimension | Fact | Applicant-specific interpretation | Confidence |
| --- | --- | --- | --- |
| Computational materials core | Group scope explicitly includes CSP, periodic DFT, energy materials, CO₂ capture/catalysis and global optimization. [UHEM group](https://uhem.itu.edu.tr/en/our-center/research-groups/theoretical-chemistry-and-computational-design-of-energy-materials) | Direct alignment with computational materials science rather than a peripheral application. | High |
| Scientific software | PNcsp/PNcsp+ are public Python research tools; FFCASP and NICE-FF are published method/software contributions. [PNcsp+](https://github.com/tccdem/PNcsp_Plus) · [FFCASP](https://doi.org/10.1021/acs.jctc.0c01197) · [NICE-FF](https://doi.org/10.1063/5.0176641) | An experienced engineer’s skills can be scientifically legible if tied to a hypothesis, benchmark and validation. | High |
| AI for materials discovery | Current PNcsp+ and perovskite work use GNN potentials, ML models and DFT validation; current projects include LLM-assisted crystal generation. [PNcsp+](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/) · [PCCP study](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b) · [ITU projects](https://research.itu.edu.tr/en/persons/tekinad/) | Good fit for principled ML in materials, particularly if the candidate values transparent models and validation over generic AI branding. | High |
| Python and engineering practice | Public repositories are Python-based and courses cover Unix/scripting/Make/Fortran/C and programming. [PNcsp+](https://github.com/tccdem/PNcsp_Plus) · [HBM 801](https://ninova.itu.edu.tr/en/courses/institute-of-informatics/13508/hbm-801/form) | The candidate can contribute immediately while learning scientific Python conventions. | High |
| Mature RSE culture | Public code has documentation and pinned dependencies, but no publicly visible license, release, test, CI or governance surface. [repository](https://github.com/tccdem/PNcsp_Plus) · [public tree](https://api.github.com/repos/tccdem/PNcsp_Plus/git/trees/main?recursive=1) | Strong opportunity, but a risk if the advisor sees quality/maintenance work as non-scholarly. Must be negotiated. | High for public evidence; unknown for private practice |
| Mentorship | Thesis records and repeat student authorship show continuity; public cadence/student feedback/alumni records do not. [theses](https://akademi.itu.edu.tr/en/tekinad/Thesis) · [Samet Demir profile](https://sametd.github.io/) | Promising signal, insufficient alone for a 5–10 year career decision. | Medium/high |
| Research environment | ITU documents 5 active projects and UHEM/TRUBA-linked compute use. [projects](https://research.itu.edu.tr/en/persons/tekinad/) · [PCCP paper](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b) | A viable platform for computational work, subject to a practical access test. | High |
| International path | German/Denmark training, international coauthors and Horizon collaboration are documented. [career profile](https://akademi.itu.edu.tr/en/tekinad/Adem-Tekin/) · [PEROSOLAR](https://web.itu.edu.tr/~tekinad/?news=horizon-2020-grant-perosolar) | Credible network signal; not proof of placements, sponsorship, or references to named schools. | Medium |

## Candidate-specific answers

### Would he value an experienced software engineer?

**Interpretation — high confidence:** Probably, provided the candidate presents software engineering as a means to produce more rigorous and useful science. Public method papers and repositories demonstrate that the group builds computational tools, not only inputs files to external software. [FFCASP](https://doi.org/10.1021/acs.jctc.0c01197) · [PNcsp+](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/)

The most persuasive framing is: *“I want to make the group’s scientific questions more reproducible, testable and scalable, then evaluate whether that changes the materials conclusion.”* The least persuasive framing is: *“I can modernize your codebase.”*

### Would Materials Atlas be valuable?

**Interpretation — medium confidence:** Yes, but only as a small, research-bound infrastructure contribution. PNcsp+ already relies on databases and candidate records; the perovskite workflow moves candidates through explicit filters and validations. A provenance-rich benchmark/candidate card could be useful. [PNcsp+ README](https://github.com/tccdem/PNcsp_Plus) · [PCCP study](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b)

**Boundary:** Materials Atlas should not become the thesis by brand. Offer a concrete module only after the advisor identifies a data/benchmark problem it solves.

### Would Research Landscape be relevant?

**Interpretation — medium confidence:** It is credible portfolio evidence of structured data/evidence design, but it is only indirectly related to computational materials. Mention it once as an example of how the candidate thinks about provenance and human-readable systems; do not ask the advisor to supervise it.

### Would open-source work help the application?

**Interpretation — high confidence:** Yes if it is connected to scientific results, cited software/data, reproducible benchmarks and documented validation. Public code alone is a weaker signal; a small, maintainable contribution tied to a paper-quality evaluation is much stronger. The group’s public PNcsp/PNcsp+ activity gives this a natural home. [PNcsp](https://github.com/tccdem/PNcsp) · [PNcsp+](https://github.com/tccdem/PNcsp_Plus)

**Unknown:** Whether a new contribution can be publicly released or accepted into the group’s repository has not been established. Ask before investing.

## MSc decision

### Would I pursue an MSc under this advisor?

**Yes—conditionally.** The candidate has unusually relevant transferable strengths: software architecture, open-source workflow, automation and data-system thinking. The missing pieces—DFT, crystallography, thermodynamics, physical validation and materials-science judgement—are exactly the skills an MSc should develop.

### Minimum gates before applying

1. **Scientific thesis statement:** one question that cannot be answered solely by software quality (for example, when a CSP rank/escalation policy alters structure-recovery or stability conclusions).
2. **Artifact agreement:** code/data/tests/documentation are named thesis outputs, with ownership and authorship expectations stated.
3. **Validation agreement:** a benchmark plus DFT/physical/literature check is defined before implementation.
4. **Mentorship agreement:** individual and technical-review cadence is stated; one current and one former student can be consulted.
5. **Reproducibility test:** a small existing workflow can be run with documented data/compute access within the first 30 days.

If all five are satisfied, the candidate can enter with a strong comparative advantage. If any of the first three are missing, choose a more clearly scoped advisor/project even if the topic is exciting.

## PhD decision

### Would I pursue a PhD under this advisor?

**Conditional “possibly,” not an automatic yes.** For a PhD, require stronger evidence than an MSc: sustained funding, a coherent multi-paper agenda, demonstrated student outcomes, clear code/research credit, and direct access to collaborators/validation channels.

**Reasoning:** The public trajectory and current projects support a credible PhD environment, but public sources do not establish current student load, placement outcomes or long-term funding beyond specific project dates. A well-executed MSc in this environment could be the best evidence-gathering step; it would let the candidate test the relationship before a four-year commitment.

## International PhD path: KTH, Chalmers, ETH, EPFL, TU Delft

| Question | Evidence-based answer |
| --- | --- |
| Could this MSc strengthen an application to KTH or Chalmers? | **Potentially.** The strongest signal would be a reproducible computational-materials paper/software artifact, DFT/HPC competence, and a detailed reference—not university association alone. Tekin’s DTU experience is relevant context, but public placement evidence is unknown. |
| Could it strengthen an application to ETH or EPFL? | **Potentially, with a high bar.** A published method/benchmark, rigorous physics validation, strong grades and concrete collaboration are more persuasive than generic “AI for materials.” The group’s CSP and method-development work aligns conceptually; no outcome is guaranteed. |
| Could it strengthen an application to TU Delft? | **Potentially.** Materials data, scientific computing and reproducibility can be compelling if tied to a clear materials problem and well-documented artifact. Again, a named placement pipeline is not evidenced. |
| What should the candidate aim to leave with? | One strong research narrative: **transparent candidate generation/selection + reproducible scientific software + validated computational materials result**; ideally a paper, citable code/release where possible, documented data and a specific reference letter. |

**Confidence:** Medium. The prerequisite research signals are real; predictive claims about named-school outcomes would be speculation without applicant record, future opportunities and direct reference evidence.

## 30–90–180 day decision plan

| Timing | Deliverable | Decision test |
| --- | --- | --- |
| Before meeting | Read top 3 papers; prepare one reproducibility/benchmark hypothesis. | Can the candidate speak scientifically, not only as a developer? |
| Meeting + 7 days | Send a one-page summary of the discussed problem and proposed first milestone. | Does the advisor correct/refine it with specific scientific guidance? |
| First 30 days | Reproduce a small published/benchmark result with a run record. | Is the data/compute/software pathway real and supported? |
| First 90 days | Agree on thesis hypothesis, validation route, artifact scope and cadence. | Is the project research-led and bounded? |
| First 180 days | Produce a baseline, failure analysis and written project-review note. | Is mentorship effective and has the candidate gained materials judgement? |

## Final statement

**Opinion, evidence-informed:** If I had this candidate profile, I would take this meeting seriously and would be optimistic about an MSc under Adem Tekin—but I would make the decision only after a technically specific conversation and student references. The highest-value version of the relationship is one where the candidate helps turn active CSP/materials workflows into transparent, validated, reusable scientific software **and** develops enough materials-science depth to own the scientific claims.
