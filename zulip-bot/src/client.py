###############################################################################
##  `client.py`                                                              ##
##                                                                           ##
##  Purpose: Wraps Zulip API interactions into a single client class         ##
###############################################################################


from src.constants import (
    BOT_USER_ID,
    NOTICE_STREAM_ID, NOTICE_SUBJECT, STATUS_KEYWORD
)


class ZulipClient:
    def __init__(self, client):
        self.client = client
        self.bot_user_id = BOT_USER_ID

    def send_dm(self, text_content, recipient_id):
        # Send DM to user who reached out
        self.client.send_message({
            "type": "private",
            "to": [recipient_id],
            "content": text_content
        })

    def send_notification(self, notification_msg, stream_id, subject):
        # Send message to channel (stream_id)
        self.client.send_message({
            "type": "stream",
            "to": stream_id,
            "topic": subject,
            "content": notification_msg
        })

    def fetch_latest_message(self):
        # Fetch bot's most recent message from specified channel / topic
        result = self.client.get_messages({
            "anchor": "newest",
            "num_before": 1,
            "num_after": 0,
            "narrow": [
                {"operator": "sender", "operand": self.bot_user_id},
                {"operator": "channel", "operand": NOTICE_STREAM_ID},
                {"operator": "topic", "operand": NOTICE_SUBJECT},
                {"operator": "search", "operand": STATUS_KEYWORD},
            ],
            "apply_markdown": False
        })

        # Stored as array of message objects, so get 0th
        if result.get("messages"):
            return result["messages"][0]
        return {}

    def subscribe_to_all_public_streams(self):
        # Get all streams bot can see
        streams_response = self.client.get_streams()
        if streams_response["result"] != "success":
            raise RuntimeError(f"Failed to fetch streams: {streams_response}")

        # Get streams bot is already subscribed to
        subs_response = self.client.get_subscriptions()
        if subs_response["result"] != "success":
            raise RuntimeError(f"Failed to fetch subscriptions: {subs_response}")

        current_subs = {s["name"] for s in subs_response["subscriptions"]}

        # Only include streams bot isn't already subscribed to
        streams_to_subscribe = [
            {"name": stream["name"]}
            for stream in streams_response["streams"]
            if stream["name"] not in current_subs
        ]

        if streams_to_subscribe:
            add_resp = self.client.add_subscriptions(streams_to_subscribe)
            if add_resp["result"] != "success":
                raise RuntimeError(f"Failed to subscribe: {add_resp}")
            return [s["name"] for s in streams_to_subscribe]

        return []

    def call_on_each_event(self, callback, event_types):
        self.client.call_on_each_event(callback, event_types=event_types)


