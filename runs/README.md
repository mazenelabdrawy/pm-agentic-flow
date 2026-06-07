# Run registry — pm-agentic-flow's memory

`registry.jsonl` is an append-only log: **one JSON object per `/pm-flow` run**. It is how the
pipeline gets a memory across runs — the orchestrator appends an entry when a run ends, and
`/qbr` and `/metrics` read it for a portfolio view and process metrics. This is the piece a
grab-bag of independent skills can't have.

## Entry schema

```json
{
  "run_id": "YYYY-MM-DD-<slug>",          // stable id, also stored in the PCO `meta.run-id`
  "idea": "<the problem-seed>",
  "started": "<ISO timestamp>",
  "ended": "<ISO timestamp>",
  "stage_verdicts": {                       // final verdict per stage ("fail->pass" if it revised)
    "hypothesis": "pass", "research": "pass", "synthesis": "pass",
    "prd": "pass", "prototype-spec": "pass", "eval-runner": "pass", "deploy": "pass"
  },
  "revisions": { "synthesis": 1, "prd": 2 },// revision round-trips per gate
  "final_score": 0.82,                      // eval-runner aggregate
  "threshold": 0.75,
  "verdict": "pass",                        // overall
  "learnings": [ "<durable learning that feeds the next hypothesis>" ]
}
```

## How it's used
- **`/qbr`** — reads every entry to produce a portfolio narrative (scale / sustain / sunset) grounded in real run data, not manual recall.
- **`/metrics`** — aggregates entries into process metrics: gate-failure rate per transition, revisions per stage, time-to-deploy, first-pass rate.
- **Next `/pm-flow`** — a new run's `hypothesis` can read prior `learnings` so it starts smarter.

## Notes
- Append-only; never rewrite history. One line per run (JSONL).
- Per-run working directories (`runs/<run_id>/`) are runtime artifacts and are gitignored; only
  `registry.jsonl` and this README are tracked.
