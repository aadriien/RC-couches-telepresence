###############################################################################
##  `utils.py`                                                               ##
##                                                                           ##
##  Purpose: Utility helpers for parsing message fields and timestamps       ##
###############################################################################


from datetime import datetime, timezone


def get_message_contents(message):
    return message["content"] if message else ""


def get_message_timestamp_unix(message):
    return message["timestamp"] if message else None


def unix_timestamp_to_datetime(timestamp):
    if timestamp is None:
        return datetime.now(timezone.utc)
    return datetime.fromtimestamp(timestamp, tz=timezone.utc)


def mins_elapsed_since_message(message):
    if not message:
        return float('inf')
    
    time_now = datetime.now(timezone.utc)
    msg_timestamp_unix = get_message_timestamp_unix(message)
    msg_time = unix_timestamp_to_datetime(msg_timestamp_unix)

    time_diff = time_now - msg_time
    return time_diff.total_seconds() // 60


