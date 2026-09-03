---
name: github-actions
description: "Run the daily nudge and weekly digest unattended on GitHub Actions, with no organization Owner role and no local machine. Step by step, including the dry-run week before real messages go out."
license: MIT
metadata:
  author: growthtoday
  version: "1.0.0"
  category: internal-ops
---

# Running it on GitHub Actions

The point of this path: it reuses the scripts that already work. No logic gets rebuilt in a visual builder, so there is only ever one definition of "behind". It needs repo admin rather than an organization Owner, it costs nothing, and GitHub's runners have no egress restriction, so the proxy problem that blocks a cloud session does not exist here.

What you give up: the copy is templated. Claude writes a better nudge per person from the same numbers, and only Claude can turn a week of scores into "these hours were reconstructed on Friday night". The Actions path gets you the nudge and the table. Keep the review as a weekly paste into a session.

## What you need

- A **private** repository. The run logs print who is behind and by how much, so this cannot live in a public repo.
- Repo admin on it, to add secrets.
- The Asana token from `references/setup.md` step 2.
- A Slack app with a bot token.

## 1. Create the private repo and put the skill in it

Create `Growth-Today/gt-int-timesheet-compliance` as **private**, then put the contents of this skill folder at the repo root, so the paths are `scripts/`, `config/`, `requirements.txt`.

Two things to get right:

- **Commit `config/roster.json` here.** In the public monorepo it is gitignored for good reason. In a private repo it belongs in git, otherwise a runner has no roster. Delete the `config/roster.json` line from `.gitignore` when you move it, or the commit will silently skip it.
- **Keep `.env` gitignored.** The token goes in repo secrets, never in a file.

## 2. Create the Slack app

At api.slack.com/apps, **Create New App**, then **From a manifest**, pick the Growth Today workspace.

The paste box opens on a **JSON** tab with a pre-filled skeleton, and it has a **YAML** tab beside it. Two things go wrong here:

1. **Clear the box before pasting.** Pasting into the skeleton leaves its outer braces behind and the result parses as neither format.
2. **Match the file to the tab.** Paste `github-actions/slack-app-manifest.json` on the JSON tab, or `slack-app-manifest.yml` on the YAML tab. Both files describe the same app, so it makes no difference which you pick as long as they agree.

Use the manifest rather than **Blank app** (which is what Slack now calls the old "From scratch"). It sets the scopes for you, and a missing `im:write` is the single most common reason every DM fails at run time, hours after you thought you were finished.

The three scopes and what each one buys:

| Scope | Without it |
|---|---|
| `chat:write` | cannot send anything |
| `im:write` | cannot open a DM, so every nudge fails |
| `chat:write.public` | must invite the bot to a public channel before it can post there |

Then **OAuth & Permissions → Install to Workspace**, and copy the **Bot User OAuth Token** (starts with `xoxb-`).

**The approval gate is at Install, not at create.** A workspace that restricts app installation lets you build the app and then stops you here, so do not assume it worked until you are holding the token.

If the digest goes to a **private** channel, invite the bot to it: `/invite @Timesheet Nudge`. Private channels always require membership, whatever the scopes say.

## 3. Add the secrets

Repo **Settings → Secrets and variables → Actions → Secrets → New repository secret**:

| Secret | Value |
|---|---|
| `ASANA_ACCESS_TOKEN` | the Asana personal access token |
| `ASANA_WORKSPACE_GID` | the workspace whose entries you are scoring |
| `SLACK_BOT_TOKEN` | the `xoxb-` token |
| `SLACK_REPORT_CHANNEL` | channel ID for the weekly digest |
| `SLACK_ALERT_CHANNEL` | channel ID for failure alerts, your own DM is fine |
| `ROSTER_JSON` | optional, see below |

`ROSTER_JSON` is only needed if you did not commit `config/roster.json`. Paste the whole file content as the secret value. A committed file always wins over the secret, so setting both is harmless.

Channel IDs come from the channel's Slack URL, or from **View channel details** at the bottom.

## 4. Add the variables that keep it quiet

