###############################################################################
##  `validator.py`                                                           ##
##                                                                           ##
##  Purpose: Validates couches bridge state to guard against noise           ##
###############################################################################


from src.constants import (
    COUCHES_ACTIVE_NOTICE, COUCHES_CLOSED_NOTICE, 
    COOLDOWN_MINS
)
from src.utils import (
    get_message_contents, 
    mins_elapsed_since_message
)


def status_is_active(zulip_client):
    msg = zulip_client.fetch_latest_message()
    contents = get_message_contents(msg)
    return contents == COUCHES_ACTIVE_NOTICE


def status_is_closed(zulip_client):
    msg = zulip_client.fetch_latest_message()
    contents = get_message_contents(msg)
    return contents == COUCHES_CLOSED_NOTICE


def was_recently_announced(zulip_client, status_check_fn, cooldown_mins=COOLDOWN_MINS):
    if status_check_fn(zulip_client):
        latest_msg = zulip_client.fetch_latest_message()
        mins_elapsed = mins_elapsed_since_message(latest_msg)
        return mins_elapsed < cooldown_mins
    return False


