#!/usr/bin/env python3
"""HubSpot portal audit — read-only metric collection.

Reads HUBSPOT_ACCESS_TOKEN from .env, queries the HubSpot REST API across the
eight audit dimensions, and writes raw results to reports/audit-raw.json.

Stdlib only. Every call is a read (GET, or POST to /search which is read-only).
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

BASE = "https://api.hubapi.com"
DAY_MS = 86_400_000

# ---------------------------------------------------------------- token / http

def load_token():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    for line in open(env_path):
        line = line.strip()
        for key in ("HUBSPOT_ACCESS_TOKEN", "HUBSPOT_API_TOKEN"):
            if line.startswith(key + "="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("No HUBSPOT_ACCESS_TOKEN / HUBSPOT_API_TOKEN found in .env")


TOKEN = load_token()
CALLS = 0


def call(method, path, body=None, retries=4):
    """One API call. Returns (ok, payload). Never raises."""
    global CALLS
    url = path if path.startswith("http") else BASE + path
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Authorization": f"Bearer {TOKEN}"}
    if data:
        headers["Content-Type"] = "application/json"

    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            CALLS += 1
            with urllib.request.urlopen(req, timeout=60) as f:
                time.sleep(0.12)  # 100 req / 10s private-app limit
                return True, json.load(f)
        except urllib.error.HTTPError as e:
            raw = e.read().decode()[:500]
            if e.code == 429:
                time.sleep(2 ** attempt)
                continue
            if e.code in (502, 503, 504):
                time.sleep(1 + attempt)
                continue
            return False, {"http_status": e.code, "error": raw}
        except Exception as e:  # noqa: BLE001 - network flakiness
            if attempt == retries - 1:
                return False, {"error": repr(e)}
            time.sleep(1 + attempt)
    return False, {"error": "retries exhausted"}


def count(obj, filters=None):
    """Total records matching filters, via the Search API `total` field."""
    body = {"limit": 1, "properties": ["hs_object_id"]}
    if filters:
        body["filterGroups"] = [{"filters": filters}]
    ok, res = call("POST", f"/crm/v3/objects/{obj}/search", body)
    if not ok:
        return {"error": res}
    return res.get("total", 0)


def page_all(obj, properties, limit=100, max_records=200_000):
    """Paginate every record of an object type. Returns list of property dicts."""
    out, after = [], None
    while True:
        body = {"limit": limit, "properties": properties}
        if after:
            body["after"] = after
        ok, res = call("POST", f"/crm/v3/objects/{obj}/search", body)
        if not ok:
            return out, res
        out.extend(r.get("properties", {}) for r in res.get("results", []))
        after = res.get("paging", {}).get("next", {}).get("after")
        # Search API hard-caps pagination at 10k records
        if not after or len(out) >= max_records or len(out) >= 9_900:
            return out, None


if __name__ != "__main__":
    raise ImportError(
        "audit_portal runs its audit at import time — do not import it, run it as a script"
    )

NOW = datetime.now(timezone.utc)
NOW_MS = int(NOW.timestamp() * 1000)


def ago(days):
    return str(NOW_MS - days * DAY_MS)


R = {"meta": {"run_at": NOW.isoformat(), "portal": None}}


def rec(dim, key, value):
    R.setdefault(dim, {})[key] = value
    shown = value if not isinstance(value, dict) else f"ERR {str(value)[:90]}"
    print(f"  {key:<44} {shown}", flush=True)


# ---------------------------------------------------------------------- audit

print("== account ==", flush=True)
ok, acct = call("GET", "/account-info/v3/details")
R["meta"]["portal"] = acct if ok else {"error": acct}
print(f"  portal {acct.get('portalId') if ok else acct}", flush=True)

print("== 1. database size ==", flush=True)
rec("size", "contacts_total", count("contacts"))
rec("size", "companies_total", count("companies"))
rec("size", "deals_total", count("deals"))
rec("size", "marketing_contacts", count("contacts", [
    {"propertyName": "hs_marketable_status", "operator": "EQ", "value": "true"}]))
rec("size", "non_marketing_contacts", count("contacts", [
    {"propertyName": "hs_marketable_status", "operator": "EQ", "value": "false"}]))

print("== 2. deliverability ==", flush=True)
rec("deliver", "hard_bounced", count("contacts", [
    {"propertyName": "hs_email_hard_bounce_reason_enum", "operator": "HAS_PROPERTY"}]))
rec("deliver", "soft_bounced_no_hard", count("contacts", [
    {"propertyName": "hs_email_bounce", "operator": "GT", "value": "0"},
    {"propertyName": "hs_email_hard_bounce_reason_enum", "operator": "NOT_HAS_PROPERTY"}]))
rec("deliver", "global_unsubscribes", count("contacts", [
    {"propertyName": "hs_email_optout", "operator": "EQ", "value": "true"}]))
rec("deliver", "never_emailed", count("contacts", [
    {"propertyName": "hs_email_last_send_date", "operator": "NOT_HAS_PROPERTY"}]))
rec("deliver", "bounces_3_plus", count("contacts", [
    {"propertyName": "hs_email_bounce", "operator": "GTE", "value": "3"}]))
rec("deliver", "ever_emailed", count("contacts", [
    {"propertyName": "hs_email_last_send_date", "operator": "HAS_PROPERTY"}]))

print("== 3. completeness (contacts) ==", flush=True)
for prop in ["email", "company", "industry", "country", "state", "city",
             "lifecyclestage", "hubspot_owner_id", "jobtitle", "phone", "firstname", "lastname"]:
    rec("complete_contacts", f"missing_{prop}", count("contacts", [
        {"propertyName": prop, "operator": "NOT_HAS_PROPERTY"}]))

print("== 3b. completeness (companies) ==", flush=True)
for prop in ["domain", "industry", "city", "state", "country", "numberofemployees",
             "lifecyclestage", "hubspot_owner_id"]:
    rec("complete_companies", f"missing_{prop}", count("companies", [
        {"propertyName": prop, "operator": "NOT_HAS_PROPERTY"}]))

print("== 4. engagement ==", flush=True)
buckets = [("active_0_30d", 0, 30), ("active_31_90d", 30, 90), ("active_91_180d", 90, 180),
           ("active_181_365d", 180, 365)]
for name, lo, hi in buckets:
    rec("engage", name, count("contacts", [
        {"propertyName": "hs_last_activity_date", "operator": "LT", "value": ago(lo)},
        {"propertyName": "hs_last_activity_date", "operator": "GTE", "value": ago(hi)}]))
rec("engage", "active_365d_plus", count("contacts", [
    {"propertyName": "hs_last_activity_date", "operator": "LT", "value": ago(365)}]))
rec("engage", "never_any_activity", count("contacts", [
    {"propertyName": "hs_last_activity_date", "operator": "NOT_HAS_PROPERTY"}]))
rec("engage", "never_opened_email", count("contacts", [
    {"propertyName": "hs_email_last_open_date", "operator": "NOT_HAS_PROPERTY"}]))
rec("engage", "never_clicked_email", count("contacts", [
    {"propertyName": "hs_email_last_click_date", "operator": "NOT_HAS_PROPERTY"}]))
rec("engage", "opened_last_90d", count("contacts", [
    {"propertyName": "hs_email_last_open_date", "operator": "GTE", "value": ago(90)}]))
rec("engage", "clicked_last_90d", count("contacts", [
    {"propertyName": "hs_email_last_click_date", "operator": "GTE", "value": ago(90)}]))
rec("engage", "emailed_last_90d", count("contacts", [
    {"propertyName": "hs_email_last_send_date", "operator": "GTE", "value": ago(90)}]))
rec("engage", "zero_page_views", count("contacts", [
    {"propertyName": "hs_analytics_num_page_views", "operator": "EQ", "value": "0"}]))
rec("engage", "no_page_view_data", count("contacts", [
    {"propertyName": "hs_analytics_num_page_views", "operator": "NOT_HAS_PROPERTY"}]))
rec("engage", "zero_form_submissions", count("contacts", [
    {"propertyName": "num_conversion_events", "operator": "EQ", "value": "0"}]))
rec("engage", "ghost_emailed_never_opened", count("contacts", [
    {"propertyName": "hs_email_last_send_date", "operator": "HAS_PROPERTY"},
    {"propertyName": "hs_email_last_open_date", "operator": "NOT_HAS_PROPERTY"}]))

print("== 6. owner health ==", flush=True)
ok, active_owners = call("GET", "/crm/v3/owners?limit=500")
ok2, arch_owners = call("GET", "/crm/v3/owners?limit=500&archived=true")
R["owners"] = {
    "active": active_owners.get("results", []) if ok else {"error": active_owners},
    "archived": arch_owners.get("results", []) if ok2 else {"error": arch_owners},
}
print(f"  active={len(R['owners']['active']) if ok else 'ERR'} "
      f"archived={len(R['owners']['archived']) if ok2 else 'ERR'}", flush=True)

rec("owner_health", "contacts_no_owner", count("contacts", [
    {"propertyName": "hubspot_owner_id", "operator": "NOT_HAS_PROPERTY"}]))
rec("owner_health", "companies_no_owner", count("companies", [
    {"propertyName": "hubspot_owner_id", "operator": "NOT_HAS_PROPERTY"}]))
rec("owner_health", "deals_no_owner", count("deals", [
    {"propertyName": "hubspot_owner_id", "operator": "NOT_HAS_PROPERTY"}]))

deactivated = []
if ok2:
    for o in arch_owners.get("results", []):
        oid = str(o.get("id"))
        row = {
            "id": oid,
            "email": o.get("email"),
            "name": f"{o.get('firstName') or ''} {o.get('lastName') or ''}".strip(),
            "contacts": count("contacts", [{"propertyName": "hubspot_owner_id", "operator": "EQ", "value": oid}]),
            "companies": count("companies", [{"propertyName": "hubspot_owner_id", "operator": "EQ", "value": oid}]),
            "deals": count("deals", [{"propertyName": "hubspot_owner_id", "operator": "EQ", "value": oid}]),
        }
        deactivated.append(row)
        print(f"  deactivated {row['email']:<38} c={row['contacts']} co={row['companies']} d={row['deals']}", flush=True)
R["owner_health"]["deactivated_detail"] = deactivated

print("== 7. lists / workflows / forms ==", flush=True)
ok, lists = call("POST", "/crm/v3/lists/search", {"count": 500, "offset": 0})
R["lists"] = lists.get("lists", []) if ok else {"error": lists}
print(f"  lists: {len(R['lists']) if ok else R['lists']}", flush=True)

ok, wf = call("GET", "/automation/v3/workflows")
R["workflows"] = wf.get("workflows", []) if ok else {"error": wf}
print(f"  workflows: {len(R['workflows']) if ok else R['workflows']}", flush=True)

ok, forms = call("GET", "/marketing/v3/forms?limit=100")
R["forms"] = forms.get("results", []) if ok else {"error": forms}
print(f"  forms: {len(R['forms']) if ok else R['forms']}", flush=True)

print("== 8. deal pipeline ==", flush=True)
rec("deals", "missing_amount", count("deals", [
    {"propertyName": "amount", "operator": "NOT_HAS_PROPERTY"}]))
rec("deals", "missing_closedate", count("deals", [
    {"propertyName": "closedate", "operator": "NOT_HAS_PROPERTY"}]))
rec("deals", "open_stale_60d", count("deals", [
    {"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"},
    {"propertyName": "hs_last_activity_date", "operator": "LT", "value": ago(60)}]))
rec("deals", "open_no_activity_ever", count("deals", [
    {"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"},
    {"propertyName": "hs_last_activity_date", "operator": "NOT_HAS_PROPERTY"}]))
ok, pipes = call("GET", "/crm/v3/pipelines/deals")
R["pipelines"] = pipes.get("results", []) if ok else {"error": pipes}

print("== 5. duplicates + property inventory ==", flush=True)
comp_props, err = page_all("companies", ["name", "domain", "createdate"])
R["companies_sample"] = {"fetched": len(comp_props), "error": err}
print(f"  companies fetched for dup analysis: {len(comp_props)}", flush=True)

from collections import Counter
dom = Counter(c["domain"].strip().lower() for c in comp_props if c.get("domain"))
nam = Counter(c["name"].strip().lower() for c in comp_props if c.get("name"))
R["duplicates"] = {
    "companies_scanned": len(comp_props),
    "dup_domain_groups": sum(1 for v in dom.values() if v > 1),
    "dup_domain_records": sum(v for v in dom.values() if v > 1),
    "dup_name_groups": sum(1 for v in nam.values() if v > 1),
    "dup_name_records": sum(v for v in nam.values() if v > 1),
    "top_dup_domains": [{"domain": k, "count": v} for k, v in dom.most_common(25) if v > 1],
    "top_dup_names": [{"name": k, "count": v} for k, v in nam.most_common(25) if v > 1],
}
for k in ("dup_domain_groups", "dup_domain_records", "dup_name_groups", "dup_name_records"):
    print(f"  {k:<44} {R['duplicates'][k]}", flush=True)

for obj in ("contacts", "companies", "deals"):
    ok, props = call("GET", f"/crm/v3/properties/{obj}")
    items = props.get("results", []) if ok else []
    R.setdefault("properties", {})[obj] = {
        "total": len(items),
        "custom": sum(1 for p in items if not p.get("hubspotDefined")),
        "custom_names": [p["name"] for p in items if not p.get("hubspotDefined")],
    } if ok else {"error": props}
    print(f"  properties {obj}: {R['properties'][obj].get('total')} "
          f"(custom {R['properties'][obj].get('custom')})", flush=True)

os.makedirs("reports", exist_ok=True)
with open("reports/audit-raw.json", "w") as f:
    json.dump(R, f, indent=2, default=str)
print(f"\nDone. {CALLS} API calls. -> reports/audit-raw.json", flush=True)
