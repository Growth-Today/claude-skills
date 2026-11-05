---
name: list-building-deep-dives
---

# List Building — Detailed Reference

Deep dives into each phase, ICP construction, multi-source workflows, and the Apollo + Clay template.

---

## ICP Deep Dive: Building Your Ideal Customer Profile

### Step 1: Analyze Your Best Customers

Pull top 20–30 customers by: highest LTV, fastest close, lowest churn, highest NPS, easiest to work with.

**Answer:**
- What industries are they in?
- What's their average company size?
- What tools do they use?
- What triggered them to buy?
- What do they have in common?

**Tool:** Export from CRM → enrich in Clay with firmographics/technographics → look for patterns.

### Step 2: Analyze Your Worst Customers (Anti-ICP)

Pull customers who: churned quickly, had long/painful sales cycles, required excessive support, low LTV.

**Answer:**
- What made them a bad fit?
- What should have been a red flag?
- What do they have in common?

### Step 3: Interview Your Team

- **Sales:** "Who closes fastest? Who's most excited about our product?"
- **Customer Success:** "Who gets the most value? Easiest to onboard?"
- **Marketing:** "What content resonates? What channels work best?"
- **Product:** "Who uses the product most effectively?"

### Step 4: Document Your ICP

One-page document with must-haves, nice-to-haves, and disqualifiers (see template in SKILL.md).

### Step 5: Score Your ICP

Build a 0–100 scoring system in Clay as a formula column that auto-scores every company.

**30-Minute Exercise:**
1. List top 10 best customers
2. Find 3 patterns they share
3. List top 5 worst customers
4. Find 2 patterns they share (anti-ICP)
5. Write ICP hypothesis in one paragraph
6. Create scoring rubric

---

## ICP Layer Details

### Layer 1: Firmographics

| Criteria | Questions | Example |
|---|---|---|
| Industry | What industries do best customers operate in? | SaaS, E-commerce, Manufacturing |
| Company Size | How many employees? | 50–500 (mid-market) |
| Revenue | Annual revenue range? | $10M–$100M ARR |
| Location | HQ? Where do they operate? | US-based, expanding to EU |
| Company Age | Startup vs established? | 3–10 years old |
| Business Model | B2B, B2C, B2B2C? | B2B SaaS companies |
| Funding Stage | Bootstrapped to PE-backed? | Series A-B |

**Data sources:** Your CRM (best), LinkedIn Sales Nav, Clay enrichments, Clearbit, People Data Labs.

### Layer 2: Technographics

| Category | What to Look For | Why |
|---|---|---|
| CRM | Salesforce, HubSpot, Pipedrive | Sales sophistication, budget |
| Marketing Automation | Marketo, Pardot, ActiveCampaign | Marketing maturity |
| Sales Tools | Outreach, SalesLoft, Apollo | Active outbound motion |
| Analytics | Segment, Amplitude, Mixpanel | Data-driven culture |
| Infrastructure | AWS, GCP, Azure | Technical sophistication |
| Complementary Tools | Tools that integrate with yours | Easy adoption path |
| Competitor Tools | Using your competitors | Ripe for switching |

**Data sources in Clay:** BuiltWith, Clearbit, 6sense, HG Insights.

### Layer 3: Behavioral Signals

| Signal | What to Track | Where to Find |
|---|---|---|
| Hiring | Roles related to your solution | LinkedIn, job boards, Clay job tracking |
| Funding | Recent rounds | Crunchbase, PitchBook, news |
| Expansion | New offices, new markets | News, LinkedIn, company websites |
| Leadership Changes | New C-level hires | LinkedIn, press releases |
| Product Launches | New products/features | Product Hunt, news, social |
| Tech Stack Changes | Adding/removing tools | BuiltWith, technographic tracking |
| Content Engagement | Downloads, pricing page visits | Your analytics, intent data |
| Competitor Activity | Competitor mentions, visits | 6sense, Bombora, G2 |

**In Clay:** Claygent for news monitoring, job change tracking, Crunchbase/PitchBook integrations, 6sense/Bombora for intent.

