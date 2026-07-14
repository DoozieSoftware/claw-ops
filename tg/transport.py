"""Transports. ConsoleTransport simulates Telegram locally so the MVP is
runnable without a bot token. TelegramTransport is the production wiring."""
from tg.cards import Card


class ConsoleTransport:
    @staticmethod
    def present(card: Card) -> None:
        print(card.render())

    @staticmethod
    def present_text(text: str) -> None:
        print(text)


class TelegramTransport:
    """Production transport. Wire to the Telegram Bot API with a token.
    Not active in this environment (no TELEGRAM_BOT_TOKEN)."""

    def __init__(self, token: str):
        self.token = token

    def present(self, card: Card) -> None:
        raise NotImplementedError(
            "Set TELEGRAM_BOT_TOKEN and implement Bot API send (reply_markup inline keyboard)."
        )
