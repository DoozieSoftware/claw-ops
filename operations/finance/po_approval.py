"""Finance operation: PO approval card + execution."""
from tg.cards import Card, Button
from capabilities.approve_po import approve_po


def po_card(po: dict, vendor_name: str) -> Card:
    return Card(
        title="Invoice Approval",
        subtitle=f"{po['id']} · {vendor_name}",
        lines=[
            f"Amount : ₹{po['amount']:,}",
            f"Matched: ✓ 3-way",
            f"Risk   : {po.get('risk', 'LOW')}",
        ],
        buttons=[
            Button("Approve", f"approve_po:{po['id']}", "primary"),
            Button("Reject", f"reject_po:{po['id']}", "danger"),
            Button("Open ERP", f"open_erp:{po['id']}"),
        ],
    )


def run_po_approval(po: dict, memory, tally):
    vendor = tally.get_vendor(po["vendor_id"])
    po["risk"] = memory.vendor_risk(po["vendor_id"])
    card = po_card(po, vendor["name"])
    result = approve_po(po, memory, tally)
    return card, result
