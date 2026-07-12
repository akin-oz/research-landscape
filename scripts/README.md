# Scripts

`research_landscape.py` is the repository's deterministic knowledge-graph
validator and projection tool. It reads canonical entity Markdown and
`views/definitions.yaml`; it never writes facts back to entities or invents
relationships.

Install the reproducible development dependencies first:

```bash
python3 -m pip install -r requirements-dev.txt
```

Run structural validation:

```bash
python3 scripts/research_landscape.py validate
```

Generate public navigation projections and the repository-health report:

```bash
python3 scripts/research_landscape.py generate
```

Verify that committed generated output is current without writing files:

```bash
python3 scripts/research_landscape.py generate --check
python3 scripts/research_landscape.py recommend
python3 scripts/research_landscape.py recommend --check
python3 -m unittest discover -s scripts/tests
```

Generated files live in `views/generated/` and `reports/generated/`. They are
reviewable projections containing concise metadata and canonical links; do not
edit them manually. Correct data at its canonical owner, then regenerate.

The tool validates v2 frontmatter/schema shape, stable-ID uniqueness, reference
and relationship integrity, record-local source IDs, ADR 0006 group hosts,
local Markdown links, duplicate-name signals, and orphan-entity signals. It
also produces quality metrics by entity type, confidence, and predicate. Do not
put credentials or unreviewed scraping logic in this directory.
