
import discord

from discord.ext.commands import Bot

BOT_PREFIX = '+'
TOKEN = 'NTM1MzI0NTI5NTUyMTMwMDUw.DyU5qw.bm9vNkgcLMl0L0EuSh0qzsgKwmY'

client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def init_level(before, after):
    await discord.on_member_update(before, after)
    client.change_nickname(after, "Lvl. 1 " + before.nick)


client.run(TOKEN)
