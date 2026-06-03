# Check: traceability

**Purpose:** Every requirement is earned by evidence — no requirement appears that isn't backed by a synthesis finding.

## Inputs
- The `prd.requirements` list and the `synthesis.key-insights` list.
- `min_confidence_to_advance` (from `rubric.yaml`) — the lowest finding confidence allowed to back a requirement.

## Procedure
1. For each `prd.requirements[]`, read its `traces-to` field.
2. Confirm the referenced `synthesis` insight id exists.
3. Confirm that insight's `confidence` ≥ `min_confidence_to_advance`.
4. A requirement may trace to more than one finding; at least one must satisfy the confidence floor.

## Verdict
- **pass** — every requirement traces to an existing finding at or above the confidence floor.
- **fail** — a requirement has no `traces-to`, points at a missing insight, or rests only on findings below the floor. Feedback lists each.

## Feedback format
```
traceability FAIL in `prd`:
  - REQ-4 "Add SSO" traces to no synthesis finding. Add evidence or move to open-questions.
  - REQ-7 traces to INS-2 (confidence: low) — below the `medium` floor.
```
