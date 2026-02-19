import discord
from discord.ext import commands
from utils.bot import UPLBot
import sqlite3
from config import CHANNEL_ID

class Utility(commands.Cog):
    def __init__(self, bot: UPLBot):
        self.bot = bot
        self.scrape_channels = set()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addChannel(self, ctx, channelId: int):

        channel = self.bot.get_channel(channelId)

        if channel is None:
            await ctx.send('Could not find that channel.')
            return
        
        CHANNEL_ID.add(channelId)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removeChannel(self, ctx, channelId: int):

        channel = self.bot.get_channel(channelId)

        if channel is None:
            await ctx.send('Could not find that channel.')
            return
        
        CHANNEL_ID.discard(channelId)
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def currentChannels(self, ctx):
        
        if CHANNEL_ID is None:
            ctx.send('Currently no channels being scrapped')
            return

# We must add this line for every cog file we have
async def setup(UPLBot):
    await UPLBot.add_cog(Utility(UPLBot))

