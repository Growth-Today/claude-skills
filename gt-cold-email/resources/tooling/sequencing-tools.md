# Sequencing Tool Recommendations
**Version:** 4.0
**Last updated:** April 9, 2026 · Maintained by [Brigitta Ruha](https://linkedin.com/in/brigittaruha)

---

## Email Sequencing (Automated Outbound)

| Tool | Best For | Volume | Preference |
|------|----------|--------|------------|
| **Emailbison** | High volume, sophisticated warmup, Clay HTTPS update | 1000s/day | ✅ Primary |
| **Instantly** | Ease of use, good deliverability | 1000s/day | ✅ Secondary |
| **SmartLead** | High volume, AI warmup | 1000s/day | Fallback |
| **Apollo** | All-in-one (data + sending) | Medium | Fallback |
| **Lemlist** | Multi-channel - see below | Medium | See multi-channel |

**Preference order:**
1. **Emailbison** - always start here
2. **Instantly** - if deviating from Emailbison
3. **SmartLead or Apollo** - last resort

### Why Emailbison is preferred

- **Warmup quality:** Emailbison has a high-volume, sophisticated email warmup that is significantly more stable than competitors. Because anyone can join Instantly or SmartLead, warmup pool quality varies by user - Emailbison's pool is more controlled.
- **Clay integration - live lead updates via HTTPS:** Emailbison supports updating leads via HTTPS at any point after they have entered a sequence. If you launch a campaign and realize a custom variable is missing or incorrect, you can update the lead in real time without re-importing. Instantly and SmartLead do not support this reliably once a lead is active in a sequence.
- **Easier to build on:** Emailbison is significantly simpler to develop against and maintain.

### Emailbison known limitation - inbox removal

If you remove email inboxes from a workspace while leads are active in a sequence, those leads will error out and cannot be re-prospected automatically. You would need to re-import them and manually determine which step each lead had reached. This does not happen with Instantly or SmartLead, which handle inbox removal more gracefully.

This is a rare scenario. If campaigns are planned carefully and deliverability hygiene is maintained, this will not be an issue in practice.

---

## LinkedIn Sequencing

| Tool | Best For | Preference |
|------|----------|------------|
| **HeyReach** | Automated LinkedIn outreach at scale | ✅ Primary |
| **Expandi** | LinkedIn automation | ✅ Primary |
| **Dripify** | LinkedIn sequences | Good alternative |

---

## Multi-Channel Sequencing

| Tool | Channels | Preference |
|------|----------|------------|
| **Lemlist** | Email + LinkedIn + WhatsApp | ✅ Primary |
| **LaGrowthMachine** | Email + LinkedIn + Twitter | Alternative |
| **Reply.io** | Email + LinkedIn + Calls | Alternative |

### Why Lemlist is preferred for multi-channel

- **AI voice notes:** Lemlist supports AI-generated voice notes natively - strong differentiator for multi-channel sequences.
- **Channel coverage:** Email + LinkedIn in one workflow, with WhatsApp now supported (2026).
- **Warmup included:** Email warmup is built in.
- **Cost efficiency (2026 pricing):** At $99/month per user, Lemlist includes 5 email inboxes + 1 LinkedIn account. If you only need LinkedIn sequencing, it is still $99 for 1 LinkedIn account per user - same price as LinkedIn-only tools like HeyReach. At higher volume, bulk options bring the per-user cost down further.

---

## Integration Pattern with Clay

**Emailbison (preferred)**

```
Clay Table
    ↓
[Add to Emailbison Campaign]
    ↓
Map variables:
- first_name → {{First Name}}
- last_name → {{Last Name}}
- email → {{Work Email}}
- first_line → {{AI First Line}}
- company → {{Company Name}}
- custom_1 → {{Use Case}}
- [any additional custom properties]
```

⚠️ **Important - Emailbison custom variables:**
Custom variables must be created manually in the client's Emailbison workspace before mapping from Clay. If the custom variable does not exist in the workspace, Clay cannot push data to it. Create all custom variables in Emailbison first, then map in Clay.

**SmartLead (alternative)**

```
Clay Table
    ↓
[Add to SmartLead Campaign]
    ↓
Map variables:
- first_name → {{First Name}}
- last_name → {{Last Name}}
- email → {{Work Email}}
- first_line → {{AI First Line}}
- company → {{Company Name}}
- custom_1 → {{Use Case}}
```

Note: SmartLead and Instantly create custom variables automatically when data is pushed from Clay. No manual setup needed.

---

## Cold Call Script (1 Minute - 5 Steps)

```
1. Pattern Interrupt Opening:
   "Hey {{firstName}}, this is [Name] from [Company]-
   I know I'm catching you out of the blue."

2. Permission-Based Transition:
   "Mind if I take 30 seconds to tell you why I called?
   Then you can decide if it's worth continuing."

3. Problem Statement:
   "I work with [ICP] who are struggling with [problem]."

4. Social Proof:
   "We just helped [similar company] achieve [result]."

5. CTA:
   "Is that something you're dealing with right now?"
```

## No-Show Phone Script

```
"Hey {{firstName}}, it's [Name] from [Company].

We had a call scheduled for [time]-
wanted to make sure everything's okay.

No worries if something came up.
Would [alternative time] work better?"
```

## Tone by Channel

**Agency Services:** Consultative, Strategic, Calm
**Accelerator:** Slang professional, Friendly, Curious
**Outbound Cold:** Pattern interrupt, Short, Clear

## Definition of Success
- Reply
- Conversation started
- Meeting booked

**NOT:** Long messages, Clever wording, Over-explaining, Sounding impressive

---

*Last updated: April 9, 2026 · Maintained by [Brigitta Ruha](https://linkedin.com/in/brigittaruha) · If you would like to reuse these skills or have any questions, connect with me on LinkedIn.*
