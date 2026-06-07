# Check: consistency

**Purpose:** Catch claims that contradict each other *across* PCO sections — the failure a grab-bag of independent steps can't see, because no one holds the whole picture. A run can be fully cited and still be internally incoherent (e.g. a niche ICP paired with a mass-market TAM).

## Inputs
- The PCO sections relevant to the gate (synthesis gate: `problem-statement` + `synthesis` + the three research sections; prd gate: `synthesis` + `prd`).

## What it checks (cross-section invariants)
1. **Scope vs sizing** — the target user / ICP scope in `problem-statement` is consistent with the `market-size` in `research-market` (a narrow ICP can't claim a mass-market TAM, and vice-versa).
2. **Requirements vs non-goals** — no `prd.requirements[]` restates or contradicts a `prd.non-goals` entry.
3. **Metrics vs success-criteria** — `prd.metrics` actually measure the `problem-statement.success-criteria` (not vanity proxies).
4. **No circular evidence** — no `synthesis.key-insights[]` rests *only* on another insight; each must ultimately trace to a cited research claim.
5. **Coverage vs bets** — every `problem-statement.bets` entry is addressed by at least one insight or requirement, or is explicitly parked in `open-questions`.

## Procedure
For each invariant, compare the relevant sections and flag any contradiction. Quote both sides of the conflict. A contradiction is a hard finding; an unaddressed bet is a soft one (revise).

## Verdict
- **pass** — no cross-section contradictions; every bet addressed or parked.
- **fail** — a contradiction exists. Feedback quotes both sides and names the sections to reconcile.

## Feedback format
```
consistency FAIL:
  - scope vs sizing: problem-statement.target-user = "Fortune-500 RevOps leaders" but
    research-market.market-size TAM = "$4.2B (all mid-market SaaS)" — the TAM is for a
    different segment than the ICP. Reconcile in synthesis.
  - metrics vs success-criteria: success-criteria says "reduce churn"; prd.metrics tracks
    only "logins/week" — a proxy that doesn't measure the bet. Fix in prd-writer.
```
