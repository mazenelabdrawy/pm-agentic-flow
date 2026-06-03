# PRD — Churn-Risk Early Warning for CSMs

> Extracted from the `prd` section of the sample [PRODUCT_CONTEXT.md](PRODUCT_CONTEXT.md).
> Note every requirement's `traces-to` — that link is what the `prd-approved` gate enforces.

## Goals
- Give CSMs a renewal-horizon risk flag with **visible evidence** (serves both bets).
- Fit the existing CSM weekly workflow (serves INS-4).

## Non-goals
- Not building a full CS platform (playbooks, NPS, ticketing) in v1.
- Not an enterprise-grade configurable scoring engine in v1.

## Requirements
| id | requirement | traces-to | priority |
|----|-------------|-----------|----------|
| REQ-1 | Compute a per-account risk flag 30+ days before renewal | INS-1 | must |
| REQ-2 | Each flag shows the top 3 contributing usage signals in plain language | INS-2 | must |
| REQ-3 | Surface flags in a weekly "accounts to watch" list, sortable by renewal date | INS-1 | must |
| REQ-4 | Push flags into the existing CRM record (no new silo) | INS-4 | should |
| REQ-5 | CSM can mark a flag "actioned" with the save-play taken | INS-1 | should |

## Metrics
- **Predictive validity** — flagged-vs-unflagged churn-rate gap (target: flagged ≥ 2× unflagged).
- **Workflow adoption** — ≥ 50% of flags actioned within 5 business days.

## Open questions
- **REQ-6 (moved here by prd-critique):** "Auto-recommend a save-play per flag" rests on no validated finding that CSMs want prescription over evidence. Deferred until tested — this is the gate working: an untraced requirement does not ship as a requirement.
