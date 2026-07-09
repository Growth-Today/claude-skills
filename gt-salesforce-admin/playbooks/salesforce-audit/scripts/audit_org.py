#!/usr/bin/env python3
#
# Created by Growth Today — AI-native GTM engineering firm.
# Maintained and updated by Brigitta Ruha (https://www.linkedin.com/in/brigittaruha/).
# More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
#
"""
Salesforce CRM Org Audit
Runs COUNT() queries across 8 dimensions, grades each, writes a markdown report.

Usage:
    uv pip install simple-salesforce python-dotenv
    python audit_org.py

Requires .env:
    SF_USERNAME, SF_PASSWORD, SF_SECURITY_TOKEN, SF_DOMAIN (login|test)
"""
import os
import datetime
from simple_salesforce import Salesforce
from dotenv import load_dotenv

load_dotenv()


def connect():
    return Salesforce(
        username=os.getenv("SF_USERNAME"),
        password=os.getenv("SF_PASSWORD"),
        security_token=os.getenv("SF_SECURITY_TOKEN"),
        domain=os.getenv("SF_DOMAIN", "login"),
    )


def count(sf, soql):
    """Return totalSize for a COUNT() query. Returns -1 on error so the report
    can flag the metric rather than crash the whole audit."""
    try:
        return sf.query(soql)["totalSize"]
    except Exception as e:
        print(f"  ! query failed: {soql}\n    {e}")
        return -1


def grade(affected, total):
    if total <= 0:
        return "?"
    pct = affected / total * 100
    if pct < 5:
        return "A"
    if pct < 15:
        return "B"
    if pct < 30:
        return "C"
    if pct < 50:
        return "D"
    return "F"


