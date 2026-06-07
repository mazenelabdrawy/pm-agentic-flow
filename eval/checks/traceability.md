# Check: traceability

**Purpose:** Every requirement is earned by evidence — and the chain of evidence is unbroken end to end. No requirement appears that isn't backed by a finding; no acceptance criterion or eval criterion floats free of a requirement.

## The trace chain
pm-agentic-flow tracks a single dependency chain through the PCO:

```
problem-statement.bets → synthesis.key-insights → prd.requirements (REQ-n)
   → prototype-spec.acceptance-criteria (covers: REQ-n) → eval-results.criteria
```

Each link must reference the one before it. The chain is what lets the run answer "why does this exist?" at every node and "what breaks if this changes?" at every edge.

## Inputs
- `problem-statement.bets`, `synthesis.key-insights`, `prd.requirements`, `prototype-spec.acceptance-criteria`, `eval-results.criteria`.
- `min_confidence_to_advance` (from `rubric.yaml`) — the lowest finding confidence allowed to back a requirement.

## Procedure
1. **insight → finding:** each `synthesis` insight ultimately rests on a cited research claim (not only another insight).
2. **requirement → insight:** each `prd.requirements[]` has a `traces-to` naming an existing insight whose `confidence ≥ min_confidence_to_advance` (≥1 if multiple).
3. **criterion → requirement:** each `prototype-spec.acceptance-criteria[]` `covers:` an existing `REQ-n`.
4. **bet coverage:** each `problem-statement.bets` entry is addressed somewhere downstream or parked in `open-questions`.

## Change-impact (used by the orchestrator on revision)
Because the chain is explicit, when an **upstream** section changes, the downstream nodes that depend on it must be re-checked. The orchestrator surfaces this as a note:

```
change-impact: synthesis INS-2 was revised →
  re-check: REQ-3, REQ-5 (trace to INS-2) → AC for REQ-3/REQ-5 → eval-results.
```

## Verdict
- **pass** — every link in the chain resolves; confidence floor met; all bets covered or parked.
- **fail** — any broken link. Feedback lists each.

## Feedback format
```
traceability FAIL:
  - REQ-4 "Add SSO" traces to no synthesis finding. Add evidence or move to open-questions.
  - REQ-7 traces to INS-2 (confidence: low) — below the `medium` floor.
  - acceptance criterion "import retry" covers REQ-9 which does not exist.
  - bet "CSMs will act on a trusted flag" is not addressed by any insight or requirement.
```
