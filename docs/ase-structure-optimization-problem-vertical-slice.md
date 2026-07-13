# ASE Structure-Optimization Research Problem Vertical Slice

**Status:** reviewed evidence-bounded slice, 2026-07-13.

## Scope

This slice adds Atomistic Structure Optimization as a first-class Research
Problem. It is bounded to optimizing or relaxing atomistic structures through
local or global methods, not a claim about the best optimizer, calculator,
potential, starting geometry, workflow, software, research group, or
researcher.

## Canonical path

```text
PROBLEM-ATOMISTIC-STRUCTURE-OPTIMIZATION
  addresses → AREA-COMPUTATIONAL-MATERIALS-SCIENCE

SW-ASE
  supports → PROBLEM-ATOMISTIC-STRUCTURE-OPTIMIZATION
  implemented_in → PROGRAMMING-LANGUAGE-PYTHON

ECO-ASE
  includes → SW-ASE

RG-DTU-CAMD
  develops → SW-ASE
```

Each arrow above has its own record-local source ID. The group-development path
does not claim that CAMD works on, owns, endorses, supervises, or is available
for the named problem.

## Evidence boundary

ASE's official documentation identifies local and global structure-optimization
algorithms and optimization classes that relax atomic positions; it also
documents optional cell optimization through filter classes. CAMD's published
atomic-scale materials-design page supplies the controlled Computational
Materials Science classification. Neither source establishes an optimizer's
quality, convergence on a specific system, calculator or potential coverage,
performance, support, maintenance activity, funding, mentorship, openings, or
applicant fit.

## Discovery

```bash
python3 scripts/research_landscape.py discover-problems --software SW-ASE
python3 scripts/research_landscape.py discover-software --problem PROBLEM-ATOMISTIC-STRUCTURE-OPTIMIZATION
python3 scripts/research_landscape.py discover-ecosystems --problem PROBLEM-ATOMISTIC-STRUCTURE-OPTIMIZATION
python3 scripts/research_landscape.py discover-groups --problem PROBLEM-ATOMISTIC-STRUCTURE-OPTIMIZATION
python3 scripts/research_landscape.py discover-problems --language PROGRAMMING-LANGUAGE-PYTHON
python3 scripts/research_landscape.py inspect --entity PROBLEM-ATOMISTIC-STRUCTURE-OPTIMIZATION
```

All outputs are deterministic evidence discovery, not rankings or comparative
recommendations.
