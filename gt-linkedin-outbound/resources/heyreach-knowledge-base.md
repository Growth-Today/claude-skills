---
name: heyreach-knowledge-base
version: 1.0
updated: 2026-05-01
description: External reference library of HeyReach resources - guides, templates, and product mechanics - mapped to the gt-linkedin-outbound sub-skills they inform. Use when looking for the source behind a benchmark, framework, or tool-specific workflow referenced elsewhere in this skill.
---

# HeyReach Knowledge Base

HeyReach is the LinkedIn outreach platform GT defaults to (see `rented-engine/rented-engine.md` for the full tooling rationale). Their content team publishes the highest-signal LinkedIn outbound material in the industry - much of it backed by their internal dataset of 96,000+ analyzed campaigns. This file catalogs the resources we draw from, what each adds, and which sub-skill consumes the insight.

When the underlying article updates, this file is the place to revisit before pushing changes into the sub-skills.

---

## How to use this file

- **Building or revising a sub-skill?** Find the relevant section below, read the source article, then update the sub-skill in place.
- **Looking up a benchmark or framework attribution?** This file shows which article each data point came from.
- **Want to point a teammate or client at HeyReach's own writing?** The links below are the canonical entry points.

---

## Source 1 - LinkedIn Outreach Strategy (2026)

**URL:** https://www.heyreach.io/blog/linkedin-outreach-strategy
**Author:** Umer Ishaq (HeyReach)

### What this source uniquely contributes

- **Campaign decay curve.** Every LinkedIn campaign follows a predictable arc: launch window (Days 1-10), plateau (Weeks 2-3), fatigue zone (Week 4+). Most teams misread the plateau as failure. The article frames the fix as structural (segmentation, sender rotation, angle variation) rather than copywriting.
- **Micro-segmentation as decay defense.** Build 3-5 micro-segments rather than one monolithic list, so you can rotate fresh segments in as performance ebbs. Examples include: new-role hires (last 90 days), recently funded companies, prospects who posted on a relevant topic in the last 30 days, and companies hiring for the role your product serves.
- **The "active in last 30 days" Sales Navigator filter.** A high-impact filter most teams skip - surfaces prospects who are actually using LinkedIn and lifts acceptance rates immediately.
- **Decay signals with numeric thresholds.** Acceptance dropping with flat send volume, accepted-but-silent ratio above 60-70%, time-to-first-reply stretching past a week, positive reply ratio declining.
- **External links flagged in DMs (2026 algorithm update).** Keep early-stage messages link-free. Describe the resource and offer to send it on reply.
- **The "Depth Score" and Entity Alignment updates (Jan 2026).** LinkedIn now weights dwell time, saves, and substantive comments far above likes; AI-generated content faces reach reductions; profile-prospect topical alignment affects message visibility.
- **Multi-account math.** Five accounts at 20-25 connection requests each per day = 100-125 daily touches with no single account near its ceiling. Cited LinkedIn cap is 20-40 per account per day.
- **Multi-channel lift number.** LinkedIn + email coordinated sequencing lifts results 45-60% over single-channel.

### Embedded into

| Sub-skill | What was added |
|---|---|
| `copywriting/examples/dm-sequence.md` | Phase-based campaign decay framing in the sequence-management section |
| `copywriting/re-engagement.md` | Decay signal thresholds for triggering re-engagement |
| `copywriting/examples/connection-notes.md` | "Active in last 30 days" Sales Nav filter as a pre-send hygiene step |
| `resources/linkedin-metrics-benchmarks.md` | Decay signal thresholds in diagnostics; phase performance logic |
| `rented-engine/rented-engine.md` | LinkedIn's 20-40/day per-account cap referenced against GT's 15-18 operating range |
| `copywriting/copywriting.md` | "No external links in M1/M2" rule added to universal copy rules |

### Full sub-skill version

→ `resources/campaign-strategy.md` - the full playbook, GT-voiced, covering decay curve, micro-segmentation, multi-account math, and the 3-day setup checklist.

---

## Source 2 - How to Follow Up on LinkedIn

**URL:** https://www.heyreach.io/blog/how-to-follow-up-on-linkedin
**Author:** Nađa Komnenić (HeyReach)

### What this source uniquely contributes

- **The 4-State Follow-up Model.** The single best framework for deciding whether to follow up. Every prospect-thread sits in one of four states, and the right action depends on the state - not on a calendar:
  1. **Not accepted** → don't follow up. Withdraw and route to email.
  2. **Accepted, no reply** → one follow-up max, 7+ day delay, then stop.
  3. **Active, no reply** (posting/engaging on LinkedIn but ignoring you) → wait for new signal or 3-4 weeks. No nudge.
  4. **Replied once, then stalled** → one thoughtful contextual follow-up referencing the prior exchange. No third nudge.
