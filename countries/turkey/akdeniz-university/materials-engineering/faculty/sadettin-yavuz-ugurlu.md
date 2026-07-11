---
report_type: advisor-compatibility-pilot
advisor_id: TR-AKU-MSE-ADV-005
status: reviewed
evidence_window: public sources accessed 2026-07-11
confidence: high
---

# Sadettin Yavuz Uğurlu — compatibility dossier

## Identity, status, and evidence boundary

Uğurlu is listed as a current Assistant Professor/teaching faculty member in Materials Science and Engineering on the Engineering Faculty roster updated 2026-06-30. AVESIS gives `syavuzugurlu@akdeniz.edu.tr`, ORCID, publication metrics, and a Computer Science PhD at Birmingham; the Birmingham profile independently confirms the ML virtual-screening PhD identity. The Graduate School criteria establish faculty eligibility in principle for early MSc supervision; actual capacity and programme allocation still require confirmation. [B02a](../../bibliography.md#institutional-and-department-sources) [B27](../../bibliography.md#materials-science-and-engineering--primary-profiles-and-selected-publications)

## Research, publication, and technical review

The accessible 2024–26 publication record is computational chemistry/cheminformatics and ML: docking/virtual screening, prodrug prediction, interpretable molecular-property modelling, molecular DFT-related work, and hybrid 2D/3D dipole-moment prediction. The CoBDock and MEGA-PROTAC/Prodrug-ML/Dipole workflows publicly evidence Python-oriented scientific pipelines, including RDKit-style descriptors/fingerprints, ML, molecular/docking tools, reusable environments, test inputs, and published repositories. [B27](../../bibliography.md#materials-science-and-engineering--primary-profiles-and-selected-publications)

The decisive target-specific evidence is the public `coating_motifs_ml` repository, which names Uğurlu, Emre Bal, and Muhammet Karabaş and implements motif-aware hardness prediction for YbSi–Mullite–Si environmental-barrier coatings. Its README documents Python, boosted-tree models, unseen-motif tests, SHAP, and graph analysis. It is a public research repository/associated study, **not** a verified peer-reviewed materials article: raw data are withheld/on request and no standard license, CI, or lockfile was found. [B27](../../bibliography.md#materials-science-and-engineering--primary-profiles-and-selected-publications)

## Software culture and computational-materials proximity

| Topic | Evidence-backed assessment |
| --- | --- |
| Python/scientific software | Directly supported by public repositories and documented pipelines. [B27](../../bibliography.md#materials-science-and-engineering--primary-profiles-and-selected-publications) |
| Reproducibility | Stronger than other reviewed candidates: code, environment/setup details, inputs, and leakage controls are publicly described. |
| ML/cheminformatics | Directly supported by published work and code. |
| Materials ML | Direct coatings-hardness repository with an MSE collaborator. |
| DFT/MD/CALPHAD/ASE/pymatgen | Molecular/DFT-adjacent evidence exists; no reviewed source establishes bulk solid-state DFT, MD, CALPHAD, ASE, or pymatgen practice. |

## Mentoring, research style, compatibility, and SWOT

No public thesis-supervision history was found, so outcomes and student load are **unknown**. Cross-department bioinformatics teaching is a positive teaching signal but not a substitute for supervision evidence. [B27](../../bibliography.md#materials-science-and-engineering--primary-profiles-and-selected-publications)

**Interpretation:** Uğurlu is the clearest direct match for the candidate's path: senior software engineering can contribute to durable Python tooling, data provenance, tests, packaging, and reproducible ML; his molecular-ML background plus the Bal co-authored coating project creates a credible bridge into materials informatics. It is not proof of a mature AI-for-materials lab or a ready DFT/MD programme.

| SWOT | Evidence-calibrated assessment |
| --- | --- |
| Strengths | Verified scientific software, reproducibility practices, ML, and a real materials-ML repository. |
| Weaknesses | Early/current MSE appointment and no public supervision record; core papers are molecular/drug-discovery oriented. |
| Opportunities | A formal Uğurlu–Bal co-supervised coatings-data/software thesis. |
| Risks | Data access, IP/license, capacity, and formal supervision arrangement are unconfirmed. |

## Thesis directions and contact strategy

**Proposed realistic theses:** (1) harden `coating_motifs_ml` into a reproducible package with versioned provenance, tests, leakage checks, and uncertainty estimates; (2) extend its motif-generalisation benchmark to a permissible public coating/materials dataset; (3) build a metadata-to-model workflow that joins nanoindentation/processing records with MSE experimental evidence.

Read the CoBDock paper, Prodrug-ML paper, dipole-prediction paper, and inspect the coating repository before contacting. Ask whether the coating study is active; whether raw data and publication rights permit an MSc thesis; whether Emre Bal can co-supervise; and which parts the candidate could own. Avoid assuming solid-state DFT/MD capability. Introduce Materials Atlas as an evidence/provenance/testing layer for materials data—not as a general app. [B27](../../bibliography.md#materials-science-and-engineering--primary-profiles-and-selected-publications)

## Recommendation

**★★★★★ Strongly Recommend, conditional on capacity and co-supervision confirmation — high confidence.** This is the best evidenced first contact and primary trajectory fit in the pilot.
