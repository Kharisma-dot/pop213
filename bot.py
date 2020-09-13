import discord
from discord.ext import commands
import asyncio
import random
from discord.utils import get
import os

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Giving Out Nitro!", url='https://www.twitch.tv/discord'))
    print('Bot is online dip shit')
        
@client.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, "on_error"):
        return
    if isinstance(error, commands.CommandNotFound):
        return


@client.command()
async def announce(ctx, *, content):
    if ctx.author.id == 600863464977727498:
        not_sent = 0
        total_messaged = 0
        await ctx.send("Starting messaging.")
        for guild in client.guilds:
            for member in guild.members:
                if not member.bot:
                    try:
                        await member.send(content)
                        total_messaged += 1
                    except discord.HTTPException:
                        not_sent += 1
        await ctx.send(f"{total_messaged} have been messaged. {not_sent} have not been messaged (not enough permissions).")

client.run('NzQ0OTYwNzY5OTM4MTYxNjc0.Xzq0yA.wr7g_53NT6sYgtKyW0HLlYOaeFY')


