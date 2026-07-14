"""Capability: approve a purchase order against the ERP."""
from memory.store import ClawMemory


def approve_po(po: dict, memory: ClawMemory, tally) -> dict:
    vid = po["vendor_id"]
    risk = memory.vendor_risk(vid)
    po["risk"] = risk
    # Human-in-the-loop: late vendors above threshold need Finance sign-off.
    if memory.requires_finance(vid) and po["amount"] > 100_000:
        return {"status": "escalated", "to": "finance", "risk": risk}
    res = tally.approve_po(po)
    memory.learn(f"vendor:{vid}", {"last_approved": po["id"]})
    return {"status": "approved", "erp": res}
