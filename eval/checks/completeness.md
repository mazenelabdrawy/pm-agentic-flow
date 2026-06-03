# Check: completeness

**Purpose:** A stage cannot advance with required structure missing or empty.

## Inputs
- `required_fields` — list of sub-fields that must be present and non-empty, **or**
- `rule` — a named structural rule (e.g. `every-requirement-has-acceptance-criterion`).

## Procedure
1. If `required_fields` given: confirm each is present in the owning PCO section and not a placeholder (`<...>`, empty, or `TBD`).
2. If `rule` given, evaluate it:
   - `every-requirement-has-acceptance-criterion` — each `prd.requirements[].id` is referenced by at least one `prototype-spec.acceptance-criteria[].covers`.

## Verdict
- **pass** — all required fields present / rule satisfied.
- **revise** — something is missing. Feedback names exactly what.

## Feedback format
```
completeness REVISE in `problem-statement`:
  - success-criteria is empty — define a measurable signal the bet is proven.
```
