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
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    global guild
    guild = client.get_guild(0) # to be filled in later

# test command
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# on member join
@client.event
async def on_member_join(member):
    # await chat.send(f'{member} hath joined the fray')
    pass

# make channel
async def make_ticket(member):
    channel = await guild.create_text_channel('test',
                                              overwrites={
                                                  guild.default_role: discord.PermissionOverwrite(read_messages=False),
                                                  guild.me: discord.PermissionOverwrite(read_messages=True),
                                                  member: discord.PermissionOverwrite(read_messages=True)
                                              })

# truly start bot
client.run(token)
