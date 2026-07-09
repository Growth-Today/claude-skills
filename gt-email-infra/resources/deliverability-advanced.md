# Advanced Deliverability: Metrics, Security Gateways & SURBL

Deliverability problems that catch experienced senders off guard, because none of them is fixed by warmup, authentication, or better copy alone. This covers the metrics that tell you *before* a domain burns, a receiving-side security layer that blocks cold mail on purpose, and a blocklist that judges your *links* rather than your sending IP.

This builds on the basics in `deliverability-guide.md` (authentication, blacklist monitoring, bounce management) and connects to the diagnosis workflow in `blacklist-bounce-audit.md`.

---

## Part 1 — Secure Email Gateways (Mimecast, Proofpoint, Barracuda)

### What they are

A Secure Email Gateway (SEG) is a filtering layer a company puts *in front of* Google Workspace or Microsoft 365. Mimecast, Proofpoint, and Barracuda are the common ones. Their whole job is to protect employees from unsolicited mail — which means cold outreach is exactly what they are built to stop. This is the key mental shift: a SEG block is not a deliverability defect on your side, it's the receiving organization's security policy working as designed.

### How to recognize it

The tell is a hard rejection that references security or policy rather than the address. The classic Mimecast signature is a `554` rejection worded around "security policies" — you'll see it in the bounce body alongside Mimecast-specific hostnames. If you're categorizing bounces (see `blacklist-bounce-audit.md`), these land in the **Corporate** bucket (`5.7.1`, policy rejection, gateway rejected), not the Unverified/Bad Data bucket.

SEGs judge far more than domain reputation. They weigh the sending pattern, the presence of tracking, links in the body, and how many messages hit the org at once. A common enterprise setting blocks a sending domain outright once it pushes more than a handful of messages into the org in a short window — so "mass" sending patterns work against you here specifically.

### What actually helps

Ordered from most to least useful:

1. **Set up a custom tracking domain.** SEGs dislike shared tracking links most of all. A custom tracking domain is the single highest-leverage move and often the difference on borderline filters.
2. **Turn off open and click tracking** for SEG-heavy segments. Tracking pixels and click-wrapped URLs are among the strongest triggers. If you don't need the opens data, dropping it removes a major flag.
3. **Reduce concurrency into the same org.** Don't fire many inboxes at one company at once — spread sends out so you don't trip the "too many messages" rule.
4. **Keep links minimal.** Fewer URLs in the body, no link shorteners, no image-heavy HTML.

### The honest limit

No sending platform, warmup routine, or DNS tweak overrides a receiving company's SEG policy. If a domain is behind Mimecast or Proofpoint and their policy is to block cold outreach, your mail will be filtered even with flawless infrastructure. Set expectations accordingly:

- **Expect lower reply rates** on segments heavy with SEG-protected domains, and don't read it as a broken setup.
- **Go multi-channel.** Pair email with LinkedIn (and phone where it fits) so email isn't your only path into SEG-protected accounts.
- **Prioritize reachable segments.** Where email still lands well, lean in; where a whole segment sits behind aggressive SEGs, shift weight to other channels rather than burning domains trying to force it.

---

## Part 2 — SURBL and new-domain risk

### Why SURBL is different

Most blocklists (Spamhaus SBL, Barracuda) judge *who is sending* — the IP or host. SURBL judges *what your message links to* — the domains and URLs inside the body. That distinction changes everything: a spotless sending IP gives you zero protection if a link in your email points to a domain SURBL has flagged. The recipient's server extracts the URLs, queries SURBL during processing, and can reject or spam-file the message on that basis alone.

SURBL is not one list but several sub-lists, each a different threat category (phishing, malware, cracked sites, high-volume abuse) combined into a single `multi` lookup. Which sub-list you're on determines the fix.

### The new-domain trap (why this bites cold email)

One of SURBL's strongest triggers is **new-domain velocity**: linking to a domain registered in roughly the last 24–72 hours. A brand-new domain has no history and no reputation, so a fresh link into it reads as suspicious on its own. This is precisely the situation cold email creates — you buy fresh sending domains, warm them, and start linking to your site or tracking domain before any reputation exists. Running cold outbound from a domain with no history, with content patterns that already look like outreach, is the exact profile SURBL is tuned to catch.

### The signals (they're quiet)

SURBL failures are often silent — they don't always announce themselves as a blacklisting:

- **`554` bounces on a clean sending IP** — almost always a URI block, not a sender-reputation problem.
- **A sudden drop in click-through rate** — Gmail and Outlook use SURBL data to disable links inside messages that were otherwise delivered. The mail arrives; the links just don't work.
- **"Too many hops" / `5.4.6`-style notices** — a receiving server hit its limit trying to scan your URLs.
- **Complaint or failure spikes tied to a specific URL** rather than your sending domain — isolate that URL.

### How to fix it (sequence matters)

1. **Confirm the listing.** Run the domain (and any tracking/link domains in your emails) through the SURBL lookup and note which sub-list it's on — that sets the remediation path.
2. **Fix the root cause before requesting removal.** SURBL won't delist while the underlying issue is live. Common causes for legitimate senders: a hacked CMS with injected redirect scripts, an insecure contact/"tell a friend" form being abused, snowshoe-style subdomain patterns, or simply linking from a too-new domain.
3. **Then submit a detailed removal request** — specific cause, specific steps taken, no vague language.

