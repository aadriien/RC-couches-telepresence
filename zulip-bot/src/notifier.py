###############################################################################
##  `notifier.py`                                                            ##
##                                                                           ##
##  Purpose: Sends message to topic in channel notifying couch status        ##
###############################################################################


STREAM_ID = "test-bot" # channel (e.g. checkins)
SUBJECT = "RC-couches-telepresence-bridge" # topic (e.g. FirstName LastName)


def send_notification(client):
    couches_active_notice = "Couch bridge is active!"

    # Send a channel message
    client.send_message({
        "type": "stream",
        "to": STREAM_ID,
        "topic": SUBJECT,
        "content": couches_active_notice
    })


