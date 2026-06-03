![GitHub stars](https://img.shields.io/github/stars/mazenelabdrawy/pm-agentic-flow?style=flat-square)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Companion: pm-toolkit](https://img.shields.io/badge/companion-pm--toolkit-blue?style=flat-square)](https://github.com/mazenelabdrawy/pm-toolkit)

# PM Agentic Flow — an eval-gated agentic pipeline for product management

> Drive a raw idea through **hypothesis → research → PRD → prototype → eval → deploy → monitor** — where every handoff passes an **evidence gate** before the next agent runs. Nothing advances on an unsupported claim.

<!-- demo GIF: add .docs/images/pm-flow-demo.gif here once recorded -->

Designed for **Claude Code** and **Cowork**. The agents' knowledge files work with any assistant that reads the skill format.

---

## 🚀 Start Here

| You have… | Run |
|-----------|-----|
| A new idea | `/pm-flow <your idea>` — the whole gated loop |
| Just need framing | `/hypothesis <idea>` |
| Need the research | `/research all` |
| Writing a PRD | `/prd write` |
| Validating before ship | `/eval` |
| Briefing stakeholders | `/stakeholder-translator` |

If pm-flow helps you, ⭐ the repo.

## 🤔 Why pm-flow?

Most PM AI tooling is a **skill grab-bag** — a pile of useful prompts with nothing stopping a confident, unsupported claim from flowing straight into a PRD and out the door.

pm-flow is a **gated loop**. Between every stage sits an evaluation gate that reads the shared state and checks: *are the claims cited? does the work meet the team's rubric? are the required fields there?* A synthesis insight resting on an uncited research claim **fails** and returns for revision. A PRD requirement with no backing finding gets moved to open questions. A prototype scoring below your bar never reaches deploy.

The result: **better product decisions, traceable to evidence** — not just faster documents.

## 🧭 How It Works (Agents · Gates · the Loop)

- **Agents** are the building blocks — each is a `skills/<name>/SKILL.md` holding its role, the PCO sections it reads/writes, its gate, and its system prompt.
- **Commands** are how you invoke them — `/<agent>` runs one standalone; **`/pm-flow`** chains them all through the gates.
- **The PCO** (`PRODUCT_CONTEXT.md`) is the single shared-state file. Agents read and write it — no copy-paste handoff. **GitHub is the system of record.**
- **Dual-mode:** every agent runs solo *or* as a node in the loop, from one definition.

```
1 · hypothesis ──[gate: framing complete?]──▶
      ├── research-market ┐
      ├── research-competitive ├─▶ 3 · synthesis ──[gate: every claim cited?]──▶
      └── research-user ┘
4 · prd-writer ⇄ prd-critique ──[approved: every requirement traced]──▶
5 · prototype-spec ──[gate: spec complete?]──▶
6 · eval-runner ──[gate: score ≥ threshold?]──▶
7 · deploy ──▶ 8 · monitor ──[learnings loop back to hypothesis]──┐
      └──────────────────────────────────────────────────────────┘
```

Full diagram + rationale: [docs/architecture.md](docs/architecture.md).

## 📦 Installation

### Claude Code (CLI)
```bash
claude plugin marketplace add mazenelabdrawy/pm-agentic-flow
claude plugin install pm-agentic-flow@pm-agentic-flow
```

### Claude Cowork (recommended for non-developers)
Customize (bottom-left) → Browse plugins → Personal → **+** → **Add marketplace from GitHub** → enter `mazenelabdrawy/pm-agentic-flow`.

### Other AI assistants (skills only)
The `skills/*/SKILL.md` files follow the universal skill format. Commands (`/slash`) are Claude-specific.

| Tool | How | What works |
|------|-----|------------|
| **Gemini CLI** | copy skill folders to `~/.gemini/skills/` | skills |
| **OpenCode** | copy skill folders to `.opencode/skills/` | skills |
| **Cursor** | copy skill folders to `.cursor/skills/` | skills |
| **Codex CLI** | copy skill folders to `.codex/skills/` | skills |

## ▶️ Usage

Run the full loop on an idea:

```
/pm-flow A churn-risk early warning tool for B2B SaaS customer success managers
```

…or use any agent standalone — each reads what it needs from the PCO and writes its section back, so you can mix solo runs and the orchestrated loop freely.

**See it with zero setup:** [`examples/sample-run/`](examples/sample-run/) is a complete worked run — the [PCO](examples/sample-run/PRODUCT_CONTEXT.md), the [PRD](examples/sample-run/PRD.md), the [eval results](examples/sample-run/eval-results.md), and the [handoff](examples/sample-run/handoff.md) — including the two places a gate caught an unsupported claim.

## 🗂️ Available Agents

<details>
<summary><strong>Pipeline agents</strong> — the gated loop, hypothesis → monitor (12 agents)</summary>

| # | Agent | Reads (PCO) | Writes (PCO) | Gate before advancing |
|---|-------|-------------|--------------|------------------------|
| 1 | `hypothesis` | problem-seed | problem-statement (problem, target-user, bets, success-criteria) | framing complete |
| 2a | `research-market` | problem-statement | research-market (size, trends — cited) | every claim cited |
| 2b | `research-competitive` | problem-statement | research-competitive (matrix, gaps — cited) | every claim cited |
| 2c | `research-user` | problem-statement | research-user (needs, pains, JTBD — cited) | every claim cited |
| 3 | `synthesis` | the 3 research sections | synthesis (insights + confidence) | every insight cited |
| 4a | `prd-writer` | synthesis | prd (requirements traced to findings) | every requirement traced |
| 4b | `prd-critique` | prd, synthesis | prd (flags) | no unsupported-claim flags |
| 5 | `prototype-spec` | prd | prototype-spec (screens, flows, states, criteria) | every requirement covered |
| 6 | `eval-runner` | prototype-spec, prd, synthesis | eval-results (scores vs rubric) | score ≥ threshold |
| 7 | `deploy` | eval-results, prd, prototype-spec | deploy (handoff, checklist, rollout) | eval gate passed |
| 8 | `monitor` | deploy, prd, problem-statement | monitor (metrics, learnings) | — (loops back) |

**Examples**
- `/pm-flow A meeting-cost calculator that shows live $ burn during calls`
- `/hypothesis Reduce onboarding drop-off in our mobile app`
- `/synthesis` (after research) — reconcile the streams into confidence-tagged insights

</details>

<details>
<summary><strong>Cross-cutting agents</strong> — attach to any stage, or run standalone (4 agents)</summary>

| Agent | Purpose |
|-------|---------|
| `responsible-ai-review` | AI governance checklist — data lineage, consent, hallucination/bias risk; issues a go/no-go before launch |
| `stakeholder-translator` | rewrites one update three ways — technical (eng), outcome-focused (execs), plain-language (users) |
| `launch-readiness` | pressure-tests the launch like a skeptical VP — model card, rollback plan, monitoring hooks, on-call |
| `qbr` | pulls OKRs, ship log, and metrics into a QBR narrative with a scale/sustain/sunset recommendation |

**Examples**
- `/responsible-ai-review` before any AI feature ships
- `/stakeholder-translator` to brief eng, execs, and users from one source of truth
- `/qbr` to turn a quarter of runs into a portfolio decision

</details>

## 🛠️ Contributing

pm-flow is built to be extended. **Add an agent in two files** — a `skills/<name>/SKILL.md` (its knowledge + contract) and a `commands/<name>.md` (its invocation) — run `python3 validate_agents.py`, open a PR, and get listed.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the agent contract, conventions, and the validator. New-agent ideas start with the [New agent issue template](.github/ISSUE_TEMPLATE/new_agent.md).

## 🙏 About

pm-flow encodes the rigor of evidence-based product practice — cited claims, traceable requirements, a tunable quality bar — into an agentic loop instead of leaving it to discipline. The team rubric in [`eval/rubric.yaml`](eval/rubric.yaml) lets each team set its own standard.

Built by **Mazen El-Badrawy** — AI Product Manager.

## 🔗 Part of the PM stack

| Repo | What's inside |
|------|---------------|
| [pm-toolkit](https://github.com/mazenelabdrawy/pm-toolkit) | PRD template, prioritization, GTM frameworks |
| [pm-portfolio](https://github.com/mazenelabdrawy/pm-portfolio) | PM case studies — discovery, strategy, growth |
| [product-teardowns](https://github.com/mazenelabdrawy/product-teardowns) | Deep product analyses — strategy, positioning, UX |
| [profile](https://github.com/mazenelabdrawy) | The whole stack + background |

## 📄 License

MIT — see [LICENSE](LICENSE).

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/mazen-el-badrawy)
[![Portfolio](https://img.shields.io/badge/Portfolio-View-black?style=flat)](https://mazens-product-journey.lovable.app/)
