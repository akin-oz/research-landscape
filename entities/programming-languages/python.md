---
schema_version: 2
entity_type: programming-language
id: PROGRAMMING-LANGUAGE-PYTHON
name: Python
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-PYTHON-LANGUAGE-REFERENCE
label: Python
website: https://www.python.org/
---

# Python

Python is the controlled programming-language entity for explicitly documented
software implementation links. It is not a proxy for an individual’s skills,
a research group's working language, a training requirement, or applicant fit.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-PYTHON-LANGUAGE-REFERENCE` | [Python Language Reference](https://docs.python.org/3/reference/introduction.html) identifies itself as the reference manual for the Python programming language. Accessed 2026-07-12. |

## Boundary and limitations

This entity records only the language concept. A software record must carry an
evidence-bearing `implemented_in` assertion before a language-based discovery
query may use it.