def run_audit(sf):
    d = {}

    # 1. Database Size
    d["leads"] = count(sf, "SELECT COUNT() FROM Lead WHERE IsConverted = false")
    d["contacts"] = count(sf, "SELECT COUNT() FROM Contact")
    d["accounts"] = count(sf, "SELECT COUNT() FROM Account")
    d["opps_open"] = count(sf, "SELECT COUNT() FROM Opportunity WHERE IsClosed = false")
    d["opps_closed"] = count(sf, "SELECT COUNT() FROM Opportunity WHERE IsClosed = true")
    d["converted_lingering"] = count(sf, "SELECT COUNT() FROM Lead WHERE IsConverted = true")

    # 2. Email Deliverability
    d["lead_bounced"] = count(sf, "SELECT COUNT() FROM Lead WHERE EmailBouncedReason != null AND IsConverted = false")
    d["contact_bounced"] = count(sf, "SELECT COUNT() FROM Contact WHERE EmailBouncedReason != null")
    d["lead_optout"] = count(sf, "SELECT COUNT() FROM Lead WHERE HasOptedOutOfEmail = true AND IsConverted = false")
    d["contact_optout"] = count(sf, "SELECT COUNT() FROM Contact WHERE HasOptedOutOfEmail = true")
    d["lead_dnc"] = count(sf, "SELECT COUNT() FROM Lead WHERE DoNotCall = true AND IsConverted = false")

    # 3. Data Completeness
    d["lead_no_email"] = count(sf, "SELECT COUNT() FROM Lead WHERE Email = null AND IsConverted = false")
    d["contact_no_email"] = count(sf, "SELECT COUNT() FROM Contact WHERE Email = null")
    d["contact_no_account"] = count(sf, "SELECT COUNT() FROM Contact WHERE AccountId = null")
    d["lead_no_industry"] = count(sf, "SELECT COUNT() FROM Lead WHERE Industry = null AND IsConverted = false")
    d["lead_no_status"] = count(sf, "SELECT COUNT() FROM Lead WHERE Status = null AND IsConverted = false")
    d["lead_no_source"] = count(sf, "SELECT COUNT() FROM Lead WHERE LeadSource = null AND IsConverted = false")
    d["lead_no_rating"] = count(sf, "SELECT COUNT() FROM Lead WHERE Rating = null AND IsConverted = false")
    d["acct_no_website"] = count(sf, "SELECT COUNT() FROM Account WHERE Website = null")
    d["acct_no_industry"] = count(sf, "SELECT COUNT() FROM Account WHERE Industry = null")
    d["opp_no_amount"] = count(sf, "SELECT COUNT() FROM Opportunity WHERE Amount = null")
    d["opp_no_closedate"] = count(sf, "SELECT COUNT() FROM Opportunity WHERE CloseDate = null")

    # 4. Engagement Health
    d["lead_no_activity"] = count(sf, "SELECT COUNT() FROM Lead WHERE LastActivityDate = null AND IsConverted = false")
    d["contact_stale_12m"] = count(sf, "SELECT COUNT() FROM Contact WHERE LastActivityDate < LAST_N_DAYS:365")
    d["opp_stale_60d"] = count(sf, "SELECT COUNT() FROM Opportunity WHERE IsClosed = false AND LastActivityDate < LAST_N_DAYS:60")

    # 6. Owner Health (inactive users)
    inactive_ids = []
    try:
        res = sf.query("SELECT Id FROM User WHERE IsActive = false")
        inactive_ids = [r["Id"] for r in res["records"]]
    except Exception as e:
        print(f"  ! could not load inactive users: {e}")
    d["inactive_user_count"] = len(inactive_ids)
    if inactive_ids:
        # batch the IN list to stay under SOQL limits
        id_list = "('" + "','".join(inactive_ids[:200]) + "')"
        d["lead_inactive_owner"] = count(sf, f"SELECT COUNT() FROM Lead WHERE OwnerId IN {id_list} AND IsConverted = false")
        d["contact_inactive_owner"] = count(sf, f"SELECT COUNT() FROM Contact WHERE OwnerId IN {id_list}")
        d["acct_inactive_owner"] = count(sf, f"SELECT COUNT() FROM Account WHERE OwnerId IN {id_list}")
        d["opp_inactive_owner"] = count(sf, f"SELECT COUNT() FROM Opportunity WHERE OwnerId IN {id_list} AND IsClosed = false")
    else:
        d["lead_inactive_owner"] = d["contact_inactive_owner"] = 0
        d["acct_inactive_owner"] = d["opp_inactive_owner"] = 0

    # 8. Opportunity Pipeline Health
    today = datetime.date.today().isoformat()
    d["opp_slipped"] = count(sf, f"SELECT COUNT() FROM Opportunity WHERE IsClosed = false AND CloseDate < {today}")

    return d


