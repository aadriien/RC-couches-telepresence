###############################################################################
##  `bridge.py`                                                              ##
##                                                                           ##
##  Purpose: Processes request pipeline to open couches bridge               ##
###############################################################################


from src.notifier import send_dm, send_request_succeeded, send_request_failed 


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
        send_dm(False, sender_id, client)
    else:
        send_dm(True, sender_id, client)


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
        send_request_succeeded(mention_markdown, curr_stream_id, curr_subject, client)


