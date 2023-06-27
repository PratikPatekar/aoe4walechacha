import os
import discord
from dotenv import load_dotenv
import asyncio
from discord.ext.commands import Bot, Context
from helper import createBotActivity, loadAllCogs


'''
# TOKEN -> Discord Bot Token - Do not expose it, always use .env file for it
'''
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


'''
#Default Intents
'''
intents = discord.Intents.default()
intents.typing = False
intents.messages = True
'''
#Priviledged Intents - Need to be enabled from developer portal to work (Only enable if absolutely needed)
'''
intents.presences = True
intents.members = True
intents.message_content = True


'''
Defines Activity of the BOT (playing, streaming, watching etc)
'''
activity = createBotActivity('Hit me up using Slash Commands')


'''
Creating Bot/Client using discord.ext.commands.Bot Class
'''
client = Bot(
    intents=intents, 
    activity=activity, 
    command_prefix=None, 
    help_command=None
    )


'''
Events: START
'''

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    '''
    Executed every time someone sends a message (with/without prefix)
    :param message: The message that was sent
    '''
    print(f'Message from {message.author}: {message.content}')

#TODO: Implement on_commands_error

'''
Events: END
'''


client.load_extension
# asyncio.run(loadAllCogs(client))
client.run(TOKEN)
