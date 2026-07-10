---
name: linkedin-formats
description: Select the optimal LinkedIn content format and follow format-specific guidelines. Use when the user asks about carousels, video posts, text posts, polls, LinkedIn newsletters, format selection, reach multipliers, or content format specs. Do NOT use for post writing/structure (use storytelling) or posting schedule (use scheduling).
---

# LinkedIn Content Formats

You are a specialist in selecting and optimizing LinkedIn content formats based on reach multipliers, content goals, and audience behavior.

## Reference

Load `{SKILL_BASE}/resources/references/gt-linkedin-algorithm.md` for the complete format performance data, specs, and guidelines.
All visuals are designed in **Claude Design**, where the GT brand system (colors, backgrounds, fonts) already lives — this skill decides *which format* to use, not the visual styling.
Read `{SKILL_BASE}/resources/performance/performance-playbook.md` for character count sweet spots by post type and visual companion impact data.

## Format Performance Table

| Format | Status | Avg Engagement | Notes |
|--------|--------|----------------|-------|
| **Single Image Infographic** | ✅ PRIMARY | High saves + reach | Only format boostable as Thought Leadership Ad |
| **Text-Only** | ✅ Allowed | 2-3% | Personal stories, hot takes — all GT "text-only" posts actually had PDF attachments historically; now replaced by single image |
| **Polls** | ✅ Sparingly | High clicks | Max 1/week, audience research only |
| **Newsletters** | ✅ Allowed | 30-50% open | Deep content, subscriber growth |
| **PDF Carousel** | 🚫 PROHIBITED | — | Cannot be boosted as Thought Leadership Ad |
| **Native Video** | ⚠️ Type-dependent | Varies | Make it short + catchy (Shorts/Reels style) OR longer substantial (webinar). Drive to YouTube / IG Reels. Watch analytics |
| **Animated Infographic (MP4/GIF loop)** | ✅ Allowed | High | MP4 loop (from Figma) or GIF — but never cheap/generic GIFs |
| **Cheap/generic GIF** | 🚫 PROHIBITED | — | Looks bad, boring, off-brand |
| **External Links in post** | 🚫 Avoid | -40-60% reach | Put links in first comment instead |

## GT Format Policy — Single Image First

Every GT LinkedIn post must be a **single image (PNG or JPG, 1080×1350px, 4:5)** as the default. Animated infographics (MP4 loop or GIF) are also allowed. A visual is mandatory on every post.

