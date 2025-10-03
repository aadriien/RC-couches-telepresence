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
@click.option('--client', is_flag=True, help="Run in client mode")
@click.option('--server', is_flag=True, help="Run in server mode")
def launch_program(client, server):
    if client and server:
        click.echo("ERROR: You can't use --client and --server together")

    # Bot acts as a one-off script to send announcement for bridge opening
    elif client:
        click.echo("Running in client mode...")
        send_announcement(bot.client)

    # Bot acts as a server running 24/7 to listen for & respond to messages
    elif server:
        click.echo("Running in server mode...")
        bot.run()

    else:
        click.echo("ERROR: Please specify --client or --server")


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


