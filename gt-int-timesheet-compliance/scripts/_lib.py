"""Shared helpers for the timesheet compliance scripts.

Everything numeric lives here or in score.py so the model never has to add up
minutes. Warnings go to stderr and are meant to be read, not swallowed: a score
built on a missing field is worse than no score.
"""

import json
import os
import sys
import time
from datetime import date, datetime, timedelta

import requests
from dotenv import load_dotenv

try:
    from zoneinfo import ZoneInfo
except ImportError:  # Python 3.8 and older
    ZoneInfo = None

SKILL_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG_DIR = os.path.join(SKILL_ROOT, "config")

load_dotenv(os.path.join(SKILL_ROOT, ".env"))

API_BASE = "https://app.asana.com/api/1.0"


def warn(message):
    print("WARN: {}".format(message), file=sys.stderr)


def die(message):
    print("ERROR: {}".format(message), file=sys.stderr)
    sys.exit(1)


def token():
    value = os.environ.get("ASANA_ACCESS_TOKEN")
    if not value:
        die(
            "ASANA_ACCESS_TOKEN is not set. In a scheduled Routine it has to be an "
            "environment variable on the remote environment, not a local .env file. "
            "See references/setup.md."
        )
    return value


def workspace_gid():
    value = os.environ.get("ASANA_WORKSPACE_GID")
    if not value:
        die("ASANA_WORKSPACE_GID is not set. See references/setup.md.")
    return value


def _strip_comments(obj):
    """Drop the _comment and _fields keys we use to document the config files."""
    if isinstance(obj, dict):
        return {k: _strip_comments(v) for k, v in obj.items() if not k.startswith("_")}
    if isinstance(obj, list):
        return [_strip_comments(v) for v in obj]
    return obj


def load_json(path, what):
    if not os.path.exists(path):
        die("{} not found at {}".format(what, path))
    with open(path, "r", encoding="utf-8") as handle:
        return _strip_comments(json.load(handle))


def load_scoring():
    config = load_json(os.path.join(CONFIG_DIR, "scoring.json"), "scoring.json")
    total = sum(config["weights"].values())
    if abs(total - 1.0) > 1e-6:
        die("scoring.json weights sum to {}, they must sum to 1.0".format(total))
    return config


def load_roster():
    path = os.path.join(CONFIG_DIR, "roster.json")
    if not os.path.exists(path):
        die(
            "config/roster.json not found. Copy config/roster.example.json to "
            "config/roster.json and fill it in. The real roster is gitignored on purpose."
        )
    roster = load_json(path, "roster.json")
    people = [p for p in roster.get("submitters", []) if p.get("active", True)]
    if not people:
        die("roster.json has no active submitters.")
    for person in people:
        for field in ("asana_gid", "name", "timezone", "daily_target_hours"):
            if not person.get(field):
                die("roster entry {} is missing {}".format(person.get("name", "?"), field))
    return people


# ----------------------------------------------------------------- Asana API


def api_get(path, params=None, max_pages=200):
    """GET an Asana collection, following offset pagination. Returns a list."""
    headers = {"Authorization": "Bearer {}".format(token())}
    params = dict(params or {})
    params.setdefault("limit", 100)
    results = []
    pages = 0

    while True:
        for attempt in range(4):
            response = requests.get(
                "{}{}".format(API_BASE, path), headers=headers, params=params, timeout=60
            )
            if response.status_code == 429:
                wait = int(response.headers.get("Retry-After", 5))
                warn("rate limited, waiting {}s".format(wait))
                time.sleep(wait)
                continue
            if response.status_code >= 500 and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            break

        if response.status_code != 200:
            die(
                "Asana returned {} for {}: {}\nIf this is a 403 on a time tracking "
                "endpoint, the token is missing the time_tracking_entries:read scope. "
                "A personal access token carries your full user scope; an OAuth app "
                "connection may not.".format(response.status_code, path, response.text[:400])
            )

        payload = response.json()
        results.extend(payload.get("data", []))
        pages += 1

        offset = (payload.get("next_page") or {}).get("offset")
        if not offset:
            break
        if pages >= max_pages:
            warn("stopped after {} pages, results may be truncated".format(max_pages))
            break
        params["offset"] = offset

    return results


