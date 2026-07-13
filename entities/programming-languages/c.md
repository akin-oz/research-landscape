---
schema_version: 2
entity_type: programming-language
id: PROGRAMMING-LANGUAGE-C
name: C
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids: [SRC-SPGLIB-DOCUMENTATION]
label: C
website: https://en.cppreference.com/w/c
---

# C

C is the controlled programming-language entity for explicitly documented
research-software implementation links. It is not a proxy for an individual's
skill, a research group's working language, a training requirement, or
applicant fit.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-SPGLIB-DOCUMENTATION` | [Spglib documentation](https://spglib.readthedocs.io/en/stable/) describes Spglib as a library for finding and handling crystal symmetries written in C. Accessed 2026-07-13. |

## Boundary and limitations

This entity records only the language concept. A software record must carry an
evidence-bearing `implemented_in` assertion before a language-based discovery
query may use it.
