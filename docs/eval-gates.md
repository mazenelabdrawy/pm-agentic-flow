# Eval Gates

An **eval gate** is a validation checkpoint on a transition between agents. It reads the PCO and decides whether work may advance.

```
agent A ──writes PCO──▶ [ GATE ] ──pass──▶ agent B
                            │
                          fail/revise
                            ▼
                    back to agent A with feedback
```

Every gate returns one of three verdicts, recorded in the PCO `run-log`:

- **pass** — requirements met; the next agent runs.
- **fail** — a hard violation (e.g. an uncited claim). Control returns to the same agent with the specific feedback; this counts as a revision round.
- **revise** — soft miss (e.g. a missing optional field the rubric wants). Same agent, lighter feedback.

After `defaults.max_revisions` (in [`eval/rubric.yaml`](../eval/rubric.yaml)) round-trips without a pass, the orchestrator **escalates to the user** rather than looping forever.

## Reusable checks

Gates are composed from the reusable checks in [`eval/checks/`](../eval/checks/). A gate may run one check or several (e.g. `prd-approved` runs `citation` + `traceability`).

| Check | File | Passes when |
|-------|------|-------------|
| **citation** | `eval/checks/citation.md` | Every claim-shaped statement in the target section(s) carries a `[[cite: … ]]` marker. |
| **completeness** | `eval/checks/completeness.md` | All `required_fields` (or the rule) for the stage are present and non-empty. |
| **traceability** | `eval/checks/traceability.md` | Every PRD requirement names a `synthesis` finding it traces to, and that finding exists. |
| **score** | `eval/checks/score.md` | Aggregate score ≥ `threshold` and no criterion below `per_criterion_floor`. |

## Gate-by-transition map

| Transition | Gate (rubric key) | Check(s) |
|------------|-------------------|----------|
| hypothesis → research | `framing-complete` | completeness |
| research → synthesis | `research-cited` | citation (per research section) |
| synthesis → prd-writer | `synthesis-cited` | citation (+ confidence required) |
| prd-writer ⇄ prd-critique → prototype-spec | `prd-approved` | citation + traceability + critique-clear |
| prototype-spec → eval-runner | `spec-complete` | completeness (every requirement has an acceptance criterion) |
| eval-runner → deploy | `eval-threshold` | score |
| deploy → monitor | (precondition) | eval gate must have passed |
| monitor → hypothesis | (loop-back) | learnings appended to bets; no gate |

## Tuning

Thresholds, required confidence, and revision limits all live in `eval/rubric.yaml`. A team raises or lowers its bar there without touching any agent. That is what makes the pipeline adapt to a team's actual standard rather than a hard-coded one.
