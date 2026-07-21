"""
security-health-audit — BEFORE audit.

Lists users, counts Super Admins, and flags accounts for security review.
Use alongside Settings > Account Defaults > Security (HubSpot's own
Security Health checklist).

Read-only: this script does not modify any users or data.

Env: HUBSPOT_ACCESS_TOKEN in a .env file in the playbook folder (../.env).
Deps: requests, python-dotenv  (pip install -r ../../../requirements.txt)
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
BASE = "https://api.hubapi.com"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def get_all_users():
    users, after = [], None
    while True:
        url = f"{BASE}/settings/v3/users?limit=100"
        if after:
            url += f"&after={after}"
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        data = r.json()
        users.extend(data.get("results", []))
        after = data.get("paging", {}).get("next", {}).get("after")
        if not after:
            break
    return users


def main():
    users = get_all_users()
    supers = [u for u in users if u.get("superAdmin")]
    no_team = [u for u in users if not u.get("primaryTeamId")]

    print(f"Total users (paid + partner): {len(users)}")
    print(f"Super Admins: {len(supers)}  (target: 2-3)")
    for u in supers:
        print(f"  - {u.get('email')}")
    print(f"\nUsers with no primary team: {len(no_team)}")
    for u in no_team:
        print(f"  - {u.get('email')}")

    print("\nNext: check Settings > Account Defaults > Security for 2FA/SSO status,")
    print("reassign records for any departed users (reassign-deactivated-owners),")
    print("then deactivate their seats.")


if __name__ == "__main__":
    main()
