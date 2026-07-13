# GPAW ecosystem vertical slice review

**Review date:** 2026-07-13

**Scope:** a bounded GPAW canonicalization covering software, ecosystem, and
the existing CAMD development link.

**Outcome:** the slice adds two canonical entities and three evidence-bearing
relationships. It retains the distinction among GPAW as software, the GPAW
ecosystem contribution surface, and CAMD's independently evidenced group-level
development relationship.

## Evidence coverage

| Claim family | Primary evidence | Review result |
| --- | --- | --- |
| Software purpose | GPAW documentation | Supports DFT, PAW, ASE, and Python-code scope. |
| Openness and implementation | GPAW license and installation documentation | Supports GPL-3.0-or-later and mostly-Python implementation with performance-critical C code. |
| CAMD development | DTU Atomic-scale Materials Design | Supports CAMD's group-level GPAW-development relation. |
| Contribution process | GPAW development workflow | Supports public development environment, tests, merge requests, CI, and review workflow. |

## Relationship review

| Check | Result |
| --- | --- |
| Software ecosystem inclusion | `ECO-GPAW → includes → SW-GPAW` is backed by GPAW's official documentation. |
| Ecosystem and group connection | `ECO-GPAW → connects → RG-DTU-CAMD` is backed by DTU's direct GPAW-development statement. |
| Group software development | `RG-DTU-CAMD → develops → SW-GPAW` has the same direct DTU evidence and does not imply exclusivity. |
| Language implementation | `SW-GPAW → implemented_in → PROGRAMMING-LANGUAGE-PYTHON` is backed by GPAW documentation and installation guidance. |
| Area metadata | GPAW's software record has bounded Computational Materials Science and DFT/Electronic Structure classifications from the documented code scope. |
| No duplicated ownership | Software facts remain in GPAW; participation context remains in its ecosystem record; CAMD's group-level development relation remains a separate assertion. |

## Deliberate non-claims

1. The sources do not establish a complete GPAW contributor, maintainer,
   reviewer, institution, funder, package, dependency, method, or user graph.
2. A GitLab workflow, CI, issue, mailing-list, or chat route does not establish
   membership, review authority, response, support, employment, mentoring,
   supervision, or availability.
3. The documented ASE basis does not create a software-dependency assertion;
   the current relationship contract does not safely represent one.
4. The slice makes no claim about technical performance, scientific quality,
   project activity, funding, openings, admissions, or applicant outcomes.

## Verification record

Acceptance requires clean canonical validation, deterministic generated output
and recommendation checks, and regression coverage of the four-criterion GPAW
software-discovery path. The slice introduces no schema, generator, or scoring
model change.
