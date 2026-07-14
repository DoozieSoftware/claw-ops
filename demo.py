"""ClawOps v3.0 MVP demo — proves the COO can run operations from Telegram
(here simulated via ConsoleTransport). No laptop required.

Run:  python3 demo.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from tg.transport import ConsoleTransport
from tg.command_palette import render_menu
from memory.store import ClawMemory
from connectors.tally.connector import TallyConnector
from connectors.github.connector import GitHubConnector
from connectors.jira.connector import JiraConnector
from connectors.m365.connector import M365Connector
from connectors.azure.connector import AzureConnector
from core.gateway import Gateway
from workflow_engine.engine import po_loop, deploy_loop, ticket_loop


def banner(t: str) -> None:
    print("\n" + "=" * 42 + "\n" + t + "\n" + "=" * 42)


def main() -> None:
    memory = ClawMemory(path="/tmp/clawmemory.json")
    tally = TallyConnector()
    # ClawMemory learns vendor behavior from the ERP on first sync.
    for vid, v in tally.vendors.items():
        memory.learn(f"vendor:{vid}", {"late_deliveries": v["late_deliveries"]})

    ctx = {
        "memory": memory,
        "tally": tally,
        "github": GitHubConnector(),
        "jira": JiraConnector(),
        "m365": M365Connector(),
        "azure": AzureConnector(),
        "sample_po": {"id": "INV-4201", "vendor_id": "ABC", "amount": 248100},
        "sample_release": {"branch": "release-2.3"},
        "sample_ticket": {"id": "T-99", "summary": "Payment webhook 500", "customer_email": "cust@x.com"},
    }

    banner("COMMAND PALETTE  (Telegram  / )")
    print(render_menu())

    banner("LOOP 1 · Approve PO  (low-risk vendor)")
    card, res = po_loop(ctx, po_id="INV-4201")
    ConsoleTransport.present(card)
    print("→ ClawOps → Tally :", res)

    banner("LOOP 1b · Approve PO  (late vendor → Finance)")
    ctx["sample_po"] = {"id": "INV-5002", "vendor_id": "LATE", "amount": 320000}
    card, res = po_loop(ctx, po_id="INV-5002")
    ConsoleTransport.present(card)
    print("→ decision        :", res)
    if res["status"] == "escalated":
        print("→ Finance approves → ClawOps → Tally")
        final = ctx["tally"].approve_po(ctx["sample_po"])
        print("   ERP ref        :", final)
        memory.learn("vendor:LATE", {"flagged": "finance review"})

    banner("LOOP 2 · Deploy Release  (GitHub → Azure)")
    card, res = deploy_loop(ctx)
    ConsoleTransport.present(card)
    print("→ GitHub → Azure  :", res)

    banner("LOOP 3 · Customer Ticket  (Jira → PR → Deploy → Notify)")
    card, res = ticket_loop(ctx)
    ConsoleTransport.present(card)
    print("→ pipeline        :", res)

    banner("Gateway smoke test  (dispatch '/approvals')")
    gw = Gateway(ctx)
    out = gw.dispatch("menu:approvals")
    if isinstance(out, str):
        print(out)
    else:
        ConsoleTransport.present(out[0])
        print("→", out[1])

    banner("DONE · Founder ran the company from Telegram. No laptop required.")


if __name__ == "__main__":
    main()