- **Follow-up Priority Rule.** Manual judgment effort gets allocated by prospect value, not by activity. High-value prospects get manual contextual follow-ups; medium-value gets structured automation; low-value gets exited early.
- **"Generic follow-up advice optimizes for activity, not outcome."** The reframe that 5-7 follow-ups is a cargo-cult borrowed from email - LinkedIn is socially visible, so over-messaging changes how you're perceived, not just whether you're ignored.
- **Weekly review workflow.** 30 minutes per week, max 10-15 prospects reviewed manually. Filter Unibox for unanswered threads (>7 days), cut to 10-15 highest-value, signal-check each, decide-tag-move-on.
- **Tag-and-list architecture.** Tags like "Accepted - No Reply" and "Stalled - Stop" become reusable exclusion lists. Operationalizes restraint instead of relying on rep willpower.

### Embedded into

| Sub-skill | What was added |
|---|---|
| `copywriting/re-engagement.md` | Full 4-State model as the central re-engagement framework |
| `copywriting/examples/dm-sequence.md` | State-aware branching at the no-reply step instead of a single linear M2 |
| `resources/linkedin-metrics-benchmarks.md` | The 7+ day no-reply threshold for state transition; weekly review cadence |
| `copywriting/atl-messaging.md` | "Active, no reply" handling for senior prospects who view but don't respond |

### Full sub-skill version

→ `resources/follow-up-system.md` - the full playbook on follow-up discipline. Covers the 4-state model in depth, follow-up priority rule, tag-and-list workflow, and the 30-minute weekly review.

---

## Source 3 - LinkedIn Drip Campaigns

**URL:** https://www.heyreach.io/blog/linkedin-drip-campaigns
**Author:** Bojana Vojnović (HeyReach)

### What this source uniquely contributes

- **Reference-quality benchmarks (older, aspirational).** Per LeadLoft cited in the article: 50%+ acceptance and 30%+ reply rate as healthy. These are aspirational and predate HeyReach's 96K-campaign dataset; we use the HeyReach numbers (Source 4) as primary, but track the gap because some agency clients still target the older benchmarks.
- **Wpromote / State of B2B Digital Marketing stat.** 89% of B2B marketers use LinkedIn for lead generation; 62% report LinkedIn actually generates leads. Useful for proposals and client onboarding decks.
- **Channel comparison stat.** LinkedIn message reply rates can reach ~10.3% vs. ~5.1% typical cold email. Lower than HeyReach's own dataset but closer to what mixed-quality outreach looks like in the wild - useful as a conservative benchmark when projecting client outcomes.
- **HeyReach campaign template library (7 pre-built sequences).** Partnership proposal · Engagement response sequence · Comment follow-up sequence · New connection nurture · Value-first outreach · Social proof sequence · Expand your network sequence. These are starting points for HeyReach users, not GT-blessed copy - but the names map cleanly to angle categories worth keeping in mind.
- **Three full sequence cadences.** The article gives complete day-by-day templates (Day 0 → 1 → 3 → 5 → 8 / Day 0 → 1 → 2 → 5 → 8 → 12 / Day 0 → 1 → 4 → 7 → 10) showing how others structure spacing. GT's standard cadence is in `copywriting/examples/dm-sequence.md`; these are useful as comparison points.
- **Lead import sources.** HeyReach can pull leads from LinkedIn search, Sales Navigator URLs, post reactors, webinar attendees, and CSV - wider than most teams realize.
- **Mid-campaign editing rule.** Message copy can be edited inside an active campaign; sequence steps cannot. Plan accordingly: structure first, copy iterates.

### Embedded into

| Sub-skill | What was added |
|---|---|
| `resources/linkedin-metrics-benchmarks.md` | Aspirational vs. realistic benchmark distinction (LeadLoft 50%+/30%+ vs. HeyReach 21%/22%) |
| `rented-engine/rented-engine.md` | Lead import source list under HeyReach operating notes |
| `personalization/personalization.md` | Confirmed examples of company-, role-change-, and recent-activity-based personalization |
| `copywriting/copywriting.md` | Note that mid-campaign copy edits are possible but step structure is locked |

### Full sub-skill version

→ `resources/drip-campaigns.md` - the full step-by-step build guide for drip campaigns in HeyReach (or similar tools). Covers lead import, sender selection, sequence templates, three full daily-cadence templates, and six common mistakes.

---

## Source 4 - LinkedIn Sales Strategy (LinkedIn-First Engine)

**URL:** https://www.heyreach.io/blog/linkedin-sales-strategy
**Author:** Bojana Vojnović (HeyReach)

### What this source uniquely contributes

- **The 96,051-campaign benchmark dataset.** HeyReach's internal analysis. Sets the new GT-standard benchmarks: ~21% typical acceptance, ~22% typical reply rate, sub-13% indicates a problem, 32-33%+ indicates elite performance. The most defensible LinkedIn benchmark dataset publicly available.
- **The "10.7% of campaigns generate zero replies after acceptance" stat.** Empirical justification for a strong M2 / multi-touch strategy - 1-in-10 campaigns have an opener that lands zero replies, full stop.
- **Diagnostic decision tree.** Maps metric combinations to root causes:
  - Low acceptance + low reply → **targeting** problem
  - High acceptance + low reply → **messaging** problem
  - Both fine but few meetings → **conversion** problem (CTA / qualification)
  - Everything decent but volume low → **infrastructure** problem