### Layer 4: Psychographics

| Indicator | How to Identify |
|---|---|
| Growth vs optimization mindset | Hiring velocity, funding, leadership messaging |
| Innovation vs conservative | Tech stack (cutting-edge vs legacy), company age |
| Data-driven culture | Analytics tools, data team size |
| Customer-centric | NPS scores, CS team size, reviews |
| Compliance-focused | Industry (healthcare, finance), certifications (SOC2, GDPR) |
| Remote-first | Job postings, office locations, culture |

**Research:** About page, careers page, blog, Glassdoor reviews, leadership LinkedIn posts, customer case studies, Claygent for website summaries.

---

## ICP Examples

### Sales Engagement Platform
- Industry: B2B SaaS, Professional Services, Agencies
- Size: 50–500 employees, $5M–$50M revenue
- Tech: Salesforce or HubSpot CRM
- Signals: Hiring SDRs/AEs, raised Series A/B
- Psychographics: Growth-focused, outbound sales motion

### HR Tech Platform
- Industry: Technology, Financial Services, Healthcare
- Size: 200–2,000 employees, $20M–$200M revenue
- Tech: Workday, BambooHR, or Greenhouse
- Signals: Hiring HR Ops, headcount expanding >15% YoY
- Psychographics: Employee experience-focused, remote-first

### Marketing Automation Tool
- Industry: E-commerce, DTC Brands, B2C SaaS
- Size: 20–200 employees, $2M–$20M revenue
- Tech: Shopify, Klaviyo, or Attentive
- Signals: Launching new products, expanding to new channels
- Psychographics: Data-driven, customer acquisition-focused

---

## Multi-Source Company Discovery: Detailed Workflows

### Source 1: Clay Find Companies

1. Create new table in Clay
2. Add Source → Find Companies
3. Set filters matching ICP (industry, employees, location, technologies, funding)
4. Preview results → run source
5. Use "OR" logic for technologies to maximize coverage
6. Save filter templates for reuse

**Cost:** Free to search; credits for enrichment columns.

### Source 2: Apollo (CSV → Clay Import)

1. Apollo.io → Company search
2. Set same ICP filters
3. Use keywords to narrow (e.g., "B2B SaaS" in description)
4. Export as CSV (always include Domain field)
5. Clay → new table → Import CSV → map columns

**Cost:** Free tier: 50 exports/month | Basic $49/mo (10K) | Pro $79/mo (unlimited).

### Source 3: LinkedIn Sales Navigator

1. Sales Navigator → Company Search
2. Advanced filters: headcount, growth %, hiring, posted recently, technologies
3. Save as Lead List (max 2,500)
4. Export via Phantombuster ($50–100/mo) or Evaboot
5. Import to Clay

**Unique filters:** Headcount Growth, Posted on LinkedIn, Hiring on LinkedIn.
**Cost:** Core $99/mo | Advanced $149/mo + export tools.

### Multi-Source Merge Workflow

1. Table 1: Clay Companies (from Clay Find Companies)
2. Table 2: Apollo Companies (from CSV import)
3. Table 3: Merged — use "Write to Other Table" from both Table 1 and Table 2
4. In Table 3: dedupe by Domain
5. (Optional) Table 4: LinkedIn Sales Nav companies → write to Table 3 → dedupe again

**Typical result:** 40–70% more companies than single source.

### Advanced Strategies

**Waterfall Sourcing:** Start with highest-quality source (LinkedIn with intent signals), add next source only if you need more volume.

**Source by Segment:** Enterprise → ZoomInfo + LinkedIn; Mid-market → Clay + Apollo; Startups → Crunchbase + Clay.

**Layered Sourcing:** Broad search (10K) → add intent signals (filter to 3K) → enrich and score (final 1K A-tier).

---

## Apollo + Clay Template: 6-Table Workflow

### Table 1: Apollo Companies (CSV Import)
- Import CSV from Apollo export
- Key fields: Company name, domain, industry, employee count, revenue, location

