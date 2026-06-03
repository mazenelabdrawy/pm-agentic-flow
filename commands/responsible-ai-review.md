---
description: Run an AI governance checklist — data lineage, consent, hallucination and bias risk — and issue a go/no-go before launch.
argument-hint: (reads prd, prototype-spec, synthesis from the PCO)
---

# /responsible-ai-review

Load the `responsible-ai-review` skill (`skills/responsible-ai-review/SKILL.md`) and run it.

Read `prd`, `prototype-spec`, and `synthesis` from `PRODUCT_CONTEXT.md`. Work the governance checklist (data lineage, consent & privacy, hallucination risk, bias & fairness, transparency); for each, state the risk, severity, and a concrete mitigation. Write the `responsible-ai` section ending in a clear **go / go-with-mitigations / no-go**. Mitigations flow into `deploy.rollout-notes`. An unmitigated high-severity risk is a no-go.
