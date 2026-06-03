# Eval Results — Churn-Risk Early Warning for CSMs

> Extracted from the `eval-results` section of the sample [PRODUCT_CONTEXT.md](PRODUCT_CONTEXT.md).
> Scored by **eval-runner** against [`eval/rubric.yaml`](../../eval/rubric.yaml).

| Criterion | Score | Floor | Verdict | Note |
|-----------|-------|-------|---------|------|
| problem-fit | 0.90 | 0.50 | ✅ pass | directly serves the lead-time job |
| evidence-grounding | 0.85 | 0.50 | ✅ pass | all v1 requirements trace to findings |
| completeness | 0.80 | 0.50 | ✅ pass | states + edge cases covered |
| feasibility | 0.75 | 0.50 | ✅ pass | usage-only model flagged as a risk |
| responsible-ai | 0.80 | 0.50 | ✅ pass | consent mitigation required |

**Aggregate: 0.83 / threshold 0.75 → PASS**

## What the gates caught on the way here
- **synthesis-cited:** INS-3 (the mid-market wedge) was first stated without a source. The gate **failed** the transition; synthesis revised it to cite the market-sizing finding and dropped its confidence to `medium`.
- **prd-approved:** REQ-6 ("auto-recommend a save-play") traced to no finding. prd-critique flagged it; the gate **failed** until prd-writer moved it to `open-questions`. It is not in the shipped requirement set.

This is the point of pm-flow: the same artifacts a normal PM process produces, but **nothing advanced on an unsupported claim.**
