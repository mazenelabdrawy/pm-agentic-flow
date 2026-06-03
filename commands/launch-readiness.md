---
description: Pressure-test a launch like a skeptical VP — model card, rollback plan, monitoring hooks, on-call — and return a ready/not-ready verdict.
argument-hint: (reads deploy, prd metrics, responsible-ai from the PCO)
---

# /launch-readiness

Load the `launch-readiness` skill (`skills/launch-readiness/SKILL.md`) and run it.

Read `deploy`, `prd.metrics`, and any `responsible-ai` from `PRODUCT_CONTEXT.md`. Interrogate the launch: model card/spec sheet, rollback plan, monitoring hooks & alerts, on-call ownership, kill criteria. For each, mark present / partial / missing and what's needed. Write the `launch-readiness` section ending in **ready / not-ready** with ordered blockers. A missing rollback plan or un-instrumented success metric is not-ready; those blockers flow into `deploy.rollout-notes`.
