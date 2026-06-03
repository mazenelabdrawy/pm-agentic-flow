# Build Handoff — Churn-Risk Early Warning for CSMs

> Extracted from the `deploy` section of the sample [PRODUCT_CONTEXT.md](PRODUCT_CONTEXT.md).
> Produced by **deploy** only after the eval gate passed.

## Summary
- **Problem:** CSMs find out an account is unhappy after it's already churning; usage data exists but isn't turned into an early warning.
- **Target user:** CSMs at B2B SaaS ($1M–$50M ARR), 20–60 accounts each.
- **Approved scope:** A renewal-horizon (30+ day) per-account risk flag with the top 3 contributing usage signals shown in plain language, surfaced in a weekly "accounts to watch" list and written back to the CRM record.
- **Non-goals:** Full CS platform; enterprise-grade configurable scoring engine.

## Success metrics
- Flagged accounts churn ≥ 2× unflagged (predictive validity).
- ≥ 50% of flags actioned within 5 business days (adoption).

## Build checklist
1. [ ] Usage-signal ingestion + 48h staleness guard
2. [ ] Risk-flag job (30-day renewal horizon) with insufficient-data handling
3. [ ] Top-3 templated signal generator (no free-text inference)
4. [ ] Accounts to Watch list + Account Detail
5. [ ] CRM write-back (REQ-4)
6. [ ] Actioned + save-play capture (REQ-5)

## Rollout notes
- **Phasing:** internal dogfood → 3 design-partner CS teams → GA.
- **Required before GA:** consent confirmation (responsible-ai), predictive-validity check on design-partner data.
- **Kill criterion:** if flagged accounts don't churn measurably more than unflagged after one renewal cycle, halt and revisit the model.

## Open questions
- Auto-recommended save-plays (deferred REQ-6) — validate CSM demand before building.
