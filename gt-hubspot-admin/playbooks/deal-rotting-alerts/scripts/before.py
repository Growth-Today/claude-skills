"""
deal-rotting-alerts — BEFORE audit.

Reports, per deal stage, how many OPEN deals exceed common age buckets
(30 / 60 / 90 days in current stage). Use the output to set a realistic
max-age threshold per stage before building the alert workflow.

Read-only: this script does not modify any data.

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

MS_PER_DAY = 1000 * 60 * 60 * 24  # hs_time_in_dealstage is returned in milliseconds


def get_stage_labels():
    """Map dealstage id -> readable label, per pipeline."""
    r = requests.get(f"{BASE}/crm/v3/pipelines/deals", headers=HEADERS)
    r.raise_for_status()
    labels = {}
    for p in r.json().get("results", []):
        for s in p.get("stages", []):
            labels[s["id"]] = f'{p["label"]} / {s["label"]}'
    return labels


def audit_open_deals():
    """Paginate open deals, bucket time-in-stage per stage."""
    buckets = defaultdict(lambda: {"total": 0, "over30": 0, "over60": 0, "over90": 0})
    after = None
    while True:
        payload = {
            "filterGroups": [{"filters": [
                {"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"}
            ]}],
            "properties": ["dealstage", "hs_time_in_dealstage"],
            "limit": 100,
        }
        if after:
            payload["after"] = after
        r = requests.post(f"{BASE}/crm/v3/objects/deals/search", headers=HEADERS, json=payload)
        r.raise_for_status()
        data = r.json()
        for d in data.get("results", []):
            props = d.get("properties", {})
            stage = props.get("dealstage") or "(none)"
            raw = props.get("hs_time_in_dealstage")
            days = (int(raw) / MS_PER_DAY) if raw else 0
            b = buckets[stage]
            b["total"] += 1
            if days > 30:
                b["over30"] += 1
            if days > 60:
                b["over60"] += 1
            if days > 90:
                b["over90"] += 1
        paging = data.get("paging", {}).get("next", {})
        after = paging.get("after")
        if not after:
            break
    return buckets


def main():
    labels = get_stage_labels()
    buckets = audit_open_deals()
    print(f"{'Stage':<45}{'Open':>7}{'>30d':>7}{'>60d':>7}{'>90d':>7}")
    print("-" * 73)
    for stage_id, b in sorted(buckets.items(), key=lambda x: -x[1]["total"]):
        name = labels.get(stage_id, stage_id)[:44]
        print(f"{name:<45}{b['total']:>7}{b['over30']:>7}{b['over60']:>7}{b['over90']:>7}")
    print("\nSet each stage's max-age threshold below the point where deals clearly rot.")


if __name__ == "__main__":
    main()
