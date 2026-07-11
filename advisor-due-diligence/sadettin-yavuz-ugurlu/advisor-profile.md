---
report_type: advisor-due-diligence-profile
advisor_id: TR-AKU-MSE-ADV-005
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: medium
---

# Sadettin Yavuz Uğurlu — advisor profile and publication audit

## Executive assessment

**Fact — high confidence.** Uğurlu is publicly listed in Akdeniz University's
Materials Science and Engineering unit. His public education record shows a
Bioengineering BSc at Marmara University (2010–2015), a UK MSc (2017–2019), and
a Computer Science PhD at the University of Birmingham (2019–2025). Birmingham
identifies the doctoral project as *Machine-learning applications on Virtual
Screening*, supervised by Shan He and Jinming Duan. [Akdeniz roster](https://muhendislik.akdeniz.edu.tr/tr/akademik_personel-2472)
[AVESIS education](https://avesis.akdeniz.edu.tr/syavuzugurlu/egitim)
[Birmingham doctoral profile](https://www.birmingham.ac.uk/staff/profiles/computer-science/research-student/ugurlu-sadettin-yavuz)

**Interpretation — medium confidence.** This trajectory is not the usual
solid-state-computational-materials path. It is a credible bridge from
bioengineering and molecular modelling to applied ML, scientific pipelines, and
now an MSE appointment. That makes him potentially excellent for an applicant
whose differentiator is reliable research software, but it makes explicit
materials-domain co-supervision and experimental/data ownership more important
than they would be in an established DFT/MD materials group.

## Research evolution

| Period | Evidence-backed development | What it means for this candidate |
| --- | --- | --- |
| 2019–2025 | **Fact:** Birmingham PhD in virtual screening/ML. [Birmingham profile](https://www.birmingham.ac.uk/staff/profiles/computer-science/research-student/ugurlu-sadettin-yavuz) | Direct training in computational workflows and ML evaluation rather than an exclusively wet-lab or experimental route. |
| 2024 | **Fact:** CoBDock and MEF-AlloSite are open peer-reviewed method papers, with public code. [CoBDock](https://doi.org/10.1186/s13321-023-00793-x) [MEF-AlloSite](https://doi.org/10.1186/s13321-024-00882-5) | Evidence of designing end-to-end scientific pipelines, not merely applying a single black-box model. |
| 2025–2026 | **Fact:** the publication list shifts toward interpretable molecular-property models, PROTAC/docking workflows, safety-oriented target ranking, and experimental dipole prediction. [AVESIS publication list](https://avesis.akdeniz.edu.tr/syavuzugurlu/yayinlar) | Current methodological centre of gravity is cheminformatics, model selection, rank aggregation, and reproducible ML. |
| 2026 materials bridge | **Fact:** a public repository co-credits Uğurlu, Emre Bal, and Muhammet Karabaş on ML for hardness in YbSi–mullite–Si environmental-barrier coatings. [Coating repository](https://github.com/yauz3/coating_motifs_ml) | This is the strongest direct entry point from his work into materials informatics, but it is a code/manuscript artefact—not a verified peer-reviewed materials paper or a verified active MSc project. |

### Research philosophy visible in methods

**Fact — high confidence.** The accessible papers and repositories repeatedly use
feature engineering, explicit train/test separation, feature selection, ensemble
or rank aggregation, validation against external/held-out cases, and
interpretable outputs (e.g., RuleFit or SHAP). CoBDock combines independent
docking/cavity signals rather than trusting a single method; MEF-AlloSite tackles
many features with a small training set through feature selection; the dipole
study contextualises performance against a similarity-conditioned noise estimate.
[CoBDock full paper](https://doi.org/10.1186/s13321-023-00793-x)
[MEF-AlloSite full paper](https://doi.org/10.1186/s13321-024-00882-5)
[Dipole full paper](https://doi.org/10.1186/s13321-026-01215-4)

**Interpretation — medium confidence.** The recurring pattern is pragmatic,
benchmark-conscious scientific ML rather than end-to-end deep learning for its
own sake. That is a good philosophical match for a senior engineer who cares
about provenance, leakage prevention, and maintainable workflows.

## Publication evidence audit

The AVESIS list exposes **14 journal articles plus two full-text conference
proceedings** at the review date—fewer than the requested ~20, so every visible
record is included below. “Read level” is deliberately precise: it distinguishes
open full-text review from publisher metadata/abstract plus public code. It does
not claim access to unavailable full text.

| # | Work | Read level and primary source | Actual scientific contribution / boundary |
| --- | --- | --- | --- |
| 1 | **Prodrug-ML** (2026) | Publisher record and [public pipeline](https://github.com/yauz3/prodrug-ml) reviewed. [DOI](https://doi.org/10.1007/s10822-025-00725-x) | Builds prodrug-likeness modelling around negative-decoy construction rather than treating the negative class as given: overlap control, early untouched test isolation, hardness/ratio checks, source/domain-bias checks, and cross-decoy validation. The public code supports the workflow claim; positive data are not redistributed, so numerical results are not independently reproducible from the repository. |
| 2 | **Experimental dipole moment prediction** (2026) | Open paper and [public code](https://github.com/yauz3/dipole_moment) reviewed. [DOI](https://doi.org/10.1186/s13321-026-01215-4) | Progressively fuses multi-view 2D fingerprints, descriptor/shape features and a conformer-derived EGNN-style 3D graph model; its important scientific move is judging error against twin-pair dispersion in a noisy experimental collection rather than presenting a raw score alone. The paper reports test R² 0.844/MAE 0.399 D; those reported values were not re-run here. |
| 3 | **De-TarDis** (2026) | Publisher record and [repository](https://github.com/yauz3/De-TarDis) reviewed. [DOI](https://doi.org/10.7240/jeps.1834505) | Organises safety-relevant “do-not-hit” targets from distinct evidence lists and reconciles their rankings with reciprocal-rank fusion. This is a data-integration/ranking contribution, not a new materials model. Repository documentation still contains template-like sections, so dataset completeness and release stability require confirmation. |
| 4 | **MEGA-PROTAC** (2025) | Open full text and [public code](https://github.com/yauz3/MEGA-PROTAC) reviewed. [DOI](https://doi.org/10.1038/s41598-024-83558-2) | Converts a huge ternary-complex search into sequential filtering: MEGADOCK seeds, distance and protein-interface filters, multiple scores, rank aggregation, clustering, then local docking. The paper openly discusses rigid-docking and known-pose limitations; that methodological candour matters more than headline comparison numbers. |
| 5 | **CoBdock-2** (2025) | Publisher method record and [public code](https://github.com/yauz3/cobdock-2) reviewed; full publisher article was not openly available. [DOI](https://doi.org/10.1007/s10822-025-00629-w) | Extends the original system by extracting 1-D structural/interaction features and comparing 21 feature-selection methods over a 9,598-feature space. It reports better binding-site and pose performance than CoBDock across five benchmarks. Treat this as a strong method direction, not as a claim independently reproduced here. |
| 6 | **μOR-ligand** (2025) | Publisher method record and [public code](https://github.com/yauz3/-OR-Ligand) reviewed; full publisher article was not openly available. [DOI](https://doi.org/10.1007/s10822-025-00686-1) | Tests whether target-conditioned molecular-interaction features add signal beyond ligand fingerprints/descriptors for agonist/antagonist classification. It compares view-specific models with a stacked/hybrid fusion and controls resampling on fixed splits. It is molecular pharmacology, not a materials application. |
| 7 | **Inter-HVI** (2025) | Publisher record and [public code](https://github.com/yauz3/inter-hvi) reviewed. [DOI](https://doi.org/10.1007/s10953-025-01509-5) | The code exposes a two-stage SMILES-to-features then rule-based training workflow for hypervalent-iodine reactivity. It evidences interpretability-oriented Python practice; accessible material here does not establish a materials-science use case. |
| 8 | **Inter-Pol** (2025) | Publisher method record and [public code](https://github.com/yauz3/inter-pol) reviewed. [DOI](https://doi.org/10.1007/s10953-025-01508-6) | Predicts empirical solvent polarity with descriptor/fingerprint features and RuleFit-derived human-readable rules. Its real contribution is an interpretable structure–property model, a useful conceptual analogue for materials-property work, not proof of a materials dataset capability. |
| 9 | **Inter-Hammett** (2025) | Publisher record and [public code](https://github.com/yauz3/inter-hammet) reviewed. [DOI](https://doi.org/10.1002/slct.202501778) | Uses molecular feature generation and an interpretable rule-oriented training workflow to predict Hammett constants. The repository documents RDKit/Open Babel input handling and a downstream train/evaluate script, showing a reusable cheminformatics workflow. |
| 10 | **Machine Learning Applications in Drug Discovery** (2025) | Open full-text review inspected. [DOI](https://doi.org/10.17721/fujcv13i1p1-66) | A synthesis of supervised/unsupervised learning, neural networks and reinforcement learning across drug-discovery stages; it adds conceptual breadth but is not a new computational method or evidence of supervision outcomes. |
| 11 | **CoBDock** (2024) | Open full text and [public code](https://github.com/yauz3/cobdock) reviewed. [DOI](https://doi.org/10.1186/s13321-023-00793-x) | Combines four docking engines and two cavity detectors in parallel; maps their outputs to a 10 Å voxel grid, ranks candidate sites with ML, then runs local PLANTS docking. Ablation analysis tests why the consensus helps. This is the clearest end-to-end software/pipeline evidence in the record. |
| 12 | **MEF-AlloSite** (2024) | Open full text and [public code](https://github.com/yauz3/MEF-AlloSite) reviewed. [DOI](https://doi.org/10.1186/s13321-024-00882-5) | Integrates pocket and amino-acid features (9,460 variables) for only 90 proteins, then uses multiple selected feature subsets and AutoGluon models to reduce dimensionality/overfitting risk. Evaluation across 51 split variants is stronger evidence of validation awareness than a single split. |
| 13 | **Computational Methods in Drug Discovery and Development** (2024) | Open full-text review inspected. [DOI](https://doi.org/10.23647/ca.md20241230) | Maps molecular modelling, docking, MD and ML methods for drug discovery. It demonstrates breadth and teaching/review ability, not a new software artefact. |
| 14 | **Metallacages for cisplatin encapsulation using DFT** (2024) | Open full text inspected. [DOI](https://doi.org/10.23647/ca.md20240412) | Compares ten M₂L₄ metallacages with PBE0/Hartree–Fock and LanL2DZ in WebMO to assess one/two-cisplatin encapsulation, identifying endo-N Ni²⁺/Cu²⁺ candidates in the reported calculation. It is real electronic-structure-adjacent work, but molecular DFT is not evidence of bulk solid-state DFT/MD/CALPHAD practice. |
| 15 | **PDB-Quantifier** (2026 proceedings) | AVESIS full-text-proceeding record inspected. [AVESIS list](https://avesis.akdeniz.edu.tr/syavuzugurlu/yayinlar) | A one-class-learning quality/prioritisation topic for PDB structures. No substantive public code/data were found in the reviewed record; do not infer a stable tool from the title. |
| 16 | **PDBMINER** (2026 proceedings) | AVESIS record and [repository README](https://github.com/yauz3/PDBminer) reviewed. [AVESIS list](https://avesis.akdeniz.edu.tr/syavuzugurlu/yayinlar) | A Python workflow that collects PDB structures by UniProt, filters structural-quality criteria, uses rank aggregation, and exports a ranked spreadsheet. The codebase makes the workflow plausible; the proceeding was not treated as independent validation of every implementation claim. |

## Methods and technical stack

| Capability | Evidence | Due-diligence judgement |
| --- | --- | --- |
| Python | **Fact:** public research repositories are primarily Python and give Conda/pip workflows. [GitHub profile](https://github.com/yauz3) | Directly evidenced. **High confidence.** |
| Cheminformatics / molecular ML | **Fact:** RDKit, Open Babel, fingerprints, structural descriptors, docking, feature selection and model evaluation recur in code/papers. [CoBDock](https://doi.org/10.1186/s13321-023-00793-x) [Dipole code](https://github.com/yauz3/dipole_moment) | Directly evidenced. **High confidence.** |
| ML interpretability | **Fact:** RuleFit/feature selection recur; coating code/README use SHAP and feature networks. [Inter-Pol](https://doi.org/10.1007/s10953-025-01508-6) [Coating repository](https://github.com/yauz3/coating_motifs_ml) | Directly evidenced. **High confidence.** |
| Materials ML | **Fact:** coating repository maps layer composition/depth/nanoindentation signals to hardness. [Source code](https://github.com/yauz3/coating_motifs_ml/blob/main/01_build_features.py) | One concrete but currently narrow materials case. **Medium confidence.** |
| DFT | **Fact:** metallacage paper uses molecular DFT through WebMO. [Paper](https://doi.org/10.23647/ca.md20240412) | Molecular DFT only. No evidence of VASP, Quantum ESPRESSO, solid-state DFT, ASE, pymatgen, CALPHAD or molecular dynamics production workflows. **High confidence in this boundary.** |
| Scientific RSE practices | **Fact:** GitHub, readable instructions, environment files, fixed seeds/held-out checks appear in several projects. | Good foundation, but not a mature RSE standard: across reviewed active research repositories, no project-specific test suite or GitHub Actions workflow was found; several repositories have no explicit licence file despite README usage statements. **High confidence for the inspected repositories; do not generalise to private work.** |

### The coating repository: the key materials evidence

**Fact — high confidence.** The repository accepts five private Excel datasets,
parses YbDSi/mullite/Si layer composition, generates depth/composition/instrument
features, trains on motif E and evaluates on unseen motifs A–D. It explicitly
excludes two possible instrument columns, fits feature selection on train data,
and records a fixed random state. [Feature builder](https://github.com/yauz3/coating_motifs_ml/blob/main/01_build_features.py)
[Training/validation code](https://github.com/yauz3/coating_motifs_ml/blob/main/02_model_training_and_validate.py)

**Fact — high confidence.** Raw nanoindentation data are withheld for stated
copyright/data-ownership reasons and available only on reasonable request.
[Repository README](https://github.com/yauz3/coating_motifs_ml)

**Interpretation — medium confidence.** This is the best thesis seed because it
connects experimental MSE, Python, validation design, interpretable ML, and
software improvement. It is **not** a finished open-science platform: public data
are absent, the README describes more numbered stages than the two visible Python
files, and the training-file header mentions model choices not all instantiated
in the visible builder. A prospective student should frame this as an opportunity
to harden a research workflow, not assume that the current code/data are thesis
ready.

## Research group, mentorship, and collaboration evidence

### Publicly verifiable group picture

**Fact — medium confidence.** The public profile lists an MSE affiliation and a
substantial individual publication/code record. The reviewed AVESIS project,
experience/thesis, and activity pages did not expose a named laboratory roster,
current MSc/PhD student list, alumni outcomes, seminar programme, open positions,
or funded-project entries. [Profile](https://avesis.akdeniz.edu.tr/syavuzugurlu)
[Projects](https://avesis.akdeniz.edu.tr/syavuzugurlu/projeler)
[Experience/theses](https://avesis.akdeniz.edu.tr/syavuzugurlu/deneyim)
[Activities](https://avesis.akdeniz.edu.tr/syavuzugurlu/bilimselfaaliyetler)

**Unknown — high confidence in the classification.** This is not evidence that
there are no students, grants, meetings, or collaborations; it is evidence that
they were not established by the public sources reviewed. Ask rather than infer.

**Fact — high confidence.** The material-specific public collaboration links
Uğurlu with Emre Bal and Muhammet Karabaş on coating hardness modelling.
[Repository](https://github.com/yauz3/coating_motifs_ml)

**Interpretation — medium confidence.** Bal is the clearest evidenced experimental
counterpart for a materials-data thesis. A formal co-supervision arrangement would
reduce domain and data-access risk substantially.

### Mentorship signal

| Finding | Classification and confidence |
| --- | --- |
| Clear, stepwise software documentation and public reference implementations are a positive teaching/communication signal. | **Interpretation, medium.** They demonstrate how methods are explained, not how students are supervised. |
| The PhD was embedded in an international Birmingham setting with recurring co-authorship with Shan He. | **Fact, high** for the collaboration; **interpretation, low-to-medium** for future international-network value. |
| No public supervised-thesis list, student authorship sequence, or alumni-outcome evidence was verified. | **Unknown, high.** This is the largest mentorship evidence gap. |

## Candidate compatibility

| Candidate asset | Evidence-based fit judgement |
| --- | --- |
| Senior software architecture / open source | **Interpretation, high:** unusually complementary. The advisor's work is code-first and workflow-heavy; a senior engineer could add package boundaries, tests, release discipline, metadata, reproducible environments, data validation, provenance, CI, and documentation. [GitHub profile](https://github.com/yauz3) |
| Scientific Python learning | **Interpretation, high:** direct entry point. Public code already uses Python/Conda/pip and scientific-ML libraries, so learning can be tied to a real research problem rather than toy exercises. |
| Materials Atlas | **Interpretation, medium:** relevant if introduced narrowly as a materials-data evidence/provenance and reproducibility layer for coating measurements/models. It is less credible if pitched as a generic product or as a substitute for a scientific question. |
| Research Landscape | **Interpretation, low-to-medium:** useful as evidence/metadata engineering experience, but tangential to his molecular/materials methods. Mention briefly only after the scientific software fit is clear. |
| AI for materials discovery | **Interpretation, medium:** a credible transition route through the coating project and property-prediction methods, but no public source establishes an active bulk-materials discovery programme. |
| Future PhD abroad | **Unknown/conditional:** Birmingham training and international coauthorship are positive signals, but no public placement record or commitment to support external applications was found. Ask directly about recent students and letters/collaborations. |

## Profile conclusion

**Recommendation: pursue a research conversation promptly, then apply only if the
four gates in [decision.md](decision.md) clear.** The candidate would not be
asking Uğurlu to turn into a software mentor from scratch; software and ML are
already central to the visible work. The uncertainty is whether the same work can
be anchored in a live, properly supervised, publishable materials problem.
