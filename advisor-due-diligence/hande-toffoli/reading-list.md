---
report_type: advisor-due-diligence-reading-list
status: evidence-reviewed
evidence_window: public sources accessed 2026-07-11
confidence: high
---

# Reading list — Hande Toffoli

The goal is not to imitate a literature review. Read enough to formulate one precise, technically honest question. The notes below distinguish full-paper reading from bibliographic verification.

**Interpretation — high confidence.** The ten papers below are ordered by practical reading priority. Eight have accessible full text and were reviewed in depth; the two explicitly marked record-only items are included to complete the research trajectory without inventing details that their accessible primary record does not establish. **Unknown — high confidence in the limitation:** this reading list cannot establish today’s active projects, student capacity, or Hande Toffoli’s individual contribution to every multi-author work.

## Essential full-paper reading

### 1. Molten-metal methane pyrolysis — start here

[Erbasan et al., 2024, *ACS Applied Energy Materials*](https://doi.org/10.1021/acsaem.3c03235)

**Fact — high confidence.** The paper compares Cu and Al promoters in Bi–Ni molten-metal systems for methane pyrolysis using many AIMD runs, rather than only a static NEB calculation. It uses VASP with PBE, PAW, D3, 340 eV cutoff, NPT/NVT dynamics at 3000 K, and Packmol-generated models. It classifies H-dissociation events across the reaction mechanism and uses local binding/charge descriptors to interpret the rates; Cu performs better under the stated simulation conditions. The paper names Hande Ustunel as corresponding author and acknowledges TRUBA resources. [Full text](https://open.metu.edu.tr/bitstream/handle/11511/109700/erbasan-et-al-2024-insights-into-reaction-mechanisms-in-liquid-metals-from-density-functional-theory-ch4-pyrolysis-in.pdf)

**Read for:** How a computational campaign becomes a scientific argument; which run-level inputs and derived labels a reproducibility/data pipeline would need; the boundary between a descriptor and a predictive ML model.

**Ask after reading:** “If this line is active, would reproducible trajectory/event labeling and provenance be scientifically useful before an ML-screening step?”

### 2. Classical MD of graphene/Au tribology

[Maden, Ustunel & Toffoli, 2024, *Lubricants*](https://doi.org/10.3390/lubricants12020046)

**Fact — high confidence.** The paper uses LAMMPS, not a black-box MD label. It specifies EAM for Au, AIREBO for carbon, a Lennard-Jones Au–C interaction, velocity-Verlet integration, a 1 fs step, explicit NVT preparation/production stages, and model sizes. It varies tip geometry, temperature, direction, load proxy, deformability, and size. The reported scientific result is that geometry and direction change friction/stick–slip behavior; allowing a small tip to deform changes contact and response, while a larger tip more clearly recovers stick–slip features comparable to experiment. [Open full text](https://www.mdpi.com/2075-4442/12/2/46)

**Read for:** Why an input deck alone is not reproducibility; what needs to be recorded about potentials, geometry construction, equilibrium, observations, and post-processing.

**Ask after reading:** “Which of those protocol decisions are currently explicit and reusable across students, and which are implicit?”

### 3. Quantum ESPRESSO catalytic pathway study

[Demirtas, Ustunel & Toffoli, 2023, *Molecules*](https://doi.org/10.3390/molecules28237928)

**Fact — high confidence.** The article uses open-source Quantum ESPRESSO and XCrySDen, tests progressively doped Pt/Au(111) models, and calculates adsorption/reaction information for methanol dehydrogenation. The conclusion is mechanistic: Pt-induced electronic/strain effects lower the activation barrier, while preadsorbed oxygen plus Pt can lower it further in the reported model. [Open full text](https://open.metu.edu.tr/bitstream/handle/11511/107162/molecules-28-07928.pdf)

**Read for:** A thesis-scale DFT problem with explicit model variants, convergence choices, a tractable scientific outcome, and open-source software.

**Ask after reading:** “Would a convergence/uncertainty harness for a narrowly defined QE surface-reaction question be of value, or are the current unknowns elsewhere?”

### 4. Water adsorption on boron surfaces

[Eroğlu et al., 2023, *Journal of Boron*](https://doi.org/10.30728/boron.1283831)

**Fact — high confidence.** The paper compares reconstructed, unreconstructed, and defective alpha-boron plus a beta-boron subunit, with single and multiple water molecules. It reports that adsorption depends strongly on phase/defects and water multiplicity. [Full text](https://open.metu.edu.tr/bitstream/handle/11511/116775/Exploring%20the%20interaction%20of%20water%20with%20boron%20surfaces.pdf)

**Read for:** Careful construction of a small comparative dataset: each structure, adsorption configuration, and calculation assumption should have a stable identity.

### 5. 2025 Al hydrolysis — read the source boundaries too

[Mutlu et al., 2025, *Applied Energy*](https://doi.org/10.1016/j.apenergy.2025.126814)

**Fact — medium/high confidence.** The METU publication record reports a combined experimental/first-principles study that uses impedance, XRD, SEM, H2-volume measurement, and a six-step DFT reaction mechanism for Al hydrolysis. [Official METU record](https://avesis.metu.edu.tr/yayin/2c0bce39-feb5-4239-b88c-f1dc27069f48/hydrolysis-of-al-for-hydrogen-production-a-joint-experimental-and-first-principles-density-functional-theory-investigation)

**Evidence boundary.** Full text was not available from a primary source during this review; do not infer its code, workflow, or individual-author role. It is still a useful discussion anchor for theory–experiment collaboration.

### 6. PEEK on graphene and CNTs — a reproducibility model

[Toraman et al., 2021, *Computational Materials Science*](https://doi.org/10.1016/j.commatsci.2021.110320)

**Fact — high confidence.** The authors use QE/vdW-corrected DFT to benchmark ReaxFF-lg LAMMPS MD, then test PEEK adsorption as chain length, temperature, substrate, CNT geometry, and initial configuration vary. This is useful because it has an explicit “small accurate model → validated larger simulation” logic. The CRediT statement records Hande Ustunel’s supervision, investigation, writing, and project administration for this project. [Primary postprint](https://arts.units.it/bitstream/11368/2992708/5/CMS-2021-TOFFOLI-Post_print.pdf)

**Read for:** How a workflow can preserve the link between DFT validation and larger MD campaigns instead of treating force-field simulation as self-validating.

### 7. h-BN/Au nanotribology — convergence discipline

[Baksi et al., 2019, *J. Phys. Chem. C*](https://doi.org/10.1021/acs.jpcc.9b06767)

**Fact — high confidence.** The study uses Quantum ESPRESSO with tightly described cutoffs, k-points, smearing, vacuum, geometry constraints, a PES grid, and multiple lateral-force estimates. It separates a near-commensurate periodic h-BN/Au interface from finite Au clusters, revealing why edge effects cannot be inferred from the bulk model. [Full article](https://open.metu.edu.tr/bitstream/handle/11511/28648/Nanotribological_properties_of_the_h_bn_au%28111%29_interface_a_dft_study.pdf)

**Read for:** A concrete example of why stable configuration identifiers, convergence records, and model-boundary documentation belong in the result, not merely the supplement.

### 8. Formaldehyde selectivity — theory/experiment coupling

[Karatok et al., 2021, *ACS Catalysis*](https://doi.org/10.1021/acscatal.1c00344)

**Fact — high confidence.** Spectroscopy and DFT are used together to identify a selectivity/conversion trade-off on Ag(111) as oxygen coverage changes and surface reconstruction occurs. Hande Ustunel is a coauthor, but the public text reviewed here does not assign individual roles. [Primary postprint](https://arts.units.it/retrieve/07f53437-61ba-4a31-937a-4b56ebdda8c4/acscatal_2021_TOFFOLI-Post_print.pdf)

**Read for:** The difference between a simulation that is computationally tidy and one that is connected to measurable mechanisms.

### 9. DFT tribology review — know the method boundary

[Ustunel & Toffoli, 2022, *Electronic Structure*](https://doi.org/10.1088/2516-1075/ac7188)

**Fact — high confidence.** The review explains what DFT can calculate in atomic-scale tribology and why temperature/velocity behavior often needs classical MD. [OpenMETU full-text record](https://open.metu.edu.tr/handle/11511/98251)

**Read for:** A useful guardrail when proposing any “unified” pipeline: document method limits rather than hiding them behind automation.

### 10. Defect and layer effects in graphene — a bounded context paper

[Toffoli et al., 2019, *Applied Surface Science*](https://doi.org/10.1016/j.apsusc.2019.02.040)

**Fact — medium confidence.** The official OpenMETU record establishes this as a study of the combined effect of point defects and layer number on graphene; its full text was not deep-read in this dossier. [OpenMETU record](https://open.metu.edu.tr/handle/11511/49275)

**Read for:** A compact 2D-materials context that can reveal how the group scopes a controlled family of structural variants. Treat it as a question-led preparation item: after reading the full paper, identify the model hierarchy, observables, and validation boundary rather than assuming its exact computational stack from the title alone.

## Training / ecosystem reading

1. [TÜBİTAK-ULAKBİM: Density Functional Theory with Quantum ESPRESSO](https://acikders.ulakbim.gov.tr/course/view.php?id=35&lang=en) — direct evidence of QE, Linux/HPC prerequisites, XCrySDen, and hands-on instruction.
2. [METU PHYS518: Simulations of Many-Particle Systems](https://catalog2.metu.edu.tr/course/PHYS518/2300518) — direct evidence of a graduate MD/MC/simulation teaching context.
3. [TRUBA winter-school schedule/materials](https://indico.truba.gov.tr/event/6/timetable/?view=standard_numbered) — direct evidence of LAMMPS/OVITO/Packmol training and publicly exposed example inputs.
4. [METU/EuroCC3 record](https://ak.metu.edu.tr/tr/node/15) — current 2026–29 HPC context, not evidence of a particular thesis slot.
5. [Şişecam EuroCC proof of concept](https://eurocc.truba.gov.tr/?page_id=9494) — current industry-facing computational-materials discovery context; read with care about IP.

## Record-only recent works — do not over-read titles

The following works are part of the newest-20 audit in [advisor-profile.md](advisor-profile.md). Their metadata are verified through the [official AVESIS publication list](https://avesis.metu.edu.tr/ustunel/yayinlar), but their full text or Hande-specific contribution was not established in this dossier:

- 2025: *Self-Assembled Superacid Monolayers on c-Si Provide Exceptional Surface Passivation and Low Contact Resistivity* (*Solar RRL*).
- 2024: *Oxygen-Promoted on-Surface Synthesis of Polyboroxine Molecules* (*Chemistry — A European Journal*).
- 2024: *Hydrogen production using aluminum-water splitting: A combined experimental and theoretical approach* (*International Journal of Hydrogen Energy*).
- 2022–2016: the seven other remaining works in the publication-evidence table, including DFT thermoelasticity, catalysis, battery, and silicon-quantum-dot work.

This distinction matters: bibliographic breadth supports a trajectory assessment, but only accessible full text supports detailed claims about tools, data, methods, reproducibility, and research contribution.

## A compact note-taking template

For each paper, capture:

```text
Question / system:
Model and assumptions:
Software, version, potential/pseudopotential:
Input-space choices (cell, slab, cutoff, k-points, ensemble, timestep):
Output / observable:
Claim supported by the result:
What could a software artifact improve?
What remains unknown?
```

Bring only two completed notes to the meeting: methane-pyrolysis AIMD and the LAMMPS tribology study. Quality of attention is a better signal than an ungrounded long reading list.