### Table 2: Clay Companies (Native Search)
- Clay "Find Companies" source
- Match Apollo search criteria

### Table 3: Merged & Deduped Companies + Enrichment
- "Write to Other Table" from Table 1 and Table 2 into Table 3
- Dedupe by company domain
- Add: company tiering logic (formula/AI), scoring, additional enrichment

**Step-by-step merge:**
1. Create blank Table 3 ("Merged Companies - Deduped")
2. In Table 1: Add "Write to Other Table" column → select Table 3 → map fields → run all rows
3. In Table 2: Add "Write to Other Table" column → select Table 3 → map same fields → run all rows
4. In Table 3: Select Domain (or Company Name) column → click DeDupe → Value → delete duplicates
5. Add enrichment columns (tiering, scoring, qualification)

**Pro tips:**
- Field mapping must be consistent across both source tables
- Use run conditions to only write qualified companies
- Re-running Write to Table will auto-update Table 3

### Table 4: Apollo People
- Import domains from Table 3 (filtered for qualified companies)
- Apollo people search: job titles, seniority, departments

### Table 5: Clay People
- Same domains from Table 3
- Clay "Find People" source with matching criteria

### Table 6: Merged & Deduped People (Final Output)
- Import from Table 4 and Table 5
- Dedupe by email (primary) or name + company domain
- Final enrichment: email validation, phone waterfalls, personalization data, AI messaging
- **Output: final list ready for outreach**

---

## Local Prospecting

For clients selling to local businesses (gyms, clinics, logistics, real estate, etc.) that don't appear in Apollo/LinkedIn.

