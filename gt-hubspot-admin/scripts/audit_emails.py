#!/usr/bin/env python3
"""Re-scan contact emails with a correct validation regex, and cache them.

The first pass used ^[^@\\s]+@[^@\\s.]+\\.[a-zA-Z]{2,}$ which rejects any domain
with more than one label (.co.uk, .com.au, subdomains) — ~3k false positives.
This caches emails to reports/contact_emails.json so re-analysis needs no API calls.
"""

import json
import os
import re
import time
import urllib.error
import urllib.request
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN = next(l.split("=", 1)[1].strip().strip('"').strip("'")
             for l in open(os.path.join(ROOT, ".env"))
             if l.startswith(("HUBSPOT_ACCESS_TOKEN=", "HUBSPOT_API_TOKEN=")))
CACHE = "reports/contact_emails.json"


def get(path, retries=4):
    for attempt in range(retries):
        try:
            req = urllib.request.Request("https://api.hubapi.com" + path,
                                         headers={"Authorization": f"Bearer {TOKEN}"})
            with urllib.request.urlopen(req, timeout=60) as f:
                time.sleep(0.11)
                return json.load(f)
        except urllib.error.HTTPError as e:
            if e.code in (429, 502, 503, 504):
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("retries exhausted")


if os.path.exists(CACHE):
    rows = json.load(open(CACHE))
    print(f"using cache: {len(rows)} contacts")
else:
    rows, after, n = [], None, 0
    while True:
        q = "/crm/v3/objects/contacts?limit=100&properties=email,hs_email_optout,hs_email_hard_bounce_reason_enum"
        if after:
            q += f"&after={after}"
        res = get(q)
        rows.extend(r.get("properties", {}) for r in res.get("results", []))
        n += 1
        if n % 100 == 0:
            print(f"  ...{len(rows)}", flush=True)
        after = res.get("paging", {}).get("next", {}).get("after")
        if not after:
            break
    json.dump(rows, open(CACHE, "w"))
    print(f"cached {len(rows)} contacts")

RX = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9](?:[A-Za-z0-9\-]*[A-Za-z0-9])?"
                r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9\-]*[A-Za-z0-9])?)*\.[A-Za-z]{2,}$")

emails = [r["email"].strip().lower() for r in rows if r.get("email")]
bad = [e for e in emails if not RX.match(e)]
dupes = Counter(emails)

ROLE = {"info", "sales", "support", "admin", "contact", "hello", "office", "marketing",
        "help", "team", "noreply", "no-reply", "enquiries", "hr", "billing", "accounts"}
role = [e for e in emails if e.split("@")[0] in ROLE]

FREE = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com",
        "icloud.com", "me.com", "gmx.com", "protonmail.com", "yandex.com"}
free = Counter(e.split("@")[1] for e in emails if e.split("@")[1] in FREE)

# Deliverability-hostile patterns that a plain regex passes but you should never mail.
NOISE_SUFFIX = ("intercom-mail.com", "zendesk.com", ".sentry.io", "hubs.ly",
                "mxtoolbox.com", "glockapps.com", "invoice.ziphq.com")
noise = [e for e in emails if e.split("@")[1].endswith(NOISE_SUFFIX)]

out = {
    "contacts_scanned": len(rows),
    "with_email": len(emails),
    "without_email": len(rows) - len(emails),
    "invalid_email_format": len(bad),
    "invalid_samples": bad[:30],
    "duplicate_email_groups": sum(1 for v in dupes.values() if v > 1),
    "duplicate_email_excess": sum(v - 1 for v in dupes.values() if v > 1),
    "role_based_emails": len(role),
    "freemail_total": sum(free.values()),
    "freemail_breakdown": dict(free),
    "system_noise_emails": len(noise),
    "system_noise_samples": noise[:15],
    "top_email_domains": Counter(e.split("@")[1] for e in emails).most_common(20),
}

R = json.load(open("reports/audit-raw.json"))
R["contact_quality"] = out
json.dump(R, open("reports/audit-raw.json", "w"), indent=2, default=str)

for k, v in out.items():
    if isinstance(v, (int, str)):
        print(f"  {k:<26} {v}")
print("  invalid samples:", out["invalid_samples"][:12])
print("  noise samples:", out["system_noise_samples"][:8])
