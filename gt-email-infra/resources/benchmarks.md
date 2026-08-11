# Performance Benchmarks & Data

External market benchmarks for cold email, the numbers that tell you **what's good, what's bad, and where a campaign stands.** Update this file when a new benchmark study lands.

> **Source:** Smartlead *State of Cold Email 2026* (850M+ cold emails analyzed, Q2 2026), with Growth Today data and commentary added. These are **market benchmarks** for evaluation.

> **Results side vs. automation side, why the numbers here differ from `reference.md`.** This file is the **results / investigation** lens: universal market figures for judging outcomes and reply *levels*, independent of any tool. `reference.md` §2–§3 is the **automation / operational** lens: the exact thresholds our system uses to *tag* an inbox (Active / Warmup Needed / Burnt / New) and set its limits. They are meant to differ, one asks *"is this result good vs. the market?"*, the other asks *"should the automation act on this inbox now?"*. Use this file to evaluate performance; use `reference.md` to operate the infrastructure.

## How to read this

- **"Contacts per (positive) reply", LOWER is better** (fewer people contacted to earn one reply). It is the cleanest efficiency metric because it blends list quality, targeting, and copy into one number.
- **Percentile bands** let you place any client metric: are we top-quartile or bottom-10%?
- Each section ends with a **strategic read** for evaluation.

---

## 1. Reply efficiency, contacts per positive reply

| Percentile | Contacts per positive reply |
|---|---|
| Top 5% | **26** |
| Top 10% | 38 |
| Top 25% | 70 |
| Typical / median | **135** |
| Bottom 25% | 270 |
| Bottom 10% | **625** |

**Strategic read.** The typical sender needs **135 contacts per reply**; the top 10% sit near **27–33**. The spread from best to worst is ~**24×** (26 → 625), and that gap is almost entirely **list quality + targeting**, not copy. Where we stand: **< 70 = top quartile**; **> 270 = fix targeting and data before touching the message.**

---

## 2. Bounce rate

| Band | Bounce rate | "1 in X" |
|---|---|---|
| Best 10% | **0.28%** | ~1 in 357 |
| Typical | **1.54%** | ~1 in 65 |
| Worst 10% | **6.71%** | ~1 in 15 |

By provider: **Gmail ~2.95%**, **Outlook ~4.34%** (Outlook lists punish bad data harder).

**Good / bad line:** keep bounce **under 2%** (benchmark pro-tip). Growth Today operational: **> 3% → Burnt**, **> 5% → hard action** (`reference.md` §3).

**Strategic read.** Bounce is a **data-quality readout, not an infra problem**: a wave of hard bounces means the list wasn't valid when sent (see the bounce-audit sub-skill). Above 2%, fix verification/enrichment first. Outlook-heavy segments bounce higher, so verify those lists harder.

---

## 3. Reply rate by follow-up step

| Email # | Reply rate |
|---|---|
| 1 | **1.18%** |
| 2 | 0.73% |
| 3 | 0.56% |
| 4 | 0.49% |
| 5 | 0.37% |
| 6 | 0.35% |
| 7 | 0.33% |

Email 1 is **~3× as efficient as email 7.** Typical campaign = **3 emails**; bottom 10% send **1**; top 10% run 5-9.

