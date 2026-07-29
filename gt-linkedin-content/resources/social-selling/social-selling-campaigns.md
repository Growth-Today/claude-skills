# LinkedIn Social Selling Campaigns

This is how you turn the warm audiences your organic content creates into conversations and pipeline. It is the bridge from the content engine to revenue.

It is not cold outreach. Cold outreach to strangers (rented engine, anti-detect browsers, proxies, multi-account, cold connection requests) lives in the `gt-linkedin-outbound` skill, and that skill is the source of truth for it. Every audience here is warm: they viewed your profile, followed you, connected with you, or engaged with your posts. Content did the warming. This file is about catching that intent and starting a conversation.

## The four warm audiences

Every one of these is downstream of content. No content, no audience.

| Audience | What it is | How you pull it | Qualification + Scoring |
|---|---|---|---|
| **Content Engagers** | People who commented, liked, or reposted your posts (or a competitor's, or a thought leader's) | Scrape post engagers via API, or pull commenters straight into Expandi from a post URL | Always qualify the company and contact, scoring: optional |
| **Profile Viewers** | People who viewed your profile | Sales Navigator with "Viewed your profile recently" toggled on, refreshed into Expandi | Use Sales Navigator inclusion and exclusion logic to remove the irrelevant people |
| **Profile Followers** | People who started following your profile | LinkedIn Boolean search with "Follower of", pulled into Expandi or Aimfox | Use Sales Navigator inclusion and exclusion logic to remove the irrelevant people |
| **First-degree Connections** | Your existing 1st-degree network | Sales Navigator filtered to 1st-degree, messaged 1:1 and manually | Manual, you already know them |

## The three flows

### Flow 1: ICP buying-committee warm-up (optional, colder)
Proactively connecting with the buying committee at target ICP accounts. This is the one colder motion, and it competes with your other campaigns for LinkedIn's connection limit, so many teams leave it out. If you want to run it, use the `gt-linkedin-outbound` skill.

### Flow 2: Audience-based (conversation starter, no scoring)
New followers and profile visitors can't be qualified or scored up front, so you don't try. You start a conversation and let the reply tell you who is worth your time.

- **New followers** come from a Sales Navigator link with your personas set as filters, so the persona filters have to be right.
- **Profile visitors** come from an Expandi link. Expandi refreshes the list automatically every 3 days.
- Both get a conversation starter message via Lemlist. 
- When someone replies, the owner monitors it. If they qualify, the sales rep follows up and converts them for meetings. 

### Flow 3: Signal-based (you qualify and score)

