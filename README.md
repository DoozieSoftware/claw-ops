# ClawOps v3.0 — Telegram-Native Operations Console

Telegram as SSH for enterprise operations. Run a company from your phone; ClawOps
executes the work and surfaces only the decisions that need human judgment.

## Run the MVP demo
```
cd clawops
python3 demo.py
```
The demo simulates the Telegram console (ConsoleTransport) and exercises three real
loops against mock ERP/Dev connectors:
1. Approve PO (with vendor-risk escalation to Finance)
2. Deploy a release (GitHub → Azure)
3. Resolve a customer ticket (Jira → PR → Deploy → Notify)

## Layout
See `docs/STRATEGY_v3.md`. Production swaps ConsoleTransport for TelegramTransport
(Bot API) and the mock connectors for TallyPrime / SAP B1 / Zoho / GitHub / Jira / M365.
