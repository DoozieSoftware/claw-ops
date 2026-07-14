"""Mock Azure connector."""


class AzureConnector:
    def deploy(self, branch: str) -> dict:
        return {"branch": branch, "url": f"https://azure.example/{branch}", "status": "live"}
