"""ClawMemory: enterprise operational memory (powered by Doozie Cortex).
Stores SOPs, vendor behavior, past decisions, lessons learned."""
import json
import os
from typing import Dict, Any


class ClawMemory:
    def __init__(self, path: str = ".clawmemory.json"):
        self.path = path
        self.data: Dict[str, Any] = {"vendors": {}, "lessons": []}
        if os.path.exists(path):
            with open(path) as f:
                self.data = json.load(f)

    def learn(self, key: str, fact) -> None:
        self.data["lessons"].append({"key": key, "fact": fact})
        if key.startswith("vendor:"):
            vid = key.split(":", 1)[1]
            existing = self.data["vendors"].get(vid, {})
            existing.update(fact if isinstance(fact, dict) else {"note": fact})
            self.data["vendors"][vid] = existing
        self._save()

    def vendor_risk(self, vid: str) -> str:
        late = self.data["vendors"].get(vid, {}).get("late_deliveries", 0)
        if late >= 3:
            return "HIGH"
        if late >= 1:
            return "MEDIUM"
        return "LOW"

    def requires_finance(self, vid: str) -> bool:
        return self.vendor_risk(vid) in ("HIGH", "MEDIUM")

    def _save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)
