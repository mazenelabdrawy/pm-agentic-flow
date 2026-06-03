# PCO Schema — `PRODUCT_CONTEXT.md`

The **Product Context Object (PCO)** is pm-flow's single shared-state file. Every agent reads the sections it needs at start and writes its output back. There is **no copy-paste handoff** — the PCO *is* the handoff.

This document is the spine of the system. Eval gates, agent contracts, and the validator all reference the section IDs defined here.

---

## How the PCO works

- One file per product idea, created from [`templates/PRODUCT_CONTEXT.template.md`](../templates/PRODUCT_CONTEXT.template.md).
- Each agent owns specific sections (it **writes** them) and consumes others (it **reads** them). Ownership is defined in each agent's `SKILL.md` and summarized in the README's "Available Agents" tables.
- The PCO is committed to the repo at every stage — **GitHub is the system of record**. The run log captures the sequence of agents and gate verdicts.
- Sections are addressed by their stable **`id`** (e.g. `problem-statement`), not their heading text, so renames don't break gates.

## Citation rule (the heart of the eval gates)

Any **claim** — a market number, a user pain point, a competitor capability, a requirement justification — must carry a **citation marker** of the form:

```
[[cite: <source> | <accessed/confidence> ]]
```

- `<source>` — a URL, a document name, an interview ID, or `user-provided`.
- `<accessed/confidence>` — a date, or one of `high | medium | low` confidence when the source is qualitative.

Example:

```
- TAM for mid-market RevOps tooling is ~$4.2B [[cite: https://example.com/report-2025 | 2026-05-30]]
- Enterprise buyers distrust black-box scoring [[cite: interview-07 | high]]
```

The **citation check** (`eval/checks/citation`) fails a gate if a section that requires citations contains claim-shaped statements with no marker. A claim with no source cannot advance a stage.

## Confidence levels

Synthesis and downstream agents tag findings with confidence (`high | medium | low`) derived from source quality and corroboration. The rubric (`eval/rubric.yaml`) can require a minimum confidence for a finding to back a PRD requirement.

---

## Sections

Legend — **R** = required before its owning stage's gate can pass · **O** = optional.

### `meta` — Run metadata (R)
Owner: **orchestrator**
- `idea` — the raw seed the run started from
- `created` / `last_updated` — ISO timestamps
- `rubric` — path to the active rubric (default `eval/rubric.yaml`)

### `run-log` — Pipeline run log (R)
Owner: **orchestrator** (append-only)
Each entry: `{ stage, agent, started, ended, gate, verdict (pass|fail|revise), notes }`. The audit trail of what ran and which gates passed.

### `problem-seed` — Problem seed (R)
Owner: **orchestrator** (from user input) → read by **hypothesis**
The unrefined problem/idea in the user's words.

### `problem-statement` — Problem statement & bets (R)
Owner: **hypothesis**
- `problem` — the root problem (not the symptom)
- `target-user` — who has it
- `bets` — the hypotheses we're making
- `success-criteria` — what proving the bet looks like (measurable)
- **Gate:** `framing complete` (completeness) — all four sub-fields present.

### `research-market` — Market research (R for stage 2)
Owner: **research-market** · Requires citations.
- `market-size` / `tam-sam-som`, `trends`, `tailwinds-headwinds` — each claim cited.

### `research-competitive` — Competitive research (R for stage 2)
Owner: **research-competitive** · Requires citations.
- `competitor-matrix`, `positioning-gaps` — each claim cited.

### `research-user` — User research (R for stage 2)
Owner: **research-user** · Requires citations.
- `user-needs`, `pain-points`, `jtbd` — each claim cited.

### `synthesis` — Consolidated findings (R)
Owner: **synthesis** · Requires citations + confidence tags.
- `key-insights` — each insight references the research claims it rests on, with a `confidence` tag.
- `confidence-summary` — overall confidence and the biggest open unknowns.
- **Gate:** `every claim cited` (citation) — no insight may rest on an uncited research claim.

### `prd` — Product Requirements (R)
Owner: **prd-writer**, critiqued by **prd-critique**
- `goals`, `non-goals`, `requirements`, `metrics` — **each requirement traced to a `synthesis` finding** via its id.
- `open-questions`
- **Gate:** `prd approved` — every requirement traces to a finding (citation) **and** `prd-critique` has no unresolved unsupported-claim flags.

### `prototype-spec` — Prototype specification (R)
Owner: **prototype-spec**
- `screens`, `flows`, `states`, `edge-cases`, `acceptance-criteria` — acceptance criteria map to PRD requirements.
- **Gate:** `spec complete` (completeness) — every PRD requirement has at least one acceptance criterion.

### `eval-results` — Evaluation results (R)
Owner: **eval-runner**
- `criteria` — per-criterion pass/fail with the score and the rubric threshold it was measured against.
- `score` — aggregate vs `rubric.yaml` threshold.
- **Gate:** `score ≥ threshold` (score) — aggregate score must meet the rubric bar.

### `deploy` — Deploy & handoff (R for stage 7)
Owner: **deploy**
- `handoff-doc`, `build-checklist`, `rollout-notes`.
- **Gate:** `eval gate passed` (precondition) — deploy may not write unless `eval-results` passed.

### `monitor` — Production monitoring (R for stage 8)
Owner: **monitor**
- `production-metrics`, `incidents`, `learnings`.
- `learnings` feed back as new entries into `problem-seed` / `problem-statement` bets — closing the loop.

### Cross-cutting sections (O — written when the agent runs)
- `responsible-ai` — owner **responsible-ai-review**: data lineage, consent, hallucination/bias risks, go/no-go.
- `stakeholder-comms` — owner **stakeholder-translator**: the same update in 3 registers (eng / exec / user).
- `launch-readiness` — owner **launch-readiness**: model card, rollback plan, monitoring hooks, on-call.
- `qbr` — owner **qbr**: OKR pull, ship log, metrics, scale/sunset recommendation.

---

## Section ID reference (for the validator)

Stable IDs an agent may declare in its `## Inputs` / `## Outputs`:

```
meta · run-log · problem-seed · problem-statement · research-market ·
research-competitive · research-user · synthesis · prd · prototype-spec ·
eval-results · deploy · monitor · responsible-ai · stakeholder-comms ·
launch-readiness · qbr
```

`validate_agents.py` checks that every PCO section an agent claims to read/write exists in this list. New agents that need a new section must add it here in the same PR.