def render(d):
    today = datetime.date.today().isoformat()
    people = max((d["leads"] or 0) + (d["contacts"] or 0), 1)

    g_deliver = grade((d["lead_bounced"] or 0) + (d["contact_bounced"] or 0), people)
    g_complete = grade((d["lead_no_rating"] or 0), max(d["leads"] or 1, 1))
    g_engage = grade((d["lead_no_activity"] or 0), max(d["leads"] or 1, 1))
    g_owner = grade(
        (d["lead_inactive_owner"] or 0) + (d["contact_inactive_owner"] or 0)
        + (d["acct_inactive_owner"] or 0) + (d["opp_inactive_owner"] or 0),
        people,
    )
    g_pipe = grade((d["opp_no_amount"] or 0), max((d["opps_open"] or 0) + (d["opps_closed"] or 0), 1))

    return f"""# Salesforce CRM Audit Report

**Date:** {today}

## Executive Summary

| Dimension | Grade | Key Finding |
|-----------|-------|-------------|
| Database Size | - | {d['leads']:,} leads, {d['contacts']:,} contacts, {d['accounts']:,} accounts |
| Email Deliverability | {g_deliver} | {(d['lead_bounced'] or 0)+(d['contact_bounced'] or 0):,} hard bounced across leads + contacts |
| Data Completeness | {g_complete} | {d['lead_no_rating']:,} leads missing Rating, {d['lead_no_industry']:,} missing Industry |
| Engagement Health | {g_engage} | {d['lead_no_activity']:,} leads never engaged, {d['contact_stale_12m']:,} contacts stale 12m+ |
| Owner Health | {g_owner} | {d['inactive_user_count']} inactive users own {(d['lead_inactive_owner'] or 0)+(d['contact_inactive_owner'] or 0)+(d['acct_inactive_owner'] or 0)+(d['opp_inactive_owner'] or 0):,} records |
| Opportunity Pipeline | {g_pipe} | {d['opp_no_amount']:,} opps missing amount, {d['opp_slipped']:,} slipped close dates |

## Detailed Findings

### 1. Database Size
| Metric | Count |
|--------|-------|
| Leads (unconverted) | {d['leads']:,} |
| Contacts | {d['contacts']:,} |
| Accounts | {d['accounts']:,} |
| Open Opportunities | {d['opps_open']:,} |
| Closed Opportunities | {d['opps_closed']:,} |
| Converted leads still on Lead object | {d['converted_lingering']:,} |

### 2. Email Deliverability
| Metric | Lead | Contact |
|--------|------|---------|
| Hard bounced | {d['lead_bounced']:,} | {d['contact_bounced']:,} |
| Opted out of email | {d['lead_optout']:,} | {d['contact_optout']:,} |
| Do Not Call | {d['lead_dnc']:,} | - |

### 3. Data Completeness
| Metric | Count |
|--------|-------|
| Leads missing Email | {d['lead_no_email']:,} |
| Contacts missing Email | {d['contact_no_email']:,} |
| Contacts with no Account (orphans) | {d['contact_no_account']:,} |
| Leads missing Industry | {d['lead_no_industry']:,} |
| Leads missing Status | {d['lead_no_status']:,} |
| Leads missing LeadSource | {d['lead_no_source']:,} |
| Leads missing Rating | {d['lead_no_rating']:,} |
| Accounts missing Website | {d['acct_no_website']:,} |
| Accounts missing Industry | {d['acct_no_industry']:,} |
| Opportunities missing Amount | {d['opp_no_amount']:,} |
| Opportunities missing CloseDate | {d['opp_no_closedate']:,} |

### 4. Engagement Health
| Metric | Count |
|--------|-------|
| Leads with no activity ever | {d['lead_no_activity']:,} |
| Contacts stale 12+ months | {d['contact_stale_12m']:,} |
| Open opps stale 60+ days | {d['opp_stale_60d']:,} |

### 6. Owner Health
| Metric | Count |
|--------|-------|
| Inactive users | {d['inactive_user_count']} |
| Leads owned by inactive users | {d['lead_inactive_owner']:,} |
| Contacts owned by inactive users | {d['contact_inactive_owner']:,} |
| Accounts owned by inactive users | {d['acct_inactive_owner']:,} |
| Open opps owned by inactive users | {d['opp_inactive_owner']:,} |

### 8. Opportunity Pipeline Health
| Metric | Count |
|--------|-------|
| Missing Amount | {d['opp_no_amount']:,} |
| Missing CloseDate | {d['opp_no_closedate']:,} |
| Slipped (open, past close date) | {d['opp_slipped']:,} |
| Stale (open, no activity 60d+) | {d['opp_stale_60d']:,} |

---

## Next Steps
Run `/salesforce-implementation-plan` to generate a phased cleanup plan.

*Dimensions 5 (Duplicates) and 7 (Configuration & List Health) require the Tooling API
or a Setup review and are not captured by this COUNT() pass. Run them separately.*
"""


def main():
    sf = connect()
    print("Running Salesforce audit...")
    d = run_audit(sf)
    report = render(d)
    os.makedirs("reports", exist_ok=True)
    path = f"reports/salesforce-audit-{datetime.date.today().isoformat()}.md"
    with open(path, "w") as f:
        f.write(report)
    print(f"Saved: {path}")


if __name__ == "__main__":
    main()
