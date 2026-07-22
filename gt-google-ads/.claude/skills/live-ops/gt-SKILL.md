---
name: google-ads-live-ops
description: Operate a live Google Ads account safely — read-only analysis via the API/MCP with GAQL, PPC math and forecasting, and guarded write operations. Use when the user wants to connect Claude to a live Google Ads account, run GAQL queries, pull live performance/search-terms/auction data, forecast budgets or CPA/CPL, calculate break-even bids, or make account changes (pause, bids, budgets, keywords) safely. Triggers on "connect to my account", "live data", "GAQL", "run a query", "MCP", "pull my campaigns", "forecast", "break-even CPC", "budget projection", "pause campaign", "change bids", "update budget", "make this change". Do NOT use for strategy without live data (use the relevant strategy sub-skill) — this is the operational/execution layer.
---

# Google Ads Live-Ops (B2B)

The operational layer: analyze a **live** account and make changes **safely**. Three modes, all B2B (judge to pipeline/SQL, never to raw clicks or e-commerce ROAS).

## Operating model
1. **Read-only by default.** Live access (Google Ads API via an MCP connector) is for **analysis** — pulling campaigns, search terms, keywords, auction insights, conversion value. Read-only needs no write scope and is the safe default. Connectors are read-only unless explicitly granted write access; the user stays in control.
2. **Analyze with GAQL** → Read `{SKILL_BASE}/resources/references/gaql-queries.md` for B2B query templates (performance, wasted spend, Quality Score, pipeline value, impression share, device/geo). Values are in micros.
3. **Forecast with math** → Read `{SKILL_BASE}/resources/references/ppc-math.md` for break-even CPL/CPC from close rate + ACV, cost-per-SQL, budget projections, impression-share opportunity, and the Smart Bidding data floor.
4. **Change only via CEP** → any mutation (pause, bid, budget, keyword, ad) follows **Confirm → Execute → Post-check** — Read `{SKILL_BASE}/resources/references/safe-write-cep.md`. Never write without explicit, scoped confirmation.

## Routing
- Pure strategy / no live account → use the strategy sub-skills (campaign-setup, keywords, bidding, etc.).
- Live pull + diagnosis → GAQL templates, then hand findings to the matching strategy sub-skill (e.g. wasted terms → negative-keywords).
- Any account change → **CEP protocol, read-only until confirmed.**
- Attribution/tracking still governs everything → `{SKILL_BASE}/resources/references/crm-attribution.md`.

## Discipline
Read live data to CRM outcome; state forecast assumptions as estimates; default to read-only; one confirmation = one scoped change. Vendor/API performance claims are claims to validate.

*Live-ops patterns acknowledged from itallstartedwithaidea/google-ads-skills (Apache-2.0), reimplemented GT-native for B2B.*

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
