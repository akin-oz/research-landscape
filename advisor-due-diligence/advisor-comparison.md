---
report_type: advisor-due-diligence-comparison
status: evidence-reviewed
evidence_window: public sources accessed 2026-07-11
confidence: medium
---

# Advisor comparison — evidence-led decision view

## Scope and decision rule

This is a comparison of three named advisors for one applicant profile, not a league table. It privileges a *publishable materials question with an explicit, durable software artifact* over name recognition, raw publication counts, or claims about admission probability.

The relevant question is not whether an advisor has ever used code. It is whether the applicant can own a scientifically necessary software/data/workflow contribution while being mentored into rigorous computational materials research.

| Dimension | Adem Tekin — ITU | Hande Toffoli — METU | Sadettin Yavuz Uğurlu — Akdeniz |
| --- | --- | --- | --- |
| Direct fit to computational materials + AI discovery | **Very strong, high confidence.** Crystal-structure prediction, computational materials design, energy materials, ML screening, and DFT are visible in the current group record and recent papers. | **Very strong for atomistic foundations, high confidence.** The group explicitly uses DFT and classical MD for low-dimensional materials and surfaces; recent outputs connect calculation to catalysis, interfaces, and energy materials. | **Promising but conditional, medium confidence.** The current appointment is in materials engineering and a public coatings-ML repository exists, but the main recent publication stream is cheminformatics/drug discovery rather than solid-state materials discovery. |
| Scientific-software evidence | **Strongest materials-specific evidence, high confidence.** Public PNcsp+ / PNcsp work and FFCASP demonstrate research software tied to the core science. | **Solid software literacy, medium confidence.** Quantum ESPRESSO contribution/training and computation-heavy courses are public; a faculty-owned codebase, CI practice, or Python stack was not verified. | **Strong individual pipeline evidence, high confidence.** Public CoBDock/MEGA-PROTAC repositories and `coating_motifs_ml` demonstrate code-centric methods; group-wide engineering practice remains unverified. |
| Research-environment and supervision signals | **Active and visible, high confidence.** The group page names current PhD/MSc members, alumni, projects, courses, and an open-inquiry route. This supports activity, not capacity for a new student. | **Substantive but date-sensitive, medium/high confidence.** A group-maintained site labels an MSc/PhD cohort and former graduates, while institutional records establish a substantial supervision history and a coherent DFT/MD programme. Neither proves current intake. | **Insufficient public supervision evidence, high confidence in the gap.** No public thesis-outcome record or current lab roster was found in the reviewed evidence. |
| International research-development signal | **Meaningful, medium confidence.** Public funding/collaboration history and alumni destinations indicate international connections, but not a guaranteed pathway to any particular PhD. | **Strongest visible international academic trajectory, high confidence.** Cornell PhD, SISSA postdoctoral training, and the continuing Trieste/METU group relationship are direct facts. | **Meaningful personal network, medium confidence.** Birmingham doctoral training and international coauthorship are visible; a materials-specific placement pathway is not established. |
| Principal decision risk | A software-intensive deliverable could be regarded as support work unless its scientific question, ownership, authorship, and release terms are agreed up front. | The candidate must prove that a software artifact advances a real DFT/MD question; public evidence does not establish a modern open-code workflow. | A material-science thesis, co-supervision, data rights, group capacity, and supervisory track record all need confirmation before this becomes a primary option. |

