###############################################################################
##  `bridge.py`                                                              ##
##                                                                           ##
##  Purpose: Processes request pipeline to open couches bridge               ##
###############################################################################


from src.notifier import send_request_succeeded, send_request_failed


def process_request(msg_event, client):
    if msg_event["type"] != "message":
        return
    
    msg = msg_event["message"]
    
    # Determine message type (DM vs mention in channel)
    is_dm = msg["type"] == "private"
    is_mention = "mentioned" in msg_event.get("flags", [])

    if is_dm:
        print("message is DM!")

        print(msg_event)
        print(msg["content"])


    elif is_mention:
        print("message is mention!")

        print(msg_event)
        print(msg["content"])

        parse_message(msg, client)


def parse_message(msg, client):
    VALID_PROMPTS = [
        "open the portal",
        "open the couch portal",
        "open the bridge",
        "open the couch bridge"
    ]

    # Tag person who requested bridge to notify them of result
    user_to_mention = msg["sender_full_name"]
    mention_markdown = f"@**{user_to_mention}**"

    curr_stream_id, curr_subject = msg["stream_id"], msg["subject"]

    content = msg["content"].lower()

    if not any(prompt in content for prompt in VALID_PROMPTS):
        send_request_failed(mention_markdown, curr_stream_id, curr_subject, client)
    else:
        send_request_succeeded(mention_markdown, curr_stream_id, curr_subject, client)


