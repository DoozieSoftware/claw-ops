"""Mock Jira connector."""


class JiraConnector:
    def create_ticket(self, summary: str) -> dict:
        return {"key": "INC-2042", "summary": summary}

    def root_cause(self, ticket: dict) -> dict:
        return {"cause": "Null pointer in payment webhook", "component": "billing-svc"}
