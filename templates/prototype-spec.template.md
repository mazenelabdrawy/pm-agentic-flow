<!-- Prototype spec template — populated by prototype-spec into the PCO `prototype-spec` section.
     Every PRD requirement must be covered by at least one acceptance criterion. -->

# Prototype Spec — <product / feature>

## Screens
- **<screen>** — purpose; key elements.

## Flows
- **<flow name>**: <screen> → <screen> → … (the path to complete a job)

## States
For each screen: empty · loading · error · success · (role/permission variants)
- **<screen>**: <state> — <what the user sees / can do>

## Edge cases
- <awkward input or condition> — expected behavior.

## Acceptance criteria
| criterion | covers |
|-----------|--------|
| Given <context>, when <action>, then <observable result> | REQ-1 |
