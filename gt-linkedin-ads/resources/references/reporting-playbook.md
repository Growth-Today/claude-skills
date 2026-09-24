# LinkedIn Ads Reporting Playbook

The recurring-report reference: what to pull, how to define each metric, how to grade a period, and what a report must refuse to claim. Pair with `benchmarks.md` for the numbers and `measurement-attribution.md` for the tracking that produces them.

---

## 1. The reporting contract

Settle these before pulling data. A report written without them will be argued about instead of acted on.

| Item | Why it matters |
|------|----------------|
| Audience | In-house exec wants the verdict; a client wants the work shown; a board wants spend-to-pipeline only |
| Cadence | Determines which sections are legitimate (see §5) |
| Date window + comparison window | Equal-length windows, same weekday count |
| Objective per campaign | A brand-awareness campaign graded on CPL is a broken report, not a bad campaign |
| Currency and spend | Benchmarks are USD; state the conversion if not |
| Targets | Without stated targets a report grades against benchmarks only. Say so explicitly |
| Data access | What exists: platform export, ZenABM, CRM, native post analytics |

---

## 2. Data sources and pull order

1. **ZenABM MCP** - `https://app.zenabm.com/api/mcp`. Per-ad and per-format metrics, account-level ABM views, and the benchmark dataset the grading in `benchmarks.md` is anchored to. Preferred when connected: it removes the manual export step and makes the report automatable.
2. **LinkedIn Campaign Manager export** - ad-level CSV over the window. Ask for the export, not screenshots; screenshots lose the columns that matter (landing-page clicks, dwell, per-format splits).
3. **CRM** - HubSpot or Salesforce for leads, MQL/SQL, opportunities, pipeline. Loop and model details in `crm-attribution.md`.
4. **Native post analytics** - required for Thought Leader Ads. Ads Manager under-reports follower and save actions on TLAs; the creator's own post analytics is the control source. Where the two disagree, name both numbers and say which one you trust.

**Non-negotiable:** a metric that cannot be sourced is reported as `n/a` with the reason. Never interpolate, never estimate to fill a table, never carry a number forward from a previous period as if it were current.

---

## 3. Metric definitions

Ambiguity here is where most reporting arguments come from. Define once, use consistently.

| Metric | Definition | Trap |
|--------|-----------|------|
| Spend | Platform-billed spend in the window | Billing lag on the last 1-2 days of a window |
| Impressions | Served impressions | Not reach |
| Reach / frequency | Unique members / impressions per member | Target ~3 impressions/week/person; above ~5-6 expect fatigue |
| Clicks (total) | All chargeable clicks: landing page, social actions, profile, company page, carousel swipes | Inflates CTR heavily on TLAs and carousels |
| Landing-page clicks | Clicks that actually reached the destination URL | The only click that can convert |
| CTR | Total clicks / impressions | Compare per format only; see grading rule below |
| CPC (raw) | Spend / total clicks | Flattering on formats with high social-action volume |
| **Effective CPC-to-LP** | **Spend / landing-page clicks** | **The honest cost of traffic. Use this for every link-driving format** |
| CPM | Cost per 1,000 impressions | The real lever on awareness campaigns |
| Dwell time | Seconds spent on the ad | Best single read of whether the body copy held attention |
| Leads / CPL | Platform or CRM lead count; spend / leads | State which source. Platform lead-gen-form leads and CRM leads are different numbers |
| MQL / SQL | CRM-defined only | Never platform-derived |
| Pipeline | CRM opportunity value influenced in window | Quarterly metric, not monthly (§5) |
| Pipe-to-spend | Influenced pipeline / spend | The only number some execs read. Give it a window and a model |

---

## 4. Grading rules

- **Grade per format, never blended.** Median CTR runs from 2.68% (Thought Leader Ads) to 0.02% (Text Ads) in the same dataset. A blended account CTR grades format mix, not performance.
- **Link-driving formats are graded on effective CPC-to-LP, not raw CPC.** Derived from the LP-clicks-per-$1K figures in `benchmarks.md`:

  | Format | Median CPC (raw) | LP clicks per $1K | Effective CPC-to-LP |
  |--------|-----------------|-------------------|---------------------|
  | Thought Leader Ads | $2.29 | 327 | ~$3.06 |
  | Single Image Ads | $13.23 | 71 | ~$14.08 |
  | Video Ads | $15.61 | 62 | ~$16.13 |

  TLAs stay the cheapest route to a landing page, but the gap narrows once non-LP clicks are stripped out. Report both columns so nobody is surprised later.
