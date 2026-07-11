---
report_type: advisor-due-diligence-reading-list
advisor_id: TR-AKU-MSE-ADV-005
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: high
---

# Reading list — ten items before the meeting

Read the first four in full (paper plus code where available) before contacting
Uğurlu. The goal is not to recite results; it is to ask informed questions about
data, validation and future materials translation.

## Priority 1 — the actual materials bridge

### 1. Coating Motifs ML repository and both visible Python scripts

- **Source:** [repository](https://github.com/yauz3/coating_motifs_ml),
  [feature builder](https://github.com/yauz3/coating_motifs_ml/blob/main/01_build_features.py),
  [training/validation](https://github.com/yauz3/coating_motifs_ml/blob/main/02_model_training_and_validate.py)
- **Read for:** the problem definition, whether motif E versus A–D is a defensible
  scientific generalisation test, what layer/depth/composition variables actually
  mean, which data are private, and where a software contribution could make a
  material difference.
- **Scientific contribution to understand:** it turns multi-layer coating
  nanoindentation records into composition/depth/instrument feature tables,
  tests transfer to unseen motifs, and uses post-hoc interpretation. It is not
  a publicly reproducible benchmark because raw data are unavailable.
- **Meeting payoff:** ask about experimental independence, data rights, and what
  the model is allowed to claim about coating design.
- **Evidence status:** code and README directly reviewed; associated manuscript
  metadata are incomplete. **Confidence: high** for the software/data boundary.

### 2. “Experimental dipole moment prediction with a progressive 2D–3D hybrid framework and twin-pair-based diagnostic evaluation” (2026)

- **Source:** [open paper](https://doi.org/10.1186/s13321-026-01215-4),
  [code](https://github.com/yauz3/dipole_moment)
- **Read for:** the distinction between predictive performance and a defensible
  claim on heterogeneous experimental labels; how 2-D, 3-D and noise diagnostics
  are combined.
- **Scientific contribution to understand:** rather than claiming a universal
  “best” architecture, it constructs a multi-view fingerprint/descriptor model,
  a conformer-based EGNN-style model, and a hybrid; it then contextualises error
  using similar molecule pairs. That is a useful intellectual template for
  materials property data whose measurement noise and specimen hierarchy matter.
- **Meeting payoff:** ask what the equivalent of a twin-pair diagnostic would be
  for coating measurements.
- **Evidence status:** open paper and code reviewed. **Confidence: high.**

## Priority 2 — scientific workflow design

### 3. “CoBDock: an accurate and practical machine learning-based consensus blind docking method” (2024)

- **Source:** [open paper](https://doi.org/10.1186/s13321-023-00793-x),
  [code](https://github.com/yauz3/cobdock)
- **Read for:** end-to-end pipeline composition, component failures, target/ligand
  preparation, independent tool agreement, voxelisation, ablation and benchmark
  design.
- **Scientific contribution to understand:** the work does not merely average
  docking scores. It takes predictions from four docking engines and two
  pocket-finders, represents their spatial agreement in 10 Å grid cells, learns
  a site ranking, and then performs local docking. The ablation analysis asks
  whether each component adds distinct information.
- **Meeting payoff:** ask how that validation mindset should change when the
  “ground truth” comes from experiments rather than a molecular benchmark.
- **Evidence status:** open paper and code reviewed. **Confidence: high.**

### 4. “MEF-AlloSite: an accurate and robust Multimodel Ensemble Feature selection for the Allosteric Site identification model” (2024)

- **Source:** [open paper](https://doi.org/10.1186/s13321-024-00882-5),
  [code](https://github.com/yauz3/MEF-AlloSite)
- **Read for:** the danger of a very wide feature space with a small number of
  independent proteins, multiple feature-selection subsets, repeated split
  evaluation and comparison methodology.
- **Scientific contribution to understand:** it combines pocket/structural and
  amino-acid features (9,460 total) for 90 proteins, rather than pretending more
  features automatically help. It uses selected subsets to drive multiple models
  and evaluates across 51 split variants.
- **Meeting payoff:** ask which selection and split-stability methods would be
  appropriate for small, correlated materials datasets.
- **Evidence status:** open paper and code reviewed. **Confidence: high.**

### 5. “MEGA-PROTAC … sequential filtering and rank aggregation” (2025)

- **Source:** [open paper](https://doi.org/10.1038/s41598-024-83558-2),
  [code](https://github.com/yauz3/MEGA-PROTAC)
- **Read for:** how a computationally expensive search gets reduced through
  explicit stages, what ranking aggregates, and what limitations the authors
  themselves identify.
- **Scientific contribution to understand:** it is a rigid, sequential ternary
  complex workflow: docking seeds, distance/interface filters, multiple scoring
  criteria, rank aggregation, clustering and local docking. The paper names
  limitations around fixed poses, sequential search and potential early filtering
  losses—important modelling humility.
- **Meeting payoff:** ask how to design an auditable staged workflow for coating
  experiments without hiding rejected cases.
- **Evidence status:** open paper and code reviewed. **Confidence: high.**

## Priority 3 — interpretable chemistry-to-property modelling

### 6. “Inter-Pol: An Interpretable Machine Learning Framework for Solvent Polarity Prediction” (2025)

- **Source:** [publisher record](https://doi.org/10.1007/s10953-025-01508-6),
  [code](https://github.com/yauz3/inter-pol)
- **Read for:** feature construction, RuleFit explanations, and why readable
  rules may be more useful than opaque small performance gains.
- **Scientific contribution to understand:** it predicts empirical solvent
  polarity using descriptor/fingerprint information, then exposes rules linking
  molecular properties to the predicted parameter. It is a model of
  *interpretability as an output*, not proof of causality.
- **Meeting payoff:** ask how explanation stability and experimental expert review
  would be introduced for materials features.
- **Evidence status:** publisher metadata/abstract and code were reviewed; full
  text was not openly accessible in this diligence. **Confidence: medium.**

### 7. “Inter-Hammett: Enhancing Interpretability in Hammett’s Constant Prediction via Extracting Rules” (2025)

- **Source:** [publisher record](https://doi.org/10.1002/slct.202501778),
  [code](https://github.com/yauz3/inter-hammet)
- **Read for:** a compact chemistry ML workflow—data source, RDKit/Open Babel
  conversion steps, feature creation and train/evaluate separation.
- **Scientific contribution to understand:** the relevant lesson is not the
  Hammett constant itself; it is the attempt to extract interpretable patterns
  from a property-prediction workflow.
- **Meeting payoff:** ask what “interpretable” must mean in a coating setting:
  stable across samples, physically plausible, and independently testable.
- **Evidence status:** repository and publisher record reviewed. **Confidence: medium.**

### 8. “CoBdock-2: enhancing blind docking performance through hybrid feature selection…” (2025)

- **Source:** [publisher record](https://doi.org/10.1007/s10822-025-00629-w),
  [code](https://github.com/yauz3/cobdock-2)
- **Read for:** the distinction between an ensemble of models and an ensemble of
  feature-selection views; the need to compare against the original system
  across several benchmarks.
- **Scientific contribution to understand:** the publisher describes extraction
  of 1-D structural/interaction features and a comparison of 21 selection methods
  across 9,598 features. The useful question is whether added complexity earns
  robust, not merely internal, performance.
- **Meeting payoff:** ask how much feature-engineering complexity is justified for
  the size and quality of an available materials dataset.
- **Evidence status:** code and publisher record reviewed; full article was not
  open in this review. **Confidence: medium.**

## Priority 4 — research integrity around negatives and external validity

### 9. “Prodrug-ML: prodrug-likeness prediction via machine learning on sampled negative decoys” (2026)

- **Source:** [publisher record](https://doi.org/10.1007/s10822-025-00725-x),
  [code](https://github.com/yauz3/prodrug-ml)
- **Read for:** leakage prevention: overlap checks, test-set isolation before
  feature/model choice, negative-class hardness checks, domain-bias tests and
  cross-decoy evaluation.
- **Scientific contribution to understand:** it treats creation of the negative
  class as a scientific design problem. That transfers directly to any materials
  project where different coating runs/specimens can create shortcuts.
- **Meeting payoff:** ask how a materials project will document every split and
  reject the temptation to score on near-duplicate measurements.
- **Evidence status:** code and publisher record reviewed; source positive data
  are not redistributed. **Confidence: medium.**

### 10. “Investigation of metallacages for cisplatin encapsulation using Density Functional Theory (DFT)” (2024)

- **Source:** [open paper](https://doi.org/10.23647/ca.md20240412)
- **Read for:** the advisor's non-ML computational chemistry work and the limits
  of translating molecular DFT experience to solid materials.
- **Scientific contribution to understand:** it computes ten metallacages with
  PBE0/Hartree–Fock and LanL2DZ in WebMO to compare cisplatin encapsulation
  configurations. It is evidence of molecular electronic-structure practice,
  not an example of solid-state DFT, molecular dynamics, CALPHAD or high-
  throughput materials discovery.
- **Meeting payoff:** ask directly which solid-materials simulation tools, if any,
  are active locally—do not assume they follow from this paper.
- **Evidence status:** open paper reviewed. **Confidence: high.**

## Remaining accessible works: skim before a final proposal

These records complete the current public inventory but are lower priority for a
materials-software meeting:

- [De-TarDis (2026)](https://doi.org/10.7240/jeps.1834505) — rank-fused safety
  target lists; code at [GitHub](https://github.com/yauz3/De-TarDis).
- [μOR-ligand (2025)](https://doi.org/10.1007/s10822-025-00686-1) — target-aware
  feature views for opioid ligand functional classes; code at
  [GitHub](https://github.com/yauz3/-OR-Ligand).
- [Inter-HVI (2025)](https://doi.org/10.1007/s10953-025-01509-5) — interpretable
  hypervalent iodine reactivity workflow; code at
  [GitHub](https://github.com/yauz3/inter-hvi).
- [Machine Learning Applications in Drug Discovery (2025)](https://doi.org/10.17721/fujcv13i1p1-66) — broad review.
- [Computational Methods in Drug Discovery and Development (2024)](https://doi.org/10.23647/ca.md20241230) — broad review.
- **PDB-Quantifier** and **PDBMINER** 2026 proceedings, listed on
  [AVESIS](https://avesis.akdeniz.edu.tr/syavuzugurlu/yayinlar); PDBMINER's
  [repository](https://github.com/yauz3/PDBminer) is useful for its transparent
  rank-aggregation workflow.

## Reading protocol

For every item, write only five notes:

1. What is the independent unit of analysis?
2. What data are unavailable or restricted?
3. What leakage/selection-bias risk is recognised or unrecognised?
4. What exact artifact is reproducible from public materials today?
5. What one question would transfer responsibly to a coating/materials setting?

This prepares the candidate to have a scientific conversation rather than perform
admiration. It also guards against treating impressive method names as evidence
that a thesis route is already viable.
