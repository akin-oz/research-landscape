# Scoring model

The model describes fit as a vector of dimension scores, each on a 0–100 scale where sufficient evidence exists. It does not create a universal ranking. Scoring contracts are immutable by major version under [`scoring/`](../scoring/); reports record the exact model reference. Applicants may supply weights to calculate a compatibility score:

`compatibility = Σ(weightᵢ × dimension scoreᵢ) / Σ(weightᵢ for available dimensions)`

The output must list unavailable dimensions, coverage, confidence, evidence window, and `scoring-model` version. Scores are calculated only from metric definitions in this repository. No score may be derived from institutional reputation, nationality, demographics, or unverified anecdotes.

Dimensions: research alignment, publication activity, research quality, mentorship, open science, software engineering, scientific computing, international collaboration, industry collaboration, student outcomes, funding activity, and interdisciplinary work. See [v1 weights](../scoring/v1/weights.md) and the versioned entity score contracts.
