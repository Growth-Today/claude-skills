"""
lead-status-taxonomy — BEFORE audit.

Prints the distribution of hs_lead_status values across contacts so you can
see ad hoc / duplicate statuses to consolidate into a defined taxonomy.

Read-only: this script does not modify any data.

Env: HUBSPOT_ACCESS_TOKEN in a .env file in the playbook folder (../.env).
Deps: requests, python-dotenv  (pip install -r ../../../requirements.txt)
"""
import os
import requests
from collections import Counter
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
BASE = "https://api.hubapi.com"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


def main():
    counts = Counter()
    blank = 0
    after = None
    total = 0
    while True:
        payload = {"properties": ["hs_lead_status"], "limit": 100}
        if after:
            payload["after"] = after
        r = requests.post(f"{BASE}/crm/v3/objects/contacts/search", headers=HEADERS, json=payload)
        r.raise_for_status()
        data = r.json()
        for c in data.get("results", []):
            total += 1
            val = (c.get("properties", {}).get("hs_lead_status") or "").strip()
            if val:
                counts[val] += 1
            else:
                blank += 1
        after = data.get("paging", {}).get("next", {}).get("after")
        if not after:
            break

    print(f"Contacts scanned: {total}")
    print(f"Blank lead status: {blank}\n")
    print("Lead status distribution (consolidate ad hoc values):")
    for val, n in counts.most_common():
        print(f"  {val:<30} {n}")


if __name__ == "__main__":
    main()
