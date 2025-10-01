###############################################################################
##  `bridge.py`                                                              ##
##                                                                           ##
##  Purpose: Processes request pipeline to open couches bridge               ##
###############################################################################


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


