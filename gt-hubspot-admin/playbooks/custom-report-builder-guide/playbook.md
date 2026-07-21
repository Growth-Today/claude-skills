---
name: custom-report-builder-guide
description: "Use HubSpot's custom report builder correctly. Explains when to use each report type — single-object, cross-object, funnel, attribution, cohort — and how to build reliable reports that reconcile with source-of-truth data."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: reporting
---

# Custom Report Builder Guide

A practical guide to HubSpot's custom report builder: which of the five report types to use for which question, and how to build reports that leadership can trust. This is the how-to that `revops-core-dashboards` references.

## Why This Matters

The single most common reporting mistake is picking the wrong report type — trying to force a cross-object question into a single-object report, or hand-counting what a funnel report does automatically. Knowing the five types and when to use each is the difference between a report that reconciles with reality and one that quietly misleads.

## Prerequisites

- Access to Reports > Reports > Create custom report
- Governed, correctly-typed properties (`property-architecture-governance`)
- Clarity on the exact question the report must answer (write it down first)

## Critical Concept: The Five Report Types

| Type | Use it when you need… | Example |
|---|---|---|
| **Single-object** | Metrics from one object only | Deals by stage; contacts by source |
| **Cross-object** | Fields from related objects together | Deals with their company's industry |
| **Funnel** | Conversion + drop-off across ordered stages | Lifecycle or deal-stage funnel |
| **Attribution** | Which touches influenced a deal/revenue | Deal-create attribution by source |
| **Cohort** | Behavior of groups over time | Retention of customers by signup month |

Choosing the type is 80% of the work — start from the question, then pick the type that answers it natively.

## Plan

1. Write the exact question and the audience
2. Pick the report type from the table above
3. Build: choose object(s), filters, breakdowns, visualization
4. Validate the numbers against source-of-truth
5. Save to the right dashboard with the right sharing

## Execute

### Step 1: Start from the question
Write it as one sentence ("What is our SQL→Opportunity conversion rate by month?"). The verbs tell you the type — "conversion across stages" → funnel; "influenced by source" → attribution; "over time by group" → cohort.

### Step 2: Build the report
Reports > Create custom report > pick the type. Add the object(s), then filters (date range, pipeline, team), breakdowns (by owner, source, stage), and choose a visualization that fits (trend = line, comparison = bar, composition = funnel).

### Step 3: Common pitfalls to avoid
- **Wrong object as primary** in cross-object reports skews counts — the primary object determines what's being counted.
- **Date property choice matters** — "create date" vs "close date" vs "became a customer date" answer different questions.
- **Filters that silently exclude** — an unintended filter (e.g. one pipeline) makes totals look wrong.

### Step 4: Validate
Reconcile the report against a known number (e.g. total open pipeline in the deals index). If it doesn't match, check the primary object, date property, and filters before trusting it.

## After State

**Verification checklist:**

1. Each report uses the type that natively answers its question.
2. Reports reconcile with source-of-truth spot-checks.
3. Date properties and filters are deliberate and documented in the report description.
4. Reports are saved to the correct dashboard with appropriate sharing.
5. Attribution/cohort reports are only used where the tier supports them (some require Marketing Hub Enterprise).

## Key Technical Learnings

- **Question first, type second.** The five types map to five kinds of questions — match them.
- **Primary object + date property are the two silent error sources** in cross-object and time-based reports.
- **Always reconcile.** A report that doesn't match a known total isn't trustworthy yet.
- **Tier limits are real.** Revenue attribution and some cohort features need higher tiers — check before promising them.
- **Feeds `revops-core-dashboards`** — this is the how-to behind those dashboard tiles.
