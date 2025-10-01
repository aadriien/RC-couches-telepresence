###############################################################################
##  `bot.py`                                                                 ##
##                                                                           ##
##  Purpose: Handles all setup & logic for Zulip couches-bridge bot          ##
###############################################################################


from src.setup import create_client, subscribe_to_all_public_streams
from src.bridge import process_request
from src.notifier import send_notification


class CouchesBridgeBot:
    def __init__(self):
        self.client = create_client()

        self.subscribed_streams = subscribe_to_all_public_streams(self.client)

    def run(self):
        self.client.call_on_each_event(
            lambda msg_event: process_request(msg_event, self.client), 
            event_types=["message"]
        )

    # bot receives trigger
    # bot sends notification


if __name__ == "__main__":
    bot = CouchesBridgeBot()
    bot.run()

    # send_notification(bot.client)
    


