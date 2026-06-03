# Check: citation

**Purpose:** No claim advances a stage without a source.

## Inputs
- `sections` — the PCO section ids to scan (from the gate config in `rubric.yaml`).
- `require_confidence` (optional) — if true, each claim must also carry a confidence tag.

## What counts as a claim
A claim-shaped statement is any assertion of fact about the market, users, competitors, or the product's effect — anything a skeptical reader could ask "says who?" about. Headings, questions, TODOs, and the agent's own framing are not claims.

## Procedure
1. For each target section, split into bullet/sentence units.
2. For each unit that is claim-shaped, require a citation marker:
   `[[cite: <source> | <date|confidence> ]]`.
3. If `require_confidence` is set, the marker's second field must be one of `high | medium | low`, **or** the claim must carry a separate `confidence:` tag.

## Verdict
- **pass** — every claim-shaped unit has a valid marker.
- **fail** — one or more claims have no marker, or `user-provided` is used to launder an unverifiable assertion that the rubric requires to be sourced. The feedback lists each offending line.

## Feedback format (returned to the owning agent)
```
citation FAIL in `synthesis`:
  - "Buyers will pay 30% more for explainability" — no source. Cite or downgrade to an open question.
```
