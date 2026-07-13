---
schema_version: 2
entity_type: research-software
id: SW-GPAW
name: GPAW
status: reviewed
created_at: "2026-07-13"
updated_at: "2026-07-13"
last_review: "2026-07-13"
confidence: high
source_ids:
  - SRC-GPAW-DOCUMENTATION
  - SRC-GPAW-INSTALLATION
  - SRC-GPAW-LICENSE
research_area_ids:
  - AREA-COMPUTATIONAL-MATERIALS-SCIENCE
  - AREA-DENSITY-FUNCTIONAL-THEORY-AND-ELECTRONIC-STRUCTURE
open_source: "yes"
website: https://gpaw.readthedocs.io/
repository_url: https://gitlab.com/gpaw/gpaw
license: GPL-3.0-or-later
programming_language_ids:
  - PROGRAMMING-LANGUAGE-PYTHON
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-GPAW-DOCUMENTATION, SRC-GPAW-INSTALLATION]
    confidence: high
    evidence_window: 2026-07
    notes: GPAW's official documentation identifies it as a Python DFT code, with mostly Python implementation and performance-critical C code. This records a documented implementation path, not a group-wide language policy or individual skill claim.
  - predicate: supports
    target_id: PROBLEM-DENSITY-FUNCTIONAL-ELECTRONIC-STRUCTURE-CALCULATION
    source_ids: [SRC-GPAW-DOCUMENTATION]
    confidence: high
    evidence_window: 2026-07
    notes: GPAW documentation describes a DFT code and electronic-structure calculation tutorials; this assertion is limited to support for the named computational challenge.
---

# GPAW

GPAW is represented as a distinct open-source DFT and electronic-structure
software artifact. Its separate ecosystem record owns the public installation,
learning, contribution, testing, and contact surfaces; this record does not
model every calculation mode, setup, basis, dependency, accelerator, developer,
or user.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-GPAW-DOCUMENTATION` | [GPAW documentation](https://gpaw.readthedocs.io/) describes GPAW as a density-functional-theory Python code based on the projector-augmented-wave method and the Atomic Simulation Environment (ASE). Accessed 2026-07-13. |
| `SRC-GPAW-INSTALLATION` | [GPAW installation](https://gpaw.readthedocs.io/install.html) identifies ASE as a required Python library and states that GPAW is mostly written in Python with C code for performance-critical parts and external numerical-library interfaces. Accessed 2026-07-13. |
| `SRC-GPAW-LICENSE` | [GPAW LICENSE](https://gitlab.com/gpaw/gpaw/blob/master/LICENSE) publishes GNU General Public License version 3 or later terms for GPAW. Accessed 2026-07-13. |

## Boundary and limitations

This record does not establish that every GPAW component, configuration,
dependency, setup, output, benchmark, or workflow shares a single
implementation or support condition. It makes no claim about performance,
correctness, review, support, funding, openings, mentoring, admissions, or
applicant fit.
