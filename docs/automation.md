# Automation

Research Landscape automation is a reproducible consumer of canonical
knowledge, never another source of truth. It parses entity frontmatter and
declared view contracts, reports structural problems, and derives navigation
indexes. Editorial evidence, relationship meaning, confidence, and corrections
remain owned by the canonical entity records.

## Commands

Install the pinned development dependencies, then run:

```bash
python3 scripts/research_landscape.py validate
python3 scripts/research_landscape.py generate
python3 scripts/research_landscape.py generate --check
python3 scripts/research_landscape.py recommend
python3 scripts/research_landscape.py recommend --check
python3 scripts/research_landscape.py recommend --list
python3 scripts/research_landscape.py recommend --query groups-ai-for-materials
python3 scripts/research_landscape.py freshness --as-of 2026-07-12
```

`validate` checks v2 schema/frontmatter, IDs, reference fields, relationship
endpoint types, record-local evidence keys resolved specifically from each
record's `## Evidence` table (including duplicate-key detection, public-URL,
and ISO access-date checks), ADR 0006 direct-host integrity, local Markdown
links, possible duplicate names, and orphan signals.

`generate` first validates the corpus, then derives public views from
[`views/definitions.yaml`](../views/definitions.yaml) and the generated
repository-health report. It uses a content fingerprint of the view manifest,
schema, and canonical entity corpus rather than a wall-clock timestamp, so the
same inputs yield byte-identical outputs. `--check` fails if committed generated
output is missing or stale.

`recommend` validates the corpus and the versioned public recommendation model,
then derives evidence-discovery results in `reports/generated/`. It exposes
documented matching signals, confidence, coverage, and unavailable dimensions;
it does not rank prestige, calculate private accessibility, or infer missing
evidence.

`recommend --list` renders a deterministic catalog of public query IDs, titles,
aliases, and available/unavailable status. It reads no private profile or
shortlist data. `recommend --query <id-or-alias>` renders one listed query for
interactive discovery; neither form writes generated output.

`freshness` produces a non-generated, reproducible maintenance audit from
review dates and declared volatile-assertion deadlines. Pass `--as-of` for a
repeatable result; without it, the command uses the local current date. Its
thresholds and repair boundaries are defined in the [review freshness
policy](freshness-policy.md).

## Generated-output boundary

`views/generated/` and `reports/generated/` are committed, reproducible
projections. Their generated-file banner and input fingerprint make their
provenance inspectable. They may contain concise metadata and canonical links,
but never copied entity bodies, private shortlist data, scores, inferred inverse
facts, or conclusions about opportunities, mentorship, funding availability,
language, or fit.

Private views (My Shortlist, Current Focus, and Waiting List) intentionally
produce no public files. Their required private inputs are declared in the view
manifest; no applicant-owned data is read by this tool.

## Repair workflow

1. Fix a public fact or relationship in its canonical entity and evidence table.
2. Run validation and address errors; review warnings as health signals.
3. Regenerate outputs and inspect the diff.
4. Run `generate --check` before committing.

Do not repair a generated index by hand. Do not treat a warning count as a
research-quality, prestige, mentorship, or recommendation score.
