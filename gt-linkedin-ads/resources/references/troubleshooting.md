# Troubleshooting LinkedIn Ads

Work through systematically from top to bottom. Allow at least 2 weeks before major modifications, unless CTR < 0.1%.

## 0. Default Settings Audit (check this first — it is where most budget leaks)

LinkedIn's default Campaign Manager settings quietly waste spend in ways most internal teams never catch. Before optimising anything else, strip these out:

- **Audience Expansion** — ON by default. **Turn OFF.** It broadens delivery beyond your defined targeting to "similar" people you did not pick.
- **LinkedIn Audience Network (LAN)** — ON by default. **Turn OFF** for most B2B. It serves impressions on third-party apps and sites, usually low-quality placements that drain budget without intent.
- **ABM budget concentration** — on a named-account campaign, check the Demographics tab for spend distribution. The classic failure is 90% of budget hitting 3-4 accounts out of 400 because a few large companies win every auction. Fix with tighter campaign segmentation and bid controls so spend spreads across the list.
- **Frequency capping** — left uncapped, the same person gets hit far more than ~3x/week, burning budget and causing fatigue. Set a cap.
- **Bid strategy** — "Maximum delivery" (automated) often overspends on cheap, low-value impressions. Switch to manual or target-cost bidding to control what you actually pay per result.

Rebuild bidding, frequency capping, and account-level distribution from scratch rather than trusting the defaults. This single audit recovers more wasted spend than any creative change.

## 1. Audience Targeting Issues
**Symptoms**: Low relevance, poor engagement from wrong people

**Diagnosis**:
- Check Demographics tab: are the right job titles, companies, industries being reached?
- Is Audience Expansion enabled? → **Turn OFF** unless intentionally broadening
- Are multiple personas mixed in one campaign?

**Fixes**:
- Narrow job title targeting
- Layer interest-based filters
- Refresh exclusion lists
- Segment campaigns by customer tier
- Separate 500+ employee companies from <500

## 2. Delivery Problems
**Symptoms**: Under-spending budget, ads not reaching priority accounts

**Diagnosis**:
- Review Demographics tab for spend distribution across accounts
- LinkedIn auction may favor cheaper impressions over higher-value ones

**Fixes**:
- Use bid multipliers (+50%) for priority segments
- Switch from CPM to CPC bidding
- Increase bids if consistently under-spending
- Check if audience is large enough (minimum 300 for LinkedIn)

## 3. Message Misalignment
**Symptoms**: Impressions but low engagement, people see ads but don't interact

**Diagnosis**:
- Compare ad copy against recent customer interviews
- Is messaging leading with features instead of problems?
- Does copy use industry-specific language?

**Fixes**:
- Lead with problems rather than solutions
- Use customer's own language (from sales calls, reviews)
- Test video formats for complex topics
- Simplify messaging — if prospects can't articulate the problem + solution after reading, it's too complex

## 4. Creative Fatigue
**Symptoms**: Declining CTR over time, increasing CPM

**Diagnosis**:
- CTR below **0.45%** for Sponsored Content = problem
- Check frequency — over 3 impressions/week/person = fatigue
- Same creative running for 6+ weeks?

**Fixes**:
- Refresh creative every 4-6 weeks
- Rotate between ad formats
- Test new messaging angles (not just surface-level variations)
- Use Thought Leader Ads for authentic feel

## 5. Landing Page Disconnect
**Symptoms**: Good CTR but low conversions, high bounce rate

**Diagnosis**:
- Is landing page message consistent with ad?
- Does page load quickly on mobile?
- Are form fields excessive?

**Fixes**:
- Ensure ad-to-landing-page message match
- Test mobile rendering
- Reduce form to essential fields only
- Prioritize copy over design in hero section
- Add social proof (logos, testimonials, case studies)

## 6. CTA Misalignment
**Symptoms**: Wrong actions from wrong audience segments

**Diagnosis**:
- Are you asking cold audiences to "Book a demo"?
- Are warm retargeting audiences getting soft CTAs?

**Fixes**:
- **Cold audiences**: Soft CTAs ("Watch walkthrough", "Read guide")
- **Warm audiences**: Medium CTAs ("See case study", "Join webinar")
- **Hot audiences**: Direct CTAs ("Book demo", "Start trial")
- Match CTA strength to awareness level

## Quick Diagnostic Checklist
- [ ] Audience Expansion = OFF
- [ ] LinkedIn Audience Network = OFF (unless intentional)
- [ ] Bid strategy is manual / target-cost (not uncapped Maximum delivery)
- [ ] ABM spend spread across the list, not concentrated on 3-4 accounts
- [ ] Demographics tab reviewed weekly
- [ ] Exclusion lists up to date
- [ ] Creatives refreshed within last 6 weeks
- [ ] CTR > 0.45% for Sponsored Content
- [ ] Landing page loads < 3s on mobile
- [ ] Message match between ad and landing page
- [ ] CTA matches funnel stage
- [ ] Frequency < 3 impressions/week/person
- [ ] Budget spending at least 80% of daily allocation

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
