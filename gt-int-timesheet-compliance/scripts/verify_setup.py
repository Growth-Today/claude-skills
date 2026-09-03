"""Check the setup before trusting anything the other scripts say.

  python scripts/verify_setup.py

Answers, in order: is there a usable credential, can we reach Asana, does the
token's owner see everybody's time or only their own, and are the fields the
scoring depends on actually populated. Run this once after the token is in
place, and again any time a score looks wrong.

Exit code separates two very different things:

  1  the setup cannot produce numbers at all (no credential, no workspace, no
     entries, or a credential that only sees its own owner's time)
  0  numbers can be produced, possibly with caveats that limit what they mean

Deferred configuration is a caveat, not a failure. The approval endpoint is
deliberately unset until someone verifies it against the workspace, and the
attribution allowlist is deliberately empty until a baseline period has run.
Failing the run for those would make this check red on a perfectly good setup,
and a check that is always red is one nobody reads.
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


def note_line(label, detail=""):
    """For a deferred setting. Not a pass, and not a failure either.

    Printing FAIL next to something we deliberately left unset makes the whole
    report read as broken when it is working as intended.
    """
    print("{:4}  {:34} {}".format("....", label, detail))


def main():
    print("Timesheet compliance setup check\n")
    blockers = []   # cannot produce numbers at all
    notes = []      # numbers are possible, but limited in what they mean

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
        blockers.append("set ASANA_WORKSPACE_GID")
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
        blockers.append(
            "no entries came back. Either nobody logged time in this range, or the "
            "credential cannot see time entries at all"
        )
        print()
        for item in blockers:
            print("  next: {}".format(item))
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
        blockers.append(
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
        notes.append(
            "no created_at on any entry, so backfill detection is off and daily "
            "hygiene (30% of the score) degrades to 'any entry counts'. The nudge "
            "still works; the hygiene number just means less than it looks"
        )
    if not line(
        with_attr > 0,
        "attributable_to populated",
        "{} of {} entries".format(with_attr, total),
    ):
        notes.append(
            "no attributable_to on any entry, so attribution (30% of the score) cannot "
            "be scored at all. That is a task structure problem, not a scoring one, and "
            "no config change fixes it"
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
    if configured:
        line(True, "approval endpoint configured", "on-time submission will be scored")
    else:
        note_line("approval endpoint", "not set yet, on-time reports as unavailable")
    if not configured:
        notes.append(
            "the timesheet approval endpoint is not configured, so on-time submission "
            "reports as unavailable and every score is flagged partial. Expected until "
            "someone verifies the endpoint against this workspace"
        )

    scoring_attr = scoring.get("attribution", {})
    if not (scoring_attr.get("attributable_project_gids") or []):
        notes.append(
            "the attribution allowlist is empty, so any attributed time counts and the "
            "metric cannot tell client work from a catch-all task. Expected until a "
            "baseline period has run. The list above is what fills it"
        )

    print()
    if blockers:
        print("BLOCKED. This setup cannot produce usable numbers:")
        for item in blockers:
            print("  - {}".format(item))
        if notes:
            print("\nAlso worth knowing once the above is fixed:")
            for item in notes:
                print("  - {}".format(item))
        sys.exit(1)

    print("Setup works. Numbers can be produced from this data.")
    if notes:
        print("\nCaveats on what those numbers mean:")
        for item in notes:
            print("  - {}".format(item))
        print(
            "\nNone of these block the nudge. They limit the score, and each one is "
            "expected at this stage rather than broken."
        )


if __name__ == "__main__":
    main()
