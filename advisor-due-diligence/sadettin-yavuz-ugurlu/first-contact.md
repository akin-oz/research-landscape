---
report_type: advisor-due-diligence-first-contact
advisor_id: TR-AKU-MSE-ADV-005
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: medium
---

# First contact — advice-seeking email

## Send only after

- Reading the first four items in [reading-list.md](reading-list.md).
- Replacing bracketed details with truthful, specific information.
- Checking the current institutional contact route on the
  [AVESIS profile](https://avesis.akdeniz.edu.tr/syavuzugurlu).

Do not attach a large portfolio, a speculative proposal, or an admissions form.
One short CV/GitHub link is enough if it adds real context.

## Subject options

- `Research-direction advice: reproducible ML for materials data`
- `Request for a short discussion on scientific software and materials ML`

## Email draft

> Dear Dr. Uğurlu,
>
> I hope you are well. I am a senior software engineer with [X] years of
> experience in software architecture and open-source development. I am now
> deliberately building depth in Scientific Python, computational materials
> science, and AI for materials discovery.
>
> I have been reading your recent work on reproducible computational workflows.
> In particular, CoBDock's use of independent docking/cavity signals and the
> validation design in your experimental dipole-moment work made me think more
> carefully about leakage, uncertainty, and what a model should be allowed to
> claim. I was also very interested in the YbSi–mullite–Si coating ML repository
> with Dr. Emre Bal and Muhammet Karabaş, especially its cross-motif evaluation
> and the challenge of making experimental data workflows reusable.
>
> My strongest contribution is likely to be at the intersection of research and
> engineering: data provenance, reproducible environments, testable Python
> pipelines, documentation, and software that remains useful after one project.
> I maintain a small open project called Materials Atlas, which has made me
> especially interested in how materials evidence and measurement metadata can be
> represented clearly. I would like to apply that discipline to a real scientific
> question rather than build a generic application.
>
> If you would be open to it, I would be grateful for a short conversation to ask
> for your advice: do you see an active materials-data or computational project
> where a carefully scoped, reproducible software contribution could be
> scientifically useful? I am particularly interested in understanding what would
> make a materials-informatics project rigorous enough to pursue further.
>
> I am not writing to ask for an admission decision by email. I would value your
> perspective on the research direction first, and I would be happy to send a
> concise one-page note or my GitHub/CV if useful.
>
> Thank you for your time,
>
> [Name]<br>
> [One-line current role]<br>
> [GitHub / Materials Atlas link, optional]<br>
> [Email / phone]

## Why this wording is calibrated

| Element | Purpose |
| --- | --- |
| CoBDock + dipole + coating references | Shows real reading across methodology and the one direct materials bridge; do not claim to have reproduced results. [CoBDock](https://doi.org/10.1186/s13321-023-00793-x) [Dipole paper](https://doi.org/10.1186/s13321-026-01215-4) [Coating repository](https://github.com/yauz3/coating_motifs_ml) |
| Software contribution description | Positions senior engineering as research-enabling work, not as a demand to run a product-development project. |
| Materials Atlas mention | Keeps it relevant to data/evidence/provenance without pitching it as the thesis. |
| Advice request | Reduces pressure and leaves room for an honest answer about capacity, data, and fit. |
| Explicit no-admission sentence | Avoids transactional framing while preserving the candidate's eventual academic interest. |

## If he responds positively

Reply with thanks and ask for a 20–30 minute meeting. Offer only this one-sentence
agenda:

> I would like to understand the active research direction, the materials
> validation/data boundary, and whether a small reproducibility-focused pilot
> could be scientifically meaningful.

Bring the question set from [meeting-questions.md](meeting-questions.md), but do
not send it as a questionnaire.

## If he asks for a proposal first

Send a one-page **concept note**, not a thesis proposal:

- one materials question;
- named data/experimental assumptions explicitly labelled “to confirm”;
- a 10–12 week pilot;
- one scientific output and one modest software output;
- a clear statement that data access, co-supervision, IP and publication rights
  must be agreed before work begins.

The strongest initial concept is the reproducible EBC benchmark/provenance
package in [meeting-preparation.md](meeting-preparation.md). Do not promise use
of restricted coating data before permission.

## If there is no response

Wait 7–10 business days, then send one brief follow-up. Do not repeatedly message
or escalate through unrelated channels. Lack of response is not evidence about
scholarly quality; it simply means the route is unresolved and should not hold up
the candidate's broader search.
