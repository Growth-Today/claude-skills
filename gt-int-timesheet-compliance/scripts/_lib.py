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
    """The Asana token, or None when the agent proxy is holding it for us.

    Two supported ways to authenticate, and the difference matters:

    1. ASANA_ACCESS_TOKEN in the environment. The script sends the Authorization
       header itself. This is the local development path.
    2. An API credential stored on the cloud environment. Anthropic's agent
       proxy attaches the Authorization header to requests for app.asana.com
       after they leave the sandbox, so the key never enters the container, the
       environment variables, or any file. Nothing here can print, log or commit
       it. This is the right path for scheduled runs.

    Returning None means we send no Authorization header and let the proxy do
    it. A 401 in that case means the credential is missing or not attached, and
    api_get says so.
    """
    return os.environ.get("ASANA_ACCESS_TOKEN") or None


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


def _roster_doc():
    """The whole roster document, from the file or from the ROSTER_JSON env var.

    The env var exists for the unattended runner: in a public repo the roster
    cannot be committed, so it travels as a repository secret instead. A file
    always wins over the env var, so a private repo can just commit it.
    """
    path = os.path.join(CONFIG_DIR, "roster.json")
    if os.path.exists(path):
        return load_json(path, "roster.json")

    raw = os.environ.get("ROSTER_JSON")
    if raw:
        try:
            return _strip_comments(json.loads(raw))
        except ValueError as error:
            die("ROSTER_JSON is set but is not valid JSON: {}".format(error))

    die(
        "No roster found. Either copy config/roster.example.json to "
        "config/roster.json (gitignored), or set ROSTER_JSON to the same content "
        "as a secret. See references/github-actions.md."
    )


def load_messages():
    return load_json(os.path.join(CONFIG_DIR, "messages.json"), "messages.json")


def timesheet_url():
    """Deep link to the Timesheets page, from the roster or the environment.

    Kept out of the committed config because it is an internal view URL.
    """
    return (
        _roster_doc().get("timesheet_url")
        or os.environ.get("TIMESHEET_URL")
        or "your Asana Timesheets page"
    )


def load_roster():
    roster = _roster_doc()
    people = [p for p in roster.get("submitters", []) if p.get("active", True)]
    if not people:
        die("roster.json has no active submitters.")
    for person in people:
        for field in ("asana_gid", "name", "timezone", "daily_target_hours"):
            if not person.get(field):
                die("roster entry {} is missing {}".format(person.get("name", "?"), field))
        if person.get("target_confirmed") is False:
            warn(
                "{}'s daily_target_hours is {} and marked unconfirmed, so their hours "
                "coverage sub-metric is provisional. Confirm the contracted hours before "
                "using their score for anything.".format(
                    person["name"], person["daily_target_hours"]
                )
            )
    return people


# ----------------------------------------------------------------- Asana API


