###############################################################################
##  `bridge.py`                                                              ##
##                                                                           ##
##  Purpose: Processes request pipeline to open couches bridge               ##
###############################################################################


from src.status import status_is_active
from src.notifier import (
    COUCHES_ALREADY_ACTIVE, REQUEST_TO_HUB, HUB_STREAM_ID, HUB_SUBJECT,
    get_dm_text, send_dm, 
    send_notification,
    send_request_succeeded, send_request_failed
) 


VALID_PROMPTS = [
    "open the portal",
    "open the couch portal",
    "open the couches portal",
    "open the bridge",
    "open the couch bridge",
    "open the couches bridge",
]

BOT_USER_ID = 971460


def process_request(msg_event, client):
    if msg_event["type"] != "message":
        return
    
    msg = msg_event["message"]
    
    # Determine message type (DM vs mention in channel)
    is_dm = msg["type"] == "private"
    is_mention = "mentioned" in msg_event.get("flags", [])

    if is_dm:
        parse_dm(msg, client)

    elif is_mention:
        # Prevent infinite loop on itself
        if "wildcard_mentioned" in msg_event.get("flags", []):
            return
        parse_message(msg, client)


def parse_dm(msg, client):
    sender_id = msg["sender_id"]
    content = msg["content"].lower()

    # Sanity check that should never come up, but to be safe with looping
    if sender_id == BOT_USER_ID:
        return

    if not any(prompt in content for prompt in VALID_PROMPTS):
        #send dm to user telling them correct way to address bot
        send_dm(get_dm_text(False), sender_id, client)
    else:
        # Request is valid, now check if couches already active
        is_already_active = status_is_active(client, BOT_USER_ID)
        if not is_already_active: 
            #send a topic message to have hub people turn it on
            send_dm(get_dm_text(True), sender_id, client)
            send_notification(REQUEST_TO_HUB, HUB_STREAM_ID, HUB_SUBJECT, client)
        else:
            #send a dm to the user telling them it's already active with link
            send_dm(COUCHES_ALREADY_ACTIVE, sender_id, client)


def parse_message(msg, client):
    # Extra check to ensure bot doesn't loop on itself
    if msg["sender_id"] == BOT_USER_ID:
        return

    # Tag person who requested bridge to notify them of result
    user_to_mention = msg["sender_full_name"]
    mention_markdown = f"@**{user_to_mention}**"

    curr_stream_id, curr_subject = msg["stream_id"], msg["subject"]

    content = msg["content"].lower()

    if not any(prompt in content for prompt in VALID_PROMPTS):
        send_request_failed(mention_markdown, curr_stream_id, curr_subject, client)
    else:
        # Request is valid, now check if couches already active
        is_already_active = status_is_active(client, BOT_USER_ID)
        if not is_already_active: 
            send_request_succeeded(mention_markdown, curr_stream_id, curr_subject, client)


