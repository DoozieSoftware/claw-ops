"""Worker Runtime: executes individual capabilities (the actions workers perform)."""


def execute(name: str, **kwargs):
    if name == "approve_po":
        from capabilities.approve_po import approve_po
        return approve_po(**kwargs)
    if name == "deploy_release":
        from capabilities.deploy import deploy_release
        return deploy_release(**kwargs)
    if name == "handle_ticket":
        from capabilities.ticket import handle_ticket
        return handle_ticket(**kwargs)
    raise ValueError(f"unknown capability: {name}")
