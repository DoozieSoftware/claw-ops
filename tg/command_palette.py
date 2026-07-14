"""Command palette. Telegram menus are perfect for this (/)."""
from dataclasses import dataclass
from typing import List


@dataclass
class MenuItem:
    label: str
    action: str


def build_menu() -> List[MenuItem]:
    return [
        MenuItem("Operations", "menu:operations"),
        MenuItem("Finance", "menu:finance"),
        MenuItem("HR", "menu:hr"),
        MenuItem("Procurement", "menu:procurement"),
        MenuItem("Deployments", "menu:deployments"),
        MenuItem("Reports", "menu:reports"),
        MenuItem("Approvals", "menu:approvals"),
        MenuItem("Incidents", "menu:incidents"),
    ]


def render_menu() -> str:
    out = ["╔══ COMMAND PALETTE ═══════════╗", "Type / or tap a section:"]
    for it in build_menu():
        out.append(f"  /{it.label.lower():<11} → {it.action}")
    out.append("╚═════════════════════════════╝")
    return "\n".join(out)
