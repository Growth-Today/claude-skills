---
name: sales-navigator-guide
---

# LinkedIn Sales Navigator & ICP Framework Guide

## Sales Navigator Advanced Search

### Lead Filters

| Filter | Description | Plan Required |
|--------|-------------|---------------|
| Keywords | Searches across profile text | Core |
| First/Last Name | Direct name search | Core |
| Title (Boolean) | Current job title with boolean operators | Core |
| Company | Current employer | Core |
| Company Headcount | Employee range (1-10 to 10,001+) | Core |
| Seniority Level | CXO, VP, Director, Manager, etc. | Core |
| Function | Sales, Marketing, Engineering, etc. | Core |
| Geography | Region, country, city, metro area | Core |
| Industry | 413 industry options | Core |
| Years in Current Position | Less than 1, 1-2, 3-5, etc. | Core |
| Years at Current Company | Same ranges | Core |
| Changed Jobs | Past 90 days | Core |
| Posted on LinkedIn | Past 30 days | Core |
| Company Revenue | Revenue ranges | Advanced+ |
| Technologies Used | 35,000+ technologies | Advanced+ |
| Buyer Intent | LinkedIn intent signals | Advanced+ |
| Company Headcount Growth | Growth percentage ranges | Advanced+ |

### Account Filters

| Filter | Description |
|--------|-------------|
| Company Headcount | Employee range |
| Revenue | Annual revenue range |
| Industry | Industry vertical |
| HQ Location | Headquarters location |
| Technologies Used | Tech stack (35K+ options) |
| Headcount Growth | Company growth signals |
| Job Opportunities | Companies actively hiring |
| Recent Activities | Company posts, news |

## Boolean Search

### Operators

| Operator | Syntax | Example | What It Does |
|----------|--------|---------|-------------|
| **AND** | `AND` | `VP AND Marketing` | Both terms must match |
| **OR** | `OR` | `CEO OR "Chief Executive"` | Either term matches |
| **NOT** | `NOT` | `VP NOT assistant` | Excludes term |
| **Quotes** | `"exact phrase"` | `"Vice President"` | Exact phrase match |
| **Parentheses** | `(group)` | `(CEO OR CTO) AND SaaS` | Group operations |

**Limitations:**
- Boolean works in Title, Company, and Keywords fields
- Does NOT work in Industry, Geography, or dropdown filters
- No wildcard (`*`) support (unlike Recruiter)
- Max ~1,000 characters per boolean string
- Nested parentheses work 2-3 levels deep

### Boolean Formulas by ICP

#### SaaS Decision Makers
```
Title: (VP OR "Vice President" OR Director OR Head OR Chief) AND (Marketing OR "Demand Gen" OR "Growth" OR "Digital")
Company Keywords: (SaaS OR "B2B software" OR "cloud-based" OR "subscription")
Seniority: VP, Director, CXO
Industry: Computer Software, Internet, IT & Services
Headcount: 51-500
```

#### C-Suite Targeting
```
Title: (CEO OR "Chief Executive Officer" OR Founder OR "Co-Founder" OR "Managing Director" OR President OR Owner)
NOT: (assistant OR intern OR student OR "job seeking")
```

#### VP of Sales at Mid-Market Tech
```
Title: ("VP Sales" OR "Vice President Sales" OR "VP of Sales" OR "Head of Sales" OR CRO OR "SVP Sales")
Industry: Computer Software, Internet, SaaS
Headcount: 201-1000
```

#### HR / People Decision Makers
```
Title: (CHRO OR "Chief People Officer" OR "VP HR" OR "Head of People" OR "Head of HR" OR "Director of Talent")
NOT: (recruiter OR coordinator OR assistant OR intern OR generalist)
```

#### IT Decision Makers
```
Title: (CTO OR CIO OR CISO OR "VP Engineering" OR "VP IT" OR "Head of Engineering" OR "Director of IT")
NOT: (intern OR junior OR associate OR student)
```

#### Startup Founders (Seed to Series B)
```
Title: (Founder OR "Co-Founder" OR CEO OR "Chief Executive")
Company keywords: (seed OR "series A" OR "series B" OR startup OR "early stage")
Headcount: 1-200
Changed jobs in past 90 days: Yes
```

#### Multi-Role Targeting (Buying Committee)
```
Search 1 (Economic Buyer): CEO OR CFO OR "VP Finance"
Search 2 (Champion): "Head of Marketing" OR "Marketing Director" OR "VP Marketing"
Search 3 (User): "Marketing Manager" OR "Digital Marketing" OR "Demand Gen Manager"
Search 4 (Blocker): "General Counsel" OR "Head of Legal" OR "Compliance"
```

