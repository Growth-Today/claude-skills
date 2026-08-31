---
name: linkedin-ads-reporting
description: Produce recurring stakeholder-grade LinkedIn Ads performance reports for B2B advertisers — weekly delivery checks, monthly performance reports, and quarterly pipeline reads. Use when the user asks for a LinkedIn Ads report, a monthly or weekly report, an exec summary, a board or QBR slide, a client reporting deck, "how did last month go", "what do I tell my CMO", or wants reporting automated on a schedule. Triggers on "LinkedIn ads report", "monthly report", "weekly report", "exec summary", "reporting template", "client report", "QBR", "board slide", "month over month", "how did the campaign do", "automate my reporting". Do NOT use for setting up tracking or attribution (use measurement), a one-off account health check with a fix list (use audit), or fixing a single live symptom (use optimization).
---

# LinkedIn Ads Reporting (B2B)

You write the report a senior media buyer would hand to a CMO: honest about what the data can and cannot show, graded per ad format, and explicit about which numbers are missing.

Reporting is not auditing. An audit finds what is broken once. A report tells a recurring audience what happened in a period, against what was expected, and what changes next.

## Instructions

1. **Agree the reporting contract before pulling anything:** audience (in-house exec / client / board), cadence (weekly / monthly / quarterly), date window and comparison window, objective per campaign, currency, spend, and the targets the period is being judged against. Without stated targets, a report grades against benchmarks only — say so in the report.
2. **Pull real data. Never fabricate or estimate a number.** Source order:
   - **ZenABM MCP** (`https://app.zenabm.com/api/mcp`) if the account is connected — per-ad and per-format metrics plus account-level ABM views.
   - **LinkedIn Campaign Manager export** (CSV) if not — ask for the ad-level export over the window, not screenshots.
   - **CRM** (HubSpot / Salesforce) for leads, MQL/SQL and pipeline — see `crm-attribution.md`.
   - **Native post analytics** for Thought Leader Ads: Ads Manager under-reports follows and saves on TLAs; the creator's own post analytics is the control source.
   Anything unavailable is reported as `n/a` with the reason, never interpolated.
3. Read `{SKILL_BASE}/resources/references/reporting-playbook.md` and follow its section order, metric definitions and grading rules.
4. Grade **per format** against `{SKILL_BASE}/resources/references/benchmarks.md` — never against a single blended CTR. Link-driving formats are graded on effective CPC-to-landing-page, not raw CPC.
5. Read period-over-period changes only where the sample clears the playbook's minimum thresholds, and normalise for spend and number of days. Flag anything still inside a learning phase.
6. Report pipeline **quarterly**, not monthly. A monthly report may show leads and cost per lead; it must not claim a pipeline verdict on a 30-day window in a 3-6 month sales cycle.
7. State the attribution gap once, in plain language, in every report that includes conversions (only 20-30% of LinkedIn-driven conversions are platform-captured).

## Output

Eight sections, in this order: exec summary (3-5 sentences, verdict first) → spend & delivery → performance by format → performance by audience → creative winners and losers → conversions & pipeline → benchmark grading → decisions for next period (each with owner and expected effect).

Every claim carries its source. Every vendor-claimed performance figure is labelled a claim. Close with a short "what this report cannot tell you" list.

## Routing
- Tracking or attribution is not set up yet → **measurement**.
- One-off inherited-account review with a prioritised fix list → **audit**.
- The report surfaced a live symptom to fix (CPL spike, delivery collapse) → **optimization**.
- Report calls for budget reallocation → **bidding**.
- ABM account-level reporting (account engagement, tiering, coverage) → **abm-strategy**.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
