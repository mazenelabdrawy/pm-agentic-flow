# Quickstart

From zero to a populated PCO + PRD + eval results + handoff.

## 1. Install

### Claude Code (CLI)
```bash
claude plugin marketplace add mazenelabdrawy/pm-agentic-flow
claude plugin install pm-agentic-flow@pm-agentic-flow
```
Then `/pm-flow <your idea>`. *(Verified end-to-end: the manifest passes `claude plugin validate`, the marketplace adds, and the plugin is discoverable.)*

### Claude Cowork
Customize (bottom-left) → Browse plugins → Personal → **+** → **Add marketplace from GitHub** → enter `mazenelabdrawy/pm-agentic-flow`.

### Try it from a local clone (no marketplace needed)
```bash
git clone https://github.com/mazenelabdrawy/pm-agentic-flow
claude plugin marketplace add ./pm-agentic-flow   # then install pm-agentic-flow@pm-agentic-flow
```

### Without installing (read-only)
Clone the repo and open [`examples/sample-run/`](../examples/sample-run/) — a complete worked run, no setup required.

> **Contributors:** run `claude plugin validate .` (manifest check) and `python3 validate_agents.py` (agent/contract check) before opening a PR.

## 2. Run the full loop

```
/pm-flow A churn-risk early warning tool for B2B SaaS customer success managers
```

The orchestrator will:
1. Create `PRODUCT_CONTEXT.md` from the template and fill `problem-seed` (reading prior `runs/registry.jsonl` learnings so it starts smarter).
2. Run each stage, printing `✓ stage — gate: verdict` as it goes.
3. Stop and ask you when a gate fails more than the rubric's `max_revisions`.
4. Leave you a populated PCO + a handoff doc, and append the run to `runs/registry.jsonl`.

After a few runs, try `/qbr` (portfolio view) and `/metrics` (where the pipeline bottlenecks).

## 3. Or use any agent standalone

```
/hypothesis Reduce onboarding drop-off in our mobile app
/research competitive
/synthesis
/prd write
/eval
```

Each agent reads what it needs from `PRODUCT_CONTEXT.md` and writes its section back — so you can mix solo runs and the orchestrated loop freely.

## 4. Tune the bar

Edit [`eval/rubric.yaml`](../eval/rubric.yaml) to match your team's standard: gate thresholds, the minimum confidence a finding needs to back a requirement, scoring weights, and how many revision rounds a gate allows before escalating.

## 5. Where things live

| You want… | Look in |
|-----------|---------|
| What each agent does + its PCO I/O | `skills/<agent>/SKILL.md` |
| How the gates decide | `docs/eval-gates.md` + `eval/checks/` |
| The shared-state schema | `docs/pco-schema.md` |
| A complete example | `examples/sample-run/` |
| Starting templates | `templates/` |
| Cross-run memory (the registry) | `runs/registry.jsonl` + `runs/README.md` |
| Scoring anchors + calibration | `eval/rubric.yaml` + `eval/exemplars/` |