- **CTR is not a pipeline proxy.** Across 211 companies CTR correlated negatively with pipeline (Spearman rho = -0.170). A CTR improvement is a delivery finding, not a business result. Never headline a report with it.
- **Grade against the campaign's own objective.** Awareness on dwell and CPM, mid-funnel on landing-page conversion, education on view/completion rate, retargeting on CPM, bottom-funnel on cost per opportunity.
- **Never grade an account down for not adopting an optional or beta feature.**
- **Minimum sample before reading a change:** ~$100 spend per creative, ~1,000 impressions per ad set, and a full 7 days outside the learning phase. Below that, report the number and label it insufficient.
- **Normalise period-over-period.** Compare cost and rate metrics, not raw totals, when spend or day count differ. A 40% impression rise on a 40% budget rise is not an improvement.

---

## 5. What each cadence is allowed to claim

| Cadence | Legitimate sections | Do not claim |
|---------|--------------------|--------------|
| **Weekly** | Delivery hygiene: spend pacing, frequency, delivery drops, disapprovals, obvious breakage | Creative verdicts, audience verdicts, anything about pipeline |
| **Monthly** | Format performance, audience performance, creative winners and losers, leads and CPL, budget reallocation | A pipeline verdict on a 30-day window |
| **Quarterly** | Everything, plus pipeline, pipe-to-spend, attribution review, incrementality reads | Certainty. State the model and its window |

B2B cycles run 3-6 months. Monthly reporting exists to manage delivery and creative; quarterly reporting exists to judge the channel.

---

## 6. Report structure

1. **Exec summary** - verdict first, 3-5 sentences. What happened, whether it met target, the one decision being asked for.
2. **Spend & delivery** - spend vs planned, pacing, impressions, reach, frequency, anything that broke.
3. **Performance by format** - per-format table with the benchmark column beside the actual.
4. **Performance by audience** - audience or account segment, with match rates and exclusions in effect.
5. **Creative winners and losers** - top and bottom by effective CPC-to-LP and dwell, with the copy or angle named so the pattern is reusable.
6. **Conversions & pipeline** - leads, CPL, CRM stages; pipeline only on a quarterly report. Include the attribution-gap sentence.
7. **Benchmark grading** - each objective graded against `benchmarks.md`, with the format and geography the benchmark applies to.
8. **Decisions for next period** - each with owner, expected effect, and how it will be measured. No more than five.

Close with **"What this report cannot tell you"**: unmeasured view-through impact, the 70-80% of conversions the platform does not capture, cross-device gaps, and any `n/a` in the tables.

---

## 7. Reporting traps

- Headlining a blended CTR improvement.
- Quoting raw CPC on Thought Leader Ads without the LP-click column.
- Treating platform lead-gen-form leads and CRM leads as the same count.
- Declaring a topic or creative dead on under $100 of spend.
- Comparing an unequal window without normalising.
- Reading pipeline monthly.
- Presenting a vendor-claimed performance figure as measured. Label claims as claims.
- Silently dropping a campaign from the table between periods. If it stopped, say when and why.

---

## 8. Automating the monthly report

A monthly report is a good scheduled-task candidate once the data pull is programmatic (ZenABM MCP or a stable CSV export path):

- Fixed window: previous calendar month, compared against the month before.
- Refuse to generate on missing data rather than filling gaps - an automated report that estimates is worse than one that fails loudly.
- Keep a running snapshot of prior periods so period-over-period does not depend on re-pulling history.
- Human review before it reaches a client or a board. Automate the assembly, not the verdict.

---

*Benchmark dataset: ZenABM 2026 (median across 161,256 ads / 211 companies), as used in `benchmarks.md`. Metric definitions follow LinkedIn Campaign Manager reporting fields. Accessed 2026-08-31.*
