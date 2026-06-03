# Check: score

**Purpose:** The prototype must clear the team's quality bar before it can ship.

## Inputs
- `eval-results.criteria` — per-criterion scores produced by **eval-runner**.
- `threshold` and `per_criterion_floor` (from `rubric.yaml`).
- `scoring_criteria` weights (from `rubric.yaml`).

## Procedure
1. Each criterion is scored 0.0–1.0 by eval-runner against its description.
2. Aggregate = weighted mean of criterion scores, weights normalized to sum 1.
3. Compare aggregate to `threshold`.
4. Compare each criterion to `per_criterion_floor` — a single criterion below the floor fails the gate even if the aggregate passes (prevents a strong area from masking a fatal weak one).

## Verdict
- **pass** — aggregate ≥ threshold **and** all criteria ≥ floor.
- **fail** — otherwise. Feedback names the failing criteria and the gap to threshold.

## Feedback format
```
score FAIL: aggregate 0.68 < threshold 0.75.
  - evidence-grounding: 0.40 (below floor 0.50) — 3 requirements untraced.
  - completeness: 0.70 — error states for the import flow are unspecified.
```