**Strategic read.** The first email does the heavy lifting; returns fall off a cliff after 3–4 steps. Run **~3 steps**, follow up **1–2 days** after email 1 (the interested need the nudge fast; the rest won't convert). Don't over-invest in long sequences.

---

## 4. Email length, contacts per reply

| Length | Contacts per reply |
|---|---|
| **Under 50 words** | **68 ← WINNER** |
| 50–99 words | 74 |
| 100–149 words | 97 |
| 150–199 words | 76 |
| 200+ words | 85 |

**Strategic read.** Shortest wins. Cutting from ~98 words to **under 50** can move you **8 contacts per reply** better. Matters most for Outlook audiences (keep the first email short and reply-seeking). Note the non-monotonic dip at 150–199, but under-50 is still the clear winner.

---

## 5. Response window (cumulative share of all replies)

| Replies land within | Cumulative % |
|---|---|
| 1 hour | **64%** |
| 24 hours | **88.5%** |
| 72 hours | **94%** |

**Strategic read.** **Reply speed is a list-quality signal.** 94% of replies you'll ever get arrive within 72 hours. If a segment stays silent past 72h, the **targeting was wrong, not the copy**: re-segment rather than rewrite.

---

## 6. Send timing, contacts per reply

**By hour:** 7am UTC (peak) = **75** · best window 6–10am UTC = **75–90** · busy 1–5pm UTC = **120**.
**By day:** Wednesday (best) = **110** · Sunday = **111** · Saturday (worst) = **122**. → **"No magic day."**

**Strategic read.** **Time-of-day beats day-of-week.** Send **6–10am UTC**; the peak (7am) is ~40% more efficient than the 1–5pm crowd (75 vs 120). Day choice is marginal (110 vs 122), don't over-optimize the day.

---

## 7. Infrastructure, performance by inbox provider

| Provider | Contacts per reply | Bounce rate |
|---|---|---|
| **Gmail** | **90** | 2.95% |
| **Outlook** | 120 | 4.34% |
| **Custom servers** | **179** |, |

**Strategic read.** **Gmail out-performs Outlook and custom SMTP** on reply efficiency, and Outlook bounces harder. Custom servers are the weakest on reply efficiency (179), use them for **scale/cost**, not as the primary sending pool. Cold-emailing Gmail/SMB recipients gives ~**3× the reply chance**; above that tier, add cold calls + LinkedIn. Warm every new mailbox **30 days**, keep **< 50 sends/day** after.

---

## 8. Targeting & personalization

- Typical campaign targets **499 prospects** (range **25 → 9,871**).
- First-email personalization: **top half of senders = 100%** (every email), **median = 75%**, **bottom quarter = 14%**.

**Strategic read.** Tight, well-matched lists beat volume. The best senders personalize **every** first email, and personalization is only possible if you have the data, which is why data foundation comes first.

---

## 9. Daily volume per mailbox

| Level | Sends/day/mailbox |
|---|---|
| Safe (low risk) | **< 50** |
| Median sender | **13.92** |
| Danger (throttling risk) | **50+** |

**Strategic read.** **Scale by adding mailboxes, never by pushing volume per mailbox**: ten inboxes at 40/day beat four at 100/day. Ties to Growth Today per-state limits in `reference.md` §1 (Active Google cold 20 / Outlook 5).

---

## 10. Good vs bad, evaluation cheat-sheet

Use this to grade any client at a glance. "Direction" shows which way is better.

| Metric | Direction | Best-in-class | Typical / median | Poor | Growth Today target |
|---|---|---|---|---|---|
| Contacts per positive reply | lower | ≤ 26–38 (top 5–10%) | 135 | ≥ 270–625 | < 70 |
| Bounce rate | lower | 0.28% | 1.54% | 6.71% | < 2% (act > 3%) |
| First-email reply rate | higher | > 1.18% | ~1.18% | < 0.5% | ≥ 0.5% (see reference §2) |
| Reply within 72h | higher |, | 94% of all replies |, | re-segment if silent past 72h |
| Email length (first email) | shorter | < 50 words | ~135 words region | 100–149 words | < 50 words, plain text |
| Sequence length | ~3 | 3 steps | 3 | 1 (bottom 10%) or 9 (top 5%) | ~3 steps |
| Daily volume / mailbox | lower risk | < 50 | 13.92 | 50+ | ≤ Active limits (ref §1) |
| Personalization (first email) | higher | 100% | 75% | 14% | 100% where data allows |

---

## 11. Growth Today's take

- **Top 20% of campaigns drive ~80% of pipeline.** Copy is overrated; **a great audience solves your copy problems** because the message writes itself.
- **Order of operations:** **Data foundation → Automation → GTM activation.** You can't run channels without data, it's table stakes, and doing it well still takes streamlined execution.
- **First-party, compounding data beats third-party.** Third-party signals drive quick ROI (great for a QBR slide) but decay; first-party data compounds. Start building the first-party signal warehouse now for a durable GTM.

---

*Benchmarks: Smartlead "State of Cold Email 2026" (850M+ emails, Q2 2026) + Growth Today. Update on each new benchmark release.*

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