- **The four-layer LinkedIn-first engine.** Targeting & enrichment → Warming → Outreach & follow-up → Conversion. Each layer feeds the next. Skip a layer and the whole engine underperforms.
- **The five-stage execution framework.** Signal-based targeting → Strategic warming → Connection & opening → Value-driven follow-up → Meeting conversion. Maps cleanly to GT's existing sub-skill structure.
- **90-day expectation timeline for leadership.** Month 1 = data only, no meetings. Month 2 = first consistent meetings. Month 3 = compounding. This is the right framing for client-facing pilot proposals.
- **Right vs. wrong metrics for LinkedIn-first teams.**
  - Track weekly: meetings booked from LinkedIn, connection-to-conversation rate, conversation-to-meeting rate, pipeline velocity
  - Track monthly: reply rate by message variant, acceptance rate by segment, multi-channel conversion rate
  - Stop tracking: total connections, messages sent per week, vanity engagement
- **"Two personalization hooks per prospect" rule.** Each prospect needs at least one timely signal and one homework detail before entering a campaign.
- **Conditional logic for follow-up branching.** Different paths based on connection accepted vs. profile viewed vs. replied vs. silent - not a single linear sequence.
- **Sender rotation as the main lever for safe scale.** One rep hammering a list is the slow path to restriction. Five accounts rotated within one campaign distribute load and let conversations land at safer per-account volumes.

### Embedded into

| Sub-skill | What was added |
|---|---|
| `resources/linkedin-metrics-benchmarks.md` | The 96K-campaign dataset numbers as primary benchmarks; diagnostic decision tree as core diagnostic framework |
| `SKILL.md` | The four-layer engine as the main mental model; 90-day timeline added to core principles |
| `copywriting/examples/dm-sequence.md` | Conditional branching logic (connected/no-reply vs. profile-viewed vs. replied) |
| `personalization/personalization.md` | "Two hooks minimum" rule (one timely signal + one homework detail) |
| `rented-engine/rented-engine.md` | Sender rotation math (5 × 25 = 125 daily) and rotation as the structural lever |
| `copywriting/re-engagement.md` | "10.7% of campaigns generate zero replies" justifies M2 design |

### Full sub-skill version

→ `resources/linkedin-first-engine.md` - the full strategic playbook for making LinkedIn the primary outbound channel. Covers the 4-layer engine, 5-stage execution, team readiness assessment, foundation work, right metrics, and the 90-day pilot timeline.

---

## Source 5 - HeyReach Templates Hub

**URL:** https://www.heyreach.io/blog-categories/templates

A category page indexing HeyReach's template articles. Useful as a discovery surface when looking for an angle GT hasn't yet documented (e.g., webinar attendee follow-up, post engager outreach, mutual-connection introductions). Treat templates here as inspiration to be adapted - not copy-pasted into GT campaigns.

### Embedded into

`copywriting/copywriting.md` - referenced in the "additional starting points" section for operators who want more pattern variety than GT's nine core frameworks.

---

## Source 6 - HeyReach Guides Hub

**URL:** https://www.heyreach.io/blog-categories/guides

A category page indexing HeyReach's guide-format articles. Useful for deep dives on specific tactics - Sales Navigator masterclass, multichannel coordination, profile optimization, and so on. When a sub-skill needs further depth on a tactic, this is the first place to check before searching elsewhere.

### Embedded into

Referenced as the canonical follow-on resource at the end of `SKILL.md` and `rented-engine/rented-engine.md`.

---

## What is NOT pulled in

For transparency:

- **Product UI screenshots and click-paths.** HeyReach's articles include detailed screenshots for setup. These belong in HeyReach's own help center, not in a copy/strategy skill. We point to their docs (`help.heyreach.io`) instead.
- **HeyReach pricing and feature tier comparisons.** Out of scope for outbound copy and account ops.
- **Affiliate or partner program references.** Not relevant to the skill.
- **Marketing CTAs and trial pitches.** Filtered out.
- **Direct quotes from the articles.** All insights paraphrased into GT's voice and framed within GT's existing structure.

---

## Refresh cadence

Re-check sources 1-4 quarterly. HeyReach updates their flagship articles with new benchmark data and 2026 algorithm changes ~2x per year. When the 96K-campaign dataset gets updated, `resources/linkedin-metrics-benchmarks.md` is the primary file to revise.

---

## Combines with

| Skill / file | Why |
|-------|-----|
| `gt-linkedin-outbound` | Main skill - all embedding lives here |
| `gt-clay` | HeyReach + Clay is the canonical enrichment-into-outreach pipeline |
| `gt-signal-sourcer` | Source 1's micro-segmentation logic is a signal-sourcer concern |
| `gt-list-building` | Source 1's Sales Nav "active in 30 days" filter is a list-building tactic |

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Built and maintained by [Nikola Siljanoski](https://www.linkedin.com/in/nikola-siljanoski/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*