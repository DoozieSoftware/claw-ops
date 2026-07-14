"""Telegram card primitive. Everything is a card, not chat."""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Button:
    label: str
    action: str            # e.g. "approve_po:INV-4201"
    style: str = "default"  # default | primary | danger


@dataclass
class Card:
    title: str
    subtitle: str = ""
    lines: List[str] = field(default_factory=list)
    buttons: List[Button] = field(default_factory=list)
    footer: str = ""

    def render(self) -> str:
        bar = "─" * 34
        out = [bar, self.title]
        if self.subtitle:
            out.append(self.subtitle)
        out.append(bar)
        for ln in self.lines:
            out.append(ln)
        out.append(bar)
        for i, b in enumerate(self.buttons, 1):
            mark = {"primary": "▶", "danger": "✖"}.get(b.style, "·")
            out.append(f"  [{i}] {mark} {b.label}")
        if self.footer:
            out.append(self.footer)
        out.append(bar)
        return "\n".join(out)
