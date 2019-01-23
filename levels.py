from character import Character

import discord
import random

from discord.ext.commands import Bot

BOT_PREFIX = '+'
TOKEN = 'NTM1MzI0NTI5NTUyMTMwMDUw.DyU5qw.bm9vNkgcLMl0L0EuSh0qzsgKwmY'

client = Bot(command_prefix=BOT_PREFIX)
toons = {}


@client.event
async def on_ready():
    for server in client.servers:
        for member in server.members:
            if member == server.owner or member == client.user:
                continue
            elif not member.nick:
                new_char = Character(member.name)
                toons[member] = new_char
                await client.change_nickname(member, toons[member].nick)
            elif member not in toons:
                new_char = Character(member.name)
                toons[member] = new_char
                await client.change_nickname(member, toons[member].nick)


@client.event
async def on_member_join(member):
    new_char = Character(member.name)
    toons[member] = new_char
    await client.change_nickname(member, toons[member].nick)


@client.event
async def on_member_remove(member):
    temp_toon = toons.pop(member, None)
    del temp_toon


@client.command(pass_context=True,
                name='changenickname',
                aliases=['changenick', 'change_nick', 'change_nickname'])
async def change_nickname(context, *args):
    author = context.message.author
    owner = context.message.server.owner
    if not args:
        await client.say(author.mention + ", You Must pass in a nickname")
    if author == client.user:
        return
    elif args[0].startswith("Lvl") or args[0].startswith("lvl"):
        await client.say(author.mention + ", This nickname is invalid.")
    elif author == owner:
        await client.say(author.mention + ", a bot does not have permission " +
                         "to change a server owner's nickname.")
    else:
        full_nick = ""
        for arg in args:
            full_nick += arg + ' '
        toons[author].update_nick(full_nick)
        await client.change_nickname(context.message.author, toons[author].nick)
        await client.say(author.mention + " Your nickname is now: " +
                         toons[author].nick)


@client.command(pass_context=True,
                name="russianroulette",
                aliases=["rr", "russian_roulette", "russian"])
async def russian_roulette(context):
    possible_responses = [
        " was just murdered to death...",
        " has just been murdered! Reports claim that the victim knew the "
        + "assailant",
        " was their own worst enemy",
        " flew too close to the sun"
    ]
    author = context.message.author
    if author == client.user:
        return;
    if random.randint(1, 6) == 6:
        toons[author].update_level(-20)
        await client.change_nickname(author, toons[author].nick)
        await client.say(author.mention + random.choice(possible_responses))
    else:
        toons[author].update_level(3)
        await client.change_nickname(author, toons[author].nick)
        await client.say(author.mention + " gained 3 levels.")


client.run(TOKEN)
