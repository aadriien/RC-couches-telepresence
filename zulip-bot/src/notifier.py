###############################################################################
##  `notifier.py`                                                            ##
##                                                                           ##
##  Purpose: Sends message to topic in channel notifying couch status        ##
###############################################################################


# NOTICE_STREAM_ID = "🧑‍💻 current batches" # channel (e.g. checkins)
# NOTICE_SUBJECT = "Virtual couches co-working" # topic (e.g. FirstName LastName)

# HUB_STREAM_ID = "397 Bridge"
# HUB_SUBJECT = "RCTV Couches Telepresence"


# TESTING FOR NOW
NOTICE_STREAM_ID = "test-bot" 
NOTICE_SUBJECT = "RC-couches-telepresence-bridge" 

HUB_STREAM_ID = "test-bot"
HUB_SUBJECT = "RC-couches-telepresence-bridge"


HUB_REQUEST_LINK = f"#**{HUB_STREAM_ID}>{HUB_SUBJECT}** "

VIRTUAL_TAG = "@**topic**"
ZOOM_LINK = "https://www.recurse.com/zoom/couches"

COUCHES_ACTIVE_NOTICE = (
    f"{VIRTUAL_TAG} The couches bridge is **active**! " 
    f"Join the Zoom call: {ZOOM_LINK}"
)

COUCHES_ALREADY_ACTIVE = (
    f"The couches bridge is already **active**! " 
    f"Join the Zoom call: {ZOOM_LINK}"
)


# Prepare request to in-person hub folks (397 Bridge channel)
MENTION_TAG = "@*Currently at the hub*"
TESTING_SPOT = "#**test-bot>RC-couches-telepresence-bridge**"

REQUEST_TO_HUB = (
    f"{MENTION_TAG} Hey hub folks! "
    "The remote RCers would like to open the couches bridge for telepresence. "
    "Can you help them out? Activate the Zoom call on RCTV!"

    "\n\nI'm a new bot being tested in production. Feel free to say hello to me! "
    f"For more info, visit {TESTING_SPOT}"
)


def get_dm_text(is_successful):
    SUCCESS = (
        f"Hey there! Thanks for pinging me. "
        f"I'll send a request to folks at the hub over in {HUB_REQUEST_LINK}"
    )
    FAIL = (
        f"Sorry, I don't understand. "
        "If you would like to request a bridge with the hub couches, say "
        "\"Please open the portal\", or \"Please open the bridge\".\n\n"
    )

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


def send_announcement(client):
    send_notification(COUCHES_ACTIVE_NOTICE, NOTICE_STREAM_ID, NOTICE_SUBJECT, client)


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


