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

At api.slack.com/apps, **Create New App**, From scratch, pick the Growth Today workspace.

Under **OAuth & Permissions**, add these **Bot Token Scopes**:

| Scope | Why |
|---|---|
| `chat:write` | send the messages |
| `im:write` | open a DM with a person |

Then **Install to Workspace** and copy the **Bot User OAuth Token** (starts with `xoxb-`).

For the weekly digest, invite the bot to the channel you want it posted in: `/invite @YourAppName` in that channel. A bot cannot post to a channel it is not in.

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
