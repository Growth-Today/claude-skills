"""
salesforce-sync-management — BEFORE audit.

Counts HubSpot records that carry a Salesforce ID (i.e. are synced) across
contacts, companies, and deals, so you know how much is synced before making
any changes. Also review Settings > Integrations > Salesforce sync health in
the UI.

Read-only.

Env: HUBSPOT_ACCESS_TOKEN in a .env file in the playbook folder (../.env).
Deps: requests, python-dotenv  (pip install -r ../../../requirements.txt)
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
BASE = "https://api.hubapi.com"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# HubSpot property that holds the synced Salesforce record id, per object.
SF_ID_PROP = {
    "contacts": "salesforcecontactid",
    "companies": "salesforceaccountid",
    "deals": "hs_salesforceopportunityid",
}


def count_synced(obj, prop):
    payload = {
        "filterGroups": [{"filters": [{"propertyName": prop, "operator": "HAS_PROPERTY"}]}],
        "limit": 0,
    }
    r = requests.post(f"{BASE}/crm/v3/objects/{obj}/search", headers=HEADERS, json=payload)
    if r.status_code != 200:
        return f"(could not query — property '{prop}' may not exist: {r.status_code})"
    return r.json().get("total")


def main():
    print("Synced records (carry a Salesforce ID):")
    for obj, prop in SF_ID_PROP.items():
        print(f"  {obj:<10} {count_synced(obj, prop)}")
    print("\nReview Settings > Integrations > Salesforce for sync errors and field mappings.")


if __name__ == "__main__":
    main()