#### Exclude False Positives
```
Title: (Director OR VP OR Head) AND Marketing NOT ("Account Director" OR "Art Director" OR "Creative Director" OR assistant OR associate)
```

## ICP Framework

### Firmographic Criteria (Company-Level)

| Criterion | Description | Sales Nav Filter |
|-----------|-------------|-----------------|
| Industry | Primary vertical | Industry filter |
| Company size | Employee count | Headcount filter |
| Revenue | Annual revenue | Revenue (Advanced+) |
| Geography | HQ location | HQ location |
| Growth rate | Headcount growth % | Growth filter |
| Funding stage | Seed to IPO | Keywords + external |

### Technographic Criteria

| Criterion | Source |
|-----------|--------|
| Tech stack | Sales Nav Tech filter (35K+), BuiltWith, Wappalyzer |
| CRM | Sales Nav Tech filter |
| Marketing automation | Sales Nav Tech filter |
| Competitive tools | Sales Nav Tech filter + intent data |

### Behavioral/Intent Criteria

| Signal | Source |
|--------|--------|
| Job postings | Sales Nav "Job Opportunities" filter |
| Funding events | Crunchbase, Sales Nav alerts |
| Leadership changes | Sales Nav "Changed jobs" filter |
| Content engagement | Sales Nav Buyer Intent, Bombora |
| Web visits | 6sense, Clearbit Reveal, Leadfeeder |

### ICP Scoring (Tier System)

For the canonical ICP Fit Score definition, full scoring matrix (7 criteria, weights), and tier thresholds, see `resources/sub-skills/icp-definition.md`.

For the full three-layer scoring decision framework (ICP Fit Score → ABM Account Prioritization → Outreach Prioritization Matrix) and decision flow, see `resources/reference/scoring-decision-framework.md`.

## List Building Best Practices

### Bypassing the 2,500 Result Limit

Sales Navigator shows max 2,500 results per search. Bypass strategies:

1. **Geographic Segmentation** — Split by state/city
2. **Industry Segmentation** — Same title across different industries
3. **Company Size** — Break 51-500 into 51-200 and 201-500
4. **Seniority Stacking** — Separate searches per role level
5. **First Name Split** — Filter A-F, G-L, M-R, S-Z
6. **Time Filters** — "Changed jobs in 90 days", "Years in position"

### List Segmentation

1. By buying stage: Cold, Warm, Hot
2. By persona: One list per buyer persona
3. By intent level: High/Medium/Low
4. By timezone: For cadence timing
5. Keep lists under 1,000 for personalization
6. Naming: `[Tier]-[Persona]-[Vertical]-[Geo]-[Date]`

## Export & Scraping Tools

### Tool Comparison

| Tool | Type | Price | Risk Level | Best For |
|------|------|-------|-----------|----------|
| **Evaboot** | Chrome extension | $29-99/mo | Medium | Clean, verified data |
| **PhantomBuster** | Cloud automation | $69-439/mo | Higher | Multi-step workflows |
| **Captain Data** | Cloud extraction | $399/mo | Medium-High | Agencies, repeatable flows |
| **Clay** | Enrichment platform | $149-800/mo | Low | Waterfall enrichment |
| **Apollo.io** | Sales intelligence | Free-$119/mo | Low | Own database, not scraping |
| **Linked Helper** | Desktop app | $15-45/mo | Medium | Budget automation |

### Recommended Workflow

```
1. BUILD LIST in Sales Navigator
   - Advanced filters + boolean
   - Segment to stay under 2,500 per search
   - Save to organized lists

2. EXPORT with Evaboot (or CRM sync)
   - Extract: Name, Title, Company, LinkedIn URL, Location
   - Auto-clean titles, filter false positives

3. ENRICH with Clay or Apollo
   - Waterfall email finding (multiple providers)
   - Phone number enrichment
   - Company data (revenue, tech stack)

4. VERIFY with ZeroBounce or NeverBounce
   - Run all emails through verification
   - Remove invalid, flag catch-all
   - Target: 95%+ valid rate

5. SEGMENT for outreach
   - Tier A/B/C based on ICP score
   - Personalization variables from enrichment
   - Route to appropriate cadence

6. MAINTAIN
   - Re-verify before each campaign
   - Quarterly full refresh
   - Monitor bounce rates in real-time
```

## ABM List Building

For the full ABM framework including target account list sizing, contact mapping per account, intent data layering, and lookalike building, see the following sub-skills:

- **Account selection, ABM tiers, stage progression** → `resources/sub-skills/account-selection.md`
- **Buying committee mapping, persona targeting** → `resources/sub-skills/persona-mapping.md`
- **Account scoring, qualify and prioritize** → `resources/sub-skills/account-qualification.md`
- **Full scoring decision framework** → `resources/reference/scoring-decision-framework.md`
