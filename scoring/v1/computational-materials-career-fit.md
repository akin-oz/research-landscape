# Computational-materials career-fit scorecard v1

**Purpose:** compare a *specific applicant, project and lab*, not people, universities or countries in the abstract.  
**Status:** operational scoring contract for the global research-intelligence collection.  
**Rule:** a score without an evidence table is invalid.

## Weights for the declared candidate profile

| Dimension | Weight | Evidence required before scoring | Never infer from |
| --- | ---: | --- | --- |
| Research fit | 16 | Current project question, methods and recent work. | Department prestige. |
| Scientific software fit | 17 | Maintained code, workflows, engineering roles or explicit practice. | A personal GitHub account. |
| Materials fit | 16 | Direct overlap with computational materials methods/domain. | Broad “AI” branding. |
| Open-source culture | 13 | Public licence, releases, contribution route, documentation and governance. | A code dump. |
| Mentorship | 13 | Current/alumni evidence, clear supervision process, student conversation. | Awards, citations or group size. |
| International network | 7 | Dated multi-institution projects, visiting/alumni/collaboration evidence. | Country or institutional reputation. |
| Career ROI | 7 | Transferable methods, portfolio outputs and plausible next-step options. | Salary rumours or rankings. |
| Industry connections | 4 | Named, relevant public collaborations or translational project evidence. | Regional industry density. |
| Long-term opportunities | 7 | Durable community/platform, transferable skills and research direction. | A single current grant. |
| **Total** | **100** |  |  |

## Calculation

Each available dimension receives an integer **0–5**, where 0 is a documented mismatch, 3 is a credible but bounded fit and 5 is unusually direct, well-evidenced fit. Unknown is blank, not zero.

```
overall_compatibility =
  sum(weight_i * score_i for available i) / sum(weight_i for available i)
```

Report both `overall_compatibility / 5`, **coverage** (`available weight / 100`) and the lowest confidence among material dimensions. Do not compare two overall scores whose coverage differs by more than 15 percentage points without an explicit sensitivity analysis.

## Confidence gates

- **High:** current primary source plus corroboration where the claim is consequential.
- **Medium:** current direct evidence with one important missing context.
- **Low:** indirect, older or incomplete evidence; use only as a research prompt.
- **Unavailable:** no defensible score.

Mentorship, immigration, work-life balance and current funding normally start as **unavailable**. They become scoreable only after programme documents and human conversations supply relevant, ethical evidence.

