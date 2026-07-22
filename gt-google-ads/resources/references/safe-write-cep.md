# Safe Write Operations — CEP Protocol (Google Ads)

Any change to a live account (pause, bid, budget, add keyword/negative, new ad, status change) follows **CEP — Confirm → Execute → Post-check**. No exceptions. Default posture is **read-only / draft**; a mutation only happens after explicit user confirmation.

---

## Step 1 — Confirm (before touching anything)
Present exactly what will change, in a table:
- **Entity** (campaign / ad group / keyword / budget) + IDs
- **Current value → proposed value**
- **Scope** (how many entities affected)
- **Why** (the data reason)
- **Risk / reversibility** (does it reset learning? affect budget pacing? hard to undo?)
Then stop and wait for an explicit "yes."

## Step 2 — Execute (only after "yes")
- Make **only** the confirmed change — nothing extra.
- Batch cautiously; for large/bulk changes, confirm the batch scope again.
- Never mass-mutate on a single approval that was scoped to one entity.

## Step 3 — Post-check (verify + watch)
- Read back the entity to confirm the change applied as intended.
- Note what to monitor and for how long (e.g. Smart Bidding re-learning ~1–2 weeks after a target/budget change; watch CPL/SQL, not day-1 noise).
- State the **rollback** (previous value) so it can be reverted fast.

## Hard rules
- **Read-only by default.** Analysis and recommendations never require write access.
- **No silent changes**, no "I'll just also fix…". One confirmation = one scoped change set.
- Anything that resets learning, changes budgets, or alters conversion setup gets an explicit risk callout.
- Judge outcomes to **pipeline/SQL** over a full B2B window, not to day-1 metrics.

*Pattern acknowledged: itallstartedwithaidea/google-ads-skills (Apache-2.0), reimplemented GT-native.*

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
