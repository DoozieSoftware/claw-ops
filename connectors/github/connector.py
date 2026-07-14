"""Mock GitHub connector."""


class GitHubConnector:
    def run_tests(self, branch: str) -> dict:
        return {"branch": branch, "tests": "PASS"}

    def create_pr(self, branch: str, title: str) -> dict:
        return {"pr": f"PR-#{(abs(hash(title)) % 9000) + 1000}", "branch": branch}
