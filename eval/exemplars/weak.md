# Calibration exemplar — WEAK (fails the score gate)

A reference for `eval-runner` to calibrate anchored scoring. This is what a failing
artifact set looks like — and crucially, it fails on the **per-criterion floor**, not just
the aggregate, so a strong area can't mask a fatal weak one.

> Scenario: the same churn-risk idea, but rushed — requirements asserted without research,
> error states skipped.

## Why each criterion lands where it does

| Criterion | Level | Anchor matched | Evidence in the artifact |
|-----------|-------|----------------|--------------------------|
| problem-fit | **0.75** | "Core flows serve the problem; one minor feature is tangential" | Still about CSM churn risk, but adds an unrelated "team chat" screen. |
| evidence-grounding | **0.25** | "Several untraced requirements; evidence base is thin" | REQ-2, REQ-4, REQ-7 have no `traces-to`; synthesis has 2 insights, both `low` confidence. |
| completeness | **0.5** | "Happy paths covered; error/empty states or edge cases partially missing" | No empty/error states; no insufficient-data handling for new accounts. |
| feasibility | **0.75** | "Buildable; one unaddressed risk" | Reasonable, but the model-validity risk is unaddressed. |
| responsible-ai | **0.5** | "Risks named but mitigations vague" | "We'll handle consent later." |

## Aggregate
Normalized weights as in strong.md.

aggregate = 0.75·0.273 + 0.25·0.273 + 0.5·0.182 + 0.75·0.182 + 0.5·0.091
          = 0.205 + 0.068 + 0.091 + 0.136 + 0.045 ≈ **0.55**

**Verdict: FAIL** — two ways:
1. aggregate 0.55 < threshold 0.75, **and**
2. `evidence-grounding` level 0.25 is **below the floor 0.50** → fails the gate on its own.

Feedback returns to **prd-writer** (untraced requirements) and **prototype-spec** (missing states).

## Calibration note
The floor is the point: even though feasibility and problem-fit are decent, the untraced
requirements (evidence-grounding below floor) block the gate. This is the whole reason the
score gate exists — it stops confident-but-unsupported work from shipping.
