import argparse
import discord

# too lazy for if name = main... oh well!

# get file path for the bot token
parser = argparse.ArgumentParser()
parser.add_argument("token_path")
args = parser.parse_args()
try:
    with open(args.token_path, 'r') as token_file:
        global token
        token = token_file.read()
except:
    print("Unable to get token from file (did you pass the correct path?)")
    quit()

# start up bot and set intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# test command
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# truly start bot
client.run(token)