Same page, the **Variables** tab. These are not secrets, they are the send switches:

| Variable | Set it to | Meaning |
|---|---|---|
| `NUDGE_SEND` | `false` | daily nudge stays in dry run |
| `REPORT_SEND` | `false` | weekly digest stays in dry run |

**Leave both at `false` for the first week.** The workflows run on schedule, compute everything, and print exactly what they would have sent without sending it. That is the whole safety mechanism, and it costs you one week.

## 5. Add the workflows

Copy all three files from `github-actions/` in this skill to `.github/workflows/` in the private repo:

- `timesheet-verify.yml` (manual only, sends nothing, run this first)
- `timesheet-nudge.yml`
- `timesheet-weekly.yml`

They assume the skill sits at the repo root. If you nest it in a subfolder, change `working-directory` in each step.

## 6. Verify first, before anything else

Repo **Actions** tab → **Timesheet verify** → **Run workflow**. It is manual only, it sends nothing, and it is the cheapest way to prove the whole chain works. No local Python needed.

Read every line of the output, but especially this one:

```
PASS  team-wide visibility    entries from 6 of 6 submitters
```

If that says 1 of 6, the token only sees its own owner's time. Every team score built on it would be quietly wrong rather than visibly broken, so stop and fix the credential before going further. The same run also prints where time is currently attributed, which is the list that fills the attribution allowlist.

The second step of that workflow prints a dry-run nudge list, so you also get to read the actual message copy before a single DM exists.

## 7. Test the nudge by hand

**Actions** → **Timesheet nudge** → **Run workflow**. Tick **force** so it ignores the local-time window and shows you everyone who is behind, not just whoever is in their afternoon right now.

Open the run log and read the send step. You should see, per person: the escalation level, which nudge of the week it is, and the exact message text. Also check the two lines at the top: how many people were on track and left alone, and anyone silenced by the weekly cap.

Read the messages as if you had received one. This is the moment to fix the copy in `config/messages.json`, before anyone sees it.

Then do the same for **Timesheet weekly**. Its run also attaches `timesheet-scores` as an artifact: download it, that JSON is what you paste into a session for the real review.

## 8. Watch one week, then go live

Let both run on schedule for a week with the switches off. Check on Friday that the daily runs fired when expected and the message list looked sane each day.

Then set `NUDGE_SEND` and `REPORT_SEND` to `true`. Nothing else changes.

## The weekly rhythm once it is live

| When | What runs | What you do |
|---|---|---|
| Weekdays, local afternoon | nudge fires, DMs whoever is behind | nothing |
| Friday after the last cutoff | digest posts, JSON attached | download the artifact |
| Friday or Monday | | paste the JSON into a session for the pattern read, the coaching notes, and the draft to the leads if someone is persistently off process |
| Every second Monday | | ask for the gate report from the same data |

## Things that will bite

- **`missing_scope` from Slack.** The bot has `chat:write` but not `im:write`. Add it and reinstall the app; scope changes need a reinstall.
- **`channel_not_found` on the weekly digest.** The bot is not in that channel. Invite it.
- **A 403 from Asana on the time endpoints.** The token's owner cannot see other people's time. `verify_setup.py` counts distinct submitters and will tell you.
- **Cron runs late.** GitHub delays scheduled jobs under load. Your nudge window is a full hour, so a 15-minute delay is harmless, but do not expect minute precision.
- **A schedule on a repo with no recent commits.** GitHub can disable scheduled workflows in repositories that have been inactive for 60 days, and it emails the repo admins first. If nudges go quiet, check the Actions tab before assuming the code broke.
- **Two rosters.** If you commit `config/roster.json` and also set `ROSTER_JSON`, the file wins. Pick one and delete the other, or you will edit the wrong one in three months.

## Comparing this against the Claude Code path later

If an Owner adds the cloud credential, you can run both and compare. They read the same Asana data with the same scripts, so the numbers will match exactly. What differs is the writing: the templated DM against the one Claude composes, and the digest table against the actual review. Judge it on whether the messages get people to log their hours, because that is the only outcome that matters.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
