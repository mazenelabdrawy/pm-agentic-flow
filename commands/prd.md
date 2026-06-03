---
description: Write a PRD whose every requirement traces to a cited finding, or critique a draft PRD for unsupported claims. Pass write or critique.
argument-hint: write | critique
---

# /prd

Dispatch on the first argument:

- `write` (default) → load `skills/prd-writer/SKILL.md`. Read `synthesis` + `problem-statement` from `PRODUCT_CONTEXT.md`; write the `prd` section with every requirement carrying a `traces-to:` finding id.
- `critique` → load `skills/prd-critique/SKILL.md`. Read the draft `prd` + `synthesis`; return a numbered list of unsupported-claim flags (or confirm it's clean).

In the orchestrated loop these alternate (write ⇄ critique) until critique raises no flags. Then self-check against the `prd-approved` gate (`eval/checks/citation.md` + `eval/checks/traceability.md`): every requirement traces to an existing finding at/above the confidence floor, and no critique flags remain. Report the verdict.
