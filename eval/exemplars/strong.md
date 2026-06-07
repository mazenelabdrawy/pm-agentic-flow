# Calibration exemplar — STRONG (passes the score gate)

A reference for `eval-runner` to calibrate anchored scoring. This is what a high-scoring
artifact set looks like. Compare the artifact under evaluation to this and to
[`weak.md`](weak.md), then snap each criterion to the nearest anchor in `eval/rubric.yaml`.

> Scenario: the churn-risk early-warning tool from `examples/sample-run/`.

## Why each criterion lands where it does

| Criterion | Level | Anchor matched | Evidence in the artifact |
|-----------|-------|----------------|--------------------------|
| problem-fit | **1.0** | "Every screen/flow maps to the stated problem for the named target user" | Accounts-to-Watch, Account Detail, CRM card all serve the CSM lead-time job; non-goals hold scope. |
| evidence-grounding | **0.75** | "All but one requirement traced; the exception is flagged as an open question" | REQ-1…REQ-5 each `traces-to` INS-1/INS-2/INS-4; REQ-6 was moved to open-questions by prd-critique. |
| completeness | **0.75** | "Full coverage with one or two minor state/edge gaps" | Every REQ has an acceptance criterion; empty/loading/error/insufficient-data states + 2 edge cases specified. |
| feasibility | **0.75** | "Buildable; one unaddressed risk or assumption" | Usage-only model named as a risk with a kill criterion; no other blocking unknowns. |
| responsible-ai | **0.75** | "Risks identified; mitigations mostly concrete" | Consent + templated-signals mitigations; go-with-mitigations verdict. |

## Aggregate
Weights (problem-fit 3, evidence 3, completeness 2, feasibility 2, responsible-ai 1) → normalized
(0.273, 0.273, 0.182, 0.182, 0.091).

aggregate = 1.0·0.273 + 0.75·0.273 + 0.75·0.182 + 0.75·0.182 + 0.75·0.091
          = 0.273 + 0.205 + 0.136 + 0.136 + 0.068 ≈ **0.82**

**Verdict: PASS** — 0.82 ≥ threshold 0.75, and every criterion ≥ floor 0.50.

## Calibration notes
- A `1.0` requires *zero* off-target scope — be strict; most good work is `0.75`.
- "Flagged as an open question" is what keeps evidence-grounding at `0.75` instead of dropping to `0.5`; an *unflagged* untraced requirement would be `0.5` or lower.
