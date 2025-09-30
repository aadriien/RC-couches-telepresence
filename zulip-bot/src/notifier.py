###############################################################################
##  `notifier.py`                                                            ##
##                                                                           ##
##  Purpose: Sends message to topic in channel notifying couch status        ##
###############################################################################


STREAM_ID = "🧑‍💻 current batches" # channel (e.g. checkins)
SUBJECT = "Virtual couches co-working" # topic (e.g. FirstName LastName)
ZOOM_LINK = "https://www.recurse.com/zoom/couches"


def send_notification(client):
    couches_active_notice = f"Couch bridge is active! Join the zoom call: {ZOOM_LINK}"

    # Send a channel message
    client.send_message({
        "type": "stream",
        "to": STREAM_ID,
        "topic": SUBJECT,
        "content": couches_active_notice
    })


