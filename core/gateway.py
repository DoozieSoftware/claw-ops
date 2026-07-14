"""Gateway: the single entry point from Telegram. Routes actions to workflows."""
from tg.command_palette import render_menu


class Gateway:
    def __init__(self, ctx: dict):
        self.ctx = ctx

    def dispatch(self, action: str):
        from workflow_engine.engine import po_loop, deploy_loop, ticket_loop

        a = (action or "").strip()
        if a in ("menu", "/", "menu:root", ""):
            return render_menu()
        if a == "menu:approvals" or a.startswith("approve_po"):
            pid = a.split(":", 1)[1] if ":" in a else None
            return po_loop(self.ctx, po_id=pid)
        if a == "menu:deployments" or a.startswith("deploy:"):
            branch = a.split(":", 1)[1] if a.startswith("deploy:") else None
            return deploy_loop(self.ctx, branch=branch)
        if a == "menu:incidents":
            return ticket_loop(self.ctx)
        return render_menu()
