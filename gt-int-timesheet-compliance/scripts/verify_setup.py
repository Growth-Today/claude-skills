"""Check the setup before trusting anything the other scripts say.

  python scripts/verify_setup.py

Answers, in order: is there a usable credential, can we reach Asana, does the
token's owner see everybody's time or only their own, and are the fields the
scoring depends on actually populated. Run this once after the token is in
place, and again any time a score looks wrong.

Exits non-zero if something is broken enough that a score would be misleading.
"""

import json
import os
import sys
from datetime import datetime, timedelta, timezone

import _lib as lib


def line(ok, label, detail=""):
    mark = "PASS" if ok else "FAIL"
    print("{:4}  {:34} {}".format(mark, label, detail))
    return ok


def main():
    print("Timesheet compliance setup check\n")
    problems = []

    # 1. Credential
    if os.environ.get("ASANA_ACCESS_TOKEN"):
        line(True, "credential", "ASANA_ACCESS_TOKEN is set, the script sends the header")
    else:
        line(
            True,
            "credential",
            "no token in the environment, relying on the proxy's API credential",
        )

    # 2. Workspace
    workspace = os.environ.get("ASANA_WORKSPACE_GID")
    if not line(bool(workspace), "ASANA_WORKSPACE_GID", workspace or "not set"):
        problems.append("set ASANA_WORKSPACE_GID")
        print("\nCannot continue without a workspace.")
        sys.exit(1)

    # 3. Roster
    people = lib.load_roster()
    line(True, "roster", "{} active submitters".format(len(people)))

    # 4. Reach the API at all, on a cheap endpoint
    try:
        me = lib.api_get("/users/me", {"opt_fields": "name,email"})
    except SystemExit:
        raise
    owner = (me[0] if isinstance(me, list) and me else me) or {}
    line(
        True,
        "asana reachable",
        "authenticated as {}".format(owner.get("name") or "unknown"),
    )

    # 5. Time entries, last 14 days
    end = lib.week_start(datetime.now(timezone.utc).date()) + timedelta(days=4)
    start = end - timedelta(days=20)
    entries = lib.fetch_entries(start, end)
    got = line(
        bool(entries),
        "time entries readable",
        "{} entries between {} and {}".format(len(entries), start, end),
    )
    if not got:
        problems.append(
            "no entries came back. Either nobody logged time in this range, or the "
            "credential cannot see time entries at all"
        )
        print()
        for p in problems:
            print("  next: {}".format(p))
        sys.exit(1)

    # 6. Visibility: does this credential see the whole team or just its owner?
    authors = {}
    for entry in entries:
        author = entry.get("created_by") or {}

        if author.get("gid"):
            authors[author["gid"]] = author.get("name") or author["gid"]
    roster_gids = {p["asana_gid"] for p in people}
    seen_from_roster = sorted(roster_gids & set(authors))
    missing = [p["name"] for p in people if p["asana_gid"] not in authors]

    if len(seen_from_roster) <= 1 and len(people) > 1:
        line(
            False,
            "team-wide visibility",
            "entries from only {} of {} submitters".format(
                len(seen_from_roster), len(people)
            ),
        )
        problems.append(
            "the credential may only see its own owner's time. A personal access token "
            "carries its creator's permissions, so it has to belong to a time reviewer "
            "or an admin. A service account with org-wide access avoids this entirely. "
            "Verify before trusting any team score"
        )
    else:
        line(
            True,
            "team-wide visibility",
            "entries from {} of {} submitters".format(len(seen_from_roster), len(people)),
        )
    if missing:
        print("      no entries in range for: {}".format(", ".join(missing)))
        print("      (could be genuine, could be a visibility problem, check one by hand)")

    # 7. The fields the scoring depends on
    total = len(entries)
    with_created = len([e for e in entries if e.get("created_at")])
    with_attr = len([e for e in entries if (e.get("attributable_to") or {}).get("gid")])

    if not line(
        with_created > 0,
        "created_at populated",
        "{} of {} entries".format(with_created, total),
    ):
        problems.append(
            "no created_at means backfill detection is off and daily hygiene (30% of "
            "the score) degrades to 'any entry counts'"
        )
    if not line(
        with_attr > 0,
        "attributable_to populated",
        "{} of {} entries".format(with_attr, total),
    ):
        problems.append(
            "no attributable_to means attribution (30% of the score) cannot be scored "
            "at all. This is a task structure problem, not a scoring one"
        )

    # 8. What people actually attribute to, which is what the allowlist needs
    projects = {}
    for entry in entries:
        target = entry.get("attributable_to") or {}
        if target.get("gid"):
            key = (target["gid"], target.get("name") or target["gid"])
            projects[key] = projects.get(key, 0) + (entry.get("duration_minutes") or 0)

    if projects:
        print("\nWhere the logged time is attributed, most hours first.")
        print("Use this to fill attribution.attributable_project_gids in scoring.json:\n")
        for (gid, name), minutes in sorted(projects.items(), key=lambda kv: -kv[1]):
            print("  {:>8.1f}h  {}  ({})".format(minutes / 60, name, gid))

    # 9. Approval endpoint
    scoring = lib.load_scoring()
    configured = bool((scoring.get("approval_endpoint", {}).get("path") or "").strip())
    line(
        configured,
        "approval endpoint configured",
        "on-time submission will be scored" if configured else "on-time reports as unavailable",
    )
    if not configured:
        problems.append(
            "verify the timesheet approval endpoint against this workspace and fill "
            "approval_endpoint.path, or every score stays flagged partial"
        )

    print()
    if problems:
        print("Not ready to trust a score yet:")
        for p in problems:
            print("  - {}".format(p))
        sys.exit(1)
    print("Setup looks good. Scores from this data can be trusted.")


if __name__ == "__main__":
    main()
