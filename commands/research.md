---
description: Run market, competitive, and/or user research on the framed problem — every claim cited. Pass a lens or run all three.
argument-hint: market | competitive | user | all  [— optional context]
---

# /research

Dispatch to the research agents based on the first argument:

- `market` → load `skills/research-market/SKILL.md`
- `competitive` → load `skills/research-competitive/SKILL.md`
- `user` → load `skills/research-user/SKILL.md`
- `all` (default) → run all three; in the orchestrated loop these run in parallel, each writing its own PCO section.

Read `problem-statement` from `PRODUCT_CONTEXT.md` (or take framing context from **$ARGUMENTS** in standalone use). Write each lens into its PCO section (`research-market` / `research-competitive` / `research-user`).

Every factual claim must carry a `[[cite: <source> | <date|confidence> ]]` marker. Before handing off, self-check against the `citation` check (`eval/checks/citation.md`) and report the verdict per section. Unsourced assertions must be downgraded to open questions, not stated as fact.
