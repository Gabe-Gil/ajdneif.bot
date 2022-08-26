from ast import alias
import discord
from discord.ext import commands
import datetime
import os
import random

#Dev Check
def is_dev(ctx):
    return (ctx.author.id == 147474616997117952) or (ctx.author.id == 661017764462461003)

class General_Commands(commands.Cog):
    def __init__(self, bot):
        #Bot Attribute
        self.bot = bot

        #Current time for tracking
        self.current_time = f'{datetime.datetime.now().time().strftime("%H:%M")}, {datetime.date.today().strftime("%m/%d/%Y")}'
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    #Print alert that cog is loaded when loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'General commands cog loaded. ({self.current_time})')

    #Delete a specific amount of previous chats, 2 if no value is entered
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.check(is_dev)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)
        await ctx.send("Messages have been cleared.", delete_after=5)

    #Sends a video
    @commands.command(aliases=['motivation'])
    async def helpineedmotivation(self, ctx):
        await ctx.send("https://youtu.be/wCIdQw95IJY")

    #Send random cat image
    @commands.command()
    async def cat(self, ctx):
        img_path = os.path.join(self.dir_path, 'pictures\cats')
        img = random.choice(os.listdir(img_path))
        new_img_path = os.path.join(img_path, img)
        
        await ctx.send(file=discord.File(new_img_path))

    #Send random good morning image
    @commands.command()
    async def morning(self, ctx):
        img_path =  img_path = os.path.join(self.dir_path, 'pictures\morning')
        img = random.choice(os.listdir(img_path))
        new_img_path = os.path.join(img_path, img)

        await ctx.send(file=discord.File(new_img_path))

    #Send timetostop image
    @commands.command()
    async def itstimetostop(self, ctx):
        img_path = os.path.join(self.dir_path, 'pictures\misc\\timetostop.jpg')
        await ctx.send(file=discord.File(img_path))

    #Send brexit image + emoji
    @commands.command(aliases=['brexit'])
    async def solutiontobrexit(self, ctx):
        img_path = os.path.join(self.dir_path, 'pictures\misc\\railroad.jpg')
        await ctx.send('<:BRIISHCHEWSDAYINNIT:867211267508404224>')
        await ctx.send(file=discord.File(img_path))

    #Send god's image
    @commands.command(aliases=['god'])
    async def faceofgod(self, ctx):
        img_path = os.path.join(self.dir_path, 'pictures\misc\\faceofgod.jpg')
        await ctx.send(file=discord.File(img_path))

    #Detailed guide on discord bot commands
    @commands.command()
    async def cmd(self, ctx):
        embed = discord.Embed(title="Detailed Bot Commands", url = "https://docs.google.com/document/d/1lNIdALf0oiO92fxNqEMkGQH6Qdqh_Gky3ZSZURYLTuk/edit", 
        description = "A list of detailed commands that this bot uses and how they work.", color = discord.Color.red())
        embed.set_author(name="Ajdneif.bot", icon_url="https://i.redd.it/qdkd046997571.png")
        embed.set_thumbnail(url="https://i.redd.it/qdkd046997571.png")
        await ctx.send(embed=embed)

    #Sends a pictures of an @'d users avatar
    @commands.command()
    async def avatar(self, ctx, *, user : discord.Member=None):
        if user == None:
            await ctx.send(ctx.author.avatar_url)
        else:
            userUrl = user.avatar_url
            await ctx.send(userUrl)

    #Sends a picture of the server icon
    @commands.command()
    async def icon(self, ctx):
        await ctx.send(ctx.guild.icon_url)

    #Grab a random online user in the server
    @commands.command(aliases=['roulette'])
    async def random(self, ctx):
        online_user_list = []

        for user in ctx.guild.members:
            if user.status == discord.Status.online and not user.bot:
                online_user_list.append(user)

        if online_user_list:
           selected = random.choice(online_user_list) 
           await ctx.send(selected)
        
        else:
            await ctx.send('Error: Nobody is online.')
    
    #For test use only
    #@commands.command()
    #async def test(self, ctx):
        #await ctx.send('hi <:HELLO:867210278369755167>')

#Cog setup
def setup(bot):
    bot.add_cog(General_Commands(bot))