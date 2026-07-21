---
name: products-and-price-books
description: "Set up Products, Price Books, and Opportunity line items so deal amounts are built from what's actually being sold — enabling accurate pricing, reporting by product, and quoting. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: opportunities-sales
---

# Products & Price Books

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Move Opportunity Amount from a typed-in number to line items built from real Products at real prices. This unlocks pricing consistency, revenue reporting by product, and quoting.

## Prerequisites
- "Customize Application"; Products/Price Books enabled
- `sales-process-and-stages` done
- A clear product catalog + pricing model from the business

## Critical concept
- **Product** = what you sell (catalog). **Price Book** = a list of products with prices (Standard Price Book + custom ones for segments/regions/currencies). **Opportunity Product (line item)** links a product+price to a deal; the Opportunity **Amount rolls up from line items** once used.
- Multi-currency or segment pricing → multiple price books. Keep the catalog lean; archive dead products (don't delete if referenced).

## Automation level
Hybrid — API to load catalog/prices (Data Loader) + audit; setup in Setup.

## Steps
1. **Model the catalog:** products, families, and the pricing model (single vs multiple price books).
2. **Create Products** + the **Standard Price Book**; add segment/region/currency price books as needed.
3. **Load prices** (Data Loader — see `data-loader-and-imports`).
4. **Enable line items** on the sales process; train reps to add products (Amount then rolls up).
5. **Report by product** (needs a product-aware custom report type — `custom-report-types`).
6. **Govern:** archive obsolete products; keep price books current.

## Notes
- Once line items are used, Opportunity Amount is driven by them — don't also hand-edit Amount.
- Feeds forecasting and product-level reporting; pairs with `forecasting-setup`, `custom-report-types`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
