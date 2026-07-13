# AFLOW High-Throughput Materials Screening Problem Vertical Slice

**Status:** reviewed evidence-bounded slice, 2026-07-13.

## Scope

This slice adds High-Throughput Materials Screening as a first-class Research
Problem. It is bounded to high-throughput materials screening with
first-principles calculations and data informatics, not a claim about the best
screening methodology, DFT setup, property target, dataset, workflow, software,
research group, or researcher.

## Canonical path

```text
PROBLEM-HIGH-THROUGHPUT-MATERIALS-SCREENING
  addresses → AREA-COMPUTATIONAL-MATERIALS-SCIENCE

SW-AFLOW
  supports → PROBLEM-HIGH-THROUGHPUT-MATERIALS-SCREENING
  implemented_in → PROGRAMMING-LANGUAGE-CPP

ECO-AFLOW
  includes → SW-AFLOW
```

Each arrow above has its own record-local source ID. Ecosystem inclusion does
not establish dominance, completeness, ownership, support, or applicant fit.

## Evidence boundary

AFLOW official documentation describes high-throughput materials discovery
using DFT and data informatics as a screening strategy. That supports the
bounded software-to-problem assertion, controlled area classification, and
direct discovery paths. It does not establish screening quality, database
coverage, scientific importance, software superiority, funding, mentorship,
openings, or applicant fit.

## Discovery

```bash
python3 scripts/research_landscape.py discover-problems --software SW-AFLOW
python3 scripts/research_landscape.py discover-software --problem PROBLEM-HIGH-THROUGHPUT-MATERIALS-SCREENING
python3 scripts/research_landscape.py discover-ecosystems --problem PROBLEM-HIGH-THROUGHPUT-MATERIALS-SCREENING
python3 scripts/research_landscape.py discover-problems --language PROGRAMMING-LANGUAGE-CPP
python3 scripts/research_landscape.py inspect --entity PROBLEM-HIGH-THROUGHPUT-MATERIALS-SCREENING
```

All outputs are deterministic evidence discovery, not rankings or comparative
recommendations.
