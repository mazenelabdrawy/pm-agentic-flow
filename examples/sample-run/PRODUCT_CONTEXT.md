<!--
  Sample PRODUCT_CONTEXT.md — a complete pm-flow run, start to finish.
  Idea: a churn-risk early-warning tool for B2B SaaS customer success managers.
  Citations use illustrative sources to show the format; replace with real ones in a live run.
-->

# Product Context — Churn-Risk Early Warning for CSMs

## meta
- idea: "Help CSMs catch at-risk accounts before renewal using product-usage signals."
- created: 2026-06-03T09:00:00Z
- last_updated: 2026-06-03T11:40:00Z
- rubric: eval/rubric.yaml

## run-log
| stage | agent | started | ended | gate | verdict | notes |
|-------|-------|---------|-------|------|---------|-------|
| 1 | hypothesis | 09:00 | 09:12 | framing-complete | pass | all four fields present |
| 2a | research-market | 09:12 | 09:34 | research-cited | pass | |
| 2b | research-competitive | 09:12 | 09:36 | research-cited | pass | |
| 2c | research-user | 09:12 | 09:40 | research-cited | pass | |
| 3 | synthesis | 09:40 | 10:05 | synthesis-cited | fail→pass | INS-3 first lacked a citation; revised |
| 4 | prd-writer ⇄ prd-critique | 10:05 | 10:48 | prd-approved | fail→pass | REQ-6 untraced, moved to open-questions |
| 5 | prototype-spec | 10:48 | 11:10 | spec-complete | pass | every REQ covered |
| 6 | eval-runner | 11:10 | 11:25 | eval-threshold | pass | aggregate 0.83 ≥ 0.75 |
| rai | responsible-ai-review | 11:25 | 11:32 | go/no-go | go-with-mitigations | usage data consent |
| 7 | deploy | 11:32 | 11:38 | eval-passed | pass | handoff produced |
| 8 | monitor | (post-launch) | — | — | — | learnings pending live data |

## problem-seed
"CSMs find out an account is unhappy when it's already churning. We have tons of product-usage data but no one turns it into an early warning. Can we flag at-risk accounts in time for the CSM to actually do something?"

## problem-statement
- problem: CSMs lack a timely, trustworthy signal of account health, so they intervene **after** disengagement is visible in revenue rather than weeks earlier when usage first dips.
- target-user: Customer Success Managers at B2B SaaS companies ($1M–$50M ARR), each owning 20–60 accounts.
- bets:
  - We believe that surfacing a usage-derived risk score 30+ days before renewal will let CSMs run save-plays that measurably reduce gross churn.
  - We believe CSMs will trust and act on the score **only if** each flag shows the specific signals behind it (not a black box).
- success-criteria:
  - Accounts flagged "at risk" churn at a materially higher rate than unflagged ones (predictive validity), measured over one renewal cycle.
  - ≥ 50% of flags are actioned by a CSM within 5 business days (adoption of the workflow).

