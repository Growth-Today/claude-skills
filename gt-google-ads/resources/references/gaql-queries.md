# GAQL Query Templates (B2B Google Ads)

Google Ads Query Language templates for read-only analysis via the API/MCP. All monetary values are in **micros** — divide by 1,000,000 for currency. Judge everything to **pipeline/SQL**, not clicks. Pull, then route findings to the relevant sub-skill.

---

## Campaign performance (last 30 days)
```sql
SELECT campaign.name, metrics.cost_micros, metrics.impressions, metrics.clicks,
       metrics.conversions, metrics.conversions_value, metrics.ctr, metrics.average_cpc
FROM campaign
WHERE segments.date DURING LAST_30_DAYS AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
```

## Wasted spend — search terms with spend, zero conversions
```sql
SELECT search_term_view.search_term, campaign.name, metrics.cost_micros, metrics.clicks, metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS AND metrics.conversions = 0 AND metrics.cost_micros > 50000000
ORDER BY metrics.cost_micros DESC
```
(`> 50000000` micros = >$50 spend. These are negative-keyword candidates — route to `negative-keywords`.)

## Keyword performance + Quality Score
```sql
SELECT ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type,
       ad_group_criterion.quality_info.quality_score, metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS AND metrics.cost_micros > 0
ORDER BY metrics.cost_micros DESC
```

## Conversions by campaign incl. value (pipeline read)
```sql
SELECT campaign.name, metrics.conversions, metrics.conversions_value, metrics.cost_micros
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.conversions_value DESC
```
(With offline conversions imported, `conversions_value` = pipeline value — the number that matters. See `crm-attribution.md`.)

## Auction Insights proxy — impression share & lost IS
```sql
SELECT campaign.name, metrics.search_impression_share,
       metrics.search_budget_lost_impression_share, metrics.search_rank_lost_impression_share
FROM campaign
WHERE segments.date DURING LAST_30_DAYS AND campaign.advertising_channel_type = 'SEARCH'
```
(Lost-to-budget vs lost-to-rank tells you whether to add budget or improve QS/bids.)

## Device & geo breakdowns
```sql
SELECT segments.device, metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM campaign WHERE segments.date DURING LAST_30_DAYS
```
```sql
SELECT geographic_view.country_criterion_id, metrics.cost_micros, metrics.conversions
FROM geographic_view WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC
```

**Discipline:** read to CRM outcome (SQL/pipeline), not raw conversions; a "conversion" that's a form-fill isn't a deal. Confirm the account maturity/date window before drawing conclusions.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
