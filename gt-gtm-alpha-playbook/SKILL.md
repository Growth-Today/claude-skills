---
name: gt-gtm-alpha-playbook
description: "GTM Alpha Playbook Generator by Growth Today (growthtoday.co) — builds comprehensive, signal-based GTM playbooks for any target vendor domain using Clay. Use this skill whenever someone provides a company domain and wants to generate a GTM Alpha playbook, signal framework, buying signal analysis, or Clay-powered outbound strategy for that company. Also triggers on: GTM Alpha, GTM playbook, signal-based selling playbook, buying signals for [domain], Clay playbook, build a playbook for [company], signal framework for [domain], GTM Alpha for [prospect], prospect playbook, generate playbook, playbook for [company name], outbound strategy for [domain]. The output is saved as a Google Doc in a GTM playbooks folder. Do NOT use for general Clay questions (use gt-clay), general cold email writing (use gt-cold-email), or general signal sourcing theory (use gt-signal-sourcer)."
---

# GTM Alpha Playbook Generator

Builds comprehensive, industry-specific GTM Alpha playbooks for any target vendor domain. Each playbook maps the vendor's pain points to high-intent buying signals, designs Clay/Claygent workflows to detect those signals, and delivers 3-5 outbound plays with email templates.

## When This Skill Triggers

The user provides a company domain (e.g., "build a GTM Alpha playbook for stamped.io") and wants a full signal-based GTM strategy. The deliverable is a Google Doc saved to a GTM playbooks folder in Google Drive.

## Execution Workflow

### Step 1: Extract the Target Domain

The user will provide a domain. Store it as `{TARGET_DOMAIN}`. This is the vendor — Growth Today's client — who will be selling to their prospects using signal-based GTM.

### Step 2: Research the Target Domain

Use web search to deeply research `{TARGET_DOMAIN}`:

1. Visit the company's website and key pages (product, pricing, about, blog)
2. Search for recent news, funding, leadership changes
3. Search for competitor landscape and market positioning
4. Search for customer reviews (G2, Capterra, TrustRadius) to understand pain points they solve
5. Search for their current GTM approach (do they have SDRs? What channels do they use?)

Synthesize findings into:
- Primary value proposition
- Key differentiators
- Target customer profile (industries, company sizes, personas)
- Current GTM approach (if discernible)
- Competitive landscape

### Step 3: Load Reference Materials

Before generating the playbook, read these resources:

| Resource | Purpose |
|----------|---------|
| `resources/playbook-prompt-framework.md` | The complete playbook generation framework — follow it section by section |
| `resources/gtm-alpha-concept.md` | GTM Alpha philosophy, signal categories, and principles |
| `resources/clay-case-studies.md` | Real Clay case studies for proof points — reference but NEVER attribute their results to {TARGET_DOMAIN} |

### Step 4: Generate the Playbook

Follow the **Required Output Structure** from `resources/playbook-prompt-framework.md` exactly. The playbook has 8 sections:

1. **Executive Summary** — Industry-specific GTM Alpha approach
2. **Business Analysis** — Company profile, offering, GTM assessment, buyer personas
3. **Signal Intelligence Framework** — Table of 5-10 high-intent signals with causal logic, Clay workflows, and quality scores
4. **GTM Playbook** — 3-5 plays each with signal triggers, email templates (using the "Poke the Bear" framework), and personalization strategy
5. **Implementation Validation** — Expected signal volume, A/B testing framework, Go/No-Go criteria
6. **Execution Plan** — 30/60/90-day week-by-week rollout
7. **Competitive Intelligence** — Traditional GTM vs GTM Alpha performance delta
8. **Final Recap** — Why Clay + GTM Alpha is the competitive edge

Key requirements for quality:
- Every signal must have a **causal explanation** for why it indicates buying intent for this specific vendor
- Every signal must have a **concrete Clay/Claygent workflow** specifying data sources and enrichment steps
- Email templates must use the **enhanced email framework** with "Poke the Bear" questions
- Signal thresholds must be specific (e.g., "3+ security job postings AND Series B+ AND no SOC2 badge on website")
- Multi-signal stacking is mandatory — no single-signal plays

### Step 5: Save to Google Drive

Save the completed playbook as a Google Doc in the user's designated GTM playbooks folder so it is stored and searchable for later reference:

- **Destination folder:** the user's GTM playbooks folder in Google Drive (ask the user for the folder, or use the folder they specified earlier in the session). Store it as `{DRIVE_FOLDER}`.
- **Document title:** `GTM Alpha Playbook — {Company Name} ({TARGET_DOMAIN})`

Format the document with clear headings, tables for signal frameworks, and callouts for key insights.

If the playbook is very long (it will be), create the document with the first section and then append the remaining content, since a single write may hit length limits.

### Step 6: Confirm Delivery

After saving, share the Google Doc link with the user and offer to:
- Refine any specific signals or plays
- Add additional plays for different personas
- Generate a companion markdown file as backup

---

## Signal Quality Standards

Every signal proposed in a playbook must pass these minimum thresholds:

- **Precision:** Must target a specific, observable event — not a vague trend
- **Detectability:** Must be collectible through Clay's data sources (job boards, news APIs, tech stack detection, website monitoring, social listening, SEC filings, G2/Capterra reviews, LinkedIn, etc.)
- **Causal Logic:** Must have a clear, explained connection between the signal and buying intent for THIS vendor's specific offering
- **Actionability:** Must enable a specific, personalized outreach message — not just "they might be interested"

Signals that fail any of these criteria should be replaced.

---

## Email Template Quality Standards

Every email template must include:
1. **Signal-specific opening** — Reference the exact signal discovered (not generic)
2. **Quantified pain** — Include a dollar figure or metric for the cost of inaction
3. **"Poke the Bear" question** — A question that forces the prospect to confront a high-stakes nuance they might be ignoring
4. **Social proof** — Reference a similar company or industry benchmark (from the vendor's own case studies if available)
5. **Low-friction CTA** — NOT "book a demo." Instead: offer immediate value (audit, benchmark, analysis)

---

## Common Pitfalls to Avoid

1. **Generic signals** — "Company is growing fast" is not a signal. "Company posted 5+ engineering roles in the last 30 days while their CTO published a blog about technical debt" is a signal.
2. **Missing causal logic** — Don't just list signals. Explain WHY each signal indicates buying intent for this specific vendor.
3. **Ignoring industry context** — A cybersecurity vendor's signals look nothing like an HR tech vendor's signals. Every playbook must be deeply industry-specific.
4. **Single-signal plays** — Always stack 2-4 signals per play. Single signals are noisy.
5. **Attributing Clay case study results to the vendor** — Reference Clay case studies as proof of the platform's capabilities, but never claim the vendor achieved those results.
6. **Vague Clay workflows** — Don't say "use Clay to find this." Specify: which data source, which enrichment provider, which Claygent prompt, which threshold.


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
