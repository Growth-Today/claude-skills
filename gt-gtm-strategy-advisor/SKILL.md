---
name: gt-gtm-strategy-advisor
description: "GTM Strategy Advisor by Growth Today (growthtoday.co) — turns your own CRM data, sales deck, website, and call recordings into a signal-based GTM playbook. Use when a VP of Sales, Head of Growth, RevOps lead, CRO, or founder wants to build, audit, or sharpen their go-to-market motion: define a data-backed ICP, map the buyer journey, document pain per persona, build a buying-signal library, write a competitor battlecard, and generate a messaging matrix. Connect your HubSpot or Salesforce or upload your materials; it outputs a ready-to-use Excel workbook. Also triggers on: GTM playbook, GTM strategy, go-to-market plan, build my ICP, ideal customer profile, buyer journey, buying signals, signal library, signal-based selling, sales battlecard, objection handling, messaging matrix, positioning, sharpen our outbound. Do NOT use for ads (gt-google-ads / gt-linkedin-ads / gt-meta-ads), CRM cleanup (gt-hubspot-admin / gt-salesforce-admin), list building (gt-list-building), or cold emails (gt-cold-email)."
---

# GTM Strategy Advisor

Turn what you already know about your business — your CRM history, your sales deck, your website, your call recordings — into a sharp, signal-based GTM playbook you can act on.

**Who this is for:** VP of Sales, Head of Growth, RevOps leads, and founder-led sales teams who want a data-backed GTM motion, not a generic template. You run this on your own company and your own prospects.

**What you get:** a complete Excel workbook — Company + Market, ICP, Buyer Journey, Pain per Persona, Signal Library, Signal Combo Plays, Messaging Matrix, Battlecard, and a STRATEGY summary — built from your real data, not guesses.

## The core idea

The quality of your playbook depends on the quality of what you feed it. Your own materials give a hypothesis; your CRM data gives real patterns. Together they produce a high-confidence playbook.

```
BRONZE            Your materials only (deck, website, positioning doc).
                  A solid starting hypothesis — good before you have data pulled.

GOLD              Your materials + real CRM data (closed-won / closed-lost patterns).
                  The standard working version — grounded in who actually buys.

GOLD + VALIDATED  The above + call recordings / transcripts.
                  Your real sales conversations confirm or correct the hypothesis.
```

## Step 0 — Feed it your data

Give the advisor as much real input as you can. Three ways, best combined:

1. **Connect your CRM.** If you have a HubSpot or Salesforce connector enabled, the advisor reads your real closed-won and closed-lost patterns, contact and account fields, and deal history — this is what turns a guessed ICP into a data-backed one. (Related GT skills for pulling and cleaning this data: `gt-hubspot-admin`, `gt-salesforce-admin`, `gt-clay`.)
2. **Upload your materials.** Sales deck, website copy, positioning doc, a CRM export (CSV), and any competitor notes. The more concrete, the sharper the output.
3. **Add call recordings.** One or two recent sales-call transcripts are the single highest-leverage input — they reveal the real objections, triggers, and champion that your deck usually gets wrong.

If you only have materials (no CRM pulled yet), you still get a BRONZE playbook — run it, then re-run once you have data.

## The workflow — 6 stages

Each stage generates specific tabs of the workbook. Review each tab before moving to the next, ideally with someone who is in the execution day to day (a working sales rep or your marketing lead) — they catch what a strategy view misses.

```
Stage 1  Company + Market Research        → Tab 0 (Dashboard) + Tab 1     [resources/skill-1-research.md]
Stage 2  ICP Hypothesis + Pain per Persona → Tab 2 + Tab 4                 [resources/skill-2-icp-persona.md]
Stage 3  Signal Library + Combo Plays      → Tab 6 + Tab 7                 [resources/skill-3-signal-library.md]
Stage 4  Sales Battlecard                  → Tab 9                         [resources/skill-4-battlecard.md]
Stage 5  Messaging Matrix                  → Tab 8                         [resources/skill-5-messaging.md]
Stage 6  Excel Assembly                    → complete .xlsx workbook       [resources/skill-6-excel-assembly.md]
```

Run them in order — each stage builds on the confirmed output of the one before.

## Sharpen with call recordings

Once you have a real sales-call recording, re-run to produce a validated version. Upload the transcript and ask the advisor to cross-reference it against your current playbook, flag every mismatch, and update the affected tabs. Call recordings almost always reveal the same high-value corrections:

```
Disqualifiers that aren't real
  Assumed: "companies with in-house teams are a disqualifier"
  Reality on the call: "we actually won one of those — not a disqualifier"

The real competitor set
  Assumed: your known 4-6 competitors
  Reality: 2-3 others that keep coming up in live deals

The real buying trigger
  Assumed: "right timing for evaluation"
  Reality: "our season is BFCM — buyers reach out in summer to prepare"

The real champion
  Assumed: "the VP is our champion"
  Reality: "it's always the Head of CX who finds us first"

The real primary channel
  Assumed: outbound is primary
  Reality: "80% of our deals come from referrals and partner intros"

A new signal you hadn't encoded
  Reality: "when companies migrate CRM they also review adjacent tools — tightly coupled"
```

When a transcript is available, the advisor pre-fills the Buyer Journey tab from real evidence (tagged confirmed vs inferred), appends new signals to the Signal Library, and adds a MISMATCHES tab (first tab) listing every gap between your assumptions and what the calls actually show, with a severity and an action per row.

## When to re-run

Re-run the advisor when: you close a batch of new deals (fresh CRM patterns), you get new call recordings, your positioning or pricing changes, or roughly every 90 days to keep the playbook current. A playbook is a snapshot — it decays as your market and motion evolve.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
