from src.character import Character
from src.pewdiepie import *

# Protected API Key
from src.config import TOKEN

from discord.ext.commands import Bot
from discord.utils import get
import discord
import random


BOT_PREFIX = '+'
client = Bot(command_prefix=BOT_PREFIX)

toons = {}

possible_responses = [
    " was just murdered to death...",
    " has just been murdered! Reports claim that the victim knew the assailant",
    " was their own worst enemy",
    " flew too close to the sun"
]
role_list = [discord.Color.red(), discord.Color.orange(), discord.Color.gold(),
             discord.Color.magenta(), discord.Color.purple(),
             discord.Color.blue()]


async def change_member_role(member):
    updated_role = get(member.server.roles, name=toons[member].meta_level)
    assert updated_role is not None
    await client.replace_roles(member, updated_role)


async def sort_members(server):
    for member in server.members:
        if member == server.owner or member == client.user:
            continue
        assert toons[member].level <= 100
        role = role_list[int(toons[member].level / 20)]
        await client.add_roles(member, role)


async def add_mafia_roles(server):
    # temporary lists used to organize role creation
    perms_list = [68608, 1121280, 3480640, 37084224, 49798209, 49798209]

    for i in range(6):
        perms_list[i] = discord.Permissions(permissions=perms_list[i])
        existing_role = get(server.roles, name=Character.titles[i])
        if existing_role is None:
            role_list[i] = await client.create_role(server,
                                                    name=Character.titles[i],
                                                    permissions=perms_list[i],
                                                    color=role_list[i],
                                                    hoist=True, position=i)
        else:
            role_list[i] = existing_role
    await sort_members(server)


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


async def create_characters(server):
    for member in server.members:
        if member == server.owner or member == client.user:
            continue
        elif member not in toons:
            if is_parse(member.nick):
                tag_nick = member.nick.split(" ")
                full_nick = " ".join(tag_nick[2:])
                toons[member] = Character(full_nick, tag_nick[1])
            else:
                nickname = "Name" if len(member.name) > 24 else member.name
                toons[member] = Character(nickname, 1)
            await client.change_nickname(member, toons[member].tag_nick)


@client.event
async def on_server_join(server):
    await create_characters(server)
    await add_mafia_roles(server)


@client.event
async def on_ready():
    for server in client.servers:
        await create_characters(server)
        await add_mafia_roles(server)


@client.event
async def on_member_join(member):
    nickname = "Name" if len(member.name) > 24 else member.name
    toons[member] = Character(nickname, 1)
    await client.change_nickname(member, toons[member].tag_nick)
    await change_member_role(member)


@client.event
async def on_member_remove(member):
    temp_toon = toons.pop(member, None)
    del temp_toon


@client.event
async def on_server_role_delete(role):
    if role in role_list:
        await client.create_role(role.server, name=role.name,
                                 permissions=role.permissions, color=role.color,
                                 hoist=True, position=role.position)
        # a loss of efficiency in sorting members in unaffected role
        await sort_members(role.server)


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
    author = context.message.author
    if not valid_user(context):
        return
    old_title = toons[author].meta_level

    # update character and server with new information
    delta = -20 if random.randint(1, 6) == 6 else 3
    toons[author].update_level(delta)
    if toons[author].meta_level != old_title:
        await change_member_role(author)

    await client.change_nickname(author, toons[author].tag_nick)
    if delta == -20:
        await client.say(author.mention + random.choice(possible_responses))
    else:
        await client.say(author.mention + " gained 3 levels.")


@client.command(aliases=['pewdssubs', 'pewds'])
async def pewdiepie():
    sub_count = get_pewdiepie_subs()
    await client.say("Pewdiepie's sub count is: " + sub_count)

client.run(TOKEN)
