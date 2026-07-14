"""Mock TallyPrime connector. Swap for real Tally/XML-RPC or SAP B1 later."""


class TallyConnector:
    def __init__(self):
        self.approved = []
        self.vendors = {
            "ABC": {"name": "ABC Industries", "late_deliveries": 0},
            "LATE": {"name": "LateLogistics Pvt Ltd", "late_deliveries": 4},
        }

    def get_vendor(self, vid):
        return self.vendors.get(vid)

    def approve_po(self, po: dict) -> dict:
        self.approved.append(po)
        return {"ok": True, "erp_ref": f"TALLY-{po['id']}"}
