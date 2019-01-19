
import random
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "NTM1MzI0NTI5NTUyMTMwMDUw.DyQKCQ.mPzAB06DcLNnMNmGAuM3_SrqhxE"

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.")
async def eight_ball():
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely'
    ]
    await client.say(random.choice(possible_responses))


client.run(TOKEN)
