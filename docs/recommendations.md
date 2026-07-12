# Explainable recommendations

Research Landscape recommendations are deterministic evidence-discovery
queries, not prestige rankings. The public model in
[`scoring/v1/evidence-recommendations.yaml`](../scoring/v1/evidence-recommendations.yaml)
selects only reviewed canonical entities with directly documented relationships.
It reports why an entity matched, record-local source IDs, confidence, coverage,
and query-specific limitations.

## What the engine can recommend now

The initial model supports evidence-backed discovery for groups with software
development, groups and PIs by controlled research area (including AI for
Materials where explicitly evidenced), PIs with licensed
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

## What it refuses to recommend

Python-heavy groups and high-mentorship environments are reported as
**unavailable**, with the missing evidence contract explained. Narrative Python
mentions, a public repository, group size, fame, awards, or citations cannot
substitute for sourced controlled-language relations or a validated mentorship
metric.

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
python3 scripts/research_landscape.py recommend
python3 scripts/research_landscape.py recommend --check
```

`--list` displays every public query ID, alias, title, and availability status;
it does not read private preferences. Correct facts at their canonical entity,
rerun the command, and review the generated diff. Do not edit generated
recommendations manually.
