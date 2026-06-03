---
description: Frame a raw idea into a problem statement, target user, explicit bets, and measurable success criteria.
argument-hint: <a raw idea or problem to frame>
---

# /hypothesis

Load the `hypothesis` skill (`skills/hypothesis/SKILL.md`) and run it.

- If `PRODUCT_CONTEXT.md` exists, read `problem-seed` (and any `monitor.learnings`) from it and write `problem-statement` back into it.
- If it does not exist, treat **$ARGUMENTS** as the problem seed. Either scaffold a PCO from `templates/PRODUCT_CONTEXT.template.md` (if the user is starting a tracked run) or, for a quick standalone framing, just output the `problem-statement` block.

After producing the framing, self-check it against the `framing-complete` gate (`eval/checks/completeness.md`): are `problem`, `target-user`, `bets`, and `success-criteria` all present and specific? Report the verdict.