### Option A: Openmart + Clay (US-based)
1. Use [Openmart](https://openmart.ai/) to find local leads by category/location
2. Export → clean CSV
3. Import to Clay → enrich (email, website, LinkedIn, owner/decision-maker)

### Option B: Google Maps Scraping via Clay
1. Clay's Google Maps integration → search by type + location
2. Pull: name, website, address, phone
3. Enrich: email, LinkedIn, ownership data

### Option C: Directory Scraping
1. Find niche directory (Clutch.co, local chambers, industry associations)
2. Use [Instant Data Scraper](https://chromewebstore.google.com/detail/data-scraping-tool/ejcgomaeiikgjcebfmhaoddenaijpgfb) Chrome extension
3. Export CSV → import to Clay → enrich
4. If domain missing: use Claygent to find company website from name

See [list-building-directories.md](list-building-directories.md) for curated industry-specific directories.

---

## Store Leads (E-Commerce List Building)

### Overview

Store Leads tracks millions of e-commerce stores across Shopify, Magento, Salesforce Commerce Cloud, and WooCommerce, providing data like installed apps, technologies, social following, and platform rank for building targeted e-commerce lists.

**Benefits:**
- **Better targeting** — filter by platform, sales, location, or tech stack to match the client's ICP.
- **Save Clay credits/time** — export a company list into Clay and enrich it for free using GT's Store Leads API key, instead of exporting every field manually.
- **Automate prospecting** — set up Store Leads workflows to auto-pull new matching companies so you're not rebuilding campaigns from scratch.
- **Personalized outreach** — use app/tech-stack insights to write more relevant, specific messaging.

### Where It Fits in the Sourcing Stack

| Source | Role | Notes |
|---|---|---|
| **Store Leads** | Primary — always start here | Most accurate/comprehensive source for e-commerce; GT has an active subscription |
| **Sales Navigator** | Secondary — only to extend a list | Less accurate; cross-check new companies against your existing Store Leads list in Clay, and only use an AI-agent website check for the ones that don't already appear (AI agent visits in Clay get expensive at scale, so use sparingly) |
| **Charm** | Not recommended | ~$800; 99% of Shopify stores are already covered by Store Leads, making it mostly redundant |
| **BuiltWith** | Optional | Find e-commerce sites by tech filter → cross-reference with Apollo/Scrubby for emails → LinkedIn/Apollo/BetterContact for decision-makers (Owner, CEO, VP E-Commerce, Marketing Manager) → validate emails with MillionVerifier. For very large lists, ExportApollo (see the Apollo section above) is usually the better path — most of the time Clay alone covers contact needs |

**Pro tip:** Default to Store Leads for accuracy and efficiency. Use Sales Navigator sparingly to fill gaps, verify anything new before adding it to a campaign, and skip Charm unless there's a specific reason Store Leads can't cover it.

### Account Access (Shared Account — VPN Required)

> GT uses one shared enterprise Store Leads account. Logging in from multiple locations at the same time gets the account flagged and suspended.

1. Before accessing Store Leads, connect to a VPN (NordVPN) — install the desktop app, log in with the credentials stored in 1Password, and set the country to Hungary.
2. Confirm the VPN connection is active before opening the Store Leads site.
3. Check the **#help-me** Slack channel first to make sure no one else is using the account at the same time.
4. For login access, ask in **#help-me** — don't create a new account or guess at credentials.

### How to Use Store Leads (High-Level)

1. **Apps & Technologies** — look up the top apps/technologies in any category; useful for spotting trends or picking a specific tool to target in outreach.
2. **Domains** — build the company list itself.
   - **Advanced Search (recommended):** filter by keywords, installed apps/technologies, country, and platform for a precisely qualified list.
   - **Basic Search (not recommended):** a simple platform/country search — too broad for real targeting.
3. **Workflows** — auto-add new matching companies into Clay or a CRM on a schedule, keeping lists evergreen without manual rebuilding.
4. **Help** — Store Leads' own help articles.
5. **Support** — Store Leads support directly, for account-level issues.

### Filter Logic & Search Mechanics

- **Or:** matches stores with *any* of the checked values.
- **Not Or:** excludes stores matching *any* of the checked values.
- **And:** matches stores meeting *all* of the checked values.
- **Not And:** excludes stores meeting *all* of the checked values.
- See [Store Leads' Advanced Search docs](https://storeleads.app/help/features/advanced-search) for worked examples of each.
- Save a search as a list (⭐ button) so you can revisit and edit the exact filters later instead of rebuilding from scratch.
- **Exporting to Clay:** you don't need to export every field from Store Leads — pull the list into Clay and enrich it with GT's Store Leads API key instead.
- When building an apps/technologies list, use the **combined list** (apps + tech together) — not all apps are tracked as technologies and vice versa, so a single-category list under-covers the market.
- Full supported lists: [Apps](https://storeleads.app/help/faq/list-of-supported-apps) · [Technologies](https://storeleads.app/help/faq/list-of-supported-technologies)

### Data Points & Filters Reference

| Filter | Definition | Usage | Notes/Best Practices |
|---|---|---|---|
| Platform | E-commerce platform used (Shopify, WooCommerce, etc.) | Target specific platforms, or use "last platform change" to spot migrations | Common platforms: Shopify, Magento, Salesforce, WooCommerce, custom carts |
| Apps & Technologies | Apps = installed tools; Technologies = broader integrations (e.g. payment gateways) | Build separate lists for each to ensure full coverage | Not all apps are categorized as technologies and vice versa — check both |
| Categories | Industry/product type (beauty, fitness, etc.) | Use main categories for broad targeting | Avoid subcategories unless the campaign needs very specific segmentation |
| Estimated Sales | Approximate store revenue | Target a sales range to prioritize by size | Approximate only — not fully accurate |
| Product Price | Min/max product price range | Target high-ticket or budget stores | Useful for luxury vs. low-cost market targeting |
| Platform Rank | Store's rank within its platform (e.g. top 50K Shopify) | Target top performers on a specific platform | Specify a rank range to filter tightly |
| Rank | Overall rank across all platforms | Broader, cross-platform targeting | Use for global campaigns |
| Combined Followers | Total social followers across platforms | Use only if social presence matters to the campaign | Not a reliable growth indicator on its own |
| Reviews & Ratings | Combined reviews + average rating | Target larger, established stores with good reviews | More useful for bigger brands |
| E-Commerce Features | Store features (POS, mobile app, etc.) | Build competitor or capability-based lists | Good for identifying unique store capabilities |
| Store Status | Active vs. inactive | Always filter to active stores | Avoids wasting outreach on dead stores |
| Country | Store location | Include/exclude by the client's ICP geography | — |
| Shipping Carriers | Logistics providers used | Target by shipping capability | Useful for logistics/3PL campaigns |
| Meta Description | Store's self-description | Read like a LinkedIn bio for positioning/products | Good signal for what the store actually sells |
| Monthly App Spend | Estimated monthly app spend | Use only if explicitly required | Not always reliable |
| Statuses | Live vs. inactive | Filter to live stores only | Always prioritize active stores |

### Pro Tips

- **ICP first:** define the client's ICP before touching filters — narrow by platform, estimated sales, and country first.
- **Segment by campaign type:** adjust filters differently for TAM lists vs. competitor lists.
- **Combine filters smartly:** e.g. Platform Rank + Apps & Technologies to find high performers using a specific tool.
- **Competitive targeting:** track platform migrations (a store switching platforms is a sales opportunity), target specific app/tech usage among competitors' customers, and use meta descriptions to confirm product/service fit.
- **Data validation:** not all apps are tracked as technologies and vice versa — build (or use the combined) list for both.
- **Integrations:** export domains to Clay, Apollo, or Sales Navigator to find contacts (see below).
- **Workflow automation:** use webhooks to auto-add new matching companies on a schedule (e.g., new Shopify stores ranked 1–10,000, weekly) and keep lists evergreen.

**Example scenarios:**
- **TAM list:** Shopify, Platform Rank 1–50,000, Category: Beauty & Fitness, Active status → a list of high-performing Shopify beauty brands.
- **Competitor list:** Magento, a specific competitor technology installed, Category: Home & Living → stores using that technology in that vertical.
- **High-ticket targeting:** Shopify, Product Price > $500, Estimated Sales $1M+ → high-value stores for a luxury-goods campaign.

### Verifying Store Leads Data Accuracy

Store Leads' platform-migration and upgrade data (e.g., a store upgrading to Shopify Plus, or migrating from another platform to Shopify) should be spot-checked before relying on it for a campaign — see [this walkthrough](https://www.tella.tv/video/store-leads-upgrades-migrates-to-shopify-co51) for the verification method GT uses.

### Building a Company List (Step by Step)

**One-time / one-off list:**
1. Build the list with Advanced Search criteria, pulling top apps/technologies if relevant to the client's onboarding form.
2. Duplicate GT's internal List Sizing Template and save the copy in the client's folder.
3. Use the client's onboarding form to decide which Store Leads filters to apply, and log every filter used in the template's Description column.
4. Click Execute Search, then save the result as a list (⭐).
5. Copy the saved list's name into the template and link it — so filters can be adjusted later without starting over.
6. Log the number of domains found.
7. Once the list is in Clay, log how the contact list itself was built (Clay, Apollo, or Sales Navigator — see next section).

**Evergreen (always-on) list:** set up the same search as a saved Workflow with a webhook (see "Automating Outreach with Webhooks" below) so new matching stores flow in automatically instead of rebuilding the list manually.

### Getting Contacts for the Companies You Found

1. **Export into Clay** — best for smaller, more targeted lists where deeper enrichment matters.
2. **Export into Apollo, verify with ExportApollo** — best for large lists (15,000+ prospects/month). ExportApollo is paid, so confirm with the client's CSM whether the cost is covered by GT or billed to the client.
3. **Export/upload into Sales Navigator** — use to extend the contact list further, then run the results through Clay's email waterfall to get verified emails.

Pick the method by list size: Clay for small/targeted, Apollo + ExportApollo for large-scale, Sales Navigator to supplement.

### Automating Outreach with Webhooks + Clay

Turn a saved Store Leads list into an evergreen Clay feed:
1. In Store Leads, open **List** → select the saved list.
2. Click **Create Workflow** → **+ Add Action to Workflow** → **Webhook action**.
3. In the client's Clay account, create a new Table → search "webhook" → select **Monitor Webhook** → New blank table.
4. Copy the webhook URL Clay generates.
5. Back in Store Leads, paste that URL into the workflow's Webhook URL field and Save.
6. Send a test webhook (⋯ menu → Send Test) and confirm it lands in the Clay table.
7. The webhook pulls new matches into Clay automatically every 24 hours, timestamped per row.

### Known Gaps

- The source knowledge base references a few training videos tied to a specific past client's workflow examples (a post-purchase-apps list and a full evergreen workflow walkthrough) — these are illustrative only; rebuild the list criteria and workflow for your actual client rather than reusing them verbatim.
- GT's internal List Sizing / Market Sizing Google Sheet templates are referenced by name but not linked here, since they require internal Google Workspace access and aren't usable outside GT — ask in #help-me for the current template link.
- The "verifying data accuracy" SOP is a single worked example (Shopify Plus upgrades/migrations), not a general accuracy-checking framework — treat it as one example of the verification habit, not exhaustive QA guidance.
- Store Leads login/access specifics (new-joiner process, internal Slack thread) are intentionally generalized here — ask in #help-me for current access instructions.

---

## TAM Scoping via DiscoLike

**When to use:** When Apollo, Clay, and LinkedIn aren't finding your targets.

**What it does:** Discovers lookalike websites based on keywords and tech tags — not limited to LinkedIn data.

**Pros:**
- Finds net-new companies outside typical B2B databases
- Search based on one or multiple sites (like Ocean.io)
- Filter by country or language

**Cons:**
- No built-in firmographic data (or very limited)
- Higher enrichment cost (~1 credit per row to qualify)

**Tips:**
- If too many results: tweak similarity variance and company start date
- Helps avoid missing high-potential lookalikes due to volume caps

---

## Contact Enrichment Best Practices

### Email Waterfalls
Use 3–5 providers sequentially — if provider 1 misses, try provider 2, etc.
- LeadMagic, Prospeo, Findymail for personal emails
- Catch-all/generic as fallback
- Always validate to remove bounces

### Phone Waterfalls
Same principle for direct dials and mobile numbers — multiple providers for coverage.

### Data Provider Performance
Review [Clay's data provider tests](https://www.clay.com/data-tests) for provider performance by specific regions and use cases.

### Deduplication Strategy
1. **Company level:** Dedupe by domain BEFORE finding people (saves credits)
2. **People level:** Dedupe by email after merging sources
   - Alternative: dedupe by full name (saves credits, small risk of false dedupes)
3. **Sequencer safety net:** Enable "Skip lead if in Workspace" in Instantly/Smartlead/etc.

---

## Common ICP Mistakes

- **Too broad:** "Any company with 10+ employees" — can't afford to target everyone
- **Too narrow:** "Only fintech in SF with exactly 150 employees" — TAM too small
- **Based on assumptions, not data:** Talk to customers, analyze CRM
- **Static ICP:** Markets change, revisit quarterly
- **Ignoring anti-ICP:** Knowing who NOT to target is equally important
- **No scoring system:** Without scoring, every lead looks the same

---

## Tools Quick Reference

### Data Sources
- Clay Find Companies (built-in)
- Apollo (apollo.io, free tier available)
- LinkedIn Sales Navigator ($99/mo, 30-day trial)
- ZoomInfo (enterprise, $15K–$30K/year)
- Crunchbase ($29–$99/mo)

### Export/Scraping
- Phantombuster (LinkedIn scraping)
- Evaboot (LinkedIn Sales Nav export)
- Instant Data Scraper (Chrome extension, free)
- Apify (web scraping)
- Claygent (built-in AI web research)

### Enrichment in Clay
- Clearbit — firmographics, technographics
- BuiltWith — tech stack data
- People Data Labs — company data
- Crunchbase — funding data
- Claygent — custom research (values, news)

### Data Quality
- Clay deduplication (built-in)
- Email validation providers (LeadMagic, Prospeo, Findymail)
- Clay formulas — custom scoring logic
- AI columns — evaluate fit based on criteria

---

