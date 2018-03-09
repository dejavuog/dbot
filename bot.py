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
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("the user name is: {}".format(user.name))
    await bot.say("the users ID is: {}".format(user.id))

@bot.command(pass_context=True)
async def embed(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="This Nigga.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)    

@bot.command()
async def repeat(times : int, content=None):
    for i in range(times):
        await bot.say(content)

bot.run("process.env.BOT_TOKEN")
