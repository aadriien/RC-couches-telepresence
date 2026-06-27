###############################################################################
##  `status.py`                                                              ##
##                                                                           ##
##  Purpose: Checks couches bridge status to prevent duplicate requests      ##
###############################################################################


from datetime import datetime, timezone

from src.constants import (
    NOTICE_STREAM_ID, NOTICE_SUBJECT, 
    STATUS_KEYWORD,
    COUCHES_ACTIVE_NOTICE, COUCHES_CLOSED_NOTICE
)


def fetch_latest_message(client, bot_user_id):
    # Fetch bot's most recent message from specified channel / topic
    result = client.get_messages({
        "anchor": "newest",
        "num_before": 1,
        "num_after": 0,
        "narrow": [
            {"operator": "sender", "operand": bot_user_id},
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


def get_message_contents(message):
    return message["content"] if message else ""


def get_message_timestamp_unix(message):
    return message["timestamp"] if message else None


def unix_timestamp_to_datetime(timestamp):
    if timestamp is None:
        return datetime.now(timezone.utc)
    return datetime.fromtimestamp(timestamp, tz = timezone.utc)


def mins_elapsed_since_message(message):
    if not message:
        return float('inf')
    time_now = datetime.now(timezone.utc)
    msg_timestamp_unix = get_message_timestamp_unix(message)
    msg_time = unix_timestamp_to_datetime(msg_timestamp_unix)

    time_diff = time_now - msg_time
    return time_diff.total_seconds() // 60


def status_is_active(client, bot_user_id):
    msg = fetch_latest_message(client, bot_user_id)
    msg_contents = get_message_contents(msg)
    return msg_contents == COUCHES_ACTIVE_NOTICE


def status_is_closed(client, bot_user_id):
    msg = fetch_latest_message(client, bot_user_id)
    msg_contents = get_message_contents(msg)
    return msg_contents == COUCHES_CLOSED_NOTICE

