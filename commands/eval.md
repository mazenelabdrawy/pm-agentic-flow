---
description: Score the prototype spec and PRD against the team rubric — per-criterion scores, an aggregate, and the pass/fail verdict that gates deploy.
argument-hint: (reads prototype-spec, prd, synthesis from the PCO)
---

# /eval

Load the `eval-runner` skill (`skills/eval-runner/SKILL.md`) and run it.

Read `eval/rubric.yaml` for `scoring_criteria`, weights, `threshold`, and `per_criterion_floor`. Read `prd`, `prototype-spec`, and `synthesis` from `PRODUCT_CONTEXT.md`. Score each criterion 0.0–1.0 with justification, compute the weighted aggregate, and apply the `eval-threshold` gate per `eval/checks/score.md`.

Write the `eval-results` section (per-criterion table, aggregate vs threshold, overall verdict). Report `pass`/`fail`; on fail, name which upstream agent should fix what. This verdict is the precondition for `/deploy`.
