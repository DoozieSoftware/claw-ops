"""Capability: resolve a customer ticket end-to-end."""


def handle_ticket(ticket: dict, jira, github, m365, deploy_fn) -> dict:
    inc = jira.create_ticket(ticket["summary"])
    rc = jira.root_cause(inc)
    pr = github.create_pr("fix/" + inc["key"], rc["cause"])
    deploy = deploy_fn({"branch": "fix/" + inc["key"]})
    notify = m365.send_email(
        ticket["customer_email"], f"Resolved {inc['key']}", "Fixed and deployed."
    )
    return {"incident": inc, "root_cause": rc, "pr": pr, "deploy": deploy, "notify": notify}
