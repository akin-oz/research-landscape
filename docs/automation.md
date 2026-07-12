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
python3 scripts/research_landscape.py catalog
python3 scripts/research_landscape.py discover-groups --area AREA-AI-FOR-MATERIALS --country COUNTRY-US
python3 scripts/research_landscape.py discover-groups --language PROGRAMMING-LANGUAGE-PYTHON
python3 scripts/research_landscape.py discover-groups --language PROGRAMMING-LANGUAGE-CPP
python3 scripts/research_landscape.py discover-groups --ecosystem ECO-MATML
python3 scripts/research_landscape.py discover-pis --area AREA-AI-FOR-MATERIALS --country COUNTRY-US
python3 scripts/research_landscape.py discover-pis --software SW-PYMATGEN --language PROGRAMMING-LANGUAGE-PYTHON
python3 scripts/research_landscape.py discover-pis --ecosystem ECO-MATERIALS-PROJECT
python3 scripts/research_landscape.py discover-universities --area AREA-AI-FOR-MATERIALS --country COUNTRY-US
python3 scripts/research_landscape.py discover-universities --area AREA-MACHINE-LEARNED-POTENTIALS --ecosystem ECO-MATML
python3 scripts/research_landscape.py discover-ecosystems --area AREA-MACHINE-LEARNED-POTENTIALS
python3 scripts/research_landscape.py discover-ecosystems --area AREA-MACHINE-LEARNED-POTENTIALS --software SW-FAIRCHEM
python3 scripts/research_landscape.py discover-software --area AREA-MACHINE-LEARNED-POTENTIALS --language PROGRAMMING-LANGUAGE-PYTHON --ecosystem ECO-MATML
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

The generated repository-health report also includes a research-area discovery
coverage matrix: direct reviewed group and PI relations, software
classification, direct-host Universities, and ecosystem paths for each
controlled area. These are maintenance coverage counts, not a score or a
statement about the importance or quality of an area.

It also includes a programming-language discovery coverage matrix: source-backed
software `implemented_in` assertions, plus direct group, PI, direct-host
University, and ecosystem paths through those software records. These counts
measure corpus coverage only; they do not claim software quality, adoption, a
group-wide language policy, individual skill, or fit.

`recommend` validates the corpus and the versioned public recommendation model,
then derives evidence-discovery results in `reports/generated/`. It exposes
documented matching signals, confidence, coverage, and unavailable dimensions;
it does not rank prestige, calculate private accessibility, or infer missing
evidence.

`recommend --list` renders a deterministic catalog of public query IDs, titles,
aliases, and available/unavailable status. It reads no private profile or
shortlist data. `recommend --query <id-or-alias>` renders one listed query for
interactive discovery; neither form writes generated output.

`catalog` lists the reviewed canonical Research Area, Country, Research
Software, and Programming Language IDs accepted by the interactive discovery
commands. It is public, deterministic, and non-generated; it contains no
private preferences or ranking data.

`discover-groups` is an interactive, non-generated AND filter over reviewed
Research Groups. It accepts one or more canonical `--area`, `--country`,
`--software`, `--language`, and `--ecosystem` IDs. The command shows the source-backed path
that satisfied each criterion: country follows the group's ADR 0006 direct
host, and language follows a documented group-development edge through a
Research Software `implemented_in` assertion. It is alphabetically ordered and
does not rank or infer fit.

An ecosystem match follows a documented group `develops` → software → ecosystem
`includes` path. It does not claim that the group belongs to, owns, or governs
the ecosystem.

`discover-pis` uses the same filters for reviewed Principal Investigators.
Country evidence follows an explicitly documented public `affiliated_with` path
to a University, Department, or Organization and then its documented country;
it does not infer employment, current availability, or supervision capacity. An
ecosystem match follows a documented PI `develops` → software → ecosystem
`includes` path rather than inferring membership.

`discover-universities` finds reviewed Universities through their documented
country and the ADR 0006 direct-host paths of reviewed Research Groups. Area,
software, language, and ecosystem signals name the hosted group that supplied
them. An ecosystem match displays the direct-host University → Group → Software
→ Ecosystem `includes` path; it does not assert university ecosystem membership.
The result is an evidence-discovery view of documented paths, not a comparison
of university strength, degree quality, ecosystem completeness, or admissions.

`discover-ecosystems` is an interactive, non-generated AND filter over
reviewed Research Ecosystems. It accepts canonical `--area` and `--software`
IDs. Area paths are limited to sourced `connects` relations to an entity with a
direct topic relation, or sourced `includes` relations to software with a
documented area classification. The command is alphabetically ordered and does
not assess ecosystem dominance, completeness, performance, or fit.

`discover-software` is an interactive, non-generated AND filter over reviewed
Research Software. It accepts canonical `--area`, `--language`, and
`--ecosystem` IDs. An area match follows the software record's sourced direct
classification, a language match follows its sourced `implemented_in`
assertion, and an ecosystem match follows the ecosystem's sourced `includes`
assertion. The command is alphabetically ordered and does not assess software
quality, performance, adoption, maintenance, support, or fit.

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
