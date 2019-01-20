import discord
import random

from discord.ext.commands import Bot

BOT_PREFIX = '+'
TOKEN = 'NTM1MzI0NTI5NTUyMTMwMDUw.DyU5qw.bm9vNkgcLMl0L0EuSh0qzsgKwmY'

client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_member_update(before, after):
    await client.change_nickname(after, None)


@client.command(pass_context=True,
                name="russianroulette",
                aliases=["rr", "russian_roulette", "russian"])
async def russian_roulette(context):
    possible_responses = [
        " was just murdered to death...",
        " has just been murdered! Reports claim that the victim knew the assailant",
        " was their own worst enemy",
        " flew too close to the sun"
    ]
    if context.message.author == client.user:
        return;
    shot = random.randint(1, 6)
    if shot == 6:
        await client.say(context.message.author.mention +
                         random.choice(possible_responses))
    else:
        await client.say(context.message.author.mention + " gained 3 levels.")


client.run(TOKEN)
