# Playbook 01 — Domain Research & Purchasing  ·  [Sales Ops]

How to ideate a clean list of sending domains and buy them safely, so a domain is never flagged *before it sends a single email*. This is the first step of any new infrastructure build. Numbers live in `../references/reference.md` §4, §5, §9; vendors in `../references/approved-vendors.md`.

**Why this matters most.** A domain's *name* and *how it was bought* can get it blocklisted before it ever sends. A 2026 longitudinal study of ~1.52 million malicious domains (Mashood & Nabeel) found the tell-tale abuse signals are exactly the ones a careless cold-email setup produces: fresh domains (median flagged age 60 days), bulk purchases from one registrar on one day (**77.9%** of abusive domains sat in a single registrar+date batch), a handful of over-used registrars, and cheap TLDs. Domain sourcing — not delisting — is where deliverability is won or lost.

---

## Part 1 — The naming rules (corrected 2026)

**Core rule: tie every domain to the brand name, never to a sales pitch.**

**DO**
- Keep the **brand word** (or a very close variant) in every domain.
- Short, professional, easy to say out loud.
- `.com` first, then `.co` as a fallback.

**DON'T**
- ❌ **Prefixes** `go / get / try / meet` — they read as bulk-outreach and combosquatting-style stacking, a documented abuse pattern.
- ❌ Hyphens or numbers.
- ❌ Cheap TLDs `.top / .xyz / .cc` (and avoid `.io / .ai / .net` for cold).
- ❌ Sales/pitch, money, urgency, authority, or security words: `leads, automation, scale, deals, offers, wealth, cash, earn, payout, free, promo, winner, secure, verify`.

**Safe rule of thumb:** if a word promises money, creates urgency, implies authority, touches account security, or sounds like a sales pitch → it does not go in a domain.

> **Naming is the default, not a hard lock.** Brand-tied naming is the standard. The GTM / account owner may deliberately choose a different route (e.g. buying aged, generic-named domains — see Part 3) as a trade-off; that's an owner decision, not a rule violation.

> **Newsletter/event domains are the one exception.** For opt-in newsletter or event sends (not cold), brand-oriented descriptors are fine (e.g. `brandwebinars`, `brandevents`). This playbook is about **cold** sending domains — keep those to the brand word alone.

---

## Part 2 — The ideation prompt

Use in Claude when generating a candidate list:

> Act as an expert cold-email deliverability strategist. Generate sending-domain candidates for **[brand]**, whose primary domain is **[brand.com]**.
> 1. Visit the site; summarize what the company actually does (industry, product category) in one line.
> 2. Keep **every** candidate tied to the brand word. Do **not** add prefixes (go/get/try/meet), hyphens, or numbers.
> 3. Prefer `.com`, then `.co`. Never suggest `.top/.xyz/.cc/.io/.ai/.net`.
> 4. Exclude names containing sales/money/urgency/authority/security words.
> 5. Exclude any domain we already own or a confusing near-duplicate.
> 6. Return 2× the number needed (some won't be available), each with the TLD and a one-word reason it's on-brand.

**Good (brand = Growth Today, growthtoday.com):** `growthtoday.co`, `growthtodaygtm.com`, `growthtodaygtm.co`.
**Reject:** `GrowthMarketingExperts.com` (too broad / not the brand), `GTBusinessSolutions.net` (.net + pitch), `TryGrowthNow.org` (prefix + not the brand + .org).

---

## Part 3 — Purchasing (spread, don't bulk-buy)

**The fingerprint to avoid.** The 2026 malicious-domains study found **77.9%** of abusive domains belong to a single (registrar, creation-date) bulk batch, and a small set of registrars plus cheap TLDs (`.top/.xyz/.cc`) dominate abuse. Buying many domains at once, from one registrar, on one day looks *identical to that* to the filters — legitimacy doesn't save you.

**How we buy (via an approved purchasing vendor — see `../references/approved-vendors.md`):**
- Buy across **multiple registrars**, spread over **~24h at 2–3h intervals**, staying **< 5 per registrar per day**.
- Spread DNS across **multiple Cloudflare accounts** (no single hub-and-spoke footprint).
- Typically **~1 day to buy + ~1 day to configure**; no impact on sales delivery.
- Duties split: a buying team places orders; a separate team configures. In-house, we keep **name research + placing the order**; the vendor buys and sets up.
- Our visibility is public info only (WHOIS, DNS, registration dates) — enough to verify the spread actually landed.

**Aged domains — owner's call.** Pre-aged domains come from specialized, pricier providers and usually have generic (off-brand) names. By default we **age our own** via the **> 30-day + warmup gate** (`reference.md` §5) rather than buy aged. The GTM / account owner may choose to buy aged domains as a deliberate trade-off (faster reputation vs. higher cost and off-brand naming).

**Legacy domains:** confirm older domains follow the same multi-registrar / multi-Cloudflare spread; if they don't, flag them for rotation.

---

## Part 4 — Hand-off to provisioning

Once purchased, the domain goes to **playbook 02** for mailboxes + DNS/auth. Two things must be true before provisioning: the destination will be **masking or a real landing page (never a bare redirect)**, and the domain will not carry links/tracking in cold sends.

---

## ✅ BUY CHECKLIST (copy-paste per batch)

```
NAMING
[ ] Every candidate contains the brand word
[ ] No prefixes (go/get/try/meet), no hyphens, no numbers
[ ] .com (or .co) only — no .top/.xyz/.cc/.io/.ai/.net
[ ] No sales/money/urgency/authority/security words
[ ] No duplicates or near-duplicates of owned domains
[ ] 2× the needed count generated (availability buffer)

PURCHASE (spread)
[ ] Split across multiple registrars
[ ] Spread over ~24h at 2–3h intervals
[ ] < 5 domains per registrar per day
[ ] DNS spread across multiple Cloudflare accounts
[ ] Aged-domain choice confirmed with GTM/account owner (default = age our own)
[ ] Order placed via an approved vendor; name research kept in-house

VERIFY (public footprint)
[ ] WHOIS shows different registrars across the batch
[ ] Creation dates staggered (not all same day/registrar)
[ ] Destination will be masking / real landing page — NOT a bare 301/302
[ ] Batch logged for the > 30-day age-before-link gate
[ ] Handed to playbook 02 for provisioning
```

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
