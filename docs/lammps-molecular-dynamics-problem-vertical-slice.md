# LAMMPS Molecular-Dynamics Research Problem Vertical Slice

**Status:** reviewed evidence-bounded slice, 2026-07-13.

## Scope

This slice adds Atomistic Molecular Dynamics Simulation as a first-class
Research Problem. It is bounded to the challenge of classical atomistic
molecular-dynamics simulation for materials modelling, not a claim about the
best potential, model, workflow, software, research group, or researcher.

## Canonical path

```text
PROBLEM-ATOMISTIC-MOLECULAR-DYNAMICS-SIMULATION
  addresses → AREA-COMPUTATIONAL-MATERIALS-SCIENCE

SW-LAMMPS
  supports → PROBLEM-ATOMISTIC-MOLECULAR-DYNAMICS-SIMULATION
  implemented_in → PROGRAMMING-LANGUAGE-CPP

ECO-LAMMPS
  includes → SW-LAMMPS

PI-AXEL-KOHLMEYER
  develops → SW-LAMMPS
```

Each arrow above has its own record-local source ID. The `develops` path does
not claim that the PI works on, owns, endorses, supervises, or is available for
the named problem.

## Evidence boundary

LAMMPS official documentation describes a classical molecular-dynamics
simulation code focused on materials modelling. That supports the bounded
software-to-problem assertion and the problem's controlled-area link. It does
not establish model quality, force-field coverage, performance, support,
maintenance activity, ecosystem dominance, funding, mentorship, openings, or
applicant fit.

## Discovery

```bash
python3 scripts/research_landscape.py discover-problems --software SW-LAMMPS
python3 scripts/research_landscape.py discover-software --problem PROBLEM-ATOMISTIC-MOLECULAR-DYNAMICS-SIMULATION
python3 scripts/research_landscape.py discover-ecosystems --problem PROBLEM-ATOMISTIC-MOLECULAR-DYNAMICS-SIMULATION
python3 scripts/research_landscape.py discover-pis --problem PROBLEM-ATOMISTIC-MOLECULAR-DYNAMICS-SIMULATION
python3 scripts/research_landscape.py discover-problems --language PROGRAMMING-LANGUAGE-CPP
python3 scripts/research_landscape.py inspect --entity PROBLEM-ATOMISTIC-MOLECULAR-DYNAMICS-SIMULATION
```

All outputs are deterministic evidence discovery, not rankings or comparative
recommendations.
