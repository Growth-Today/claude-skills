# Scoring

## How to score

Score 1 point per pass benchmark hit across the 10 dimensions. Maximum 10. Minimum 0.

A dimension scores 1 point only when it hits the ✅ Strong benchmark. 🟡 Acceptable does not earn the point. ❌ Fail does not earn the point. This keeps the score honest. A 7 means seven dimensions are genuinely strong, not "mostly okay."

For dimensions with multiple ✅ Strong conditions (7, 8, 9, 10), all required conditions must be met to earn the point. Any single ❌ Fail condition zeroes the dimension.

| Dimension | Earns the point when |
|---|---|
| 1. Coverage | 70%+ match rate on a tight ICP slice |
| 2. Email Accuracy | 90%+ valid rate on a well-defined ICP list |
| 3. Phone and Mobile | 60%+ mobile direct dial coverage on a US list |
| 4. Freshness | 90%+ of CRM contacts refreshed in the last 90 days |
| 5. Cost Per Usable Contact | Under $0.30 per usable contact on a high-volume waterfall |
| 6. Enrichment Method | Multi-source waterfall plus AI routing |
| 7. CRM Hygiene | Under 2% company duplicates AND standardized titles AND normalized geo |
| 8. Governance | One named owner AND monthly cadence AND written rules |
| 9. Compliance | 100% suppression propagation AND under 0.1% spam AND documented legal basis AND single opt-out source of truth |
| 10. Measurement | All 3 numbers tracked weekly or monthly AND visible to RevOps, GTM Eng, Sales leadership |

## Interpretation bands

| Score | Band | What it means | Priority next step |
|---|---|---|---|
| 0 to 3 | Bottleneck | The data layer is the bottleneck. Every AI agent and workflow built on top of it is degraded | Pick one dimension. Fix it this quarter. Do not try to fix all 10 at once |
| 4 to 6 | Partial | Some hygiene but no systematic governance. Decay catches you within 6 months | Audit your provider stack. You are probably paying for overlap |
| 7 to 9 | Strong | Strong foundation. Focus on 1 or 2 missing dimensions | Layer AI routing and predictive quality scoring on top |
| 10 | Top 5% | Top 5% data layer. AI agents built on top will actually perform | Maintain monthly audit cadence. Share your playbook with your team |

## What to do at each score level

### 0 to 3. Bottleneck
The data layer cannot support reliable outbound or any AI agent. The fastest path out is to stop spreading effort.

- Pick the single dimension with the largest downstream blast radius. For most teams that is Dimension 2 (Email Accuracy) or Dimension 1 (Coverage)
- Fix that one dimension to ✅ Strong before touching anything else
- Do not buy new tools yet. Most 0 to 3 scores come from process gaps, not tool gaps
- Re-score after 30 days

GT-internal recommendation: Velocity rebuild (data foundation engagement).

### 4 to 6. Partial
The team has cleaned up before but it did not hold. The missing piece is usually governance (Dimension 8) and provider overlap (Dimension 5).

- Run the provider rationalization first. Map which provider wins which field. Drop overlap
- Name a single data owner and put a monthly 30-minute audit on the calendar
- Then attack the next-lowest dimension
- Re-score after 60 days

GT-internal recommendation: GTM Engineering audit plus provider rationalization.

### 7 to 9. Strong
The foundation holds. The remaining gaps are optimization, not survival.

- Identify the 1 or 2 dimensions still at 🟡 or ❌
- For most strong teams the gap is Dimension 6 (move from static waterfall to AI routing) or Dimension 10 (measurement thresholds not yet defined)
- Add predictive quality scoring so low-confidence records get flagged before they enter a sequence
- Re-score quarterly

GT-internal recommendation: AI routing layer plus signal-based plays.

### 10. Top 5%
Nothing to rebuild. The risk now is drift.

- Keep the monthly audit cadence. A 10 decays to a 7 within two quarters if measurement stops
- Document the playbook so the score survives a personnel change
- This is the point where signal-based plays and AI agents pay off, because they run on data that holds

GT-internal recommendation: no rebuild needed. Recommend Plays implementation.

## Notes

- Present the score as "X out of 10" with the band name, then the single highest-priority fix. Do not bury the recommendation under all 10 dimension write-ups
- In client-facing mode, end with the soft CTA. In GT-internal mode, end with the engagement recommendation above
- A score is a snapshot. Always note the date scored, because the data layer decays 22% to 30% per year (Dun & Bradstreet)


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
