import discord
from discord.ext import commands
import datetime
import os

#Variables
dir_path = os.path.dirname(os.path.realpath(__file__))
cog_path = os.path.join(dir_path, 'cogs')

bot = commands.Bot(command_prefix='!')

#Time tracking
current_time = f'{datetime.datetime.now().time().strftime("%H:%M")}, {datetime.date.today().strftime("%m/%d/%Y")}'

@bot.command()
async def load(extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(extension):
    bot.load_extension(f'cogs.{extension}')
    bot.unload_extension(f'cogs.{extension}')

@bot.event
async def on_ready():
    print(f'Bot activated ({current_time})')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Invalid command used.")


for file in os.listdir(cog_path):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')

#Unload voice_chat commands at startup
bot.unload_extension(f'cogs.voice_chat')

try:
    token_collect = open('config.txt')
    token = token_collect.readline()
except FileNotFoundError:
    token = os.environ["TOKEN"]

bot.run(token)