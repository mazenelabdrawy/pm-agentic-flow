---
description: Turn an approved PRD into a buildable prototype spec — screens, flows, states, edge cases, and acceptance criteria covering every requirement.
argument-hint: (reads the approved prd from the PCO)
---

# /prototype-spec

Load the `prototype-spec` skill (`skills/prototype-spec/SKILL.md`) and run it.

Read the approved `prd` from `PRODUCT_CONTEXT.md`. Using `templates/prototype-spec.template.md` for structure, write the `prototype-spec` section (`screens`, `flows`, `states`, `edge-cases`, `acceptance-criteria`), tagging each acceptance criterion with `covers: REQ-n`.

Before handing off, self-check against the `spec-complete` gate (`eval/checks/completeness.md`, rule `every-requirement-has-acceptance-criterion`): every PRD requirement is covered by at least one acceptance criterion. Report the verdict; add criteria for any uncovered requirement.
