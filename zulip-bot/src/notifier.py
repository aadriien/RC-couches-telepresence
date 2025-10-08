###############################################################################
##  `notifier.py`                                                            ##
##                                                                           ##
##  Purpose: Sends message to topic in channel notifying couch status        ##
###############################################################################


from src.constants import (
    NOTICE_STREAM_ID, NOTICE_SUBJECT,
    HUB_STREAM_ID, HUB_SUBJECT,
    HUB_REQUEST_LINK,
    COUCHES_ACTIVE_NOTICE, COUCHES_ALREADY_ACTIVE, 
    COUCHES_CLOSED_NOTICE,
    REQUEST_TO_HUB,
    SUCCESS, FAIL
)


def get_dm_text(is_successful):
    return SUCCESS if is_successful else FAIL


def send_dm(text_content, sender_id, client):
    # Send DM to user who reached out
    client.send_message({
        "type": "private",
        "to": [sender_id],
        "content": text_content
    })


def send_notification(notification_msg, stream_id, subject, client):
    # Send message to channel (stream_id)
    client.send_message({
        "type": "stream",
        "to": stream_id,
        "topic": subject,
        "content": notification_msg
    })


def send_announcement(client, type):
    valid_types = ["--launch", "--close"]
    if type not in valid_types: return 
    
    if type == "--launch":
        send_notification(COUCHES_ACTIVE_NOTICE, NOTICE_STREAM_ID, NOTICE_SUBJECT, client)
    elif type == "--close":
        send_notification(COUCHES_CLOSED_NOTICE, NOTICE_STREAM_ID, NOTICE_SUBJECT, client)


def send_request_succeeded(mention_markdown, curr_stream_id, curr_subject, client):
    REQUEST_SUCCEEDED = (
        f"{mention_markdown} Hey there! Thanks for pinging me. "
        f"I'll send a request to folks at the hub over in {HUB_REQUEST_LINK}"
    )

    # Confirmation for user, along with request to hub
    send_notification(REQUEST_SUCCEEDED, curr_stream_id, curr_subject, client)
    send_notification(REQUEST_TO_HUB, HUB_STREAM_ID, HUB_SUBJECT, client)
    

def send_request_failed(mention_markdown, curr_stream_id, curr_subject, client):
    REQUEST_FAILED = (
        f"{mention_markdown} Sorry, I don't understand. "
        "If you would like to request a bridge with the hub couches, say "
        "\"Please open the portal\", or \"Please open the bridge\".\n\n"
        "Don't forget to tag me!"
    )

    # Error message for user, with no further action
    send_notification(REQUEST_FAILED, curr_stream_id, curr_subject, client)


def send_request_aleady_active(mention_markdown, curr_stream_id, curr_subject, client):
    REQUEST_ALREADY_ACTIVE = f"{mention_markdown} {COUCHES_ALREADY_ACTIVE}"
    send_notification(REQUEST_ALREADY_ACTIVE, curr_stream_id, curr_subject, client)

