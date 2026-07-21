"""
property-validation-rules — BEFORE audit.

Samples contacts and flags common format anomalies that validation rules
(and dropdowns) would prevent: malformed emails, phone numbers without a
country code, and high-cardinality free-text properties (dropdown candidates).

Read-only: this script does not modify any data.

Env: HUBSPOT_ACCESS_TOKEN in a .env file in the playbook folder (../.env).
Deps: requests, python-dotenv  (pip install -r ../../../requirements.txt)
"""
import os
import re
import requests
from collections import Counter
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
BASE = "https://api.hubapi.com"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# Which free-text properties to check for dropdown-worthy cardinality.
FREE_TEXT_PROPS = ["industry", "jobtitle", "state", "country"]
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
SAMPLE_LIMIT = 2000  # pages of 100


def sample_contacts():
    props = ["email", "phone"] + FREE_TEXT_PROPS
    out, after, fetched = [], None, 0
    while fetched < SAMPLE_LIMIT:
        params = {"limit": 100, "properties": props}
        if after:
            params["after"] = after
        r = requests.get(f"{BASE}/crm/v3/objects/contacts", headers=HEADERS, params=params)
        r.raise_for_status()
        data = r.json()
        results = data.get("results", [])
        out.extend(results)
        fetched += len(results)
        after = data.get("paging", {}).get("next", {}).get("after")
        if not after:
            break
    return out


def main():
    contacts = sample_contacts()
    n = len(contacts)
    bad_email = phone_no_cc = 0
    cardinality = {p: Counter() for p in FREE_TEXT_PROPS}

    for c in contacts:
        p = c.get("properties", {})
        email = (p.get("email") or "").strip()
        if email and not EMAIL_RE.match(email):
            bad_email += 1
        phone = (p.get("phone") or "").strip()
        if phone and not phone.startswith("+"):
            phone_no_cc += 1
        for prop in FREE_TEXT_PROPS:
            val = (p.get(prop) or "").strip()
            if val:
                cardinality[prop][val] += 1

    print(f"Sampled contacts: {n}\n")
    print(f"Malformed emails:            {bad_email}")
    print(f"Phones without country code: {phone_no_cc}\n")
    print("Free-text field cardinality (high = dropdown candidate):")
    for prop, counter in cardinality.items():
        print(f"  {prop:<12} distinct values: {len(counter)}")
    print("\nConvert high-cardinality fields to dropdowns; add validation rules for the rest.")


if __name__ == "__main__":
    main()
