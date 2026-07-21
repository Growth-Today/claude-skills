"""
dedupe-contacts — BEFORE audit.

Flags likely duplicate contacts by exact email and by normalized
name+company across a sample. Review in HubSpot's Manage Duplicates tool
before merging (merges are not bulk-undoable).

Read-only.

Env: HUBSPOT_ACCESS_TOKEN in a .env file in the playbook folder (../.env).
Deps: requests, python-dotenv  (pip install -r ../../../requirements.txt)
"""
import os
import requests
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
BASE = "https://api.hubapi.com"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
SAMPLE_PAGES = 20  # 100 per page


def main():
    by_email = defaultdict(int)
    by_nameco = defaultdict(int)
    after, pages = None, 0
    while pages < SAMPLE_PAGES:
        payload = {"properties": ["email", "firstname", "lastname", "company"], "limit": 100}
        if after:
            payload["after"] = after
        r = requests.post(f"{BASE}/crm/v3/objects/contacts/search", headers=HEADERS, json=payload)
        r.raise_for_status()
        data = r.json()
        for c in data.get("results", []):
            p = c.get("properties", {})
            email = (p.get("email") or "").strip().lower()
            if email:
                by_email[email] += 1
            fn = (p.get("firstname") or "").strip().lower()
            ln = (p.get("lastname") or "").strip().lower()
            co = (p.get("company") or "").strip().lower()
            if fn and ln:
                by_nameco[f"{fn}|{ln}|{co}"] += 1
        after = data.get("paging", {}).get("next", {}).get("after")
        pages += 1
        if not after:
            break

    dup_email = {k: v for k, v in by_email.items() if v > 1}
    dup_nameco = {k: v for k, v in by_nameco.items() if v > 1}
    print(f"Sampled ~{pages*100} contacts")
    print(f"Exact-email duplicates: {len(dup_email)} email(s) with >1 record")
    print(f"Name+company duplicates: {len(dup_nameco)} group(s) with >1 record")
    print("\nStart with exact-email dupes (highest confidence) in Manage Duplicates.")


if __name__ == "__main__":
    main()
