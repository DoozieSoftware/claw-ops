"""Mock Microsoft 365 / email connector."""


class M365Connector:
    def send_email(self, to: str, subject: str, body: str) -> dict:
        return {"sent": True, "to": to, "subject": subject}
