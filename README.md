# That's How Mafia Works Discord Bot
This is a project showcasing the leveling idea within a discord server. Players 
will earn levels that will be reflected within their nickname in the server.

## Getting Started
To run this on a local machine, simply invite the bot to a discord server and
run one of the commands listed below. If you already have a discord server you
can use, 
[Click here to add the bot to the server](https://discordapp.com/oauth2/authorize?client_id=535324529552130050&scope=bot&permissions=8).

**Note: This link gives the Bot admin privileges in your server, so make sure 
you know what you're doing.**

Otherwise, you're going to want to take a look at the prerequisites listed below.

### Prerequisites
This bot requires a previous understanding of the Discord client, and it
requires the ability to add a bot to a server. I won't get into it here, but you
can create an account and download the discord client on 
[Discord's Homepage](https://discordapp.com/).

Once your discord client is set up, You can create a brand new server and follow
the link listed above in order to add the bot to the server.

### Installation
This project utilizes the Discord API, along with BeautifulSoup4; You can
install them with the following commands at a terminal:
    
    python -m pip install discord.py

for discord, and
    
    python -m pip install beautifulsoup4

for BeautifulSoup4.

## Usage
This bot should dynamically respond to events within the server itself, such as 
new members joining the server, or members gaining levels. It should also
respond to commands with the '+' prefix:

There is a big exception when it comes to what the bot can do. Namely, most
of the functionality of the bot does not apply to server owners. This is because
server owners have the highest permissions within their server. A bot can 
therefore never overwrite a server owner's nickname or role. You can very easily
see why this interferes with the bot's functionality. If this is an issue for
you, I recommend adding a 3rd member, such as a friend or an alternate account,
to the server, and testing the bot through this new 3rd member.

### Examples

#### Russian Roulette
This command will randomly kill (-20 levels) the author who issued the 
command: 

![fail attempt](https://i.gyazo.com/1d53950b896b34022788bd4f0c773cb0.png 
"Better Luck Next Time")

or grant the author 3 levels: 

![success attempt](https://i.gyazo.com/f5a7f4ab50eaeefb0e8c7f19bf5739e7.png 
"Successful")

A death happens 1/6 of the time.


## License
This project is licensed under the MIT License. see the [LICENSE.md](LICENSE)
file for more details



