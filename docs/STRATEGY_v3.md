# ClawOps v3.0 — Telegram-Native Operations Console

## North Star
A founder can run an entire 100-person company from Telegram while traveling.
ClawOps executes the work and surfaces only the decisions that need human judgment.
**No laptop required.**

## Thesis
Telegram is **SSH for enterprise operations**. Not "ClawOps in Telegram" — Telegram
*as* the operating console.

```
Phone → Telegram → ClawOps → Business Systems (ERP, CRM, GitHub, Email, DB, Cloud)
```

## MVP (Phase 1)
Can a COO run company operations entirely from Telegram? If yes → product-market fit.
The web dashboard is Phase 2.

Build **one amazing loop**, not 30 packs:
1. Approve PO → Telegram → ClawOps → Tally/SAP → Done
2. Deploy Release → GitHub → Azure → Telegram notification
3. Customer Ticket → Jira → Root Cause → GitHub PR → Deploy → Notify Customer

## UX: everything is a card, not chat
Cards with buttons. Feels like GitHub Mobile + PagerDuty + Stripe Dashboard + Linear.
Command palette via `/`: Operations, Finance, HR, Procurement, Deployments, Reports,
Approvals, Incidents.

## Architecture
```
Telegram → Gateway → Core → Workflow Engine → Worker Runtime → Capabilities → Connectors
```

## Memory (ClawMemory™, powered by Doozie Cortex)
Every operation learns. Vendor "always late" → future POs require Finance approval.

## What we removed (v3.0)
Marketplace · Pricing · Website IA · Brand refresh · 30 packs · 100 capabilities.
Build a product people use every day.

## Repo layout
```
clawops/
  core/            gateway, orchestration
  tg/               cards, command palette, transport  (Telegram layer; dir is `tg/`
                     to avoid clashing with the upstream `telegram` Python library)
  command-center/  executive overview cards
  operations/      finance/ procurement/ devops/ hr/
  memory/          ClawMemory™ store
  connectors/      tally/ zoho/ github/ jira/ m365/ azure/
  workflow_engine/ operation loops
  worker_runtime/  capability execution
  capabilities/     approve_po, deploy, ticket, ...
  docs/
```
Everything revolves around operations.

## Unfair advantage
We already have ERP, Workflow, Approvals, Business Processes. That is much harder to
build than AI. Sai does not have it.
