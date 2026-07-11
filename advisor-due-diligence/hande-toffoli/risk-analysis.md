---
report_type: advisor-due-diligence-risk-analysis
status: evidence-reviewed
evidence_window: public sources accessed 2026-07-11
confidence: mixed
---

# Risk analysis — Hande Toffoli

This is a fit-and-evidence analysis, not an evaluation of a person. A “red flag” below means a decision-relevant unknown, mismatch, or constraint—not misconduct or a negative conclusion.

## Green flags

| Signal | Evidence | Why it matters to this candidate | Confidence |
| --- | --- | --- | --- |
| Current METU Physics appointment | [Faculty directory](https://phys.metu.edu.tr/en/faculty) | Establishes a current, contactable academic home. | High |
| Direct DFT/QE teaching | [TÜBİTAK-ULAKBİM course](https://acikders.ulakbim.gov.tr/course/view.php?id=35&lang=en) | Supports a concrete overlap with open scientific software, Linux, and HPC basics. | High |
| Demonstrated LAMMPS/MD practice | [2024 full paper](https://doi.org/10.3390/lubricants12020046) and [TRUBA materials](https://indico.truba.gov.tr/event/6/timetable/?view=standard_numbered) | Stronger evidence than a generic “computational” label; it exposes workflow details. | High |
| Demonstrated DFT/AIMD/HPC practice | [2024 ACS article](https://doi.org/10.1021/acsaem.3c03235) | Aligns with materials simulations, scientific computing, model/data pipelines, and TRUBA. | High |
| Current European HPC connection | [EUROCC3 record](https://ak.metu.edu.tr/tr/node/15) | Provides a current infrastructure/network signal, not a guarantee of student access. | High |
| Industry-facing computational materials work | [Şişecam EuroCC PoC](https://eurocc.truba.gov.tr/?page_id=9494) | Indicates potential for real problems and practical materials-discovery workflows. | Medium/high |
| Supervision history | [AVESIS aggregate](https://avesis.metu.edu.tr/ustunel) and [2020 MSc example](https://avesis.metu.edu.tr/yonetilen-tez/4474c474-899a-47ca-9311-023bc405d9e8/mos2-au111-yuzeyinin-baslangictan-itibaren-nanotribolojik-ozelliklerinin-incelenmesi) | Supports that computational-materials MSc supervision has occurred. | High |
| International research connection | [2024 ACS author affiliations](https://doi.org/10.1021/acsaem.3c03235) include a Trieste/CNR coauthor; [EuroCC3](https://ak.metu.edu.tr/tr/node/15) is a current European programme. | Gives real collaboration/infrastructure evidence without promising placement outcomes. | High |

## Red flags / open risks and mitigations

| Risk | Evidence status | Why it could matter | Mitigation / decision test |
| --- | --- | --- | --- |
| **Software may be auxiliary rather than thesis-valued.** | **Unknown.** Papers disclose software use, but no source defines credit for reusable code, tests, or data infrastructure. | Candidate could become the group’s informal developer without a defensible thesis contribution. | Obtain a one-paragraph project scope naming the scientific claim, software deliverable, authorship expectation, and review criteria. |
| **Scientific Python/ASE/pymatgen/workflow automation are unverified.** | **Unknown.** QE, VASP, LAMMPS, Packmol, OVITO, and XCrySDen are documented; Python/RSE tooling is not. | The candidate’s strongest experience may not match daily group practice. | Ask tool-by-tool; propose a minimal bridge, not a forced migration. |
| **No advisor-owned public code repository was verified.** | **Unknown.** Open courses and some open-access papers are visible, but code-release policy is not. | Open-source ambitions may conflict with normal lab/IP constraints. | Ask what can be released; accept reduced/synthetic public artifacts if the science allows it. |
| **Active MSc capacity is not public.** | **Unknown.** Current appointment and past supervision do not establish availability. | A strong thematic fit may still have no place or budget. | Ask early and explicitly; do not interpret a polite reply as a commitment. |
| **Industry collaboration may constrain publication/release.** | **Fact — medium/high.** The 2025 Şişecam PoC is industry-facing. [EuroCC](https://eurocc.truba.gov.tr/?page_id=9494) | Data/code could be confidential or delayed. | Ask for a non-confidential thesis analogue, IP ownership, thesis embargo rules, and release approval process. |
| **VASP can add licensing/access friction.** | **Fact — high** that VASP appears in the 2024 AIMD methods. [Paper](https://doi.org/10.1021/acsaem.3c03235) **Unknown** whether a new student has access. | It affects reproducibility and onboarding. | Prefer a QE-first subproject or confirm institutional access and permitted environments. |
| **Physics-first framing may be a curricular transition.** | **Fact — high** that the appointment/course home is Physics. [Directory](https://phys.metu.edu.tr/en/faculty) [PHYS518](https://catalog2.metu.edu.tr/course/PHYS518/2300518) | A senior SWE may need a deliberate on-ramp in quantum/materials fundamentals. | Agree on a 6–8 week preparation plan with a small reproducible exercise. |
| **AI-for-materials is not yet a demonstrated core line.** | **Fact — high** that one paper presents ML assistance as future work, not current established output. [Paper](https://doi.org/10.1021/acsaem.3c03235) | Avoid choosing this option only for an AI label. | Anchor the thesis in simulation science first; treat ML as an optional extension. |
| **Current group composition/outcomes are opaque.** | **Unknown.** No verified current student roster or placement history was found. | Team dynamics and mentoring fit cannot be inferred from publications. | Ask for a voluntary student conversation, supervision cadence, and examples of MSc outcomes. |

## SWOT for this applicant

| Strengths | Weaknesses |
| --- | --- |
| Direct evidence for DFT, QE, LAMMPS, VASP, HPC, surfaces/energy materials, open teaching, and a current European HPC programme. | No direct public evidence that research software engineering, Python ecosystems, automation, GitHub, or open source are central group outputs. |
| Candidate can contribute software architecture, data modeling, validation, reproducibility, documentation, and workflow reliability to visible simulation practices. | Candidate must bridge Physics/Materials theory and prove it through a small scientific result, not just architecture skill. |

| Opportunities | Threats |
| --- | --- |
| Define a narrow, publishable science-plus-software thesis: convergence evidence, AIMD trajectory analysis, LAMMPS benchmarking, or provenance-aware campaign design. | Confidential industrial work, no intake capacity, or unclear authorship/code ownership could make an otherwise strong thematic fit impractical. |
| Build an evidence-rich portfolio for future European doctoral applications through transparent methods, a paper-quality research artifact, and documented compute practice. | A broad platform project could drift away from a thesis; an “AI” pitch could outrun the documented research evidence. |

## Risk-adjusted recommendation

**Interpretation — medium/high confidence.** The evidence supports a meeting because the upside is unusually concrete for computational materials plus scientific computing. The key risk is not lack of relevant science; it is whether the candidate’s software contribution will be recognized as research, scoped to a live project, and compatible with data/IP rules. This is a manageable risk only if the first meeting produces clear answers to the five hard gates in [meeting-preparation.md](meeting-preparation.md).
