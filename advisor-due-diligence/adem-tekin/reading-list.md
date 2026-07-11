---
report_type: advisor-reading-list
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: high
---

# Reading list — Adem Tekin research fit

Read these in order. The goal is not to memorize every equation; it is to arrive able to discuss the group’s scientific decisions, software boundaries, and validation standards.

## 1. PNcsp+ (2026) — start here

**Cem Oran, Riccarda Caputo, Pierre Villars, Adem Tekin, “PNcsp+: A Periodic Number-Based Crystal Structure Prediction Method Enhanced by Machine Learning.”** [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13085239/) · [public code](https://github.com/tccdem/PNcsp_Plus)

**Why first:** It is the most direct synthesis of the group’s current direction: interpretable chemical representation, database-backed prototype search, GNN potentials, optional relaxation, benchmark evaluation, and released Python software.

**Read for:**

- why the Mendeleev periodic number is used as a chemical-similarity prior;
- the boundary between candidate generation and ML/DFT ranking;
- OQMD/MP/MPDS dependencies and how a candidate enters/exits the pipeline;
- benchmark design and what Top-*n* structure matching does—and does not—demonstrate;
- the stated performance/cost trade-off and the paper’s limitations for complex systems.

**Bring one observation:** “The useful engineering question is not only whether the code runs; it is which data-source, neighbour-order and calculator choices change a scientific conclusion.”

## 2. FFCASP (2021) — understand the group’s method-building lineage

**Samet Demir and Adem Tekin, “FFCASP: A Massively Parallel Crystal Structure Prediction Algorithm.”** [DOI](https://doi.org/10.1021/acs.jctc.0c01197) · [PubMed record](https://pubmed.ncbi.nlm.nih.gov/33798330/)

**Why second:** It demonstrates that the group has long treated algorithm development as scholarly work. The algorithm combines particle-swarm and simulated-annealing approaches, produces large candidate sets, and uses clustering/data mining and DFT-D3 refinement to recover known molecular-crystal structures.

**Read for:**

- the division of labour between global search, force fields, deduplication, clustering, and DFT;
- why massive parallelism changes the research question rather than only making it faster;
- which outputs need to be retained to make a search reproducible;
- how success on known polymorphs should be separated from claims of discovering new ones.

**Bring one question:** “Which FFCASP outputs would you now regard as essential provenance for an external researcher to reproduce a result?”

## 3. Phase Prediction via Crystal Structure Similarity (2024)

**Cem Oran et al., “Phase Prediction via Crystal Structure Similarity in the Periodic Number Representation.”** [DOI](https://doi.org/10.1021/acs.inorgchem.4c03137) · [PNcsp implementation](https://github.com/tccdem/PNcsp)

**Why third:** This is the conceptual bridge from periodic-number phase maps to executable PNcsp/PNcsp+. It is central to understanding why the group’s CSP approach is interpretable.

**Read for:**

- the precise meaning of “similarity” in the phase-map representation;
- what counts as a structure-type analogy versus a prediction;
- potential failure modes when phase-map coverage, composition normalisation, or structural matching is incomplete;
- why exceptions are scientifically useful, given the current phase-map-exception project.

**Note:** publisher full text was not openly accessible in this evidence pass; read it through institutional access before drawing technical conclusions beyond the DOI/code documentation.

## 4. Lead-free mixed-cation perovskites via ML (2025)

**Fatemeh Jamalinabijan, Somayyeh Alidoust, Gözde İniş Demir, Adem Tekin, “Discovering novel lead-free mixed cation hybrid halide perovskites via machine learning.”** [Open full text](https://pubs.rsc.org/en/content/articlepdf/2025/cp/d4cp04218b) · [released code/data referenced in the paper](https://github.com/tccdem/Perosolar)

**Why fourth:** This is the clearest case study for the candidate’s AI-for-materials interest. The paper does more than run a model: it constructs DFT-derived datasets, selects elemental descriptors, tunes gradient boosting with cross-validation, filters a large uncomputed set, and DFT-checks a subset.

**Read for:**

- why thresholding by tolerance factors can discard plausible candidates;
- dataset construction and split choices;
- the difference between predicted decomposition energy/band gap and experimental viability;
- model error values, 20-candidate DFT validation, and what remains unvalidated;
- Pymatgen, Matminer, scikit-learn, Quantum Espresso and GPAW as a real Python/DFT ecosystem.

**Bring one observation:** “A useful software contribution could make the screen’s assumptions, dataset versions, and validation decisions inspectable rather than only producing another model.”

## 5. Light-harvesting lead-free mixed-cation perovskites (2024)

**Somayyeh Alidoust, Fatemeh Jamalinabijan, Adem Tekin, “Light-Harvesting Lead-Free Mixed Cation Hybrid Halide Perovskites: A Density Functional Theory-Based Computational Screening Study.”** [DOI](https://doi.org/10.1021/acsaem.3c02934)

**Why fifth:** It supplies the DFT screening backbone on which the 2025 ML paper builds. Read it after the ML paper to avoid treating a model as independent of its data-generating process.

**Read for:**

- original composition-generation assumptions;
- formation-energy and band-gap filters;
- phase and stability assumptions;
- data artefacts that should flow into a provenance model;
- the difference between “promising calculated candidate” and “synthesised device material.”

**Access note:** publisher access may be required for full methods.

## 6. Sn–Ge hybrid perovskite screening (2024)

**Adem Tekin, Merve Kalpar, Emine Tekin, “Exploring the Potential of Sn–Ge Based Hybrid Organic–Inorganic Perovskites: A Density Functional Theory-Based Computational Screening Study.”** [Full article](https://doi.org/10.1063/5.0220297)

**Why sixth:** It exposes a more tightly defined high-throughput design space (7,695 variants) and uses HSE06 filters. It is a good training example for how a computational paper controls variables and reports a candidate region rather than a single “winner.”

**Read for:**

- composition/phase enumeration;
- formation-energy and band-gap thresholds;
- why HSE06 matters here;
- the paper’s explicit requirement for later experimental validation;
- author contributions, especially the data-curation role of a student collaborator.

## 7. NICE-FF (2023)

**Gözde İniş Demir and Adem Tekin, “NICE-FF: A Non-Empirical, Intermolecular, Consistent and Extensible Force Field for Nucleic Acids and Beyond.”** [ITU extended record](https://research.itu.edu.tr/en/publications/nice-ff-a-non-empirical-intermolecular-consistent-and-extensible-/) · [DOI](https://doi.org/10.1063/5.0176641)

**Why seventh:** Although it is in nucleic-acid rather than inorganic materials space, it is the best evidence that the group can frame workflow automation, ML-assisted parametrisation, extensibility, and integration into CSP as research contributions.

**Read for:**

- the automated pipeline from ab-initio interaction grids to fitted parameters;
- what “extensible” means in a scientific-method paper;
- the integration point with FFCASP;
- benchmark design (S22 and structural recovery) and how it could inform materials-code QA.

## 8. Trimetallic borohydrides (2023)

**Samet Demir et al., “Hydrogen Storage in Trimetallic Borohydrides: A Crystal Structure Prediction and Ab Initio Molecular Dynamics Simulations Study.”** [ITU extended record](https://research.itu.edu.tr/en/publications/hydrogen-storage-in-trimetallic-borohydrides-a-crystal-structure-/) · [DOI](https://doi.org/10.1021/acs.jpcc.3c02943)

**Why eighth:** This is a strong example of CSP leading into physical validation. It applies FFCASP, electronic-structure calculations, convex-hull analysis and AIMD to distinguish stable/metastable candidates and hydrogen-release behaviour.

**Read for:**

- why a low-energy structure is not enough;
- the roles of convex hull and finite-temperature dynamics;
- whether data structures capture stable, metastable and uncertain states distinctly;
- an international collaborative pattern tied to a trainee’s longer research path.

## 9. 2D-FFCASP (2022)

**Gözde İniş Demir, Samet Demir, Adem Tekin, “2D-FFCASP—A New Approach for 2D Structure Prediction Applied to Self-Assemblies of DNA Bases.”** [DOI](https://doi.org/10.1002/adts.202200308)

**Why ninth:** It shows that the group has extended a method into a new dimensionality rather than applying a fixed tool. The paper evaluates known self-assemblies with dispersion-corrected DFT and higher-level interaction calculations.

**Read for:**

- how a research code changes when the mathematical search space changes;
- expected validation when moving from 3D crystalline to 1D/2D assemblies;
- design choices that should be documented as a codebase gains a new capability.

## 10. Electron conductivity in LLZO and LPS (2024)

**Samet Demir et al., “Factors Affecting the Electron Conductivity in Single Crystal Li₇La₃Zr₂O₁₂ and Li₇P₃S₁₁.”** [ITU output record](https://research.itu.edu.tr/tr/publications/factors-affecting-the-electron-conductivity-in-single-crystal-lis/) · [DOI](https://doi.org/10.1021/acsaem.3c03092)

**Why tenth:** It is a materials-science anchor outside CSP: solid electrolytes, intrinsic electronic transport, large-scale HPC, and international collaboration. It helps evaluate whether the candidate wants breadth into battery materials or should remain focused on CSP.

**Read for:**

- the physical question and calculation scale;
- how a software/HPC contribution is embedded in a domain-science collaboration;
- the resulting trade-off between domain depth and maintaining a reusable software artifact.

## Suggested two-week plan

| Day | Work | Output to bring |
| --- | --- | --- |
| 1–2 | #1 PNcsp+ | One-page workflow diagram; three failure-mode questions. |
| 3 | Inspect PNcsp+ repository / run docs without modifying it | List of reproducibility, data-access and benchmark questions. |
| 4–5 | #2 FFCASP and #3 phase prediction | Short comparison: global search vs prototype retrieval. |
| 6–7 | #4 ML perovskites | Candidate-screening data-flow diagram and validation caveat. |
| 8 | #5 + #6 | Explain DFT-screened candidate vs experimentally demonstrated material. |
| 9 | #7 NICE-FF | One idea for software artifact + scientific result. |
| 10 | #8 borohydrides | List physical-validation stages after CSP. |
| 11 | #9 + #10 | Decide whether your thesis interest is CSP-methods, screens, or a materials application. |
| 12–14 | Meeting prep | A 90-second introduction and six tailored questions. |

## What not to overclaim after reading

- Do not say the group has experimentally discovered every predicted candidate.
- Do not equate an open repository with a fully mature release/CI/governance process.
- Do not promise a new model will beat existing methods before reproducing a baseline.
- Do not call a data/provenance contribution “just engineering”; connect it to a falsifiable scientific question and validation protocol.
