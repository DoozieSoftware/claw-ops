"""Workflow Engine: orchestrates the operation loops.
Core -> Workflow Engine -> Worker Runtime -> Capabilities -> Connectors"""
from operations.finance.po_approval import run_po_approval
from operations.devops.deploy import run_deploy
from operations.customer.ticket import run_ticket
from worker_runtime.runtime import execute


def po_loop(ctx: dict, po_id=None, auto=True):
    po = ctx.get("sample_po") or {"id": "INV-0001", "vendor_id": "ABC", "amount": 100000}
    return run_po_approval(po, ctx["memory"], ctx["tally"])


def deploy_loop(ctx: dict, branch=None):
    release = ctx.get("sample_release") or {"branch": "release-2.3"}
    return run_deploy(release, ctx["github"], ctx["azure"])


def ticket_loop(ctx: dict):
    ticket = ctx.get("sample_ticket") or {"id": "T-1", "summary": "issue", "customer_email": "c@x.com"}
    deploy_fn = lambda r: execute("deploy_release", release=r, github=ctx["github"], azure=ctx["azure"])
    return run_ticket(ticket, ctx["jira"], ctx["github"], ctx["m365"], deploy_fn)
