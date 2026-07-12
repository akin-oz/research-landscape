## Purpose

## Evidence and methodology

- [ ] Every factual claim is sourced and has an access date.
- [ ] Confidence and missing-data treatment are explicit.
- [ ] Facts are separated from interpretation.
- [ ] Scoring inputs, version, and coverage are reproducible.
- [ ] I disclosed relevant conflicts of interest.
- [ ] Canonical ownership and relationship direction are explicit; generated output was not edited by hand.

## Validation

- [ ] `python3 scripts/research_landscape.py validate`
- [ ] `python3 scripts/research_landscape.py generate --check`
- [ ] `python3 scripts/research_landscape.py recommend --check` (when recommendation inputs/output change)
- [ ] `python3 -m unittest discover -s scripts/tests` (when automation changes)

## Notes for reviewers
