from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "NTM1MzI0NTI5NTUyMTMwMDUw.DyLG1w.EX4XPY4lcNErdtwF3bxtnmPQl_4"

client = Bot(command_prefix=BOT_PREFIX)

client.run(TOKEN)