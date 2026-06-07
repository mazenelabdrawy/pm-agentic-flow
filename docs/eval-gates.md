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
| **traceability** | `eval/checks/traceability.md` | The full chain resolves: bet → insight → requirement → acceptance-criterion → eval-criterion (no broken links, confidence floor met). |
| **consistency** | `eval/checks/consistency.md` | No contradictions *across* PCO sections (scope vs sizing, requirements vs non-goals, metrics vs success-criteria, no circular evidence, bets covered). |
| **score** | `eval/checks/score.md` | Aggregate score ≥ `threshold` and no criterion below `per_criterion_floor`, using anchored levels. |

## Gate-by-transition map

| Transition | Gate (rubric key) | Check(s) |
|------------|-------------------|----------|
| hypothesis → research | `framing-complete` | completeness |
| research → synthesis | `research-cited` | citation (per research section) |
| synthesis → prd-writer | `synthesis-cited` | citation (+ confidence required) + consistency |
| prd-writer ⇄ prd-critique → prototype-spec | `prd-approved` | citation + traceability + consistency + critique-clear |
| prototype-spec → eval-runner | `spec-complete` | completeness (every requirement has an acceptance criterion) |
| eval-runner → deploy | `eval-threshold` | score (anchored) |
| deploy → monitor | (precondition) | eval gate must have passed |
| monitor → hypothesis | (loop-back) | structured learnings appended to bets + `runs/registry.jsonl`; no gate |

## Change-impact on revision

Because traceability tracks an explicit chain (bet → insight → requirement → acceptance-criterion → eval-criterion), when a gate sends an **upstream** section back for revision, the orchestrator re-checks only the **downstream** nodes that depend on it and prints a `change-impact:` note (see `eval/checks/traceability.md`). This keeps revisions targeted instead of re-running the whole loop.

## Tuning

Thresholds, required confidence, revision limits, and which checks each gate runs all live in `eval/rubric.yaml`. A team raises or lowers its bar there without touching any agent. That is what makes the pipeline adapt to a team's actual standard rather than a hard-coded one.
