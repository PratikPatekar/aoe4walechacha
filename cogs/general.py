import discord
from discord.ext import commands
from datetime import datetime
import requests

class General(commands.Cog, name="general"):
    '''
    Basic COG with simple commands like /help, /botinfo, /ping, /invite, /klingon, /yodaspeak, /piglatin, /cat, /joke etc
    '''

    def __init__(self,bot) -> None:
        self.bot = bot    

    @commands.hybrid_command(
            name='help', description='List of all available commands', with_app_command=True
    )
    async def help(self, context):
        embed = discord.Embed(
            title="Help", description="List of all available commands: "
        )
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            data = []
            for command in commands:
                description = command.description
                data.append(f'\n/{command.name} - {description}')
            final_text = '\n'.join(data)
            final_text+='\n'
            embed.add_field(
                name = i, value=f"'''{final_text}'''", inline=False
            )
        await context.send(embed=embed)

    @commands.hybrid_command(
            name='ping', description='To check if the Bot is responding or not', with_app_command=True
    )
    async def pong(self,context):
        await context.send(f'pong - {datetime.now()}')

    @commands.hybrid_command(
            name='joke', description='Want to hear a joke ?', with_app_command=True
    )
    async def joke(self,context):
        try: 
            response = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
            data = response.json()
            if data['status'] == 200:
                await context.send(f'{data["joke"]}')
            else:
                await context.send("Bhai joke kal padh lena")
        except Exception as e:
            self.bot.logger.error(f'Exception occured in joke command {e}')

    @commands.hybrid_command(
            name='cat', description='Pass any HTTP Error code as param', with_app_command=True
    )
    async def cat(self,context, errorCode):
        try:
            embed = discord.Embed()
            errorCode = errorCode.strip()
            embed.set_image(url=f'https://http.cat/{errorCode}')
            await context.send(embed=embed)
        except Exception as e:
            self.bot.logger.error(f'Exception occured in cat command {e}')

async def setup(bot):
    await bot.add_cog(General(bot))