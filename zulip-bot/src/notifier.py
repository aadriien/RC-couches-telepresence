###############################################################################
##  `notifier.py`                                                            ##
##                                                                           ##
##  Purpose: Sends message to topic in channel notifying couch status        ##
###############################################################################


NOTICE_STREAM_ID = "🧑‍💻 current batches" # channel (e.g. checkins)
NOTICE_SUBJECT = "Virtual couches co-working" # topic (e.g. FirstName LastName)

HUB_STREAM_ID = "397 Bridge"
HUB_SUBJECT = "RCTV Couches Telepresence"


# TESTING FOR NOW
# NOTICE_STREAM_ID = "test-bot" 
# NOTICE_SUBJECT = "RC-couches-telepresence-bridge" 

# HUB_STREAM_ID = "test-bot"
# HUB_SUBJECT = "RC-couches-telepresence-bridge"


ZOOM_LINK = "https://www.recurse.com/zoom/couches"
COUCHES_ACTIVE_NOTICE = f"Couch bridge is active! Join the zoom call: {ZOOM_LINK}"


def send_notification(notification_msg, stream_id, subject, client):

    # Send a channel message
    client.send_message({
        "type": "stream",
        "to": stream_id,
        "topic": subject,
        "content": notification_msg
    })


def send_request_succeeded(mention_markdown, curr_stream_id, curr_subject, client):
    hub_request_link = f"#**{HUB_STREAM_ID}>{HUB_SUBJECT}** "

    REQUEST_SUCCEEDED = (
        f"{mention_markdown} Hey there! Thanks for pinging me. "
        f"I'll send a request to folks at the hub over in {hub_request_link}"
    )

    send_notification(REQUEST_SUCCEEDED, curr_stream_id, curr_subject, client)

    # Prepare request to in-person hub folks (397 Bridge channel)
    mention_topic = "@**topic**"
    testing_spot = "#**test-bot>RC-couches-telepresence-bridge**"
    
    REQUEST_TO_HUB = (
        f"{mention_topic} Hey hub folks! "
        "The remote RCers would like to open the couches bridge for telepresence. "
        "Can you help them out? Activate the Zoom call on RCTV!"

        "\n\nI'm a new bot being tested in production. Feel free to say hello to me! "
        f"For more info, visit {testing_spot}"
    )

    send_notification(REQUEST_TO_HUB, HUB_STREAM_ID, HUB_SUBJECT, client)
    

def send_request_failed(mention_markdown, curr_stream_id, curr_subject, client):
    REQUEST_FAILED = (
        f"{mention_markdown} Sorry, I don't understand. "
        "If you would like to request a bridge with the hub couches, say "
        "\"Please open the portal\", or \"Please open the bridge\".\n\n"
        "Don't forget to tag me!"
    )

    send_notification(REQUEST_FAILED, curr_stream_id, curr_subject, client)