def api_get(path, params=None, max_pages=200):
    """GET an Asana collection, following offset pagination. Returns a list."""
    value = token()
    headers = {"Authorization": "Bearer {}".format(value)} if value else {}
    params = dict(params or {})
    params.setdefault("limit", 100)
    results = []
    pages = 0

    while True:
        for attempt in range(4):
            try:
                response = requests.get(
                    "{}{}".format(API_BASE, path), headers=headers, params=params, timeout=60
                )
            except requests.exceptions.RequestException as error:
                if attempt < 3:
                    time.sleep(2 ** attempt)
                    continue
                die(
                    "Could not reach app.asana.com: {}\n"
                    "A proxy 403 here means the environment is not allowed to reach "
                    "app.asana.com. Storing an API credential for that host on the cloud "
                    "environment opens egress to it as well as supplying the key, so it "
                    "fixes both at once. Otherwise the environment's network access level "
                    "has to permit app.asana.com.".format(error)
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
            hint = ""
            if response.status_code == 401:
                hint = (
                    "\n401 means no usable credential reached Asana. Either set "
                    "ASANA_ACCESS_TOKEN locally, or check that the cloud environment's "
                    "API credential for app.asana.com exists and is not marked Not sent."
                )
            elif response.status_code == 403:
                hint = (
                    "\n403 on a time tracking endpoint usually means the credential lacks "
                    "the time_tracking_entries:read scope, or its owner cannot see other "
                    "people's time. A personal access token carries its creator's own "
                    "permissions, so it has to belong to a time reviewer or an admin. A "
                    "service account with org-wide access avoids the problem."
                )
            die(
                "Asana returned {} for {}: {}{}".format(
                    response.status_code, path, response.text[:400], hint
                )
            )

        payload = response.json()
        data = payload.get("data")
        if isinstance(data, dict):
            # A single-object endpoint such as /users/me. Extending a list with a
            # dict yields its keys, which turns the caller's first result into the
            # string "gid" and fails somewhere unrelated. Single objects are never
            # paginated, so wrap and stop.
            results.append(data)
            return results
        if isinstance(data, list):
            results.extend(data)
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


def program_start(scoring):
    """The first day that counts, or None if everything counts.

    Set once the process actually goes live. Time logged before it is real work
    and stays in Asana, but scoring it would judge people against a rule nobody
    had been told about yet, and one bad pre-launch week would sit in the
    two-period gate for a month.
    """
    value = ((scoring or {}).get("program_start_date") or "").strip()
    return parse_date(value) if value else None


def workdays(start, end, scoring=None):
    """Monday to Friday between start and end inclusive, minus holidays.

    Takes the whole scoring config rather than just the holiday list, so the
    program start date is applied in one place. Every window, streak and nudge
    is built from this function, so flooring here is what makes "nothing before
    go-live counts" true everywhere instead of in whichever caller remembered.
    """
    scoring = scoring or {}
    skip = {parse_date(h) for h in (scoring.get("holidays") or [])}
    floor = program_start(scoring)
    if floor and start < floor:
        start = floor
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


# ------------------------------------------------ behind / streak helpers
# Shared by who_is_behind.py (today's nudge) and score.py (the weekly
# persistence rule) so the definition of "behind" exists in exactly one place.


def logged_minutes(entries, start, end, as_of=None):
    """Minutes logged for days inside the range, inclusive.

    Pass as_of to count only what had actually been entered by that date. That
    is what makes a retrospective "were they behind on Tuesday" answer match
    what the nudge saw on Tuesday: without it, someone who reconstructs a whole
    week on Friday looks like they were never behind, because their entries now
    carry the earlier dates. Entries with no created_at are always counted,
    since we cannot tell when they were typed.
    """
    total = 0
    for entry in entries:
        if not entry.get("entered_on"):
            continue
        day = parse_date(entry["entered_on"])
        if not (start <= day <= end):
            continue
        if as_of is not None:
            created = parse_created_at(entry.get("created_at"))
            if created is not None and created > as_of:
                continue
        total += entry.get("duration_minutes") or 0
    return total


def days_with_entries(entries, grace_days):
    """Days holding an entry that was created at or near the time it covers."""
    covered = set()
    for entry in entries:
        if not entry.get("entered_on"):
            continue
        entered = parse_date(entry["entered_on"])
        created = parse_created_at(entry.get("created_at"))
        if created is None or (created - entered).days <= grace_days:
            covered.add(entered)
    return covered


def behind_as_of(entries, person, day, scoring):
    """Was this person behind on hours at the end of the given day?"""
    days = workdays(week_start(day), day, scoring)
    if not days:
        return False
    expected = len(days) * float(person["daily_target_hours"]) * 60
    if expected <= 0:
        return False
    logged = logged_minutes(entries, days[0], day, as_of=day)
    return logged < scoring["nudge"]["behind_ratio"] * expected


def streak_behind(entries, person, today, scoring, lookback=10):
    """Consecutive weekdays ending behind, counting back from today."""
    streak = 0
    cursor = today
    checked = 0
    while checked < lookback:
        if cursor.weekday() < 5:
            if behind_as_of(entries, person, cursor, scoring):
                streak += 1
            else:
                break
            checked += 1
        cursor -= timedelta(days=1)
    return streak


def longest_streak_in_week(entries, person, monday, scoring):
    """Longest run of consecutive weekdays behind within a single week."""
    best = 0
    run = 0
    for day in workdays(monday, monday + timedelta(days=4), scoring):
        if behind_as_of(entries, person, day, scoring):
            run += 1
            best = max(best, run)
        else:
            run = 0
    return best


def load_escalation_contacts():
    """People the weekly persistent-pattern draft is addressed to.

    Read from roster.json, never from scoring.json, so no real person's details
    sit in a committed config file.
    """
    path = os.path.join(CONFIG_DIR, "roster.json")
    if not os.path.exists(path):
        return []
    return load_json(path, "roster.json").get("escalation_contacts", [])


def was_nudge_target_on(entries, person, day, scoring):
    """Would this person have been a nudge target at the end of the given day?

    Mirrors the live trigger (behind on hours, or missing a same-day entry) using
    only what had actually been entered by that day. That makes the count
    reproducible from the entries alone, so a weekly cap needs no stored counter.
    """
    days = workdays(week_start(day), day, scoring)
    if not days:
        return False

    expected = len(days) * float(person["daily_target_hours"]) * 60
    logged = logged_minutes(entries, days[0], day, as_of=day)
    behind = expected > 0 and logged < scoring["nudge"]["behind_ratio"] * expected

    known = [
        e
        for e in entries
        if (parse_created_at(e.get("created_at")) or day) <= day
    ]
    covered = days_with_entries(known, scoring["hygiene"]["grace_days"])
    missing = [d for d in days if d not in covered]

    return behind or bool(missing)


def nudges_this_week(entries, person, today, scoring):
    """Nudges this person has earned so far this week, today included."""
    return len(
        [
            d
            for d in workdays(week_start(today), today, scoring)
            if was_nudge_target_on(entries, person, d, scoring)
        ]
    )