- **Sources**, side by side: your own posts, competitor posts, and influencer or thought-leadership posts.
- Scrape these via [Clay](https://clay.com/?via=6fa548).
- **Qualify** everyone who engages: commenters, likers, reposters.
- **Enrich** their companies and **score** the contacts by buying role: influencer, champion, end user, or blocker.
- **Differentiate outreach by tier.** Tier 1 to 2 (high score) goes into an omnichannel Lemlist sequence and a rep works them directly. Tier 3 (lower score) goes into a lighter, email-based sequence.

## LinkedIn interaction limits

These are account-wide caps and they match the `gt-linkedin-outbound` skill. Breaching them is the fastest way to get an account restricted, so this is the most important rule on the page.

| Limit | Number |
|---|---|
| Connection requests per day (per account) | 15 to 20, hard cap |
| Connection requests per week | 100, LinkedIn's enforced ceiling |
| Profile changes per day | 1 (headline, company, photo, spread across days) |
| Account restriction rate to stay under | 5% per month |

Keep total daily activity (views, likes, comments, messages) conversational and spread through the day. Do not bulk-fire anything.

## Account warm-up

New or inactive accounts need a 2 to 3 week warm-up (14 to 21 days) before any automated outreach. During warm-up: accept connections, like, comment, and post manually. No automation. Ramp to full limits only after the account looks lived-in.

## Copywriting rules for conversation starters

1. Keep it to one short paragraph, 40 to 70 words at most. Shorter always wins.
2. No pitch in message one, ever. Its only job is to start a conversation.
3. Talk about them, not you. Use "you" and "your", not "I".
4. No flattery openers ("loved your post", "congrats on"). They kill the reply rate.
5. No emojis in outbound. They signal automation.
6. Read it aloud. If it doesn't sound like something you'd say to someone in person, rewrite it.
7. Match their tone: formal if their profile is formal, casual if they use contractions and humor.

## The conversation-starter sequence

Leave the connection request note **empty** for these warm audiences. Acceptance is equal or higher without a note, and the note burns your one chance to sound human before they've said yes.

Once connected:

**Message 1 (once connected):**
```
Good to connect.
I mostly post about [TOPIC]. Curious, was there a particular post of mine that brought you over?
```

**Message 2 (a few days later, if no reply):**
```
Anything I can help you with? Happy to be useful.
```

**Message 3 (last attempt):**
```
Figure this one slipped down the pile, no worries.

If email suits you better, I send practical [TOPIC] breakdowns here: [LINK]
```

After message 3, stop. Aggressive follow-up on LinkedIn wrecks your profile.

### Trigger-specific templates

Short, proven variants for specific signals. Fill in the `{{fields}}`.

**Profile Viewer Follow-Up** (warm reply rates run far above cold, roughly 28 to 35% vs 8 to 12%):
```
Hi {{first_name}}, saw you stopped by my profile.

Anything in particular you were after?
```

**Connection Acceptance Message:**
```
Appreciate the connect, {{first_name}}.

Out of curiosity, where does {{relevant_topic}} hurt most for you right now?
```

**Post Engager Follow-Up:**
```
Hi {{first_name}}, you reacted to my post on {{topic}}.

Is {{pain_point}} biting you over at {{company}}?
```

**Warm Intro Request:**
```
Hi {{first_name}}, looks like {{mutual_connection}} is a shared contact.

I have done some {{topic}} work with {{similar_company}}.

Would a short call be worth your time?
```

## Scheduling

- Weekdays only, Monday to Thursday best. Friday runs lower.
- Within the prospect's working hours, roughly 9 AM to 6 PM their time.
- At least one day off per week.
- Randomize timing between actions so the steps look human.

## Setup

The step-by-step build (Sales Navigator filters, Boolean strings, Expandi/Aimfox campaigns, QA checklists) sits outside this file, but three gotchas matter most: leave the connection-request note empty, allow duplicates on lead-magnet campaigns so every commenter gets the resource, and remember Expandi can only message people already connected to you (so every lead-magnet post says "make sure we're connected"). Rule of thumb: 10 to 15% of engagers are qualified, at most.

## Scoring with Clay (the upgrade)

Instead of messaging every profile viewer or engager the moment they act, capture them and score first. Treat repeat engagement as a rising score: the more often someone engages, the hotter they are. Then message them once they cross a threshold, or straight away if they are already a clear ICP fit. Clay enriches the company and scores the contact by buying role, which feeds the tiering in Flow 3. This spends your daily limits on the people most likely to convert.

## Tooling

| Tool | What it does here |
|---|---|
| **Sales Navigator** | The targeting layer. Persona and title filters, "Viewed your profile recently", 1st-degree filter. Also use "Posted within last 30 days" to target only active users and avoid wasting connection requests on dormant profiles. |
| **[Expandi](https://expandi.io/?red=linkedin1) / [Aimfox](https://aimfox.cello.so/rtLBroLjz9r)** | The automation layer for the four warm audiences. Holds the Boolean searches, the campaign inputs, connection-request steps, and the conversation-starter sequences. Pulls engagers straight from a post URL. |
| **[Clay](https://clay.com/?via=6fa548)** | Enrichment and scoring. Turns raw engagement into an engagement score and a role, so you message the right people at the right time. |
| **[Lemlist](https://get.lemlist.com/vn5ghzsrp9qi)** | The omnichannel sequence for Tier 1 to 2 in Flow 3 (LinkedIn plus email), worked alongside a rep. |

## What feeds this: lead magnets

Social selling only works if content keeps producing warm audiences. Post at least 5 times per week across ToF, MoF, and BoF. BoF lead magnets do double duty: they grow the follower base and give warm leads a reason to raise their hand. For the funnel breakdown by stage (angle, metric, CTA, frequency), see the funnel framework in `performance-playbook.md`.

---

*Created by [Growth Today](https://www.growthtoday.co), an AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
