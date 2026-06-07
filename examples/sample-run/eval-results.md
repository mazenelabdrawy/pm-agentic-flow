# Eval Results — Churn-Risk Early Warning for CSMs

> Extracted from the `eval-results` section of the sample [PRODUCT_CONTEXT.md](PRODUCT_CONTEXT.md).
> Scored by **eval-runner** with **anchored scoring** against [`eval/rubric.yaml`](../../eval/rubric.yaml)
> (procedure: [`eval/checks/score.md`](../../eval/checks/score.md); calibration: [`eval/exemplars/`](../../eval/exemplars/)).

Each criterion snaps to a rubric **anchor level** — not a free-floating decimal — so the score is reproducible.

| Criterion | Level | Anchor matched | Justification (cites the artifact) | Floor | Verdict |
|-----------|-------|----------------|-------------------------------------|-------|---------|
| problem-fit | **1.0** | every screen/flow maps to the problem for the named user | Accounts-to-Watch + Account Detail + CRM card all serve the CSM lead-time job; non-goals hold scope | 0.5 | ✅ |
| evidence-grounding | **0.75** | all but one req traced; exception flagged as open question | REQ-1…5 trace to INS-1/2/4; REQ-6 moved to open-questions by prd-critique | 0.5 | ✅ |
| completeness | **0.75** | full coverage with one or two minor gaps | every REQ has an acceptance criterion; empty/loading/error/insufficient-data states + 2 edge cases | 0.5 | ✅ |
| feasibility | **0.75** | buildable; one unaddressed risk | usage-only model named as a risk with a kill criterion | 0.5 | ✅ |
| responsible-ai | **0.75** | risks identified; mitigations mostly concrete | consent + templated-signals mitigations; go-with-mitigations | 0.5 | ✅ |

Normalized weights: problem-fit 0.273 · evidence-grounding 0.273 · completeness 0.182 · feasibility 0.182 · responsible-ai 0.091

**Aggregate: 0.82 / threshold 0.75 → PASS** (and every criterion ≥ floor 0.50)

## What the gates caught on the way here
- **synthesis-cited:** INS-3 (the mid-market wedge) was first stated without a source. The gate **failed** the transition; synthesis revised it to cite the market-sizing finding and dropped its confidence to `medium`.
- **prd-approved:** REQ-6 ("auto-recommend a save-play") traced to no finding. prd-critique flagged it; the gate **failed** until prd-writer moved it to `open-questions`. It is not in the shipped requirement set.

This is the point of pm-agentic-flow: the same artifacts a normal PM process produces, but **nothing advanced on an unsupported claim — and the quality bar was applied against explicit anchors, not a gut feel.**
