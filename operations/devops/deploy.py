"""DevOps operation: deployment card + execution."""
from tg.cards import Card, Button
from capabilities.deploy import deploy_release


def deploy_card(release: dict) -> Card:
    return Card(
        title="Production Deployment",
        subtitle=f"Branch {release['branch']}",
        lines=["Tests: ✓", "Risk : LOW"],
        buttons=[
            Button("Deploy", f"deploy:{release['branch']}", "primary"),
            Button("Cancel", f"cancel_deploy:{release['branch']}", "danger"),
        ],
    )


def run_deploy(release: dict, github, azure):
    card = deploy_card(release)
    result = deploy_release(release, github, azure)
    return card, result
