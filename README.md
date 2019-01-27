# That's How Mafia Works Discord Bot
This is a project showcasing the leveling idea within a discord server. Players 
will earn levels that will be reflected within their nickname in the server.

## Getting Started
To run this on a local machine, clone it in a local repository with the 
following prerequisites:

### Prerequisites
This bot requires a previous understanding of the Discord client, and it
requires the ability to add a bot to a server. I won't get into it here, but you
download the discord client on [Discord's Homepage](https://discordapp.com/).

You can add the Bot to your Discord Server with the following link:
https://discordapp.com/oauth2/authorize?client_id=535324529552130050&scope=bot&permissions=8
(You'll need invite privileges to add the Bot to a server.)

**Note: This link gives the Bot admin privileges in your server, so make sure 
you know what you're doing.**

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
This project is licensed under the MIT License. see the [License.md](LICENSE)
file for more details



