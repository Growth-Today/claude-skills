# Audit Output Templates

Three deliverable formats. Pick based on mode and audience. Fill the brackets. Keep GT voice rules in every format: no em dashes, no contractions, ↳ arrows only, banned vocabulary out, specific numbers, sources cited briefly.

The canonical client-facing full report lives as a Notion page at https://app.notion.com/p/38499b4b2619817f83abeed4b3ebbc37. In client-facing mode you can either re-deliver the content below or point the user to that page.

---

## Template 1: Notion full report (client-facing)

Use for a complete deliverable a prospect can keep. Mirrors the lead magnet structure.

```
# B2B Contact Data Audit for [Company name]
Scored [date] · [X] out of 10 · [Band name]

## The headline
Your data layer scored [X] out of 10. [One sentence stating the band meaning from scoring.md.]
The single highest-leverage fix: [name the lowest-scoring high-blast-radius dimension and the one action].

## Score by dimension
| # | Dimension | Result | Score |
|---|---|---|---|
| 1 | Coverage | [✅/🟡/❌] [one-line finding] | [0/1] |
| 2 | Email Accuracy | [✅/🟡/❌] [finding] | [0/1] |
| 3 | Phone and Mobile | [✅/🟡/❌] [finding] | [0/1] |
| 4 | Freshness | [✅/🟡/❌] [finding] | [0/1] |
| 5 | Cost Per Usable Contact | [✅/🟡/❌] [finding] | [0/1] |
| 6 | Enrichment Method | [✅/🟡/❌] [finding] | [0/1] |
| 7 | CRM Hygiene | [✅/🟡/❌] [finding] | [0/1] |
| 8 | Governance | [✅/🟡/❌] [finding] | [0/1] |
| 9 | Compliance | [✅/🟡/❌] [finding] | [0/1] |
| 10 | Measurement | [✅/🟡/❌] [finding] | [0/1] |
| | Total | | [X]/10 |

## What to fix first
1. [Dimension] ↳ [action]. Benchmark to hit: [number] ([source])
2. [Dimension] ↳ [action]. Benchmark to hit: [number] ([source])
3. [Dimension] ↳ [action]. Benchmark to hit: [number] ([source])

## The 3 numbers to track from here
↳ Verified email rate. Target 90%+ on active lists. Weekly
↳ Mobile connect rate. Target 18% to 22% on verified mobile. Weekly
↳ Cost per usable contact. Track quarter over quarter

## Sources
[List the sources actually cited, from sources.md]

If you want help running this audit on your stack, book a call at growthtoday.co/contact.
```

---

## Template 2: One-page PDF executive summary (client-facing)

Use for a condensed leave-behind. One screen, no scroll.

```
B2B CONTACT DATA AUDIT for [Company name]
[Date] · [X]/10 · [Band name]

SCORE: [X] out of 10
[One sentence: what the band means.]

TOP 3 FINDINGS
1. [Dimension]: [✅/🟡/❌] [finding in under 12 words]
2. [Dimension]: [✅/🟡/❌] [finding in under 12 words]
3. [Dimension]: [✅/🟡/❌] [finding in under 12 words]

FIX FIRST
[One dimension. One action. One benchmark with source.]

THE 3 NUMBERS TO TRACK
Verified email rate ↳ 90%+ · Mobile connect ↳ 18% to 22% · Cost per usable contact ↳ track quarterly

Book a call: growthtoday.co/contact
```

To produce an actual PDF file, render this with the `pdf` skill on a single page. Keep it to one page.

---

## Template 3: Slack snippet (GT-internal only)

Use when the GT team posts a quick result to a client or squad channel. 3 numbers plus next step. No fluff.

```
*Data audit for [client name]* · [X]/10 · [band]

Score by dimension: [list any ❌ and 🟡 dimensions only, one line each]

Fix first: [dimension] ↳ [action]

3 numbers:
↳ Verified email rate: [current] (target 90%+)
↳ Mobile connect: [current] (target 18% to 22%)
↳ Cost per usable contact: [current]

Recommended GT engagement: [pull from score band]
↳ 0 to 3: Velocity rebuild (data foundation)
↳ 4 to 6: GTM Engineering audit + provider rationalization
↳ 7 to 9: AI routing layer + signal-based plays
↳ 10: no rebuild, recommend Plays implementation

Client tier: [tier] · GTM Alpha Playbook: [link or "pending"]
```

---

## Format selection

| Situation | Format |
|---|---|
| Prospect downloaded the lead magnet, wants the full thing | Template 1 (or point to the Notion page) |
| Sales leave-behind, exec audience, condensed | Template 2 |
| GT team posting a result internally | Template 3 |

In client-facing mode, never include the GT engagement recommendation, client tier, or GTM Alpha Playbook link. Those are GT-internal only.


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
