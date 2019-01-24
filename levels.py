from character import Character
from pewdiepie import *
from discord.ext.commands import Bot

import discord
import random


BOT_PREFIX = '+'
TOKEN = 'NTM1MzI0NTI5NTUyMTMwMDUw.DyU5qw.bm9vNkgcLMl0L0EuSh0qzsgKwmY'

client = Bot(command_prefix=BOT_PREFIX)
toons = {}

possible_responses = [
    " was just murdered to death...",
    " has just been murdered! Reports claim that the victim knew the assailant",
    " was their own worst enemy",
    " flew too close to the sun"
]


# TODO: Fix the implementation in pewdiepie file
@client.command(aliases=['pgay', 'pewdssubs', 'pewds'])
async def pewdiepie():
    sub_count = get_pewdiepie_subs()
    await client.say("Pewdiepie's sub count is: " + sub_count)


def is_parse(nickname):
    if not nickname:
        return False

    tag_nick = nickname.split(" ")
    if len(tag_nick) < 3:
        return False
    elif tag_nick[0] == 'Lvl':
        try:
            int(tag_nick[1])
            return True
        except ValueError:
            return False
    else:
        return False


# TODO: Address names longer than 24 characters
@client.event
async def on_ready():
    for server in client.servers:
        for member in server.members:
            if member == server.owner or member == client.user:
                continue
            elif member not in toons:
                if is_parse(member.nick):
                    tag_nick = member.nick.split(" ")
                    full_nick = " ".join(tag_nick[2:])
                    toons[member] = Character(full_nick, tag_nick[1])
                else:
                    toons[member] = Character(member.name, 1)
                await client.change_nickname(member, toons[member].tag_nick)


# TODO: Address names longer than 24 characters
@client.event
async def on_member_join(member):
    toons[member] = Character(member.name, 1)
    await client.change_nickname(member, toons[member].tag_nick)


@client.event
async def on_member_remove(member):
    temp_toon = toons.pop(member, None)
    del temp_toon


# checks if user is bot, or server owner
def valid_user(context):
    return not (context.message.author == client.user or
                context.message.author == context.message.server.owner)


@client.command(pass_context=True,
                name='changenickname',
                aliases=['changenick', 'change_nick', 'change_nickname'])
async def change_nickname(context, *args):
    if not valid_user(context):
        return

    author = context.message.author
    if not args:
        await client.say(author.mention + ", You Must pass in a nickname")
    elif args[0].startswith("Lvl") or args[0].startswith("lvl"):
        await client.say(author.mention + ", This nickname is invalid.")
    elif len(''.join(args)) > 24:  # 'Lvl [1-100] [...]' takes up max of 8 chars
        await client.say(author.mention + ", This nickname is too long")
    else:
        full_nick = " ".join(args)
        toons[author].update_nick(full_nick)

        await client.change_nickname(author, toons[author].tag_nick)
        await client.say(author.mention + " Your nickname is now: " +
                         toons[author].nick)


@client.command(pass_context=True,
                name="russianroulette",
                aliases=["rr", "russian_roulette", "russian"])
async def russian_roulette(context):
    if not valid_user(context):
        return
    author = context.message.author

    delta = -20 if random.randint(1, 6) == 6 else 3
    toons[author].update_level(delta)
    await client.change_nickname(author, toons[author].tag_nick)

    if delta == -20:
        await client.say(author.mention + random.choice(possible_responses))
    else:
        await client.say(author.mention + " gained 3 levels.")


client.run(TOKEN)
