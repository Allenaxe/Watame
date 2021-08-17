from discord import channel
from core.classes import Cog_Extension
import discord
from discord.ext import commands
import asyncio
import json
class MyClient(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        async def my_background_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(864699117028114435)
            while not self.bot.is_closed():
                
                await asyncio.sleep(900)
        self.bot.loop.create_task(my_background_task())

def setup(bot):
    bot.add_cog(MyClient(bot))

