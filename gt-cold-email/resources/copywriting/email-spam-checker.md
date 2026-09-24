---
name: email-spam-checker
version: 1.0
updated: 2026-04-07
source: mailmeteor.com/blog/spam-words (January 2026), activecampaign.com/blog/spam-words
review: Quarterly - spam filter rules evolve. Update at least every 3 months.
description: Cold email spam word checker. Scans subject line and body for words that trigger spam filters and hurt deliverability. Run automatically after every cold email is drafted.
---

# Email Spam Checker

Scan the subject line and body of every cold email against this list before returning it to the user. If a spam word is found, rewrite the sentence without it. Do not ask the user to do this manually.

At the end of your response, add one line:
> Spam check: [X issues found and fixed / no issues found]

---

## Spam Trigger Words - B2B Cold Email

These words are flagged by Gmail, Outlook, and other providers as suspicious. A single word rarely kills deliverability on its own - combinations and context matter. When in doubt, rewrite.

### Financial / Offer
free, free trial, free access, free gift, free quote, for free, no cost, no credit check, no obligation, risk-free, money-back guarantee, discount, save $, save big, earn, earn $, make money, increase revenue, increase sales, profit, double your, giveaway, bonus, deal, offer, bargain, affordable, cheap, quote, ROI, investment, credit card, billing

### Urgency / Pressure
act now, act fast, urgent, limited time, offer expires, don't miss, before it's too late, final call, last chance, hurry, immediately, only today, time limited, while supplies last, do it now, don't wait, don't delete, expires today, final notice

### Scam / Overpromise
guaranteed, 100% guaranteed, guaranteed results, satisfaction guaranteed, no strings attached, no catch, amazing, incredible, unbelievable, you won't believe, pure profit, best price, lowest price, special offer, special invitation, exclusive deal, exclusive access, once in a lifetime

### Clickbait / Action (especially in subject lines)
click here, click now, click below, apply now, buy now, order now, get it now, sign up free, download now, call now, access now, get started now

### Formatting flags (not words - check for these)
- ALL CAPS anywhere in subject line or body
- Multiple exclamation marks (!!)
- Multiple question marks (??)
- Dollar signs used decoratively ($$$)
- More than 2 links in a single email
- Link shorteners (bit.ly, tinyurl) - use full URLs only
