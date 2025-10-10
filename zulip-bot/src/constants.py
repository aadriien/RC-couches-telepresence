###############################################################################
##  `constants.py`                                                           ##
##                                                                           ##
##  Purpose: Holds all immutable values for other scripts to reference       ##
###############################################################################


VALID_PROMPTS = [
    "open",
    "open portal",
    "open bridge",
    "open the portal",
    "open the bridge",
    "open the couch portal",
    "open the couch bridge",
    "open the couches portal",
    "open the couches bridge",
]

BOT_USER_ID = 971460


NOTICE_STREAM_ID = "🧑‍💻 current batches" # channel (e.g. checkins)
NOTICE_SUBJECT = "Virtual couches co-working" # topic (e.g. FirstName LastName)

HUB_STREAM_ID = "397 Bridge"
HUB_SUBJECT = "RCTV Couches Telepresence"

# # TESTING FOR NOW
# NOTICE_STREAM_ID = "test-bot" 
# NOTICE_SUBJECT = "RC-couches-telepresence-bridge" 

# HUB_STREAM_ID = "test-bot"
# HUB_SUBJECT = "RC-couches-telepresence-bridge"


HUB_REQUEST_LINK = f"#**{HUB_STREAM_ID}>{HUB_SUBJECT}** "


STATUS_EMOJI = ":test1:"
STATUS_KEYWORD = "**` STATUS: `**"
VIRTUAL_TAG = f"{STATUS_EMOJI} {STATUS_KEYWORD}"

OPEN, CLOSED = "OPEN", "CLOSED"

ZOOM_LINK = "https://www.recurse.com/zoom/couches"


COUCHES_ACTIVE_NOTICE = (
    f"---\n"
    f"{VIRTUAL_TAG}`-> {OPEN} `\n\n"
    f"The couches bridge is **active**! " 
    f"Join the Zoom call: {ZOOM_LINK}"
    f"\n---"
)

COUCHES_ALREADY_ACTIVE = (
    f"The couches bridge is already **active**! " 
    f"Join the Zoom call: {ZOOM_LINK}"
)

COUCHES_CLOSED_NOTICE = (
    f"---\n"
    f"{VIRTUAL_TAG}`-> {CLOSED} `\n\n"
    f"The couches bridge is now **closed**. " 
    f"To restore, simply tag me with a request to open the portal!"
    f"\n---"
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


SUCCESS = (
    f"Hey there! Thanks for pinging me. "
    f"I'll send a request to folks at the hub over in {HUB_REQUEST_LINK}"
)
FAIL = (
    f"Sorry, I don't understand. "
    "If you would like to request a bridge with the hub couches, say "
    "\"Please open the portal\", or \"Please open the bridge\".\n\n"
)