The sources supporting this table are the linked individual dossiers, especially [Tekin’s group roster](https://web.itu.edu.tr/~tekinad/?page_id=93), [publication record](https://web.itu.edu.tr/~tekinad/?page_id=64), [PNcsp+ article](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/), [Toffoli’s group description](https://www.compmatsci.com/), [current MSc roster](https://www.compmatsci.com/msc-students), [current PhD roster](https://www.compmatsci.com/phd-students), [Uğurlu’s Akdeniz profile](https://avesis.akdeniz.edu.tr/syavuzugurlu), [CoBDock article](https://doi.org/10.1186/s13321-023-00793-x), and [coatings repository](https://github.com/yauz3/coating_motifs_ml).

## Evidence-backed interpretation

### 1. Adem Tekin — recommended first choice

**Facts.** Tekin’s public record brings the candidate’s three desired strands into one research environment: materials computation, crystal-structure prediction/ML, and published software. His group page lists current PhD and MSc members and identifies past members now at Harvard, Purdue, and elsewhere; its teaching list includes scientific computing, computational design of energy materials, and chemoinformatics. The site also records work with MPDS, HORIZON 2020 and TÜBİTAK projects. [Group people](https://web.itu.edu.tr/~tekinad/?page_id=93) · [teaching](https://web.itu.edu.tr/~tekinad/?page_id=106) · [funding](https://web.itu.edu.tr/~tekinad/?page_id=88)

**Interpretation — high confidence.** This is the clearest setting in which a senior software engineer can credibly improve a project rather than be treated as a generic programmer: reproducibility, benchmark design, packaging, orchestration, provenance, and performance all attach naturally to crystal-structure prediction and screening. It is the best single-advisor route for the stated career direction.

**Decision gate.** Before applying, ask whether an MSc student can own a release-quality, testable component of PNcsp+/FFCASP or a related active project, and agree on publication and licensing expectations.

### 2. Hande Toffoli — recommended strongest atomistic-materials alternative

**Facts.** The Computational Materials Science Group explicitly studies atomistic material properties in low-dimensional materials and surfaces using DFT and classical MD. Its group-maintained pages label seven MSc and two PhD members as current, alongside former graduates; this is useful but date-sensitive rather than an official intake record. Toffoli’s public biography identifies a Cornell PhD and SISSA postdoc, and the group retains a Trieste connection. [Group](https://www.compmatsci.com/) · [MSc members](https://www.compmatsci.com/msc-students) · [PhD members](https://www.compmatsci.com/phd-students) · [METU record](https://open.metu.edu.tr/handle/11511/29809)

**Interpretation — high confidence.** Toffoli is the strongest choice if the applicant wants a rigorous DFT/MD apprenticeship and a mature, visible group environment. The right software contribution is not a detached platform: it should make a defined surface, catalysis, tribology, or interface calculation more reproducible, inspectable, and reusable.

**Decision gate.** Ask which active student/project needs a workflow or analysis component, what the actual simulation stack is, and whether a software deliverable can be examined and credited as a thesis contribution.

### 3. Sadettin Yavuz Uğurlu — recommended high-upside, conditional conversation

**Facts.** Uğurlu is a current Akdeniz Materials Science and Engineering faculty member with a Computer Science PhD from Birmingham. Recent work provides unusually direct evidence of code-centric, reproducible cheminformatics and ML pipelines; `coating_motifs_ml` is the key public bridge to materials, but it withholds raw data/on-request and does not by itself demonstrate a mature open materials lab. [Akdeniz profile](https://avesis.akdeniz.edu.tr/syavuzugurlu) · [Birmingham profile](https://www.birmingham.ac.uk/staff/profiles/computer-science/research-student/ugurlu-sadettin-yavuz) · [MEGA-PROTAC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11829001/) · [coatings repository](https://github.com/yauz3/coating_motifs_ml)

**Interpretation — medium confidence.** The applicant’s engineering background may be especially legible to Uğurlu, but the core decision is whether there is an active materials-science problem with data access, a co-supervisor where needed, and a real supervision arrangement. This is a strong exploratory conversation, not yet a risk-equivalent substitute for the two established computational-materials environments.

**Decision gate.** Require affirmative answers about the active materials project, candidate ownership, raw-data/IP access, material-science co-supervision, and MSc capacity before treating it as a primary application.

## Comparative SWOT

| Advisor | Strengths | Weaknesses / unknowns | Opportunity for this candidate | Main risk to control |
| --- | --- | --- | --- | --- |
| Tekin | Direct materials-informatics/software research, active visible group, clear thesis-to-code possibilities. | Exact code-governance, intake, and authorship practice are not public. | Turn a CSP/screening workflow into a reproducible community-grade research artifact. | Software work gets separated from the scientific claim. |
| Toffoli | Deep DFT/MD environment, visible student community, international academic trajectory. | Public GitHub/Python/CI practices not established. | Build a reliable research-data and workflow layer around a rigorous atomistic question. | A software proposal is too broad or not central to the materials result. |
| Uğurlu | Demonstrated ML/repository practice, direct fit to engineering strengths, materials-ML bridge. | Newer materials-facing environment; supervision, data, and group evidence are incomplete. | Co-designed, reproducible materials-ML package and benchmark with an MSE collaborator. | A thesis remains drug-discovery-adjacent or lacks material data/mentoring infrastructure. |

## Provisional ordering

1. **Adem Tekin — first application and first substantive meeting.** *High confidence in fit; medium confidence in current capacity.*
2. **Hande Toffoli — parallel first-round contact and second priority meeting.** *High confidence in atomistic research environment; medium confidence in the precise software role.*
3. **Sadettin Yavuz Uğurlu — targeted due-diligence meeting in the same outreach window.** *High confidence in individual software/ML ability; medium-to-low confidence in the unverified MSc materials-supervision conditions.*

This order should not be used serially: send all three tailored messages during the same first week. It orders attention and meeting preparation, not an instruction to wait for one reply before seeking another.
