# Predictive Audiences & Career-Signal Targeting (2026)

How LinkedIn's AI audience tools work after the lookalike sunset, and how to use them without losing targeting precision. Load alongside `targeting-audiences.md`.

---

## Lookalike audiences are gone — plan around it

LinkedIn **discontinued lookalike audiences on 29 Feb 2024.** You can no longer create new lookalikes or edit existing ones; any that remain became **static** snapshots that no longer refresh. Active ad sets already using a lookalike keep delivering against that frozen audience, but the moment you touch them they can't be rebuilt.

Practical consequence: if a legacy campaign still leans on a lookalike, treat it as a decaying asset. Migrate the scaling job to **Predictive Audiences** (below) before performance drifts.

---

## Predictive Audiences (the replacement)

Predictive Audiences combine **your first- or third-party data** (a conversion list, high-value customer list, Insight Tag / CAPI signal, or lead-gen form completers) with **LinkedIn's predictive AI** to model who is most likely to take the action your seed represents. Unlike lookalikes — which mirrored *past* customer traits — predictive audiences forecast *future* intent from recent signals (site activity, email/ad engagement, conversions).

**Rules that actually bite:**

- **Build before the campaign starts.** Predictive audiences need up to **4 days** to process; you cannot spin one up the day you launch.
- **Cap of 30 predictive audiences per ad account.** Don't burn them on throwaway tests — reserve them for real scaling jobs.
- **Seed quality is everything.** Match the seed to the action you want to replicate (e.g. seed on *closed-won* or *demo-booked*, not "all form fills"). A noisy seed produces a noisy model.
- **Best used to scale a proven retargeting/matched audience**, not to replace precise ICP targeting. Keep tight firmographic/seniority targeting for cold ABM; use predictive to expand a validated converter profile.

**When to use it:** you have a clean, meaningful conversion or customer seed (ideally 300+ members) and want reach beyond your matched audience without spraying. **When to avoid:** tiny or low-intent seeds, or strict ABM where you must stay inside a named account list.

---

## Career Journey / career-signal targeting

LinkedIn now lets you target on **career-change signals** — recent promotions, role changes, and new job placements ("Career Journey"). New-in-role buyers are disproportionately likely to evaluate and buy tools (new budget, mandate to make a mark), so this is a strong warm-ish layer.

**How to use it well:**

- Layer career signals **on top of** ICP firmographics + seniority — not alone (a "recently promoted" filter with no industry/size guardrail is too broad).
- Pair with messaging that fits the moment: "new to the [role] seat? here's the 90-day play…" converts better than a generic product pitch.
- Combine with a signal-based outbound motion (see `abm/ads-outbound-signaling-guide.md`): a job-change signal is both an ad-targeting lever and a BDR trigger.

---

## Audience Expansion vs predictive — don't confuse them

- **Audience Expansion** (the old checkbox) loosely broadens a manual audience — keep it **OFF by default**; it dilutes precision.
- **Predictive Audiences** are a deliberately modeled, separately-built audience object — the sanctioned way to scale in 2026.

Use predictive audiences intentionally; never rely on Audience Expansion to do the scaling for you.

---

*Sources: LinkedIn Marketing Solutions Help (lookalike changes; Predictive Audiences) — official docs — plus public LinkedIn-ads best-practice guidance, 2024–2026.*

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
