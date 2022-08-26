import discord
from discord.ext import commands
import datetime

class Log(commands.Cog):
    def __init__(self, bot): 
        #Bot attribute
        self.bot = bot

        #Time tracking
        self.current_time = f'{datetime.datetime.now().time().strftime("%H:%M")}, {datetime.date.today().strftime("%m/%d/%Y")}'

    #Prints to console if cog loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Log cog loaded. ({self.current_time})')

    #Prints to console if someone joins the server and sends message
    @commands.Cog.listener()
    async def on_member_join(self, ctx, member):
        print(f'{member} has joined the server. ({self.current_time})')
        await ctx.send('hi <:HELLO:867210278369755167> @{member}')

    #Prints to console if someone leaves the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server. ({self.current_time})')

    @commands.command()
    async def status(self):
        print(f'Bot functioning.\n{self.bot.latency * 1000}ms')

#Cog setup
async def setup(bot):
    await bot.add_cog(Log(bot))