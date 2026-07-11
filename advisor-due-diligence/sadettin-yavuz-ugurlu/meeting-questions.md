---
report_type: advisor-due-diligence-meeting-questions
advisor_id: TR-AKU-MSE-ADV-005
status: evidence-reviewed
evidence_window: public primary sources accessed 2026-07-11
confidence: medium
---

# Meeting questions — Sadettin Yavuz Uğurlu

These questions are designed for a research conversation. They are deliberately
not an admissions script. Ask only the subset that follows naturally from the
conversation; curiosity and listening are more valuable than completing a list.

## Research direction and scientific ownership

1. **“Of the directions visible in your recent work, which one is genuinely
   active in Antalya now?”**

   Why: distinguishes a publication history from a current research programme.
   The public record shows active molecular ML and the coating repository, but
   does not identify a current student project or lab roadmap. [AVESIS
   publications](https://avesis.akdeniz.edu.tr/syavuzugurlu/yayinlar)
   **Evidence basis: fact; confidence high.**

2. **“What scientific decision in the coating work would you most like to make
   more reliable next—generalisation across motifs, uncertainty, experimental
   validation, or data provenance?”**

   Why: lets the advisor define the real problem rather than forcing a software
   agenda onto it. [Coating repository](https://github.com/yauz3/coating_motifs_ml)

3. **“For a materials-informatics thesis, who would own the experimental
   interpretation and what would count as a convincing validation?”**

   Why: a prediction alone is not a materials result. It invites a concrete
   co-supervision discussion without assuming Emre Bal's availability.

4. **“Which parts of your CoBDock/MEF-AlloSite style of validation would you
   insist on when the data are experimental materials measurements?”**

   Why: demonstrates that the candidate has read the methodological work, and
   tests whether validation philosophy transfers across domains.
   [CoBDock](https://doi.org/10.1186/s13321-023-00793-x)
   [MEF-AlloSite](https://doi.org/10.1186/s13321-024-00882-5)

5. **“Would a thesis that produces both a materials result and a reusable,
   testable Python workflow be valuable in your group? What balance would you
   expect between the two?”**

   Why: directly tests fit for scientific software engineering while allowing an
   honest “the scientific result matters more” answer.

## Data, permission, and reproducibility

6. **“Is there a legally and academically usable subset of the EBC data that a
   student could analyse and eventually describe in a thesis/paper?”**

   Why: the repository says raw indentation data are withheld for ownership
   reasons. [Repository README](https://github.com/yauz3/coating_motifs_ml)
   This is a non-negotiable gate, not a bureaucratic afterthought.

7. **“May I see the data dictionary, unit conventions, specimen hierarchy, and
   what each motif means before proposing a model?”**

   Why: prevents pseudo-replication and accidental leakage. Do not ask to take a
   copy away or access protected data before permission is granted.

8. **“How are train/test boundaries defined here: by indentation point, specimen,
   coating run, or motif? Which grouping is scientifically independent?”**

   Why: the current code's train-on-E/test-on-A–D setup is promising, but the
   statistical unit needs a materials-scientist explanation. [Training code](https://github.com/yauz3/coating_motifs_ml/blob/main/02_model_training_and_validate.py)

9. **“Could we agree on a public synthetic or surrogate benchmark so the pipeline
   can be tested and documented without releasing restricted measurements?”**

   Why: turns a confidentiality constraint into an open-science design problem.

10. **“What are the publication, IP, data-retention and code-release expectations
    before any work begins?”**

    Why: the public repositories have mixed licence explicitness; clarify rather
    than assume open release. [GitHub profile](https://github.com/yauz3)

## Supervision and group reality

11. **“Who are the current MSc/PhD researchers I would work alongside, and what
    kinds of outputs have recent students produced?”**

    Why: public sources reviewed did not establish a student roster or outcomes.
    [AVESIS experience/theses](https://avesis.akdeniz.edu.tr/syavuzugurlu/deneyim)
    **Classification: unknown; confidence high.**

12. **“How do you normally structure a first semester: reading, a replication,
    data familiarisation, a pilot, or an immediate research question?”**

    Why: reveals mentoring style through a concrete process rather than a vague
    question about being ‘supportive’.

13. **“How often do you meet with MSc students, and how do you prefer code,
    experiments and drafts to be reviewed?”**

    Why: compatible cadence is one of the most important but non-public factors.

14. **“If a materials co-supervisor is needed, would you be comfortable defining
    the boundaries and authorship roles at the start?”**

    Why: avoids a student carrying an unowned interdisciplinary problem.

15. **“What would make you decide that a software-oriented project is too large
    for an MSc, and how would you reduce it?”**

    Why: tests thesis-scoping judgement and protects against a tool becoming a
    multi-year product project.

## Scientific software and candidate contribution

16. **“I noticed environment instructions and reproducibility notes in several
    repositories. Which part of the current workflow would benefit most from
    stronger tests, data validation, packaging, or automation?”**

    Why: specific, respectful and evidence-based. Do not say that the current
    code is ‘bad.’ [CoBDock repository](https://github.com/yauz3/cobdock)
    [Coating repository](https://github.com/yauz3/coating_motifs_ml)

17. **“Would a versioned data schema and model card help your next student reuse a
    project, or would it create overhead without a clear scientific return?”**

    Why: tests whether RSE work is valued as research infrastructure.

18. **“In the dipole project, how did the twin-pair analysis change your view of
    what a good model claim should be? Could an analogous diagnostic be defined
    for coating measurements?”**

    Why: shows deep engagement with an actual recent methodological contribution.
    [Paper](https://doi.org/10.1186/s13321-026-01215-4)

19. **“If I contributed a public Python artifact, what minimum standard would you
    want for reproducibility, documentation, authorship and maintenance after the
    thesis?”**

    Why: turns open-source enthusiasm into an explicit supervisory agreement.

## Long-term development

20. **“Which skills would you want a student with my background to build before
    trying to claim ‘AI for materials discovery’?”**

    Why: invites correction and creates a learning plan grounded in his view.

21. **“Have recent students continued to doctoral programmes or external
    collaborations? If so, what evidence or artifacts made their applications
    stronger?”**

    Why: this is appropriate career advice, not a demand for a future reference.
    Public placement evidence was not verified; an answer must be confirmed with
    names/results the advisor is comfortable sharing.

22. **“Would you recommend that I first build a small replication or contribution
    before considering a formal thesis proposal?”**

    Why: it offers a low-risk, research-first route.

## Questions **not** to ask in the first meeting

| Avoid | Why it weakens the conversation | Better move |
| --- | --- | --- |
| “Will you admit/supervise me?” | Turns research fit into a transactional yes/no before the work is defined. | Ask whether a short research-direction discussion is worthwhile and what evidence is needed to scope a pilot. |
| “Can you guarantee an international PhD/reference?” | No public source can support such a promise, and it puts the advisor in an unfair position. | Ask how past students built strong external applications and what outputs matter. |
| “Can I use all your data/code?” | Ignores ownership, privacy and collaboration norms. | Ask what subset, permissions and access process would be appropriate. |
| “Can we turn Materials Atlas/Research Landscape into my thesis?” | Centres the candidate's product rather than a materials research problem. | Offer their methods only as supporting infrastructure for a live scientific question. |
| “Why don't your repos have tests/CI?” | Sounds accusatory and assumes a public repository shows the entire workflow. | Ask which reproducibility improvement would create the highest scientific value. |
| “What is the easiest publishable AI topic?” | Signals metric-seeking rather than scientific curiosity. | Ask about an open uncertainty or validation problem that would matter to the group. |
| “Can I start contributing before enrolment?” | Can create unprotected labour and IP ambiguity. | Ask whether a small public replication/reading exercise is appropriate, with clear boundaries. |

## Evidence-aware listening checklist

Write down exact answers to these before leaving:

- What live problem/dataset exists now?
- Who owns data and experimental validation?
- Is a co-supervisor named and willing?
- What can be made public, and under which licence/IP terms?
- What is the smallest first-semester milestone?
- How will success, authorship and supervision cadence be defined?

If more than two remain vague, do not interpret enthusiasm as a go signal. The
appropriate next step is a follow-up concept note only after those uncertainties
are resolved.
