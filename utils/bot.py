import discord
from discord.ext import commands
from config import OWNERS, PREFIX, CHANNEL_ID, BACKEND_URL, BACKEND_PORT, BACKEND_ROUTE
import os
from pathlib import Path
import json
import re
import logging
import aiohttp


logger = logging.getLogger(__name__)

class UPLBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        super().__init__(
            owner_ids=OWNERS,
            command_prefix=PREFIX,
            intents=intents,
        )

        self.cogs_loaded = False
        

    async def setup_hook(self):
        await self.load_extensions('./cogs')
        self.cogs_loaded = True

    async def on_ready(self):
        print(f"Ready! {self.user.name} ID: {self.user.id}")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        
        await self.process_commands(message)
         
        if message.channel.id not in CHANNEL_ID:
            await message.channel.send(f"Cannot scrape from that channel id")

            return
        

        json_payload = {
            "content": message.content
        }

        try:
            async with aiohttp.ClientSession() as session:
                BASE_URL = f"http://{BACKEND_URL}:{BACKEND_PORT}"
                FULL_URL = f"{BASE_URL}/{BACKEND_ROUTE}"

                async with session.post(
                    FULL_URL,
                    json=json_payload
                ) as response:

                    if response.status == 201:
                        await message.channel.send("Event stored successfully ✅")
                    else:
                        text = await response.text()
                        await message.channel.send(f"Backend error: {text}")

        except aiohttp.ClientError as e:
            await message.channel.send(f"Failed to connect to backend: {e}")

        
    async def load_extensions(self, filename_):
        loaded = []
        not_loaded = {}
        i = 0
        total = 0

        for filename in Path(filename_).iterdir():
            if filename.suffix == '.py' and filename != "__init__.py":
                total += 1
                
                handle = f'{Path(filename_).name}.{filename.stem}'
                
                try:
                    await self.load_extension(handle)
                    loaded.append(handle)
                    i += 1
                except Exception as e:
                    not_loaded.update({handle: e})

        print(f"Loaded {i}/{total} extensions from {filename_}")
        return loaded, not_loaded
    
    