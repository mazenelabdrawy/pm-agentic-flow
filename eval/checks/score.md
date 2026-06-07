# Check: score

**Purpose:** The prototype must clear the team's quality bar before it can ship — and the score must be **reproducible**, not a vibe. Two evaluators reading the same artifacts against the same anchors should land on the same level.

## Inputs
- `prd`, `prototype-spec`, `synthesis` — the artifacts under evaluation.
- `scoring_criteria` with their **anchors** and weights (from `rubric.yaml`).
- `threshold`, `per_criterion_floor` (from `rubric.yaml`).
- Calibration references: `eval/exemplars/strong.md` and `eval/exemplars/weak.md`.

## Procedure (anchored scoring)
1. For each criterion, read its `anchors` in `rubric.yaml`. Pick the **single level** (`0.0 | 0.25 | 0.5 | 0.75 | 1.0`) whose description the artifact best matches. Do not interpolate to arbitrary decimals — snap to the closest anchor.
2. Record, per criterion: the chosen `level`, the matching `anchor` text, and a one-line `justification` that **quotes or cites the specific artifact** (e.g. "REQ-4 has no `traces-to`").
3. A criterion may be `n/a` only where the rubric allows it (e.g. `responsible-ai` for a non-AI product). Drop `n/a` criteria and re-normalize the remaining weights to sum 1.
4. `aggregate` = weighted mean of the chosen levels (normalized weights).
5. Apply the gate: **pass** iff `aggregate ≥ threshold` AND every scored criterion `≥ per_criterion_floor`. A single criterion below the floor fails the gate even if the aggregate passes (a strong area can't mask a fatal weak one).

## Verdict schema (eval-runner emits this into `eval-results`)
A structured object — a Markdown table is fine, but it must carry these fields:

```json
{
  "criteria": [
    {
      "id": "evidence-grounding",
      "level": 0.5,
      "anchor": "Most requirements traced; ≥1 rests on an uncited or low-confidence finding.",
      "justification": "REQ-4 'Add SSO' traces to no synthesis finding.",
      "floor": 0.5,
      "verdict": "pass"
    }
  ],
  "weights_normalized": { "problem-fit": 0.27, "evidence-grounding": 0.27, "...": "..." },
  "aggregate": 0.80,
  "threshold": 0.75,
  "verdict": "pass"
}
```

## Verdict
- **pass** — aggregate ≥ threshold AND all scored criteria ≥ floor.
- **fail** — otherwise. Feedback names each failing criterion, its level + anchor, and the gap to threshold, and points at the upstream agent that should fix it.

## Feedback format
```
score FAIL: aggregate 0.68 < threshold 0.75.
  - evidence-grounding: level 0.25 (below floor 0.50) — anchor "several untraced requirements"; REQ-3, REQ-5, REQ-7 untraced → fix in prd-writer.
  - completeness: level 0.5 — anchor "error states partially missing"; import-flow error state unspecified → fix in prototype-spec.
```
