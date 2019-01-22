from character import Character

import discord
import random

from discord.ext.commands import Bot

BOT_PREFIX = '+'
TOKEN = 'NTM1MzI0NTI5NTUyMTMwMDUw.DyU5qw.bm9vNkgcLMl0L0EuSh0qzsgKwmY'

client = Bot(command_prefix=BOT_PREFIX)
toons = {}


# TODO: UNTESTED
@client.event
async def on_member_join(member):
    new_char = Character(member)
    toons[member] = new_char
    await client.change_nickname(member, new_char.level_tag + member.name)

# TODO: UNTESTED
@client.event
async def on_member_remove(member):
    temp_toon = toons[member]
    del toons[member]
    del temp_toon
    await client.say("Another one bites the dust")


# TODO: still raises an error when passed an empty string
@client.command(pass_context=True,
                name='changenickname',
                aliases=['changenick', 'change_nick', 'change_nickname'])
async def change_nickname(context, nick):
    author = context.message.author
    owner = context.message.server.owner
    if author == client.user:
        return
    elif nick.startswith("Lvl 1"):
        await client.say(author.mention + ", This nickname is invalid.")
    elif author == owner:
        await client.say(author.mention + ", a bot does not have permission " +
                         "to change a server owner's nickname.")
    else:
        await client.change_nickname(context.message.author, nick)
        await client.say(author.mention + "your nickname is now: " + nick)


# TODO: Add character functionality
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
        await client.say(author.mention + random.choice(possible_responses))
    else:
        await client.say(author.mention + " gained 3 levels.")


client.run(TOKEN)