## research-market
- market-size: The customer success platform market is estimated at ~$2.5B in 2025, growing ~12% CAGR [[cite: https://example-research.com/cs-platforms-2025 | 2026-05-20]]. SAM (mid-market B2B SaaS in NA/EU) ≈ $600M bottom-up from ~30k companies × ~$20k ACV [[cite: https://example-research.com/cs-platforms-2025 | 2026-05-20]].
- trends:
  - Shift from reactive support to proactive, usage-driven CS [[cite: https://example-analyst.com/proactive-cs | 2026-04-11]].
  - Consolidation pressure: buyers want CS signals inside existing CRMs, not another silo [[cite: https://example-analyst.com/proactive-cs | 2026-04-11]].
- tailwinds-headwinds:
  - Tailwind: net-revenue-retention is now a board-level metric, raising willingness to pay for churn tools [[cite: https://example-survey.com/nrr-priorities-2026 | 2026-03-02]].
  - Headwind: incumbents bundle health scores for "free," so a standalone tool must clearly out-predict them [[cite: https://example-analyst.com/proactive-cs | 2026-04-11]].

## research-competitive
- competitor-matrix:
  - Gainsight — deep, enterprise-grade, expensive; health scores are configurable but opaque to end CSMs [[cite: https://gainsight-example/product | 2026-05-18]].
  - ChurnZero — mid-market focused, strong playbooks; scoring tuning requires admin effort [[cite: https://churnzero-example/features | 2026-05-18]].
  - Status quo: most teams run a spreadsheet + gut feel; no public evidence of systematic lead time [[cite: https://example-survey.com/cs-tooling-2026 | 2026-03-02]].
- positioning-gaps:
  - Explainability at the CSM (not admin) level is thin across incumbents [[cite: https://gainsight-example/product | 2026-05-18]].
  - Time-to-value is long for enterprise tools; a fast, transparent, mid-market-first score is an opening [[cite: https://example-analyst.com/proactive-cs | 2026-04-11]].

## research-user
- user-needs: CSMs need to know **which** accounts to prioritize this week and **why**, in a view they already use [[cite: interview-04 | high]].
- pain-points:
  - "By the time the exec sponsor goes quiet, it's too late" — lead time is the core pain [[cite: interview-02 | high]].
  - Distrust of opaque scores: CSMs ignore numbers they can't explain to their manager [[cite: interview-04 | high]], [[cite: interview-06 | medium]].
- jtbd:
  - When a renewal is approaching, I want to see which of my accounts are slipping and the evidence, so I can run a save-play while it still matters [[cite: interview-02 | high]].

## synthesis
- key-insights:
  - INS-1: Lead time is the product. The job is "warn me early enough to act," not "score everything." — rests on: interview-02, proactive-cs trend — confidence: high
  - INS-2: Explainability is a precondition for adoption, not a nice-to-have; an opaque score gets ignored. — rests on: interview-04, interview-06, Gainsight opacity gap — confidence: high
  - INS-3: Mid-market is the wedge — incumbents are enterprise-priced and slow to value. — rests on: cs-platforms-2025 SAM, proactive-cs time-to-value gap — confidence: medium
  - INS-4: It must live inside the CRM/CS tool CSMs already use, or it becomes another ignored silo. — rests on: consolidation trend — confidence: medium
- confidence-summary: Strong qualitative grounding on the lead-time and explainability insights (multiple interviews); market-sizing is single-source and should be corroborated before heavy investment.
- biggest-unknowns:
  - Will a usage-only model predict churn early enough without support/billing signals? (untested)
  - Will CSMs actually change behavior given a trusted flag, or just acknowledge it?

## prd
- goals:
  - Give CSMs a renewal-horizon risk flag with visible evidence (serves both bets).
  - Fit the existing CSM weekly workflow (serves INS-4).
- non-goals:
  - Not building a full CS platform (playbooks, NPS, ticketing) in v1.
  - Not an enterprise-grade configurable scoring engine in v1.
- requirements:
  | id | requirement | traces-to | priority |
  |----|-------------|-----------|----------|
  | REQ-1 | Compute a per-account risk flag 30+ days before renewal | INS-1 | must |
  | REQ-2 | Each flag shows the top 3 contributing usage signals in plain language | INS-2 | must |
  | REQ-3 | Surface flags in a weekly "accounts to watch" list, sortable by renewal date | INS-1 | must |
  | REQ-4 | Push flags into the existing CRM record (no new silo) | INS-4 | should |
  | REQ-5 | CSM can mark a flag "actioned" with the save-play taken | INS-1 | should |
- metrics:
  - Predictive validity: flagged-vs-unflagged churn rate gap (target: flagged ≥ 2× unflagged).
  - Workflow adoption: ≥ 50% of flags actioned within 5 business days.
- open-questions:
  - REQ-6 (moved here by critique): "Auto-recommend a save-play per flag" — rests on no validated finding that CSMs want prescription vs. evidence; defer until tested.

## prototype-spec
- screens:
  - **Accounts to Watch** — the weekly list: account, renewal date, risk flag, trend sparkline.
  - **Account Detail** — the flag with its top-3 signals, history, and an "Actioned" control.
  - **CRM card** — compact flag + top signal embedded in the CRM record.
- flows:
  - Triage: Accounts to Watch → sort by renewal → open Account Detail → review signals → mark Actioned with save-play.
- states:
  - Accounts to Watch: empty (no at-risk accounts), loading, error (data sync failed), populated.
  - Account Detail: flag present, insufficient-data (account too new to score), actioned.
- edge-cases:
  - New account with < 2 weeks of usage → show "insufficient data," never a false-confident flag.
  - Usage data sync stale > 48h → banner + suppress flags rather than show stale risk.
- acceptance-criteria:
  | criterion | covers |
  |-----------|--------|
  | Given an account renewing in ≥ 30 days with declining usage, when the weekly job runs, then it appears flagged in Accounts to Watch | REQ-1 |
  | Given a flagged account, when the CSM opens Account Detail, then the top 3 contributing signals are shown in plain language | REQ-2 |
  | Given multiple flagged accounts, when the CSM sorts by renewal date, then the soonest renewals appear first | REQ-3 |
  | Given a flag, when it is computed, then it is written to the linked CRM record within the sync window | REQ-4 |
  | Given a flag, when the CSM marks it actioned and selects a save-play, then the action and play are recorded | REQ-5 |
  | Given an account with < 2 weeks of usage, when scoring runs, then it shows "insufficient data" and no risk flag | REQ-1 |

## eval-results
<!-- Anchored scoring per eval/checks/score.md — each criterion snaps to a rubric anchor level. -->
- criteria:
  | criterion | level | anchor matched | justification (artifact) | floor | verdict |
  |-----------|-------|----------------|--------------------------|-------|---------|
  | problem-fit | 1.0 | every screen/flow maps to the problem for the named user | Accounts-to-Watch + Account Detail + CRM card all serve the CSM lead-time job; non-goals hold scope | 0.5 | pass |
  | evidence-grounding | 0.75 | all but one req traced; exception flagged as open question | REQ-1…5 trace to INS-1/2/4; REQ-6 moved to open-questions by prd-critique | 0.5 | pass |
  | completeness | 0.75 | full coverage with one or two minor gaps | every REQ has an acceptance criterion; empty/loading/error/insufficient-data states + 2 edge cases | 0.5 | pass |
  | feasibility | 0.75 | buildable; one unaddressed risk | usage-only model named as a risk with a kill criterion | 0.5 | pass |
  | responsible-ai | 0.75 | risks identified; mitigations mostly concrete | consent + templated-signals mitigations; go-with-mitigations | 0.5 | pass |
- weights_normalized: {problem-fit: 0.273, evidence-grounding: 0.273, completeness: 0.182, feasibility: 0.182, responsible-ai: 0.091}
- score: 0.82 / threshold 0.75
- verdict: pass

## responsible-ai
- data-lineage: scores derive from product-usage telemetry already collected under the customer's existing terms; confirm contractual permission for CS-team access per tenant.
- consent & privacy: aggregate account-level usage only; no individual end-user profiling. Document in the trust center.
- hallucination risk: the "plain-language signals" must be generated from actual feature counters, not free-text inference, to avoid fabricated reasons. Mitigation: signals are templated from real metrics.
- bias & fairness: ensure low-usage-but-healthy segments (e.g. seasonal accounts) aren't systematically over-flagged. Mitigation: "insufficient data" + seasonality guard.
- transparency: every flag is explainable to the CSM and their manager (this is INS-2).
- verdict: **go-with-mitigations** (consent confirmation + templated signals required before GA).

## deploy
- handoff-doc: see examples/sample-run/handoff.md
- build-checklist:
  1. [ ] Usage-signal ingestion + 48h staleness guard
  2. [ ] Risk-flag job (30-day renewal horizon) with insufficient-data handling
  3. [ ] Top-3 templated signal generator (no free-text inference)
  4. [ ] Accounts to Watch list + Account Detail
  5. [ ] CRM write-back (REQ-4, should)
  6. [ ] Actioned + save-play capture (REQ-5, should)
- rollout-notes:
  - Phasing: internal dogfood → 3 design-partner CS teams → GA.
  - Required before GA: consent confirmation (responsible-ai), predictive-validity check on design-partner data.
  - Kill criterion: if flagged accounts don't churn measurably more than unflagged after one cycle, halt and revisit the model.

## monitor
- production-metrics: _pending live data_ — will track flagged-vs-unflagged churn gap and % flags actioned in 5 days.
- incidents: _none yet_
- learnings:
  - (template) "If usage-only signals prove insufficient for lead time → feeds: problem-statement.bets (add billing/support signals as a bet)."
