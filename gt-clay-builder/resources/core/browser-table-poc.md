# Build Clay Tables via Browser Automation - PoC Path (Experimental)

> **EXPERIMENTAL - GT internal advisory.** This is Growth Today's own experimental playbook for
> driving the Clay UI with browser automation to build a **table** when nothing else can. It is not
> production, it is not supported, and it must be attended by a human the whole time. Read the
> LIMITATIONS block before you start.

## When to reach for it

Only when **all** of these are true:
- You need a **TABLE** built fast for a client proof-of-concept.
- The CLI / API can't do it - tables are CLI/API **read-only**, so the terminal path cannot create
  or structure a table.
- The UI-by-hand route is too slow for the moment and the PoC is small.

If you only need a **workflow**, stop - use the CLI (`cli-and-api.md`), not this.

## Happy-path playbook

One action at a time. Do it, verify it landed, then take the next action.

1. **Create the table.**
2. **Add a small source** - a CSV upload, or Find People capped at ~10-25 rows. Keep it tiny.
3. **Add 1-2 enrichment columns** with input mapping (e.g. map domain into an email enrichment).
4. **(Optional) add one simple waterfall** - two providers, no more.
5. **Run** the enrichment on the capped rows.
6. **Read the results** back from the table.
7. **Export** the output.

After every single step, verify the UI actually did what you expected before moving on.

## LIMITATIONS (mandatory read)

- **Autocomplete dropdowns and multi-step modals are the #1 failure** - the automation picks the
  wrong option or the modal changes shape mid-flow.
- **Virtualized rows** - rows render on scroll, so off-screen rows may not exist in the DOM yet.
- **Long async waits with no reliable "done" signal** - enrichment finishes when it finishes, and
  there is no dependable indicator to poll.
- **Credit burn is real money with no rollback** - a wrong click can spend credits you can't get
  back.
- **Brittle to UI changes** - any Clay UI update can break the whole flow.
- **GT's assessment: ~50-75% reliability.** Slow, not production, and must be attended.

## Credit-safety guardrails

- Use **Clay Sandbox mode** where available.
- Turn table **auto-run OFF** before importing or adding columns.
- **Cap rows** (~10-25) - never point this at a full list.
- **Watch spend** the entire time.
- **No destructive clicks** - no delete, no bulk actions.

## Hard escalation rule

The moment this becomes recurring, high-volume, or billable, **stop and move to the CLI /
Workflows** (`cli-and-api.md`) or a manual UI build. This path is a one-off PoC crutch, never a
standing process.
