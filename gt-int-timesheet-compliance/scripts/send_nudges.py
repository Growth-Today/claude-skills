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


def human_list(items):
    """Mon / Mon and Tue / Mon, Tue and Wed."""
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return "{} and {}".format(", ".join(items[:-1]), items[-1])


def hours(value):
    """23 rather than 23.0, 17.5 rather than 17.50."""
    return "{:g}".format(round(float(value), 1))


def spoken_hours(value):
    """The amount as a person would say it out loud.

    "1.3 of 8 hours" is how a database reports a total. Nobody says it, and a
    message built out of it reads as machine-written however friendly the rest
    of the sentence is. Rounded to the nearest half hour, because the point is
    "you are well short", not accountancy to the minute.
    """
    half = round(float(value) * 2) / 2
    if half <= 0:
        return "nothing"
    if half < 1:
        return "under an hour"
    if half == 1:
        return "an hour"
    if half == 1.5:
        return "an hour and a half"
    whole = int(half)
    if half == whole:
        return "{} hours".format(whole)
    return "{} and a half hours".format(whole)


def describe(target, messages):
    """Return (problem sentence, the ask) matched to what is actually wrong.

    Four situations, three different asks. Days that were never filled in need
    filling in. A total that is short needs topping up. Hours that are all
    present but arrived days late need a different habit, and telling that
    person to catch up reads as a message nobody checked, because they have
    nothing to catch up on.
    """
    short_on_hours = target["logged_hours"] < target["expected_hours"]
    missing = target.get("missing_days_human") or []
    firm = target.get("escalation") == "firm"

    fields = {
        "logged": spoken_hours(target["logged_hours"]),
        "expected": hours(target["expected_hours"]),
        "missing": human_list(missing),
        "was_were": "was" if len(missing) == 1 else "were",
        "is_are": "is" if len(missing) == 1 else "are",
        "it_them": "it" if len(missing) == 1 else "them",
    }

    def pick(clause, ask):
        return (
            messages[clause].format(**fields),
            messages["cta_{}_{}".format(ask, "firm" if firm else "light")].format(**fields),
        )

    if missing and short_on_hours:
        # Nothing at all logged: the empty days say it, and adding "showing
        # nothing against 16 hours" on top is the sentence a report writes.
        if target["logged_hours"] <= 0:
            return pick("clause_nothing", "missing")
        return pick("clause_both", "missing")
    if missing:
        # Hours add up but the days are not covered, so they went in late.
        return pick("clause_days_only", "backfill")
    if short_on_hours:
        return pick("clause_hours_only", "hours")
    return pick("clause_fallback", "hours")


def fit_case(template, placeholder, text):
    """Match the clause's first letter to where the template puts it.

    The same clause has to work in both templates: it opens a sentence in the
    firm one ("Prosper, this is day 3. You're at 0 of 32 hours") and follows a
    comma in the light one ("Hi Gaze, your hours add up"). Without this you get
    "Hi Gaze, Your hours add up", which is exactly the kind of detail that makes
    a message read as machine-written.
    """
    marker = "{" + placeholder + "}"
    before = template.split(marker, 1)[0].rstrip()
    opens_sentence = not before or before.endswith((".", "!", "?", ":"))
    if opens_sentence:
        return text[:1].upper() + text[1:]
    return text[:1].lower() + text[1:]


def build_streak_phrase(target, messages):
    """A streak crosses weeks, so "day 10" reads like nonsense in a weekly nudge."""
    streak = target.get("weekdays_behind_in_a_row") or 1
    if streak > 5:
        return messages["streak_long"]
    return messages["streak_short"].format(streak=streak)


def compose(target, messages, link):
    template = messages.get(target["escalation"])
    if not template:
        lib.die(
            "No template for escalation level '{}' in config/messages.json".format(
                target["escalation"]
            )
        )
    problem, cta = describe(target, messages)
    # A clause can open with a substituted weekday name. Recasing that gives
    # "tue and Wed are still empty", so leave a word the data supplied alone.
    supplied = set((target.get("missing_days_human") or []) + [target["name"]])
    if problem.split(" ", 1)[0].strip(",.") not in supplied:
        problem = fit_case(template, "problem", problem)
    return template.format(
        name=target["name"],
        problem=problem,
        cta=cta,
        streak_phrase=build_streak_phrase(target, messages),
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
    not_counted = payload.get("not_counted_yet") or []

    if not_counted:
        # Says out loud why a run went quiet, so an empty list before go-live
        # reads as working rather than broken.
        print(
            "Not counted yet, no weekday this week is on or after the program "
            "start date: {}".format(len(not_counted))
        )
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
