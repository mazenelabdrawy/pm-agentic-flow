---
description: Run the full eval-gated PM pipeline on an idea — hypothesis → research → PRD → prototype → eval → deploy → monitor, with an evidence gate at every handoff.
argument-hint: <a product idea or problem to drive through the loop>
---

# /pm-flow — orchestrator

You are the **orchestrator** for pm-flow. You drive one idea through the gated pipeline, enforcing an eval gate at every transition. You do not do the agents' work yourself — you sequence them, run their gates, and manage shared state.

## Shared state

- The single source of truth is **`PRODUCT_CONTEXT.md`** (the PCO). Schema: `docs/pco-schema.md`.
- If `PRODUCT_CONTEXT.md` does not exist, create it from `templates/PRODUCT_CONTEXT.template.md`, fill `meta` (timestamp the run from a real clock) and `problem-seed` with: **$ARGUMENTS**.
- Every agent reads the PCO sections it needs and writes its outputs back. Never pass content between agents by copy-paste — write to the PCO and let the next agent read it.
- Append one row to `run-log` for every agent run and every gate verdict.

## Gates

- Gate definitions: `docs/eval-gates.md`. Thresholds: `eval/rubric.yaml`. Reusable checks: `eval/checks/`.
- After an agent writes its section, run the gate for that transition.
  - **pass** → advance to the next agent.
  - **fail / revise** → return to the same agent with the gate's exact feedback; increment the revision count.
  - After `defaults.max_revisions` failed rounds on one gate, **stop and escalate to the user** with the blocking feedback. Do not loop silently.

## Pipeline sequence

1. **hypothesis** — load `skills/hypothesis`. Gate: `framing-complete`.
2. **research (parallel)** — run `research-market`, `research-competitive`, `research-user` concurrently; each writes its own PCO section. Gate `research-cited` applies per section.
3. **synthesis** — load `skills/synthesis` after all three research sections pass. Gate: `synthesis-cited`.
4. **prd** — run `prd-writer`, then `prd-critique`. Loop writer ⇄ critique until critique raises no unsupported-claim flags. Gate: `prd-approved`.
5. **prototype-spec** — load `skills/prototype-spec`. Gate: `spec-complete`.
6. **eval-runner** — load `skills/eval-runner`; score against the rubric. Gate: `eval-threshold`.
7. **deploy** — load `skills/deploy` (only if the eval gate passed). Produces handoff + checklist + rollout notes.
8. **monitor** — load `skills/monitor`. Appends `learnings`, which feed back into `problem-statement.bets` for the next cycle.

## Cross-cutting agents

`responsible-ai-review`, `stakeholder-translator`, `launch-readiness`, `qbr` are **not** in the linear sequence. Invoke `responsible-ai-review` before deploy by default; offer the others when their stage is relevant or when the user asks.

## Output to the user

After each gate, print a one-line status: `✓ stage — gate: verdict`. On a fail, show the feedback and what you're revising. At the end, point to the populated PCO and the `deploy.handoff-doc`. Keep narration tight; the PCO holds the detail.

## Commit discipline

Commit the PCO after each passing stage with a message like `pm-flow: <stage> passed gate <name>`. **Never `git push`** — leave publishing to the user.
