# Explainable recommendations

Research Landscape recommendations are deterministic evidence-discovery
queries, not prestige rankings. The public model in
[`scoring/v1/evidence-recommendations.yaml`](../scoring/v1/evidence-recommendations.yaml)
selects only reviewed canonical entities with directly documented relationships.
It reports why an entity matched, record-local source IDs, confidence, coverage,
and query-specific limitations.

## What the engine can recommend now

The initial model supports evidence-backed discovery for groups with software
development, groups and PIs by controlled research area (including Scientific
Software Engineering and AI for Materials where explicitly evidenced), PIs with licensed
open-source-software development evidence, universities directly hosting groups
with documented target-area work, software-oriented environments, and
ecosystems connected to a target area. Results are ordered by the count of
matching evidence signals, then stable name/ID. A multi-hop university result
shows both the documented host relationship and the group's direct area
evidence. An ecosystem result may similarly show a sourced `includes` relation
and a software record's evidence-backed area classification. Neither traversal
is a university-strength or ecosystem-completeness ranking.
This is a reproducible discovery priority, never a claim of research quality,
prestige, mentorship, availability, or applicant fit.

The current model also supports research groups with documented development
links to software explicitly documented as implemented in Python. This is a
software-path filter, not a statement about a group's working language or its
members' skills. It separately exposes entities with bounded, sourced public
mentorship-process evidence, including the evidence category and limitations.

## What it refuses to recommend

"High-mentorship environments," "dominant research ecosystems," "strongest
academic environments," "best research problems," and "best research advisors"
remain **unavailable**. `discover-problems` can list reviewed, bounded
computational challenges and direct software-support evidence, but does not
compare their importance, novelty, tractability, or fit. The catalog names the evidence contract required before
each comparison could be considered; [ADR 0010](adr/0010-problem-evaluation-evidence-contract.md)
defines the problem-comparison gate. Narrative Python mentions, a public
repository, group size, fame, awards, or citations cannot substitute for
sourced controlled-language relations, a validated mentorship metric, or a
governed comparative model. Documented process evidence is not a
mentorship-quality score, comparison, capacity claim, or prediction of an
applicant's experience.

## Output contract

The generated recommendation report includes:

- model and query identifier;
- canonical entity link and stable ID;
- matching relationship/evidence signals;
- confidence derived from the matching record/assertions;
- coverage as direct matched criteria over query criteria; and
- limitations and unavailable dimensions.

Accessibility, immigration, language feasibility, admissions, openings,
funding eligibility, and private preferences are excluded from public results.
They belong in a separately declared private profile and cannot change a global
or public recommendation.

## Reproducibility

Run:

```bash
python3 scripts/research_landscape.py recommend --list
python3 scripts/research_landscape.py recommend --query groups-ai-for-materials
python3 scripts/research_landscape.py recommend --query environments-for-ai-materials-software-engineers
python3 scripts/research_landscape.py recommend --query principal-investigators-open-software
python3 scripts/research_landscape.py recommend
python3 scripts/research_landscape.py recommend --check
```

`--list` displays every public query ID, alias, title, and availability status;
it does not read private preferences. Correct facts at their canonical entity,
rerun the command, and review the generated diff. Do not edit generated
recommendations manually.

For ad hoc group discovery, use the same canonical IDs with the non-generated
filter command:

```bash
python3 scripts/research_landscape.py discover-areas
python3 scripts/research_landscape.py discover-problems
python3 scripts/research_landscape.py discover-problems --area AREA-MACHINE-LEARNED-POTENTIALS
python3 scripts/research_landscape.py discover-problems --software SW-PHONO3PY
python3 scripts/research_landscape.py discover-problems --ecosystem ECO-PHONO3PY
python3 scripts/research_landscape.py discover-problems --language PROGRAMMING-LANGUAGE-C
python3 scripts/research_landscape.py discover-groups --area AREA-AI-FOR-MATERIALS --country COUNTRY-US
python3 scripts/research_landscape.py discover-groups --software SW-CHGNET --language PROGRAMMING-LANGUAGE-PYTHON
python3 scripts/research_landscape.py discover-groups --problem PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION
python3 scripts/research_landscape.py discover-pis --software SW-PYMATGEN --language PROGRAMMING-LANGUAGE-PYTHON
python3 scripts/research_landscape.py discover-pis --problem PROBLEM-MACHINE-LEARNED-INTERATOMIC-POTENTIAL-MODELING
python3 scripts/research_landscape.py discover-universities --area AREA-AI-FOR-MATERIALS --country COUNTRY-US
python3 scripts/research_landscape.py discover-universities --problem PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION
python3 scripts/research_landscape.py discover-ecosystems --area AREA-MACHINE-LEARNED-POTENTIALS
python3 scripts/research_landscape.py discover-ecosystems --problem PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION
python3 scripts/research_landscape.py discover-software --area AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE --language PROGRAMMING-LANGUAGE-JULIA
python3 scripts/research_landscape.py discover-software --area AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE --language PROGRAMMING-LANGUAGE-CPP
python3 scripts/research_landscape.py discover-software --problem PROBLEM-LATTICE-THERMAL-CONDUCTIVITY-PREDICTION
```

`discover-areas` lists reviewed controlled topics with their direct evidence
reach and source IDs. It is a topic catalog, not a research-problem ranking.
`discover-problems --area` filters only a problem's own controlled area
classification; `discover-problems --software` requires a direct sourced
software `supports` assertion; and `discover-problems --ecosystem` requires an
explicit ecosystem `includes` → software `supports` → problem path. All display
their sources and are ANDed when combined. `discover-problems --language`
requires a documented software `implemented_in` → `supports` → problem path;
it is not an individual-skill, group-practice, or fit signal. All supplied
filters are required for the remaining discovery commands. Each
command exposes documented paths;
it does not produce a score or rank. `discover-pis` follows documented public
affiliation paths for country filters and does not assert availability or
supervision capacity. `discover-universities` uses only direct-host group paths
and does not compare institutions. `discover-ecosystems` exposes only explicit
research-group connection or software-inclusion paths; a PI's separate topic
portfolio does not classify every connected ecosystem. It does not determine
which ecosystem dominates a field.

List valid public filter IDs first when needed:

```bash
python3 scripts/research_landscape.py catalog
```
