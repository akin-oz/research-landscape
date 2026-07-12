---
schema_version: 2
entity_type: research-software
id: SW-M3GNET
name: M3GNet
status: reviewed
created_at: "2026-07-12"
updated_at: "2026-07-12"
last_review: "2026-07-12"
confidence: high
source_ids:
  - SRC-M3GNET-REPOSITORY
  - SRC-M3GNET-PUBLICATION
repository_url: https://github.com/materialyzeai/m3gnet
website: https://github.com/materialyzeai/m3gnet
license: BSD-3-Clause
open_source: "yes"
research_area_ids:
  - AREA-MACHINE-LEARNED-POTENTIALS
programming_language_ids:
  - PROGRAMMING-LANGUAGE-PYTHON
relationship_assertions:
  - predicate: implemented_in
    target_id: PROGRAMMING-LANGUAGE-PYTHON
    source_ids: [SRC-M3GNET-REPOSITORY]
    confidence: high
    evidence_window: 2025-04
    notes: The archived project repository documents pip installation and Python 3.9 environment setup for the M3GNet implementation. This is a software implementation-language claim, not a current group-language policy or individual skill claim.
---

# M3GNet

M3GNet is the distinct historical graph-neural-network implementation
described by the 2022 M3GNet article. Its public repository is archived and
states that MatGL has replaced it; it remains represented as a reference
implementation so the paper, its code, and the successor software are not
collapsed into one artifact.

## Evidence

| Source ID | Evidence |
| --- | --- |
| `SRC-M3GNET-REPOSITORY` | [materialyzeai/m3gnet](https://github.com/materialyzeai/m3gnet) is a public archived repository for the M3GNet materials graph network; it states that MatGL replaces this implementation and that the repository is retained as a reference implementation. The repository identifies the BSD-3-Clause license and documents pip installation plus a Python 3.9 environment. Accessed 2026-07-12. |
| `SRC-M3GNET-PUBLICATION` | [Nature Computational Science: A universal graph deep learning interatomic potential for the periodic table](https://www.nature.com/articles/s43588-022-00349-3) describes M3GNet as a universal graph-deep-learning interatomic potential and links its source code in the article's code-availability section. Accessed 2026-07-12. |

## Boundary and limitations

This record does not claim that the archived M3GNet repository is maintained,
that MatGL is identical to M3GNet, or that an author, Materialyze.AI Lab, or
any organization currently develops or governs the archived code. It makes no
performance comparison, release-quality, support, opening, funding,
mentorship, admission, or applicant-fit claim.
