# Email Infrastructure — Reference

Single source of truth for all numbers, limits, timelines, and metrics used across the GT Email Infrastructure skill set. All other files reference this — never duplicate these values elsewhere.

---

## Send Limits per Provider

| Provider | Safe Daily Limit per Mailbox |
|---|---|
| Google Workspace | 30 emails/day |
| Microsoft 365 | 10 emails/day |

---

## Provider Split

| Provider | Allocation | Why |
|---|---|---|
| Google Workspace | 60% | Higher send limits, good deliverability |
| Microsoft 365 | 40% | Different infrastructure, risk diversification |

**Practical minimum: 15 mailboxes** (~375 emails/day capacity).

---

## Infrastructure Sizing Calculator

| Monthly Goal | Daily Volume | Mailboxes Needed (with 50% buffer) | Domains Needed |
|---|---|---|---|
| 3,000 | 150 | 10–12 | 5–6 |
| 7,500 | 375 | 18–23 | 9–12 |
| 15,000 | 750 | 38–45 | 19–23 |
| 30,000 | 1,500 | 75–90 | 38–45 |

---

## Warmup Timeline

| Period | Status | Campaigns? |
|---|---|---|
| Week 1 | Foundation — low volume warmup starts | No |
| Week 2 | Building — volume increases, health scores appear | No |
| Week 3 | Ready — health scores 70%+ (ideally 90%+) | Yes, conservatively |

**Minimum: 14 days (must have). Recommended: 3 weeks.**

---

## Domain Age Requirements

| Age | Status | Recommendation |
|---|---|---|
| 0–2 weeks | Brand new | No email. Set up DNS, create mailboxes, join warmup. |
| 2–4 weeks | Fresh | Warmup only. No cold email. |
| 4–8 weeks | Warming | Begin mixing cold (follow schedule). |
| 8–12 weeks | Establishing | Moderate cold volume. |
| 12+ weeks | Established | Full operations. Monitor ongoing. |
| 6+ months | Mature | Can push slightly higher volumes if reputation supports. |

---

## Going Live Ramp Schedule

| Week | Google | Microsoft |
|---|---|---|
| 1 | 10–15/day | 5–8/day |
| 2–3 | 15–20/day | 8–10/day |
| 4+ | 25–30/day | 10/day |

---

## Healthy Metrics

| Metric | Healthy | Warning | Stop |
|---|---|---|---|
| Open rate | 50%+ | 30–50% | Below 30% |
| Reply rate | 2%+ | 1–2% | Below 1% |
| Bounce rate | Below 3% | 3–5% | Above 5% |
| Spam complaints | 0 | Any | Multiple |
| Deliverability score | >95% | 90–95% | <90% |

---

## Bounce Codes (Soft vs Hard)

SMTP codes have the form X.X.X: first digit = outcome (4 temporary, 5 permanent), second = category (1 addressing, 2 mailbox, 3 mail system).

**4XX = soft (temporary)** — "not now", often clears on retry.

| Code | Meaning |
|---|---|
| 4.1.1 | Recipient temporarily unavailable |
| 4.2.2 | Mailbox full |
| 4.4.1 | Connection timeout |
| 4.7.1 | Temporary policy rejection |

**5XX = hard (permanent)** — "no", the address should come off the list.

| Code | Meaning |
|---|---|
| 5.1.1 | Invalid recipient (does not exist) |
| 5.2.1 | Mailbox disabled |
| 5.4.1 | Host not responding / address rejected |
| 5.7.1 | Blocked by policy / security rejection |

Root cause by type: hard 5XX → list/verification/data; soft 4XX → temporary/infra; 5.7.1 → corporate filtering/reputation. Full audit workflow: see `blacklist-bounce-audit.md`.

---

## DNS Records Required (All 4)

| Record | Purpose |
|---|---|
| MX | Routes incoming email to your provider |
| SPF | Declares which servers can send for your domain |
| DKIM | Digital signature proving email authenticity |
| DMARC | Policy for handling SPF/DKIM failures |

---

## Warmup Pool Quality Reference

| Pool | Flame Color | Quality |
|---|---|---|
| Premium | Blue | Best — aged Google/Outlook accounts |
| Standard | Green | Good — default for all accounts |
| Basic | Orange | Lower — mostly SMTP |
| Disabled | Red | Needs reactivation (DNS issue likely) |

---

## Scaling Rules

- Increase volume by max **20% per week**
- Stagger new domain launches: **1 per week max**
- New domains always go through full warmup cycle
- Never add volume AND change copy simultaneously

---

## Seasonal Factors

| Period | Expected Drop | Recovery |
|---|---|---|
| December holidays | 20–30% | Mid-January |
| July–August | 10–20% | September |
| End of quarter | 10–15% | First 2 weeks of new quarter |
| Industry conferences | 15–25% | 1 week post-event |

Do not panic during seasonal dips. Investigate only if the drop exceeds these norms or doesn't recover on schedule.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
