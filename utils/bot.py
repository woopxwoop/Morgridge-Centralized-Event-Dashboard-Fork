import discord
from discord.ext import commands
from config import OWNERS, PREFIX, CHANNEL_ID, BACKEND_URL, BACKEND_PORT, BACKEND_ROUTE, GEMINI_API_KEY
import os, sys
from pathlib import Path
import logging
import aiohttp
from google import genai

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import llmScraper

#import DiscordBot.utils.llmScraper


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
        self.geminiClient = genai.Client(api_key=GEMINI_API_KEY)

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
            return

        try:

            # Will be an empty list if no attachments
            media = {"media": [attachment.url for attachment in message.attachments]}

            response_json = await llmScraper.summarizer(self.geminiClient, message.content)
            response_json.update(media)

            json_payload = response_json

            async with aiohttp.ClientSession() as session:
                BASE_URL = f"http://{BACKEND_URL}:{BACKEND_PORT}"
                FULL_URL = f"{BASE_URL}/{BACKEND_ROUTE}"

                async with session.post(FULL_URL, json=json_payload) as response:
                    if response.status == 201:
                        pass
                    else:
                        text = await response.text()
                        logger.warning(f"Backend error: {text}") 


                        # await message.channel.send(f"Backend error: {text}")

            print(json_payload)
            
        except aiohttp.ClientError as e:
            #await message.channel.send(f"Failed to connect to backend: {e}")
            logger.warning(f"Failed to connect to backend: {e}") 
        except Exception as e:
            logger.warning(f"on_message error: {e}") 
        
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
    
    