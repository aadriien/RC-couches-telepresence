###############################################################################
##  `bot.py`                                                                 ##
##                                                                           ##
##  Purpose: Handles all setup & logic for Zulip couches-bridge bot          ##
###############################################################################


import click # for args via CLI 

from src.setup import create_client, subscribe_to_all_public_streams
from src.bridge import process_request
from src.notifier import send_announcement


class CouchesBridgeBot:
    def __init__(self):
        self.client = create_client()

        self.subscribed_streams = subscribe_to_all_public_streams(self.client)

    def run(self):
        self.client.call_on_each_event(
            lambda msg_event: process_request(msg_event, self.client), 
            event_types=["message"]
        )


# Instantiate bot just once as a global so Click can access it 
bot = CouchesBridgeBot()


@click.command()
@click.option("--launch", is_flag=True, help="Run in client mode (launch)")
@click.option("--close", is_flag=True, help="Run in client mode (close)")
@click.option("--server", is_flag=True, help="Run in server mode")
def launch_program(launch, close, server):
    # Ensure only 1 mode specified
    flags = [launch, close, server]
    if sum(flags) != 1:
        raise click.UsageError("ERROR: You must provide exactly one of --launch, --close, or --server")

    # Bot acts as a one-off script (launch or close) to send announcement for bridge status
    if launch or close:
        mode = "--launch" if launch else "--close"
        click.echo(f"Running in client ({mode}) mode...")
        send_announcement(bot.client, mode)

    # Bot acts as a server running 24/7 to listen for & respond to messages
    elif server:
        click.echo("Running in server mode...")
        bot.run()

    else:
        raise click.UsageError("ERROR: Please specify --launch or --close or --server")


if __name__ == "__main__":
    # NOTES from 10/2/25 meeting:
    #   here within main, have CLI flags to pass to run script that allow you to
    #   either use it as the 24/7 bot OR otherwise as a one-off script to run..
    #   can use Python Click to pass CLI arguments
    # For example,
    #   `python3 bot.py --client`
    #   `python3 bot.py --server`
    # Or alternativey, just use Makefile rules
    #   `make run-client`
    #   `make run-server`

    launch_program()


