from core.classes import Cog_Extension
import discord
from discord import channel
from discord.ext import commands
import random

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        self.channel = self.bot.get_channel(877045730836111361)
        if msg.author == self.bot.user or msg.channel != self.channel:
            return
        if (msg.content == '<:scissor:877097927259090964>' or msg.content == '<:stone:877098285725253662>' or msg.content == '<:paper:877097182442958848>') and msg.author != self.bot.user:
            game = ['<:scissor:877097927259090964>', '<:stone:877098285725253662>', '<:paper:877097182442958848>']
            robot = game[random.randint(0,2)]
            await msg.channel.send(robot)
            if (robot == '<:scissor:877097927259090964>' and msg.content == '<:scissor:877097927259090964>') or (robot == '<:stone:877098285725253662>' and msg.content == '<:stone:877098285725253662>') or (robot == '<:paper:877097182442958848>' and msg.content == '<:paper:877097182442958848>'):
                await self.channel.send('平手')
            elif (robot == '<:stone:877098285725253662>' and msg.content == '<:scissor:877097927259090964>') or (robot == '<:paper:877097182442958848>' and msg.content == '<:stone:877098285725253662>') or (robot == '<:scissor:877097927259090964>' and msg.content == '<:paper:877097182442958848>'):
                await self.channel.send('你輸了捏')
            elif (robot == '<:scissor:877097927259090964>' and msg.content == '<:stone:877098285725253662>') or (robot == '<:stone:877098285725253662>' and msg.content == '<:paper:877097182442958848>') or (robot == '<:paper:877097182442958848>' and msg.content == '<:scissor:877097927259090964>'):
                await self.channel.send('Watame才沒有錯呢')
     
def setup(bot):
    bot.add_cog(Event(bot))