# Quality Gate 7 review: explainable recommendations

**Gate status:** complete

**Review date:** 2026-07-12

## Gate outcome

Quality Gate 7 adds a deterministic, public evidence-discovery recommendation
model in
[`scoring/v1/evidence-recommendations.yaml`](../scoring/v1/evidence-recommendations.yaml).
The automation reads only reviewed canonical records and direct typed
relationships, then generates
[`evidence-recommendations.md`](generated/evidence-recommendations.md). It is
not an AI system and does not calculate prestige, quality, mentorship, or
accessibility rankings.

## Supported recommendations

The model supports explainable discovery queries for:

- research groups with documented software development;
- research groups in Computational Materials Science or Materials Informatics;
- groups with licensed open-source software connections;
- software-oriented research environments for an experienced software engineer;
- ecosystems connected to either controlled research area; and
- Principal Investigators with direct controlled-area relations.

Each generated candidate shows its canonical link/ID, direct matching evidence
and record-local source IDs, confidence, criterion coverage, and a
query-specific limitation. Results are ordered by direct evidence-signal count,
then stable name/ID; this is a reproducible discovery priority, not an
evaluation of people or institutions.

## Explicitly unavailable recommendations

Python-heavy groups and high-mentorship environments are emitted as
**unavailable**, not as empty or negative lists. The report explains that the
reviewed corpus lacks, respectively, a governed programming-language relation
contract and a comparable, ethically valid mentorship metric with sufficient
coverage. This makes missing information a maintenance/research task rather
than a hidden inference.

## Quality and boundary review

| Gate rule | Result |
| --- | --- |
| Deterministic and non-AI | Passed. The versioned YAML model and Python evaluator use only declared direct relationships and stable ordering. |
| Explainability | Passed. Every available row gives matching predicates, target IDs, record-local source IDs, confidence, coverage, and limitations. |
| No prestige ranking | Passed. The model has no institution, country, citation, award, popularity, or reputation input. |
| Evidence first | Passed. Candidate membership requires reviewed canonical records and typed source-bearing assertions. |
| Unknowns preserved | Passed. Unsupported Python and mentorship queries are explicitly unavailable rather than scored as zero. |
| Personal/privacy boundary | Passed. No personal profile, accessibility, admissions, immigration, funding eligibility, or contact data is used. |
| Reproducibility | Passed. `recommend --check` detects output drift using a canonical-input fingerprint and runs in CI. |

## Verification record

On 2026-07-12 the following passed:

```text
python3 scripts/research_landscape.py validate
python3 scripts/research_landscape.py recommend
python3 scripts/research_landscape.py recommend --check
python3 -m unittest discover -s scripts/tests
```

The generated recommendation report contains only canonical links and direct
evidence signals. It preserves the corpus validation result of 67 v2 entities
and 116 typed relationship assertions with no structural errors or health
warnings.

## Known limitations and QG8 handoff

- Query coverage remains limited to the reviewed canonical corpus.
- Source IDs are record-local citations rather than a source graph.
- Enabling language-, mentorship-, accessibility-, or admissions-sensitive
  recommendations requires new evidence contracts and review; no narrative
  shortcut is allowed.

Quality Gate 8 can use the validator and generated health report to audit
metadata completeness, relationship coverage, evidence gaps, automation
coverage, view coverage, and cross-reference quality across the whole
repository.
