---
description: Produce the build handoff — handoff doc, build checklist, rollout notes — only after the eval gate has passed.
argument-hint: (requires a passing eval-results in the PCO)
---

# /deploy

Load the `deploy` skill (`skills/deploy/SKILL.md`) and run it.

**Precondition:** confirm `eval-results.verdict` is `pass` in `PRODUCT_CONTEXT.md`. If it is not, stop and return control to `/eval` — do not produce a handoff for un-evaluated work.

Read `prd`, `prototype-spec`, and any `responsible-ai` / `launch-readiness`. Using `templates/handoff.template.md`, write the `deploy` section (`handoff-doc`, `build-checklist`, `rollout-notes`). Commit the PCO with a clear message. **Never `git push`** — the user publishes.
