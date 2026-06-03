---
description: Track production metrics and incidents after launch, then turn learnings into new bets — closing the loop back to hypothesis.
argument-hint: (reads deploy, prd metrics, problem-statement from the PCO)
---

# /monitor

Load the `monitor` skill (`skills/monitor/SKILL.md`) and run it.

Read `deploy`, `prd.metrics`, and `problem-statement.bets` from `PRODUCT_CONTEXT.md`. Write the `monitor` section: `production-metrics` (actuals vs success metrics, each cited; bet confirmed/killed/inconclusive), `incidents`, and `learnings`.

Write each learning so the next `hypothesis` run can consume it — tag it `→ feeds: problem-statement.bets`. This is the loop-back: the next `/pm-flow` run starts from these learnings.
