"""Customer operation: ticket triage card + execution."""
from tg.cards import Card, Button
from capabilities.ticket import handle_ticket


def ticket_card(ticket: dict) -> Card:
    return Card(
        title="Customer Ticket",
        subtitle=ticket["summary"],
        lines=[f"Customer: {ticket['customer_email']}"],
        buttons=[Button("Triage", f"triage:{ticket['id']}", "primary")],
    )


def run_ticket(ticket: dict, jira, github, m365, deploy_fn):
    card = ticket_card(ticket)
    result = handle_ticket(ticket, jira, github, m365, deploy_fn)
    return card, result
