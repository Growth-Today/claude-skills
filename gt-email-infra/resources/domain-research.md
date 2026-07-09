# Domain Research & Ideation

How to ideate a clean list of sending domains fast, on-brand, and safe from spam-trap naming patterns. Use this before buying domains (the acquisition and DNS steps live in `email-infra-guide.md` and `email-infra-step-by-step.md`).

The core rule: **always tie the domain to the brand name, never to a sales pitch.** The right prefixes/suffixes depend on the use case — for newsletter campaigns you can buy brand-oriented domains (e.g. for Ramp: `rampwebinars`, `rampnewsletters`, `rampevents`); for cold email use neutral connectors like `try`, `partner`, `go`, `meet`, `team`.

---

## The prompt (use in Claude)

> Act as an expert email marketing strategist. Keep every domain on-brand.

### 1. Understand the brand

- Visit the company website.
- Summarize the industry, purpose, and core keywords — focus on what the company *does* (SaaS, ecommerce tools, outbound automation, customer support, logistics, etc.).
- Confirm the brand identity before generating anything.

### 2. Extract relevant keywords

Identify 3–5 keywords that describe the product/service category. They must be directly relevant to the business (e.g. a customer-service SaaS: "support, helpdesk, chat, automation").

### 3. Generate secondary domains

- Each domain must include the core brand name (or a very close variant).
- Short, professional, easy to remember.
- Optionally combine with a relevant industry/service keyword for context.
- Use suffixes and prefixes to adapt the main domain. Example with `domain.com`: `domainhq.com`, `meetdomain.com`, `topdomain.com`, `partnerdomain.com`, `scalewithdomain.com`, `growwithdomain.com`.

How to think about connectors:
- **Any use case:** team, meet, partner, try
- **Selling sales outcomes:** scale, growth, marketwith, team, meet, partner, try
- **Selling analytical outcomes:** analyze, attribute, partner, team, try

### 4. Preferred extensions (ranked)

`.com` (most preferred), then `.co`.

### 5. Exclude existing domains

Do not return duplicates of already-owned domains, or confusingly similar ones.

**Final output:** a list of high-quality domain suggestions, each tied to both the core brand name and the keywords that describe what the company actually does.

---

## What to avoid

- Random/unrelated terms or generic filler.
- Sales buzzwords: "scaleyourbiz", "viraltraffic", "instantleads".
- Income-trap words: "wealth", "cash", "earn", "payout".
- Giveaway bait: "free", "promo", "winner".
- Marketing words: "leads", "automation", "scale".

**Safe rule of thumb:** if a word promises money, creates urgency, implies authority, touches account security, or sounds like a sales pitch → do not put it in a domain.

---

## Worked example (Growth Today, a GTM agency)

**Good:** GrowthToday.com, GrowthToday.io, GrowthTodayGTM.co, growthwithGT.com, partnerwithGrowthToday.com, teamGrowthToday.com, GTMwithgrowthtoday.com.

**Can't use:** GrowthMarketingExperts.com (too broad), GTBusinessSolutions.net (.net is bad), TryGrowthNow.org (not close to the brand).

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
