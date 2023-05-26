import asyncio
import json
from datetime import datetime

from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import ChannelParticipantsSearch

from config import *

client = TelegramClient('session_name', API_ID, API_HASH)

client.start(PHONE_NUMBER)


async def get_channel_users():
    all_users = []

    chat_entity = await client.get_entity(CHAT_ID)
    participants = await client(GetParticipantsRequest(
        chat_entity, ChannelParticipantsSearch(''), offset=0, limit=200, hash=0))
    for user in participants.users:
        all_users.append(user)
    print(all_users)


async def main():
    await get_channel_users()


with client:
    client.loop.run_until_complete(main())