**Prohibited formats:**
- **PDF carousel** — cannot be boosted as a Thought Leadership Ad; LinkedIn classifies it as "carousel" which excludes it from single image ad amplification; no alt text support
- **Cheap/generic GIF** — looks bad, boring, off-brand. Never use throwaway low-effort GIFs. (A well-made animated MP4 loop from Figma is a different thing — that's allowed.)

**Native video — make it the right type:**
- When we use video, it should be built for how video actually performs: either **short, catchy, and scroll-stopping** (YouTube Shorts / IG Reels style), or a **longer, substantial piece** (webinar, deep tutorial). Don't post middling in-between video.
- The play is usually to **drive to YouTube or Instagram Reels**, where the format is native and performs.
- Whenever you drive to YouTube / IG Reels, **always watch the analytics** and let them tell you what's landing.

**Why single image first:** Any post we want to amplify via paid must be a single image from the moment it's published. A well-designed cheat sheet communicates as much as a carousel. If a user requests a carousel, explain the policy and propose a cheat sheet or tool map instead.

## Text-Only Post Guidelines

**Text-only is NOT preferred.** Every post needs an aesthetic visual — a visual is mandatory. Use text-only *only* when the post is a personal story, a vulnerability piece, or something genuinely special where a visual would dilute it. Otherwise, always attach a visual.

When you do go text-only:
- Optimal length: **800-1,300 characters**
- "See more" fold at **210 characters** on mobile -- hook must land here
- Single sentences per line with blank lines between
- Use unicode bullets/arrows for visual structure
- No links in the post body (kills reach)

## Native Video — Make It the Right Type

If you use video, match how video actually performs: either **short, catchy, scroll-stopping** (YouTube Shorts / IG Reels style) or a **longer substantial piece** (webinar, deep tutorial). Nothing middling in between. The usual play is to drive people to **YouTube** or **Instagram Reels**, where the format is native. Whenever you do, watch the analytics and let them steer what you make next.

If you do publish a native video:
- Short form: fast hook in the first 2 seconds, tight cut, captions
- **85%+ of video is watched on mute** -- captions are mandatory
- Vertical format (9:16) for short form
- Talking-head + text overlay = strong combo
- Upload natively (never paste a YouTube link in the body)

## GT Design Format

All visuals are single image (1080×1350px, 4:5). For choosing the visual style based on content type, use the **Updated Visual Format Decision Tree (2026)** further down in this file — it is the single source of truth for format selection.

## External Link Workaround

Posts with links get **40-60% less reach**. Instead:
1. Post the text natively without any link
2. Add the link in the **first comment**
3. Mention "link in comments" in the post body

## Where the design happens

When a visual is needed, the actual design is done in **Claude Design**, which already holds the GT brand system (colors, backgrounds, fonts) and dimensions. Your job here is to pick the right *format* (using the decision tree below) and hand the content over — Claude Design applies the styling.

## Examples

**Example 1** -- User wants to share a 7-step framework:
Recommend **cheat sheet infographic** (FORMAT 1). 7 numbered sections, tool pills, footer stats — built in GT brand styling in Claude Design. Single image 1080×1350px. PDF carousel is prohibited — not boostable as Thought Leadership Ad.

**Example 2** -- User wants to share a personal failure story:
Recommend **text-only** post. Stories perform well in text. Use Mistake>Lesson framework, keep under 1,300 characters, strong hook in first 210 chars.

**Example 3** -- User wants to promote a blog article:
Recommend **text-only post summarizing key insights** + link in first comment. Never paste the URL in the post body. Tease the best insight to drive curiosity.

## Information-Dense Single Infographic (GT Priority Format)

This is Growth Today's highest-performing visual format based on Brigi's data.

**Why it works:** Forces viewer to zoom in → longer dwell time → more saves → algorithm boost.

**Best for:**
- Tech Stack Reveals (tool maps, funnel diagrams)
- GTM System Visualizations (end-to-end flow diagrams)
- Framework Dashboards (multi-section reference graphics)

**GT proven examples:**
- "We automated 70 outbound tasks" → 55K impressions, S-tier (Brigi)
- GTM Funnel Tech Stack format
- "Master The Game of LinkedIn" dashboard (Jani)

→ Designed in Claude Design.

---

## LinkedIn Decides — Always Start From Your Own Data

Ultimately **LinkedIn's algorithm decides which posts and formats get distributed**, not us. Treat every format rule here as a current best guess, not a fixed law. The algorithm changes materially roughly every three months, so nothing in this skill is permanent.

How to stay current:
- **Always start from your own LinkedIn analytics.** What's actually getting reach, saves, and comments *for this account, right now* beats any general rule.
- **Read the funnel numbers.** Look at how your ToF (top of funnel — reach/awareness), MoF (middle — engagement/consideration), and BoF (bottom — comments/DMs/pipeline) posts are performing, and let that steer which formats you lean into.
- **Benchmark against others.** Compare with other thought leaders and competitors in the space — what formats they're winning with is a useful signal for where the algorithm is currently rewarding.
- **Re-check quarterly.** When performance shifts, update the format mix. Don't keep publishing a format that's decaying just because it worked last quarter.

## Format Selection Always Starts From the Content

Never pick a format in the abstract. Every format decision flows from three things, in this order:
1. **Content topic** — what is the post actually about?
2. **Pillar** — which GT content pillar does it belong to?
3. **Goal** — what funnel stage / outcome is it for (ToF reach, MoF engagement, BoF pipeline)?

Once those are clear, the format follows (use the decision tree below), and the visual itself is built in **Claude Design**, where the GT brand system lives.

---

## Critical 2026 Insight: Visuals Are Non-Negotiable

Visuals are used in virtually every high-performing post. Text-only is extremely rare (maybe 1 in 100). **Never publish without a visual.**

The question is not text vs. visual — it's **which visual format** to use:
- Claude Code workflow → terminal screenshot or proof visual
- Vulnerability/personal story → portrait photo or branded card
- Contrarian take → bold single-stat graphic or comparison visual
- Lessons/frameworks → information-dense infographic or cheat sheet
- Campaign results → proof visual (real dashboard screenshot)

---

## Proof Visual Format (New Priority)

**What it is:** Real tool UI screenshot + bold title/question overlay at the top, in GT brand styling. Designed in Claude Design.

**Examples:**
- "Cold Outbound Still Works?" → Instantly.ai campaign dashboard showing 22.1K sent, 12.32% reply rate, $2.1M pipeline
- "Ads in Clay?" → Clay ad audiences UI showing 92.1% LinkedIn match rate

**Why it works:**
- Shows REAL data, not designed numbers → instant credibility
- Bold title = scroll-stopper at thumbnail size
- Information-dense (real dashboard) → save-bait
- No expensive design needed — screenshot + title overlay in Claude Design

**How it's built:**
- Tool UI screenshot as background (real dashboard — Clay, HubSpot, Instantly, etc.)
- Bold title overlay at top in GT brand styling (applied in Claude Design)
- NO logo needed in most cases (your face/name is enough)
- Dimensions: 1080×1350 (4:5)

**When to use:**
- Campaign results ("Here's what our outbound actually looked like")
- Tool comparisons ("Clay vs Apollo — real data")
- Claude Code outputs ("Here's what the terminal returned")
- Any post where you have a real dashboard/metric to show

---

## Cheat Sheet / Master Map (Highest Save-Bait Format)

**What it is:** Everything about one topic on a single dense page — roles, tools, metrics, skills, books, people. Forces zoom-in. Gets saved and referenced for months. Built in GT brand styling in Claude Design.

**When to use:**
- Comprehensive role or topic overview
- Annual resources ("2026 GTM Stack", "Full Outbound Playbook")
- Best for Tech Stack Reveals pillar and Growth Playbooks pillar

**Performance:** S-tier save rate. May have lower comment count but extremely high saves = strong algorithm signal.

**GT examples to create:**
- "The Growth Today GTM Stack 2026" — full company tech stack cheat sheet
- "GTM Engineer Cheat Sheet" — GT version with our tools and frameworks
- "The Full Outbound Playbook 2026" — end-to-end on one page

→ Designed in Claude Design.

---

## Comparison Visual (Contrarian Format)

**What it is:** Two-column visual showing the naive view vs the expert view of a topic. Built in GT brand styling in Claude Design (light background, green gradient accents, never dark).

**When to use:**
- Contrarian takes and hot opinions
- Role/concept education ("what this role actually involves")
- Before/after comparisons (2023 vs 2026 outbound)

**Hook formula for companion text:**
> "How [X] is viewed: By [Group A] vs By [Group B]"
> "Most people think [X] means [simple thing]. GTM Engineers know it means [complex thing]."

**GT examples to create:**
- "How Claude Code Is Viewed: By Most People vs By GTM Engineers"
- "How Cold Outreach Is Viewed: By Beginners vs By Top 1%"
- "How ABM Is Viewed: By Sales Teams vs By GTM Engineers"
- "Outbound in 2023 vs Outbound in 2026"

→ Designed in Claude Design.

---

## Updated Visual Format Decision Tree (2026)

```
What type of content is this?

Comprehensive overview / reference resource?
  → CHEAT SHEET (FORMAT 1 — PRIMARY, GT light background, numbered sections, save-bait)

Tech stack / tool reveal by layer?
  → TOOL MAP (FORMAT 4 — PRIMARY, numbered rows, tool logo pills)

Comparison / activation scenarios?
  → DASHBOARD GRID (FORMAT 5 — RECOMMENDED)

Contrarian take / naive vs expert view?
  → COMPARISON VISUAL (RECOMMENDED, GT light background, two columns, green gradient accents)

Real campaign results / tool output to show?
  → PROOF VISUAL (RECOMMENDED, dashboard screenshot + bold title overlay, GT brand colors)

Signal tiering / account scoring?
  → TIER RING (FORMAT 10 — RECOMMENDED)

Sequential workflow, many steps, genuinely cannot fit in 4:5?
  → FORMAT 2 or FORMAT 3 (EXCEPTIONAL — max 1x/week)
  → Always ask first: "Can I say this as a cheat sheet?" If yes → use FORMAT 1.

Personal story / vulnerability?
  → Portrait photo or simple branded card (text-only only if truly special)

Claude Code workflow?
  → Terminal screenshot OR proof visual of output

User requests carousel / PDF / cheap GIF?
  → PROHIBITED — explain policy, suggest single image alternative

Video?
  → Make it short + catchy (Shorts/Reels style) OR longer substantial (webinar). Drive to YouTube / IG Reels. Watch analytics.
```

> **Note on creative formats:** The formats above reflect GT's proven top performers as of 2026. Other creative approaches — map visuals, people grids, cover/splash visuals, hub-and-spoke diagrams, etc. — are not prohibited. Use creative judgment based on what best serves the post topic and funnel stage. The policy governs **file format** (single image first, animated MP4/GIF loop allowed, no PDF carousels or cheap GIFs), not **creative style**.


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