ENTRY_FIELDS = ",".join(
    [
        "duration_minutes",
        "entered_on",
        "created_at",
        "created_by.gid",
        "created_by.name",
        "attributable_to.gid",
        "attributable_to.name",
        "task.gid",
        "task.name",
    ]
)


def fetch_entries(start, end):
    """Time tracking entries for a date range, whole workspace.

    The workspace filter requires at least one date bound, which is why start and
    end are not optional here.
    """
    return api_get(
        "/time_tracking_entries",
        {
            "workspace": workspace_gid(),
            "entered_on_start_date": iso(start),
            "entered_on_end_date": iso(end),
            "opt_fields": ENTRY_FIELDS,
        },
    )


def fetch_approvals(scoring, people, week_starts):
    """Weekly timesheet approval status per person, if the endpoint is configured.

    Returns (data, available). We never guess the collection path: until someone
    verifies it against the workspace and writes it into scoring.json, on-time
    submission is reported as unavailable rather than invented.
    """
    config = scoring.get("approval_endpoint", {})
    path = (config.get("path") or "").strip()
    if not path:
        warn(
            "approval_endpoint.path is empty in scoring.json, so on-time submission "
            "cannot be scored. The remaining three weights will be renormalized and "
            "the output flagged partial. Verify the endpoint, then fill the path in."
        )
        return {}, False

    data = {}
    for person in people:
        for week_start in week_starts:
            rows = api_get(
                path,
                {
                    config.get("user_param", "user"): person["asana_gid"],
                    config.get("week_start_param", "week_start_on"): iso(week_start),
                    "workspace": workspace_gid(),
                },
            )
            data.setdefault(person["asana_gid"], {})[iso(week_start)] = rows
    return data, True


# ------------------------------------------------------------------- dates


def iso(value):
    return value.isoformat() if hasattr(value, "isoformat") else str(value)


def parse_date(value):
    return datetime.strptime(str(value)[:10], "%Y-%m-%d").date()


def parse_created_at(value):
    """Asana timestamps are ISO 8601 with a Z. Return a date, or None."""
    if not value:
        return None
    try:
        return parse_date(value)
    except ValueError:
        return None


def workdays(start, end, holidays=None):
    """Monday to Friday between start and end inclusive, minus holidays."""
    skip = {parse_date(h) for h in (holidays or [])}
    days = []
    cursor = start
    while cursor <= end:
        if cursor.weekday() < 5 and cursor not in skip:
            days.append(cursor)
        cursor += timedelta(days=1)
    return days


def week_start(day):
    """The Monday of the week containing day."""
    return day - timedelta(days=day.weekday())


def local_now(timezone_name):
    if ZoneInfo is None:
        die("This script needs Python 3.9 or newer for timezone handling.")
    try:
        return datetime.now(ZoneInfo(timezone_name))
    except Exception:
        die("Unknown timezone {} in roster.json. Use an IANA name like Asia/Manila.".format(timezone_name))


def pay_period_bounds(anchor_monday, weeks, index=0):
    """Start and end date of a pay period, counting back from an anchor Monday."""
    start = anchor_monday - timedelta(weeks=weeks * index)
    end = start + timedelta(days=weeks * 7 - 1)
    return start, end


# --------------------------------------------------------------- aggregation


def index_entries(entries, people):
    """Group raw entries by person GID, keeping only roster members.

    Also reports what the API actually returned, because a silently absent field
    turns into a silently wrong score.
    """
    wanted = {p["asana_gid"] for p in people}
    by_person = {gid: [] for gid in wanted}
    unknown = 0
    missing_created_at = 0
    missing_attribution = 0

    for entry in entries:
        author = (entry.get("created_by") or {}).get("gid")
        if author not in wanted:
            unknown += 1
            continue
        if not entry.get("created_at"):
            missing_created_at += 1
        if not (entry.get("attributable_to") or {}).get("gid"):
            missing_attribution += 1
        by_person[author].append(entry)

    total = sum(len(v) for v in by_person.values())
    if unknown:
        warn("{} entries belong to people outside the roster and were ignored".format(unknown))
    if total and missing_created_at == total:
        warn(
            "no entry carried created_at, so backfill detection is off and daily "
            "hygiene degrades to 'a day with any entry counts'. Check that created_at "
            "is available on this workspace."
        )
    if total and missing_attribution == total:
        warn(
            "no entry carried attributable_to, so attribution cannot be scored at all. "
            "Fix how time is logged before trusting a composite score."
        )
    return by_person
