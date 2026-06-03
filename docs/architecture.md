# Architecture

pm-flow is an **AI-native, eval-gated agentic pipeline** for product management. It drives a raw idea through a continuous loop — hypothesis → research → PRD → prototype → eval → deploy → monitor — where every handoff passes an **evaluation gate** before the next agent runs.

## Three primitives

1. **PCO (Product Context Object)** — `PRODUCT_CONTEXT.md`, the single shared-state file. Agents read the sections they need and write their output back; there is no copy-paste handoff. Schema: [pco-schema.md](pco-schema.md).
2. **Eval gate** — a validation checkpoint on every transition. It reads the PCO and checks: are claims cited? does the score meet the rubric threshold? are required fields present? **Pass** → next agent. **Fail** → back to the same agent with feedback. Definitions: [eval-gates.md](eval-gates.md).
3. **Dual-mode agents** — one definition, two invocation paths. Each agent is a `skills/<name>/SKILL.md` (the knowledge + §7 contract) plus a `commands/<name>.md` (the standalone slash command). The orchestrator (`commands/pm-flow.md`) chains them into the loop. Mode is *how it's invoked*, not different logic.

## The loop

```
orchestrator  (runs any agent solo, or the whole loop)
      │
      ▼
1 · hypothesis ──[gate: framing complete?]──▶
      │  (fan out, parallel)
      ├── research-market      ┐
      ├── research-competitive ├──▶ 3 · synthesis ──[gate: every claim cited?]──▶
      └── research-user        ┘
      ▼
4 · prd-writer  ⇄  prd-critique   (revise until claims hold) ──[approved]──▶
      ▼
5 · prototype-spec ──[gate: spec complete?]──▶
      ▼
6 · eval-runner  (score vs rubric) ──[gate: score ≥ threshold?]──▶
      ▼
7 · deploy  (ship + handoff doc)
      ▼
8 · monitor  (track production metrics) ──[learnings loop back to hypothesis]──┐
      └───────────────────────────────────────────────────────────────────────┘

cross-cutting (attach to any stage, or standalone):
  responsible-ai-review · stakeholder-translator · launch-readiness · qbr
```

## Why gates, not a skill grab-bag

Most PM AI tooling is a collection of independent skills — useful, but nothing stops a confident, unsupported claim from flowing straight into a PRD. pm-flow's difference is the **gate between every stage**: a synthesis insight resting on an uncited research claim *fails* and returns for revision; a PRD requirement with no backing finding gets moved to open questions; a prototype that scores below the team's rubric threshold doesn't reach deploy. The rigor is enforced by the structure, not left to discipline.

## Packaging

pm-flow ships as a **Claude Code / Cowork plugin marketplace**: a root `.claude-plugin/marketplace.json` registers the plugin, whose `commands/` and `skills/` are the dual-mode agents. This is what makes it one-command installable and contributor-extensible — adding an agent is adding a skill + a command. See [quickstart.md](quickstart.md) and [../CONTRIBUTING.md](../CONTRIBUTING.md).

## GitHub as the system of record

The PCO, PRD, eval results, and decisions all commit into the repo. A run's `run-log` is its audit trail: which agent ran, which gate it hit, and the verdict. The history *is* the product's decision record.
