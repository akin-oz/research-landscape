---
report_type: advisor-due-diligence-meeting-preparation
advisor_id: TR-AKU-MSE-ADV-005
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: medium
---

# Meeting preparation — Sadettin Yavuz Uğurlu

## Objective of an in-person meeting

The meeting should answer one practical question:

> Can we define a bounded MSc research problem in materials informatics where
> I own a durable, reproducible Python contribution and where materials-domain
> validation, data rights, and supervision are real rather than aspirational?

Do not use the meeting to obtain an informal admission promise. The right outcome
is either (a) a small, evidence-backed next step—such as reading a dataset
agreement and scoping a pilot—or (b) a clear decision not to proceed.

## What to know before entering the room

### Research summary to state accurately

**Fact.** Uğurlu's doctoral work at Birmingham concerned machine-learning
applications to virtual screening. His public work now spans consensus docking,
allosteric-site modelling, PROTAC ranking, interpretable molecular-property
models, and a 2026 experimental dipole model. [Birmingham profile](https://www.birmingham.ac.uk/staff/profiles/computer-science/research-student/ugurlu-sadettin-yavuz)
[AVESIS publication list](https://avesis.akdeniz.edu.tr/syavuzugurlu/yayinlar)

**Fact.** The most relevant local materials artefact is the public
YbSi–mullite–Si environmental-barrier-coating (EBC) hardness repository with
Emre Bal and Muhammet Karabaş. It uses layer/composition decoding, feature
engineering, XGBoost/LightGBM/CatBoost-style modelling, train-on-one-motif/test-
on-unseen-motifs evaluation, SHAP, and feature-network analysis; raw
nanoindentation data are not public. [Repository](https://github.com/yauz3/coating_motifs_ml)

**Fact.** The public code portfolio exposes Python environments, RDKit/Open
Babel, feature selection, validation, rank aggregation and reproducibility
controls, but inspected repositories do not expose project-specific CI/testing or
a consistently explicit licence. [GitHub profile](https://github.com/yauz3)

### Four concrete discussion anchors

1. **CoBDock:** ask how the team chose the components, handled failures of
   external tools, and defined a valid benchmark—not merely how well it scored.
   [Paper](https://doi.org/10.1186/s13321-023-00793-x)
2. **Experimental dipole work:** ask why twin-pair/noise-ceiling diagnostics were
   necessary and how such diagnostics could transfer to noisy experimental
   materials data. [Paper](https://doi.org/10.1186/s13321-026-01215-4)
3. **Coating ML:** ask whether the data/motif split is live, whether a new thesis
   can access de-identified data, and whether an experimental co-supervisor can
   validate the scientific question. [Repository](https://github.com/yauz3/coating_motifs_ml)
4. **Software maturity:** offer the candidate's skills as a research enabler:
   data contracts, provenance, testable preprocessing, environment capture,
   releaseable package/API, documentation, and CI—not as a request to rebuild
   the advisor's entire codebase.

## Recommended 35-minute conversation flow

| Time | Purpose | Suggested move |
| --- | --- | --- |
| 0–3 min | Establish shared ground | “I read CoBDock and the coating repository. I was especially interested in how you use validation and interpretable features, not only predictive accuracy.” |
| 3–8 min | Present the candidate concisely | “I have 10+ years in software architecture and open-source work. I am building scientific-Python depth and want to apply it to a real materials problem, with durable research software as part of the output.” |
| 8–16 min | Let the advisor lead | Ask what research direction is active now, what data/problem is genuinely available, and who would validate materials claims. Listen for specifics rather than selling an idea. |
| 16–25 min | Test one small collaboration concept | Present only one of the five thesis seeds below, conditioned on data rights and a materials co-supervisor. Ask what is scientifically wrong or missing in it. |
| 25–31 min | Test supervision/project fit | Ask cadence, ownership, authorship, data access, reproducibility expectations, and whether the advisor sees a one-semester pilot. |
| 31–35 min | Agree on a low-pressure next step | Offer a 1–2 page concept note or a small public-code audit after permission; do not ask “Will you admit me?” |

## How to introduce the background without sounding transactional

### Senior software engineering

Use this formulation:

> My strongest contribution is not just training a model. I can make the research
> path reliable: clear input schemas, data lineage, automated validation,
> reproducible environments, tests, documentation, and a usable artifact for the
> next student. I want that engineering to serve a materials question that you
> consider scientifically worth answering.

This is credible because the reviewed work already has code-based pipelines and
explicit leakage/validation concerns. It does **not** presume that existing code
is deficient or that the advisor wants an engineering takeover.

### Materials Atlas

Use this formulation:

> I also maintain Materials Atlas, which has made me think carefully about how
> materials evidence, measurements, metadata, and uncertainty are recorded. I
> would not try to make it the thesis. If useful, I could bring that discipline to
> a focused coating-data workflow so another researcher can understand exactly
> what was measured, transformed, trained, and validated.

The relevant bridge is provenance for EBC measurement/model data, not a generic
website. **Confidence: medium** because the fit is inferred from the coating
repository and the candidate's stated work.

### Research Landscape

Use only if asked about broader projects:

> Research Landscape is an evidence/metadata project. It taught me to distinguish
> source facts from interpretations, which is also how I think a materials ML
> workflow should report data lineage and uncertainty.

Do not make it the opening topic. Its relevance to Uğurlu's current work is
indirect. **Confidence: low-to-medium.**

## Five realistic thesis seeds

None of these is a pre-agreed project. Each becomes real only after the advisor,
data owner, and materials co-supervisor agree on the scientific question,
permissions, validation and scope.

### 1. Reproducible EBC hardness benchmark and provenance package

**Research question:** Across YbSi–mullite–Si coating motifs, what performance
is genuinely transferable when preprocessing, feature selection, and
train/test-motif separation are frozen and auditable?

**Scientific contribution:** Turn the existing motif-E-to-A–D experiment into a
versioned benchmark: explicit data schema, immutable split manifests,
preprocessing provenance, leakage tests, uncertainty intervals, baseline
models, and a materials interpretation of errors by layer/depth.

**Software contribution:** Python package/CLI, dataset cards, metadata schema,
unit/integration tests, reproducible environment, experiment registry and a
public synthetic/derived demonstration dataset if raw data cannot be released.

**Why it fits:** The repository already has a motif-generalisation design and
withheld raw data. [Repository](https://github.com/yauz3/coating_motifs_ml)

**Critical gate:** written permission to use data for an MSc and a domain
scientist who can distinguish a valid materials conclusion from a model artefact.

**Confidence: medium.**

### 2. Uncertainty-aware, physically constrained EBC property prediction

**Research question:** Can calibrated uncertainty and monotonic/physical sanity
checks reveal when a hardness prediction extrapolates beyond the observed
composition/depth regime?

**Scientific contribution:** Compare standard regression, conformal prediction,
and uncertainty-aware ensembles under leave-one-motif-out evaluation. Analyse
failure by compositional transition zone and measurement depth; pre-register
which physical trends are expected and which should not be imposed.

**Software contribution:** validation library with calibration plots, split-aware
metrics, model cards and machine-readable results.

**Why it fits:** It builds on the advisor's emphasis on test isolation,
interpretable modelling, and noise-aware evaluation. [Dipole paper](https://doi.org/10.1186/s13321-026-01215-4)
[Coating repository](https://github.com/yauz3/coating_motifs_ml)

**Critical gate:** enough independent specimens/motifs to make uncertainty
claims meaningful; do not mistake within-specimen points for independent samples.

**Confidence: medium.**

### 3. Experimental-materials data contract for coating characterisation

**Research question:** Which acquisition, processing, microstructure, layer and
nanoindentation metadata are necessary for an ML result to be reusable and
auditable across coating experiments?

**Scientific contribution:** Design and evaluate a minimal metadata model with a
retrospective EBC case study; quantify which missing fields materially alter
interpretation or model applicability.

**Software contribution:** Python validators, JSON/YAML schemas, provenance
capture, importers and a searchable catalog of approved metadata—not a broad
knowledge-graph thesis.

**Why it fits:** It gives Materials Atlas a disciplined, research-scale role and
addresses the raw-data/provenance gap directly.

**Critical gate:** access to a small representative set of legitimate lab records
and agreement that metadata engineering counts as a publishable materials-methods
contribution.

**Confidence: medium.**

### 4. Interpretable, cross-domain property modelling: molecules to ceramics

**Research question:** Which interpretability practices from molecular
property-learning transfer safely to composition/process/property models in EBCs,
and where do they fail because the physical variables differ?

**Scientific contribution:** Compare explanation stability (e.g., SHAP/rules) and
feature-selection stability across resamples/motifs; require experimental-domain
interpretation before claiming causal insight.

**Software contribution:** reusable explanation-stability and leakage-audit
toolkit, with documented examples from the coating study.

**Why it fits:** Inter-Pol and related work explicitly value interpretable
structure–property models, while the coating repository already invokes SHAP.
[Inter-Pol](https://doi.org/10.1007/s10953-025-01508-6)
[Coating repository](https://github.com/yauz3/coating_motifs_ml)

**Critical gate:** keep the claim methodological; do not advertise causal
materials discovery without experimental validation.

**Confidence: medium.**

### 5. Materials experiment-to-model workflow with a public surrogate benchmark

**Research question:** How can a private experimental coating dataset be paired
with an open surrogate benchmark so the pipeline can be reviewed and reused
without disclosing protected measurements?

**Scientific contribution:** Develop a two-tier protocol: private data for the
domain result, synthetic/open surrogate data for code tests, reproducibility and
teaching. Evaluate whether conclusions hold under both a hold-out motif protocol
and a transparently labelled surrogate setting.

**Software contribution:** data-access adapter, synthetic-data generator,
benchmark harness, CI tests, and release governance.

**Why it fits:** It is a practical response to the coating repository's explicit
data restrictions, and plays to the candidate's RSE strength.

**Critical gate:** avoid fabricating experimental evidence—surrogate data must
always be visibly labelled and never used to validate the real material claim.

**Confidence: medium.**

## What a strong answer sounds like

These signals are **not** guarantees, but they distinguish a promising fit from a
polite conversation:

- Names a live dataset/problem and a responsible materials scientist.
- Explains what a student can own, publish and release.
- Welcomes a small reproducibility/provenance deliverable alongside scientific
  results.
- Identifies a thesis-sized experimental validation path.
- Is specific about meeting cadence, capacity, authorship and data access.

## What should trigger a pause

- “We can decide the project after you enroll” with no current research artefact.
- No answer on whether the coating data can be used/published.
- A pure software cleanup detached from a materials question.
- No materials-domain person available to validate modelling claims.
- Pressure to promise work before formal supervision/data permissions are clear.

The appropriate close is: “Thank you—would it be helpful if I sent a one-page
concept note centred on the most realistic dataset and the smallest publishable
first milestone?”
