---
description: Report process metrics across all runs — gate-failure rates, revisions per stage, first-pass rate, score distribution, time-to-deploy — from the run registry.
argument-hint: [optional date range, e.g. 2026-Q2]
---

# /metrics

Load the `metrics` skill (`skills/metrics/SKILL.md`) and run it.

Read **`runs/registry.jsonl`** and compute process metrics across all runs (optionally filtered by **$ARGUMENTS**): gate-failure rate per transition, revisions per stage, first-pass rate, score distribution (vs `threshold`), time-to-deploy, and recurring learnings.

Print a short table plus 2–3 plain-language takeaways that point at the process bottleneck (e.g. "synthesis fails most — citations are the choke point"). Every number must trace to registry entries; if there are too few runs to be meaningful, say so.
