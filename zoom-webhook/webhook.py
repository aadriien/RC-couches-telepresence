import asyncio
from rctogether import WebsocketSubscription

async def main():
    async for message in WebsocketSubscription():
        if message['type'] == 'Avatar' and message.get('zoom_user_display_name'):
            print(message['person_name'], message['zoom_user_display_name'])
    await main()
