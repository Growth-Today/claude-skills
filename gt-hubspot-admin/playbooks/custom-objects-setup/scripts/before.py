"""
custom-objects-setup — BEFORE audit.

Lists all object schemas (standard + custom) so you don't create a custom
object (or property) that duplicates something already modelled.

Read-only: this script does not modify anything.

Env: HUBSPOT_ACCESS_TOKEN in a .env file in the playbook folder (../.env).
Deps: requests, python-dotenv  (pip install -r ../../../requirements.txt)
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def main():
    r = requests.get("https://api.hubapi.com/crm/v3/schemas", headers=HEADERS)
    r.raise_for_status()
    results = r.json().get("results", [])
    custom = [s for s in results if s.get("objectTypeId", "").startswith("2-")]
    print(f"Total object schemas returned: {len(results)}")
    print(f"Custom objects: {len(custom)}\n")
    for s in results:
        labels = s.get("labels", {})
        name = labels.get("plural") or s.get("name")
        is_custom = s.get("objectTypeId", "").startswith("2-")
        tag = "CUSTOM" if is_custom else "standard"
        print(f"  [{tag}] {name} (objectTypeId={s.get('objectTypeId')})")
    print("\nConfirm your concept isn't already represented before creating a new object.")


if __name__ == "__main__":
    main()
