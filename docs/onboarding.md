# Contributor onboarding

Research Landscape is a Markdown-first, evidence-backed knowledge graph. A
contribution is successful when another maintainer can identify its canonical
owner, evidence, relationship semantics, validation path, and limits without
asking the original author.

## First 15 minutes

1. Read the [repository information architecture](REPOSITORY_INFORMATION_ARCHITECTURE.md) and [repository boundaries](REPOSITORY_BOUNDARIES.md).
2. Read [entity authoring](entity-authoring.md) before creating or changing a
   canonical record; read [review process](review-process.md) before opening a
   pull request.
3. Choose the artifact type: a reusable public fact belongs in `entities/`; a
   bounded interpretation belongs in `reports/`; a repeatable rule belongs in
   `docs/`, `schemas/`, `scoring/`, or `scripts/`; applicant-owned work belongs
   outside the public canonical graph.
4. Run the local validation workflow before and after your edit.

## Essential commands

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/research_landscape.py validate
python3 scripts/research_landscape.py generate
python3 scripts/research_landscape.py recommend
python3 -m unittest discover -s scripts/tests
python3 scripts/research_landscape.py generate --check
python3 scripts/research_landscape.py recommend --check
```

Generated files under `views/generated/` and `reports/generated/` are outputs,
not authoring surfaces. Change canonical inputs or a versioned definition, then
regenerate; never edit them by hand.

## Start with a small slice

Prefer one entity plus the smallest sourced set of necessary relationships and
one reviewable documentation update. Do not bulk-import names, infer metadata
from proximity, turn a paper author into a maintainer, or create inverse
relationships for convenience. When identity, predicate, evidence, or ownership
is unclear, leave the claim out and explain the limitation in the entity or
review record.

## Help routes

- Correct public evidence with the evidence-correction issue template.
- Propose a bounded future report with the report-request template.
- Propose architectural changes through an ADR discussion; do not silently
  change a schema, entity type, predicate, or canonical boundary in a content
  pull request.
- Report security issues privately as described in [SECURITY.md](../SECURITY.md).