### Prevention for cold-email setups

- **Don't link to brand-new domains.** Let a domain age and build a little history before you route campaign links or tracking through it.
- **Keep link domains clean and stable** — a small number of established, monitored link/tracking domains beats rotating fresh ones through the body.
- **Monitor proactively.** Add your sending and link domains to your blacklist checks (SURBL among them) so a listing surfaces in hours, not weeks — the earlier you catch it, the shorter the recovery.
- **When a domain is genuinely damaged, retire and replace** rather than fighting a long rehab. New cold-email domains are cheap; a rotating-domain architecture means one bad listing doesn't disrupt everything.

---

## Part 3 — The metrics that tell you before a domain burns

The biggest fear running outbound at scale is a simple question with no simple answer: *are my domains burned?* You can't tell from one number. The only reliable read comes from tracking a small set of metrics over time, per inbox and per domain. Think of these as the four core signals — track each as a **trend**, not a one-off reading, at both the domain and inbox level.

1. **Campaign reply rate.** A falling reply rate can mean you're landing in spam or being ignored. Watch the trend. (Rule of thumb: even pure out-of-office auto-replies produce ~1%. If you're seeing *less* than that, you're probably bouncing — check the "other"/bounce folder.)
2. **Warmup score (inbox + domain).** How healthy the domain and inbox look to spam filters. Read it over 3-, 7-, and 14-day windows, and keep warmup copy neutral so the score reflects reputation, not campaign content.
3. **Inbox placement.** Run placement tests from your actual sending tool with your actual campaign copy — primary vs promotions vs spam. A test run with neutral copy tests the *inbox*; a test with real copy tests the *copy*.
4. **Bounce rate.** Segment by domain and inbox. Sudden spikes signal blocks, blacklisting, or list-quality problems.

**Bonus signals** that clarify what the core four are telling you: blacklist monitoring (Spamhaus DBL, SURBL), probabilistic spam scoring of your copy, and spam-filter testing against major providers.

**How to read them together** (one metric alone rarely tells the story):

- Low reply rate → check inbox placement first (are you in spam?).
- Failing placement → check warmup scores (poor warmup over the last week often explains it).
- High bounces → sender reputation declining, or the domain has been flagged.
- Everything healthy but still no replies → the problem is the offer or the targeting, not deliverability.

Two timing notes worth internalizing: a **rising bounce rate is a leading indicator** — it warns you early, often the same day. A **blacklist listing is a lagging indicator** — by the time it shows, the damage is already done. So watch bounces daily; don't wait for a blacklist hit to react.

> **GT does this on autopilot.** Everything in this section — scheduled placement tests every few days, warmup-score and bounce-trend monitoring, blacklist and spam-score flags, and automatic domain/inbox pausing when a threshold trips — is exactly what our Automated Inbox Management System runs continuously across every inbox and domain (see `email-infra-automation.md`). The point of the metrics is to catch early warning signs and *prevent* a burn, not just recover from one — and prevention is only realistic when the tracking is automated.

---

## Part 4 — Diagnosing: is it the copy or the inbox?

When deliverability drops, the first fork is always the same: is your **sender reputation** the problem, or your **copy**? Isolate one variable to find out.

1. Run a test campaign from a **single set of inboxes on one provider** (e.g. all Google, or all Microsoft — don't mix).
2. Swap your sales copy for a **neutral, transactional-style message** — a mock reminder or a one-liner like "See you next week!" with no links, no HTML, no images.
3. **Compare.** If the neutral email inboxes but your sales copy doesn't → the **copy** is the problem (it won't inbox no matter where you send from). If it still fails only from certain providers or specific inboxes → the **inbox/reputation** is the problem.

This pairs with the bounce categorization in `blacklist-bounce-audit.md`: a copy problem shows up as consistent spam placement everywhere; an inbox problem shows up as provider- or inbox-specific failures.

**First email in the sequence is do-or-die.** Until you've established that you reach the inbox, keep email #1 plain text — no HTML, no images (including signature images), no links. Once you're consistently landing, later emails have room to test richer elements.

---

## Part 5 — A note on Microsoft/Outlook

Microsoft filters bulk mail using a Bulk Complaint Level (BCL) threshold, and they periodically recalibrate it more aggressively — a small threshold change on their side can move a batch of previously-inboxing mail into junk overnight. If Outlook placement drops suddenly across the board with no change on your end, a provider-side filtering change is a plausible cause, not necessarily your setup.

A practical adjustment for Outlook-heavy segments: **go short**. Keep the first email concise, aim for a reply rather than a pitch, and expand only after they engage. Outlook audiences tend to respond better to brief, low-friction openers.

---

## Get these areas automated

Book a call with Growth Today to automate these areas. We can run your managed email infrastructure for you, or introduce you to trusted partners who can assist — so your deliverability stays proactive instead of reactive. Start here: https://www.growthtoday.co

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
