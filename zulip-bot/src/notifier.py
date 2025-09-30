###############################################################################
##  `notifier.py`                                                            ##
##                                                                           ##
##  Purpose: Sends message to topic in channel notifying couch status        ##
###############################################################################


STREAM_ID = "🧑‍💻 current batches" # channel (e.g. checkins)
SUBJECT = "Virtual couches co-working" # topic (e.g. FirstName LastName)


def send_notification(client):
    couches_active_notice = "Couch bridge is active!"

    # Send a channel message
    client.send_message({
        "type": "stream",
        "to": STREAM_ID,
        "topic": SUBJECT,
        "content": couches_active_notice
    })


