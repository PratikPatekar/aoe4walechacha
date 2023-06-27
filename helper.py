import discord
import os

'''
Creates a Bot Activity with message: name and type: type
'''
def createBotActivity(name):
    try:
        return discord.Activity(name=name, type=discord.ActivityType.playing)
    except Exception as e:
        #TODO: Log exceptions after implementing logger
        exception = f'{type(e).__name__}: {e}'
        print(exception)

'''
Async function to load all cogs before starting the Bot. This code runs whenever a bot is started

Get current directory -> os.path.realpath(os.path.dirname(__file__))
'''
async def loadAllCogs(client):

    for file in os.listdir(f'{os.path.realpath(os.path.dirname(__file__))}/cogs'):
        if file.endswith(".py"):
            fileName = file[:-3]
            try:
                await client.load_extension(f'cogs.{fileName}')
            except Exception as e:
                exception = f'{type(e).__name__}: {e}'
                print(exception)


