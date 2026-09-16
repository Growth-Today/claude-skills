#!/usr/bin/env python3
"""Stage 2 of the audit: fills gaps left by audit_portal.py.

- engagement recency using properties that actually exist in this portal
- deal staleness
- list / workflow detail
- full-population duplicate analysis (bypasses the Search API 10k cap)

Merges into reports/audit-raw.json. Read-only. Stdlib only.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone

BASE = "https://api.hubapi.com"
DAY_MS = 86_400_000
STAGE = sys.argv[1] if len(sys.argv) > 1 else "a"


def load_token():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for line in open(os.path.join(root, ".env")):
        line = line.strip()
        for key in ("HUBSPOT_ACCESS_TOKEN", "HUBSPOT_API_TOKEN"):
            if line.startswith(key + "="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("no token")


TOKEN = load_token()
CALLS = 0


def call(method, path, body=None, retries=4):
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
                time.sleep(0.11)
                return True, json.load(f)
        except urllib.error.HTTPError as e:
            raw = e.read().decode()[:400]
            if e.code == 429:
                time.sleep(2 ** attempt)
                continue
            if e.code in (502, 503, 504):
                time.sleep(1 + attempt)
                continue
            return False, {"http_status": e.code, "error": raw}
        except Exception as e:  # noqa: BLE001
            if attempt == retries - 1:
                return False, {"error": repr(e)}
            time.sleep(1 + attempt)
    return False, {"error": "retries exhausted"}


def count(obj, filters=None):
    body = {"limit": 1, "properties": ["hs_object_id"]}
    if filters:
        body["filterGroups"] = [{"filters": filters}]
    ok, res = call("POST", f"/crm/v3/objects/{obj}/search", body)
    return res.get("total", 0) if ok else {"error": res}


NOW_MS = int(datetime.now(timezone.utc).timestamp() * 1000)


def ago(d):
    return str(NOW_MS - d * DAY_MS)


RAW = "reports/audit-raw.json"
R = json.load(open(RAW))


def rec(dim, key, value):
    R.setdefault(dim, {})[key] = value
    print(f"  {key:<42} {value if not isinstance(value, dict) else 'ERR ' + str(value)[:80]}", flush=True)


def save():
    with open(RAW, "w") as f:
        json.dump(R, f, indent=2, default=str)


# ------------------------------------------------------------------- stage A
if STAGE == "a":
    print("== engagement recency (corrected properties) ==", flush=True)
    # hs_last_activity_date is absent in this portal; these two exist.
    for prop in ("notes_last_contacted", "lastmodifieddate"):
        for name, lo, hi in [("0_30d", 0, 30), ("31_90d", 30, 90),
                             ("91_180d", 90, 180), ("181_365d", 180, 365)]:
            rec("engage", f"{prop}__{name}", count("contacts", [
                {"propertyName": prop, "operator": "LT", "value": ago(lo)},
                {"propertyName": prop, "operator": "GTE", "value": ago(hi)}]))
        rec("engage", f"{prop}__365d_plus", count("contacts", [
            {"propertyName": prop, "operator": "LT", "value": ago(365)}]))
        rec("engage", f"{prop}__never", count("contacts", [
            {"propertyName": prop, "operator": "NOT_HAS_PROPERTY"}]))

    print("== deal staleness (corrected) ==", flush=True)
    rec("deals", "open_total", count("deals", [
        {"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"}]))
    rec("deals", "closed_total", count("deals", [
        {"propertyName": "hs_is_closed", "operator": "EQ", "value": "true"}]))
    rec("deals", "open_stale_60d", count("deals", [
        {"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"},
        {"propertyName": "notes_last_contacted", "operator": "LT", "value": ago(60)}]))
    rec("deals", "open_never_contacted", count("deals", [
        {"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"},
        {"propertyName": "notes_last_contacted", "operator": "NOT_HAS_PROPERTY"}]))
    rec("deals", "amount_zero", count("deals", [
        {"propertyName": "amount", "operator": "EQ", "value": "0"}]))

    print("== deals by stage ==", flush=True)
    stages = {}
    for pipe in R.get("pipelines", []):
        for st in pipe.get("stages", []):
            n = count("deals", [{"propertyName": "dealstage", "operator": "EQ", "value": st["id"]}])
            stages[f"{pipe['label']} / {st['label']}"] = n
            print(f"  {pipe['label']} / {st['label']:<32} {n}", flush=True)
    R["deal_stages"] = stages

    print("== list detail ==", flush=True)
    ldet = []
    for l in R.get("lists", []):
        lid = l.get("listId")
        ok, d = call("GET", f"/crm/v3/lists/{lid}?includeFilters=false")
        size = None
        if ok:
            size = d.get("list", {}).get("additionalProperties", {}).get("hs_list_size")
        ldet.append({"id": lid, "name": l.get("name"), "type": l.get("processingType"),
                     "objectType": l.get("objectTypeId"), "size": size,
                     "createdAt": l.get("createdAt"), "updatedAt": l.get("updatedAt")})
        print(f"  {str(l.get('name'))[:46]:<48} {l.get('processingType'):<10} size={size}", flush=True)
    R["list_detail"] = ldet

    print("== workflow detail ==", flush=True)
    for w in R.get("workflows", []):
        print(f"  {w.get('name')} enabled={w.get('enabled')} "
              f"enrolled={w.get('contactListIds')} type={w.get('type')}", flush=True)

    print("== marketing email presence ==", flush=True)
    ok, em = call("GET", "/marketing/v3/emails?limit=50")
    R["marketing_emails"] = {"count": len(em.get("results", [])), "sample":
                             [{"name": e.get("name"), "state": e.get("state"),
                               "publishDate": e.get("publishDate")} for e in em.get("results", [])[:15]]} \
        if ok else {"error": em}
    print(f"  marketing emails: {R['marketing_emails']}", flush=True)

    save()
    print(f"\nStage A done. {CALLS} calls.", flush=True)


# ------------------------------------------------------------------- stage B
if STAGE == "b":
    def page_list_api(obj, props, cap=200_000):
        """GET /crm/v3/objects/{obj} — paginates the full population, no 10k cap."""
        out, after, pages = [], None, 0
        while True:
            q = f"/crm/v3/objects/{obj}?limit=100&properties={','.join(props)}"
            if after:
                q += f"&after={after}"
            ok, res = call("GET", q)
            if not ok:
                print(f"  ! {res}", flush=True)
                return out
            out.extend(r.get("properties", {}) for r in res.get("results", []))
            pages += 1
            if pages % 50 == 0:
                print(f"  ...{len(out)} {obj}", flush=True)
            after = res.get("paging", {}).get("next", {}).get("after")
            if not after or len(out) >= cap:
                return out

    print("== full company scan ==", flush=True)
    comps = page_list_api("companies", ["name", "domain"])
    dom = Counter(c["domain"].strip().lower() for c in comps if c.get("domain"))
    nam = Counter(c["name"].strip().lower() for c in comps if c.get("name"))
    R["duplicates"] = {
        "companies_scanned": len(comps),
        "dup_domain_groups": sum(1 for v in dom.values() if v > 1),
        "dup_domain_excess": sum(v - 1 for v in dom.values() if v > 1),
        "dup_name_groups": sum(1 for v in nam.values() if v > 1),
        "dup_name_excess": sum(v - 1 for v in nam.values() if v > 1),
        "top_dup_domains": [{"domain": k, "count": v} for k, v in dom.most_common(30) if v > 1],
        "top_dup_names": [{"name": k, "count": v} for k, v in nam.most_common(30) if v > 1],
    }
    for k, v in R["duplicates"].items():
        if isinstance(v, int):
            print(f"  {k:<28} {v}", flush=True)
    save()

    print("== full contact scan ==", flush=True)
    cons = page_list_api("contacts", ["email", "firstname", "lastname"])
    import re
    rx = re.compile(r"^[^@\s]+@[^@\s.]+\.[a-zA-Z]{2,}$")
    emails = [c["email"].strip().lower() for c in cons if c.get("email")]
    ec = Counter(emails)
    bad = [e for e in emails if not rx.match(e)]
    role = [e for e in emails if e.split("@")[0] in {
        "info", "sales", "support", "admin", "contact", "hello", "office",
        "marketing", "help", "team", "noreply", "no-reply", "enquiries", "hr"}]
    free = Counter(e.split("@")[1] for e in emails
                   if e.split("@")[1] in {"gmail.com", "yahoo.com", "hotmail.com",
                                          "outlook.com", "aol.com", "icloud.com", "me.com"})
    R["contact_quality"] = {
        "contacts_scanned": len(cons),
        "with_email": len(emails),
        "duplicate_email_groups": sum(1 for v in ec.values() if v > 1),
        "invalid_email_format": len(bad),
        "invalid_samples": bad[:25],
        "role_based_emails": len(role),
        "freemail_total": sum(free.values()),
        "freemail_breakdown": dict(free),
    }
    for k, v in R["contact_quality"].items():
        if isinstance(v, int):
            print(f"  {k:<28} {v}", flush=True)
    save()
    print(f"\nStage B done. {CALLS} calls.", flush=True)
