"""Command Center: assemble the executive overview cards."""
from tg.cards import Card, Button


def approvals_queue(pending: list) -> Card:
    lines = [f"  {p['id']} · {p['vendor']} · ₹{p['amount']:,}" for p in pending]
    return Card(
        title="Approvals Queue",
        subtitle=f"{len(pending)} pending",
        lines=lines or ["  (none)"],
        buttons=[Button("Review", "menu:approvals", "primary")],
    )


def operations_status(ops: list) -> Card:
    lines = [f"  {o['name']}: {o['status']}" for o in ops]
    return Card(title="Operations", lines=lines or ["  (none)"])
