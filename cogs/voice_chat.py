import discord
from discord.ext import commands
import datetime
import youtube_dl
import os

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #Time tracking
        self.current_time = f'{datetime.datetime.now().time().strftime("%H:%M")}, {datetime.date.today().strftime("%m/%d/%Y")}'

    #Prints to console if cog loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Voice chat cog loaded. ({self.current_time})')

    #Connect then play video in general voice channel
    @commands.command()
    async def play(self, ctx, url : str):
        song = os.path.isfile('song.mp3')
        try:
            if song:
                os.remove('song.mp3')
        except PermissionError:
            await ctx.send("Stop the current song before playing a new one.")
            return False

        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
        await voiceChannel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                os.rename(file, 'song.mp3')
        
        voice.play(discord.FFmpegPCMAudio('song.mp3'))
    
    #Leave voice channel
    @commands.command()
    async def end(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice.is_connected():
            await voice.disconnect()

    #Pause video
    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            voice.pause()

    #Resume Video
    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice.is_paused():
            voice.resume()

    #Stop Video
    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        voice.stop()

#Cog setup
def setup(bot):
    bot.add_cog(Voice(bot))