---
name: email-metrics-benchmarks
version: 2.0
updated: 2026-04-07
description: Email metrics to track, benchmarks, and diagnostics for cold outreach. Use when analyzing campaign performance, setting benchmarks, or optimizing email metrics.
---

# Email Metrics & Benchmarks

## Metrics to Track

**Note: Open rate and click rate are NOT tracked.** Tracking pixels in cold emails hurt deliverability. We do not embed tracking pixels. Focus on reply rate and meeting rate only.

### 2X Levers (Metrics you can realistically double)

| Metric | Current Baseline | Good | Great |
|--------|------------------|------|-------|
| Cold email reply rate | 0.5–1.0% | 2–3% | 5%+ |

---

## Performance by Outreach Type

| Outreach Type | Reply Rate |
|---------------|------------|
| Cold outreach (no signal) | 3–5% |
| Signal-based outreach | 18–22% |
| Multi-signal stacked | 35–40% |
| Website visitor follow-up | 25–30% |
| Champion job change | 20–25% |

---

## Email Structure Checklist

```
Opening (trigger) + Assumption + Social proof + Open-ended question
```

| Target | Max Sentences | Max Words |
|--------|---------------|-----------|
| BTL (Managers, ICs) | 3–4 sentences | 90 words |
| ATL (VPs, C-Level) | 2–3 sentences | 60 words |

---

## Deliverability Benchmarks

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Bounce rate | <2% | 2–5% | >5% |
| Spam rate | <0.1% | 0.1–0.3% | >0.3% |
| Unsubscribe rate | <0.5% | 0.5–1% | >1% |

---

## Sequence Performance (GT Standard — SMB)

For full sequence structure, timing, thread rules, and email content → see `resources/frameworks/copywriting/copywriting-sequences.md`

### General Performance Logic

**Email 1** — Most important to optimize. The majority of replies come from here. Test multiple variations simultaneously.

**Email 2** — Performance depends on whether a lead magnet or genuinely useful content is available. SMB vs. mid-market will perform differently — test separately.

**Email 3** — Net new angle. Different value prop and framing from the previous emails.

**Email 4** — Goal is any answer, not just urgency. Multiple variants available — test them against each other.

If no reply after the sequence → re-engage according to `resources/sub-skills/re-engagement.md` and `resources/frameworks/cold-email-mastery.md`

---

## Quick Diagnostics

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Low reply rate | Message relevance or personalization | More personalization, shorten copy, stronger signal |
| Replies but no meetings | Weak CTA or poor qualification | Clearer ask, better targeting |
| High unsubscribe | Too aggressive or wrong ICP | Reduce frequency, refine targeting |
| High bounce rate | Bad list quality | Verify emails before sending, improve enrichment waterfall |

---

## Optimization Priorities

### If Reply Rate Low (<2%)
1. Improve relevance and personalization
2. Shorten message
3. Strengthen CTA
4. Add social proof
5. Test different frameworks

### If Meeting Rate Low (<20% of replies)
1. Qualify better in the message
2. Improve CTA clarity
3. Reduce friction to book
4. Follow up faster

---

## Combines with

| Skill | Why |
|-------|-----|
| `gt-cold-email` | Main orchestrator — routing and sequence structure |
| `gt-signal-sourcer` | Improve reply rates with better signals |
| `gt-list-building` | Fix bounce rate issues with better list quality |
| `gt-email-infra` | Fix deliverability issues |
