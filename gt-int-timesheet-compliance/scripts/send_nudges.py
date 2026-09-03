"""Send the daily nudge as Slack DMs, for the unattended runner.

  # see exactly what would go out, sends nothing
  python scripts/send_nudges.py --targets /tmp/targets.json

  # actually send
  python scripts/send_nudges.py --targets /tmp/targets.json --send

Reads the output of who_is_behind.py and DMs each person in nudge_now, using
the templates in config/messages.json. Dry run is the default on purpose: these
messages go to real colleagues, so sending is opt-in.

When the loop runs through Claude instead, Claude writes each message from the
same numbers and the copy is better. This exists so the nudge can run with no
model in the loop, and templated copy is the trade-off.

Needs SLACK_BOT_TOKEN with chat:write and im:write.
"""

import argparse
import json
import os
import sys

import requests

import _lib as lib

SLACK_API = "https://slack.com/api"


def slack_post(method, token, payload):
    response = requests.post(
        "{}/{}".format(SLACK_API, method),
        headers={
            "Authorization": "Bearer {}".format(token),
            "Content-Type": "application/json; charset=utf-8",
        },
        json=payload,
        timeout=30,
    )
    try:
        body = response.json()
    except ValueError:
        lib.die("Slack {} returned non-JSON: {}".format(method, response.text[:300]))

    if not body.get("ok"):
        error = body.get("error", "unknown")
        hint = ""
        if error == "not_in_channel" or error == "channel_not_found":
            hint = " The bot may not be able to open a DM with this person. Check the im:write scope."
        elif error == "invalid_auth" or error == "not_authed":
            hint = " SLACK_BOT_TOKEN is missing or wrong."
        elif error == "missing_scope":
            hint = " The bot needs chat:write and im:write. Needed: {}".format(
                body.get("needed", "?")
            )
        lib.die("Slack {} failed: {}.{}".format(method, error, hint))
    return body


def open_dm(token, user_id):
    return slack_post("conversations.open", token, {"users": user_id})["channel"]["id"]


def human_dates(dates):
    if not dates:
        return "none"
    if len(dates) == 1:
        return dates[0]
    return "{} and {}".format(", ".join(dates[:-1]), dates[-1])


def compose(target, messages, link):
    template = messages.get(target["escalation"])
    if not template:
        lib.die(
            "No template for escalation level '{}' in config/messages.json".format(
                target["escalation"]
            )
        )
    reasons = target.get("reasons") or []
    return template.format(
        detail="; ".join(reasons) if reasons else "hours are behind for this week",
        name=target["name"],
        logged="{:.1f}".format(target["logged_hours"]),
        expected="{:.1f}".format(target["expected_hours"]),
        deficit="{:.1f}".format(target["deficit_hours"]),
        missing=human_dates(target.get("missing_days") or []),
        streak=target["weekdays_behind_in_a_row"],
        link=link,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", required=True, help="who_is_behind.py output, or - for stdin")
    parser.add_argument("--send", action="store_true", help="actually send. Without this, dry run")
    args = parser.parse_args()

    if args.targets == "-":
        payload = json.load(sys.stdin)
    else:
        with open(args.targets, "r", encoding="utf-8") as handle:
            payload = json.load(handle)

    messages = lib.load_messages()
    link = lib.timesheet_url()
    targets = payload.get("nudge_now") or []
    capped = payload.get("suppressed_by_weekly_cap") or []
    on_track = payload.get("on_track_do_not_contact") or []

    print("On track, not contacted: {}".format(len(on_track)))
    if capped:
        print(
            "Hit the weekly cap, deliberately silent: {}".format(
                ", ".join("{} ({})".format(c["name"], c["nudges_this_week"]) for c in capped)
            )
        )

    if not targets:
        print("Nobody is behind. No messages sent, and that is a successful run.")
        return

    token = os.environ.get("SLACK_BOT_TOKEN")
    if args.send and not token:
        lib.die("SLACK_BOT_TOKEN is not set, so --send cannot work.")

    sent = 0
    for target in targets:
        text = compose(target, messages, link)
        channels = target.get("channels") or ["slack"]

        print("\n--- {} [{}] nudge #{} of the week".format(
            target["name"], target["escalation"],
            target.get("nudges_this_week_including_this_one", "?"),
        ))
        print("    channels: {}".format(", ".join(channels)))
        print("    {}".format(text))

        if "email" in channels:
            print("    NOTE: email is enabled for this person but this script only "
                  "sends Slack. Send the email by hand, or use the Claude loop.")

        if not args.send:
            continue

        user_id = target.get("slack_member_id")
        if not user_id:
            lib.warn("{} has no slack_member_id, skipped".format(target["name"]))
            continue

        channel = open_dm(token, user_id)
        slack_post("chat.postMessage", token, {"channel": channel, "text": text})
        sent += 1

    if args.send:
        print("\nSent {} of {} Slack DMs.".format(sent, len(targets)))
    else:
        print("\nDRY RUN. {} messages would have been sent. Add --send to send them.".format(
            len(targets)
        ))


if __name__ == "__main__":
    main()
