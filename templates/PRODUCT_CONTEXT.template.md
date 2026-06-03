<!--
  PRODUCT_CONTEXT.md — the PCO (Product Context Object), pm-flow's shared state.
  Copy this file to PRODUCT_CONTEXT.md at the start of a run. Each agent reads the
  sections it needs and writes its outputs back. Schema: docs/pco-schema.md.
  Citation marker for any claim:  [[cite: <source> | <date|confidence> ]]
-->

# Product Context — <product idea>

## meta
- idea: <raw seed>
- created: <ISO timestamp>
- last_updated: <ISO timestamp>
- rubric: eval/rubric.yaml

## run-log
<!-- append one row per agent run -->
| stage | agent | started | ended | gate | verdict | notes |
|-------|-------|---------|-------|------|---------|-------|

## problem-seed
<the unrefined problem/idea, in the user's words>

## problem-statement
- problem: <root problem, not the symptom>
- target-user: <who has it>
- bets:
  - <hypothesis 1>
- success-criteria:
  - <measurable signal the bet is proven>

## research-market
- market-size:
- trends:
- tailwinds-headwinds:
<!-- every claim needs [[cite: ... ]] -->

## research-competitive
- competitor-matrix:
- positioning-gaps:
<!-- every claim needs [[cite: ... ]] -->

## research-user
- user-needs:
- pain-points:
- jtbd:
<!-- every claim needs [[cite: ... ]] -->

## synthesis
- key-insights:
  - <insight> — rests on: <research claim ids> — confidence: <high|medium|low>
- confidence-summary:
- biggest-unknowns:

## prd
- goals:
- non-goals:
- requirements:
  - id: REQ-1
    text: <requirement>
    traces-to: <synthesis insight id>
- metrics:
- open-questions:

## prototype-spec
- screens:
- flows:
- states:
- edge-cases:
- acceptance-criteria:
  - criterion: <...> — covers: REQ-1

## eval-results
- criteria:
  - criterion: <...> — score: <n> — threshold: <n> — verdict: <pass|fail>
- score: <aggregate> / threshold: <n>
- verdict: <pass|fail>

## deploy
- handoff-doc:
- build-checklist:
- rollout-notes:

## monitor
- production-metrics:
- incidents:
- learnings:
  - <learning> → feeds: problem-statement.bets

<!-- Cross-cutting sections — present only when that agent has run -->
## responsible-ai
## stakeholder-comms
## launch-readiness
## qbr
