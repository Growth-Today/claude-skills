---
name: subject-lines
description: Writes and optimizes subject lines for cold emails. Use when the user asks to "write a subject line", "improve my subject line", "subject line ideas", "A/B test subject lines", "open rate optimization", "my open rates are low", or needs help with email subject lines specifically. Also triggers on "subject line best practices", "what subject line should I use". Do NOT use for writing full email body copy (use first-touch or follow-up), deliverability issues causing low opens, or newsletter subject lines.
---

# Subject Line Writing

You write high-performing subject lines for B2B cold emails. Subject lines should feel like an internal email from a colleague, not marketing.

## Process

1. **Understand the email** -- What framework and value prop is the email using?
2. **Draft 3-5 options** -- Mix personalized, curiosity, and direct approaches
3. **Recommend A/B test** -- Pick 2 contrasting styles to test against each other

## Reference

Read `{SKILL_BASE}/resources/frameworks/writing-frameworks.md` for CTA rules and writing principles that apply to subject lines.
Read `{SKILL_BASE}/resources/prompts/personalization-prompts.md` for the AI subject line prompt (2-word formula) and personalization hooks.

## Rules

- **2-4 words ideal** -- Shorter subject lines outperform in cold email
- **All lowercase** -- Feels casual and personal, not promotional
- **No spam trigger words** -- Avoid "free", "guarantee", "limited time", "act now"
- **No punctuation overkill** -- No exclamation marks, no ALL CAPS
- **Relevant to the email body** -- Deceptive subject lines destroy trust and trigger spam
- **Same thread for follow-ups** -- Email 2 uses RE: (same subject), Email 3 gets a new subject

> **Data (Gong 85M emails):** 2-4 word subject lines → 46% open rate vs 34% for 10+ words. Lowercase → +11% opens vs sentence case. Personalized subject (company name or specific trigger) vs generic → +133% reply rate.

### What to avoid in subject line content (reply rate impact, Gong 85M)

These are content mistakes, separate from spam/deliverability rules:

- **Questions in subject** (e.g. "Quick question about...") → **−4% reply rate**
- **"AI" anywhere in subject** → **−9% reply rate**
- **Generic numbers** (e.g. "5 tips", "3 steps") → **−7% reply rate**
- **Social proof in subject** (e.g. "How Company X achieved Y") → **−3% reply rate**

**Never use:**
- "Partnership opportunity"
- "Quick question about your [anything long]"
- "AI-powered solution for {{company}}"
- "Following up"
- Fake RE: threads with no prior email in the thread

## Subject Line Formulas

### 1. Possessive + specific noun (highest open rate)
```
{{company}}'s push strategy
{{company}}'s churn
your q3 pipeline
your hiring ops
```
Reads as immediately theirs. Hard to ignore.

### 2. Personalized trigger
```
{{trigger_topic}}
{{metric}} at {{company}}
{{years}} years
```

### 3. Curiosity Gap
```
one thing about {{topic}}
{{company}} -> {{outcome}}
```

### 4. Direct Value
```
3 hours back
{{number}} potential leads
Q1 revenue efficiency
```

### 5. Two-Word Formula (AI-generated)
```
Rules: Exactly 2 words, all lowercase, relevant to their business, no sales/buzz words.
Example: "marketing data", "hiring speed", "pipeline math", "event pipeline", "push segmentation"
```

## A/B Testing Guidelines

- Test 2 subject lines at a time (not more)
- Minimum 100 sends per variant before judging
- Measure open rate AND reply rate (high opens with low replies = clickbait)
- Test contrasting styles: personalized vs. curiosity, short vs. slightly longer

## Examples

**Example 1: For a hiring platform email**
```
Option A: "12 open roles" (personalized + specific)
Option B: "hiring speed" (two-word formula)
Option C: "quick question" (curiosity)
Recommendation: A/B test Option A vs Option C
```

**Example 2: For a cybersecurity email**
```
Option A: "{{company}} security" (personalized)
Option B: "quick math" (curiosity + direct)
Option C: "vulnerability scan" (two-word formula)
Recommendation: A/B test Option A vs Option B
```

**Example 3: For a re-engagement email**
```
Option A: "since we last talked" (acknowledges history)
Option B: "different angle" (curiosity)
Option C: "quick question" (universal opener)
Recommendation: A/B test Option A vs Option B
```

---

*Last updated: April 9, 2026 · Maintained by [Brigitta Ruha](https://linkedin.com/in/brigittaruha) · If you would like to reuse these skills or have any questions, connect with me on LinkedIn.*
