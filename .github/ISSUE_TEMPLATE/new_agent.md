---
name: New agent proposal
about: Propose a new dual-mode agent for the pipeline or a cross-cutting one
title: "[agent] "
labels: new-agent
assignees: ''
---

> Open this issue **before** sending a PR for a new agent, so we can align on the contract.

**Agent name** (kebab-case, becomes the skill directory + slash command)
e.g. `pricing-strategy`, `risk-register`

**Type**
- [ ] Pipeline agent (runs at a stage in the loop)
- [ ] Cross-cutting agent (attaches to any stage / standalone)

**Role** (one paragraph — what it does)

**PCO sections it reads**
- `<section>` — why

**PCO sections it writes**
- `<section>` — what

**Eval gate before handing off**
- check: citation / completeness / score ≥ threshold (which?)
- on pass: next agent or return to orchestrator
- on fail: what gets revised

**Why it belongs in pm-flow**
How it strengthens the gated loop rather than duplicating an existing agent.

See [CONTRIBUTING.md](../../CONTRIBUTING.md) and [docs/pco-schema.md](../../docs/pco-schema.md) before implementing.
