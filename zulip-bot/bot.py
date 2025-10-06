###############################################################################
##  `bot.py`                                                                 ##
##                                                                           ##
##  Purpose: Handles all setup & logic for Zulip couches-bridge bot          ##
###############################################################################


from src.setup import create_client
from src.notifier import send_notification


class CouchesBridgeBot:
    def __init__(self):
        self.client = create_client()

        # bot receives trigger
        # bot sends notification


if __name__ == "__main__":
    bot = CouchesBridgeBot()

    send_notification(bot.client)
