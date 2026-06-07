# Contributing to pm-flow

pm-flow is an open, contributor-driven pipeline. Whether it's a typo, a sharper agent prompt, a new eval check, or a whole new agent — contributions are welcome, and every contributor is listed publicly.

## What you can contribute

| Contribution | Where it goes |
|--------------|---------------|
| **A new agent** | `skills/<name>/SKILL.md` (the agent) + `commands/<name>.md` (its invocation) |
| **An eval check** | `eval/checks/<name>.md` + wire it into a gate in `eval/rubric.yaml` |
| **A rubric preset** | a variant of `eval/rubric.yaml` for a different team context |
| **A template** | `templates/` (PCO / PRD / spec / handoff variants) |
| **A worked example** | `examples/<your-run>/` |
| **Docs** | `docs/` or the README |

## How to contribute

- **Bugs and small fixes** — open a PR directly.
- **A new agent or a larger change** — open an issue first (use the **New agent** template) so we align on the contract before you build.
- Keep PRs focused: **one change per PR.**

## Conventions

These mirror the rest of the repo — the validator enforces most of them.

- **Skills are nouns, commands are verbs.** A skill is domain knowledge / an agent (`synthesis`, `pricing-strategy`); a command is a workflow you invoke (`/synthesis`, `/pricing`).
- **Skill `name` must match its directory.** `skills/foo/SKILL.md` has `name: foo` in frontmatter.
- **Frontmatter:** every skill needs `name` + `description`; every command needs `description` + `argument-hint`.
- **Every agent follows the §7 contract** — its `SKILL.md` must contain these sections:
  - `## Role` · `## Mode` · `## Inputs` (PCO sections read) · `## Outputs` (PCO sections written) · `## Eval gate` · `## System prompt`
- **Declare your PCO I/O.** In `## Inputs` / `## Outputs`, each bullet starts with the PCO section id in backticks (e.g. `` - `synthesis`: … ``). Any section you read or write **must exist in [`docs/pco-schema.md`](docs/pco-schema.md)** — if your agent needs a new section, add it there in the same PR.
- **Declare your gate.** State which check (`citation` / `completeness` / `traceability` / `score`) guards your handoff and what happens on pass/fail.
- **Nothing advances on an unsupported claim.** This is the whole point of pm-flow — your agent must not let an uncited claim flow downstream.

## The §7 agent contract (copy this skeleton)

```markdown
---
name: <agent-name>
description: <one line, what it does>
---

# <agent-name>

## Role
<one paragraph>

## Mode
Dual-mode: runs standalone via /<agent-name>, or as a node in the orchestrated loop.

## Inputs (PCO sections read)
- `<section>`: why

## Outputs (PCO sections written)
- `<section>`: what

## Eval gate (before handing off)
- check: <citation | completeness | traceability | score>
- on pass: <next agent / return to orchestrator>
- on fail: <what gets revised>

## System prompt
<the actual instructions the agent runs under>
```

## Before you submit

Run both checks — the agent/contract validator and Claude Code's own manifest validator:

```bash
python3 validate_agents.py      # frontmatter, §7 sections, PCO refs, gate→check refs, manifests
claude plugin validate .        # the marketplace/plugin manifest as Claude Code loads it
```

Green output from both, plus a focused PR, is all we need. If you added a new eval check, drop it in `eval/checks/<name>.md` and reference it from a gate in `eval/rubric.yaml` — the validator now confirms every referenced check exists.

## Recognition & license

Every merged contributor is credited. By contributing, you agree your work is licensed under the [MIT License](LICENSE).
