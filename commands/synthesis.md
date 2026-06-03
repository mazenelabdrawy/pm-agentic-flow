---
description: Reconcile the three research streams into consolidated, confidence-tagged insights — refusing any insight that rests on an uncited claim.
argument-hint: (reads research sections from the PCO)
---

# /synthesis

Load the `synthesis` skill (`skills/synthesis/SKILL.md`) and run it.

Read `research-market`, `research-competitive`, `research-user`, and `problem-statement` from `PRODUCT_CONTEXT.md`. Write `synthesis` (`key-insights`, `confidence-summary`, `biggest-unknowns`) back into it.

Before handing off, self-check against the `synthesis-cited` gate (`eval/checks/citation.md` with confidence required): every insight rests on a cited research claim and carries a `confidence` tag. Report the verdict; if it fails, cite the claim, lower confidence, or move the insight to `biggest-unknowns`.
