# Funding view

This public view answers: which reviewed funding programmes and projects have
documented, time-bounded connections? Its canonical contract is `funding` in
[`../definitions.yaml`](../definitions.yaml).

The view must preserve dates and source-backed relationship direction. A
historical grant or completed project must never be displayed as current funding
or an available opportunity. Results are deliberately absent until Quality Gate
6 implements deterministic generation.
