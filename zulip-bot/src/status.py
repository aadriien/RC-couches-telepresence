###############################################################################
##  `status.py`                                                              ##
##                                                                           ##
##  Purpose: Checks couches bridge status to prevent duplicate requests      ##
###############################################################################


from src.notifier import (
    NOTICE_STREAM_ID, NOTICE_SUBJECT, 
    STATUS_KEYWORD,
    COUCHES_ACTIVE_NOTICE
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
        return result["messages"][0]["content"]
    return ""


def status_is_active(client, bot_user_id):
    msg_contents = fetch_latest_message(client, bot_user_id)
    return msg_contents == COUCHES_ACTIVE_NOTICE


