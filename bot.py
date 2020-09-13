import discord
from discord.ext import commands
from asyncio import sleep
import asyncio
import datetime
import colorsys
import random
import time

client = commands.Bot(command_prefix='!', help_command=None)


async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="#FullPotential"))
        await sleep(5)
        await client.change_presence(activity=discord.Game(name='!help for commands!'))
        await sleep(5)
        await client.change_presence(activity=discord.Game(name='coded by starrz'))
        await sleep(5)
        await client.change_presence(activity=discord.Game(name='! is the Prefix'))
        await sleep(5)
        await client.change_presence(activity=discord.Game(name='Moderating Potential!'))
        await sleep(5)

@client.event
async def on_ready():
    print(f'{client.user} is online! #FullPotential')
client.loop.create_task(status())

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(colour=discord.Colour(9633643), description=f'User {member.mention} **Has Been Kicked**, should of read the <#750741623524294687>')
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(colour=discord.Colour(9633643), description=f'User {member.mention} **Has Been Banned**, should of read the <#750741623524294687>')
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(colour=discord.Colour(9633643), description='Messages Have Been Deleted!')
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    embed = discord.Embed(colour=discord.Colour(9633643), description=f'This is my ping -> ({round(client.latency * 10000)})ms')
    await ctx.send(embed=embed)

@client.event
async def on_member_join(member):
   channel = discord.utils.get(member.guild.channels, name="welcome")
   embed = discord.Embed(colour=discord.Colour(0xd0fffd), description=f'User {member.mention} Welcome! to Team Potential! read the <#750741623524294687> to get set up!')
   embed.set_thumbnail(url=f"{member.avatar_url}")
   embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
   embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
   embed.timestamp = datetime.datetime.utcnow()

   await channel.send(embed=embed)

@client.command(pass_context = True)
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def dmall(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("'" + args + "' sent to: " + member.name)

            except:
                print("Couldn't send '" + args + "' to: " + member.name)

    else:
        await ctx.channel.send("A message was not provided.")

@client.command()
async def help(ctx):
	embed = discord.Embed(colour=discord.Colour(0xa1f8ff))
	embed.set_author(name="Help Command", icon_url="https://media.discordapp.net/attachments/750746233005408296/750789626070827179/exporta.png")
	embed.add_field(name="Moderation", value="`Ban > Bans the member | needs Ban Members Permission.`                              `Kick > Kicks the member | needs Kick Members Permission.`                            `Purge > Deletes an amount of messages | Manage Messages.`                         `Dmall > sends a message to everybody | Admin Perms needed.` `addrole > adds a desired role to somebody.` `rr > removes the role from somebody.`", inline=False)
	embed.add_field(name="Other", value="`Ping > Doing this command will tell the bot's MS.`                                  `Userinfo > Doing this command will tell info on the user.`                        `Help > You just did this command, you know what this does.`", inline=False)
	embed.add_field(name="Prefix", value="`Prefix is ! | Deal with it.`", inline=False)
	embed.timestamp = datetime.datetime.utcnow()
	await ctx.send(embed=embed)

@client.command()
async def addrole(ctx, role: discord.Role, user: discord.Member):
	if ctx.author.guild_permissions.administrator:
		await user.add_roles(role)
		embed = discord.Embed(colour=discord.Colour(0xd0fffd), description=f'Role Successfully Added {role.mention} from {user.mention}.')
		await ctx.send(embed=embed)

@client.command()
async def rr(ctx, role: discord.Role, user: discord.Member):
	if ctx.author.guild_permissions.administrator:
		await user.remove_roles(role)
		embed = discord.Embed(colour=discord.Colour(0xd0fffd), description=f'Role Successfully Revoked {role.mention} from {user.mention}.')
		await ctx.send(embed=embed)

@client.command()
async def poll(ctx, *, message):
	emb=discord.Embed(title="Poll", description=f"{message}")
	msg=await ctx.channel.send(embed=emb)
	await msg.add_reaction('👍')
	await msg.add_reaction('👎')

client.run('NzI1MTM3NjY1NDYwMjczMjAy.XvKXEw.NC8iq0sYFq-ZCrcXHp9CM6J42hQ')


