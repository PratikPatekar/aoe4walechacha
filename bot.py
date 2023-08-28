import os
import discord
from dotenv import load_dotenv
import asyncio
from discord.ext.commands import Bot, Context
from helpers import helper
import logging
import logging.handlers


'''
# TOKEN -> Discord Bot Token - Do not expose it, always use .env file for it
'''
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = os.getenv('COMMAND_PREFIX')

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
activity = helper.createBotActivity('Hit me up using Slash Commands')


'''
Creating Bot/Client using discord.ext.commands.Bot Class
'''
client = Bot(
    intents=intents, 
    activity=activity, 
    command_prefix=discord.ext.commands.when_mentioned_or(PREFIX), 
    help_command=None
    )

'''
Logging: START
'''

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes= 50*1024*1024,      #50 MiB
    backupCount=3                #Rotate through 3 files
)
dt_fmt = '%d-%m-%Y %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)
client.logger = logger

'''
Logging: END
'''


'''
Events: START
'''

@client.event
async def on_ready():
    client.logger.info(f'Logged in as {client.user.name}')

@client.event
async def on_message(message) -> None:
    '''
    Executed every time someone sends a message (with/without prefix)
    :param message: The message that was sent
    '''
    print(f'Message from {message.author}: {message.content}')
    client.logger.info(f'Message from {message.author}: {message.content}')
    if message.author == client.user or message.author.bot:
        return
    await client.process_commands(message)

#TODO: Implement on_commands_error

'''
Events: END
'''

asyncio.run(helper.load_cogs(client))
client.run(TOKEN, log_handler=None)
