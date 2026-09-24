---
name: n8n-subworkflows-loops
description: Build sub-workflows and batching loops in n8n for reuse, pagination, and rate limits. Use when the user asks about the Execute Workflow node or trigger, input modes, wait vs fire-and-forget, returning data from a sub-workflow, Loop Over Items, Split In Batches, pagination loops, rate limiting, or parallelization with $runIndex. Triggers on "Execute Workflow", "sub-workflow", "Loop Over Items", "Split In Batches", "batch size", "rate limit loop", "pagination loop", "$runIndex", "fire and forget", "return data". Do NOT use for trigger/webhook setup (use triggers-webhooks).
---

# n8n Sub-Workflows & Loops

You structure n8n workflows with reusable sub-workflows and batching loops for scale and rate limits.

## Instructions

1. Extract reusable logic into a sub-workflow with a clear input contract
2. Call it with Execute Workflow; choose wait-for-completion vs fire-and-forget
3. Return only what the parent needs from the sub-workflow's last node
4. Wrap high-volume or rate-limited work in Loop Over Items / Split In Batches

## Reference

For sub-workflow input modes and reusable patterns → Read `{SKILL_BASE}/resources/n8n-core-guide.md`
For workflow architecture decisions → Read `{SKILL_BASE}/resources/sub-skills/workflow-design.md`

## Patterns

| Pattern | Flow |
|---------|------|
| Reusable module | Parent → Execute Workflow (wait) → sub returns enriched item → continue |
| Fire-and-forget | Parent → Execute Workflow (no wait) → parent continues immediately |
| Rate-limited API | Loop Over Items (batch 10) → HTTP → Wait 1s → loop until done |
| Pagination | Loop → HTTP page `$runIndex` → IF has next → loop; else Merge results |
| Parallel fan-out | Split In Batches → parallel enrich branches → Merge |

## Key Principles

- **Sub-workflow = one job, one contract** - strict input fields make it reusable and testable
- **Wait vs fire-and-forget** - wait when you need the return value; fire-and-forget for side effects
- **Batch size 10 for most APIs** - small enough for rate limits, large enough for throughput
- **`$runIndex` drives pagination** - use it as the page offset inside the loop
- **Merge after fan-out** - recombine parallel branches before the final action

## Examples

Example 1: "Reuse my email-verification logic everywhere"
→ Build it as a sub-workflow (input `{ email }`, return `{ valid, provider }`) → call via Execute Workflow (wait)

Example 2: "Pull 5,000 records without hitting the rate limit"
→ Loop Over Items (batch 10) → HTTP page `$runIndex` → Wait → loop until no next page → Merge
