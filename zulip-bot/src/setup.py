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



