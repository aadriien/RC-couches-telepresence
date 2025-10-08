###############################################################################
##  `setup.py`                                                               ##
##                                                                           ##
##  Purpose: Creates a Zulip client instance for bot to operate              ##
###############################################################################


import os
import zulip
from dotenv import load_dotenv


load_dotenv()


def create_client():
    email = os.getenv("ZULIP_BOT_EMAIL")
    api_key = os.getenv("ZULIP_API_KEY")

    if not email or not api_key:
        raise ValueError("ZULIP_BOT_EMAIL and ZULIP_API_KEY must be set in .env")

    return zulip.Client(email=email, api_key=api_key)


def subscribe_to_all_public_streams(client):
    # Get all streams bot can see
    streams_response = client.get_streams()
    if streams_response["result"] != "success":
        raise RuntimeError(f"Failed to fetch streams: {streams_response}")

    # Get streams bot is already subscribed to
    subs_response = client.get_subscriptions()
    if subs_response["result"] != "success":
        raise RuntimeError(f"Failed to fetch subscriptions: {subs_response}")

    current_subs = {s["name"] for s in subs_response["subscriptions"]}

    # Only include streams bot isn't already subscribed to
    streams_to_subscribe = [
        {"name": stream["name"]}
        for stream in streams_response["streams"]
        if stream["name"] not in current_subs
    ]

    if streams_to_subscribe:
        add_resp = client.add_subscriptions(streams_to_subscribe)
        if add_resp["result"] != "success":
            raise RuntimeError(f"Failed to subscribe: {add_resp}")
        return [s["name"] for s in streams_to_subscribe]

    return []

