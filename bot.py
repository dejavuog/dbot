#Bot by DejaVu

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import os

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("ready when you are")
    print("i am running on " + bot.user.name)
    print ("with the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="This is all i know about this nigga.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)    

@bot.command()
@commands.has_role("Moderator")
async def spam(times : int, content=None):
    for i in range(times):
        await bot.say(content)

@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def delet(ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)

bot.run("process.env.BOT_TOKEN")
