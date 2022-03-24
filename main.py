import discord
from discord.ext import commands
import music
from music import music_cog

cogs = [music]

client = discord.Client()
client = commands.Bot(command_prefix='+',intents = discord.Intents.all())

client.remove_command('help')

client.add_cog(music_cog(client))




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run('NzY3MTY5MzA2MjU3MTI5NTAz.X4uAFw.fRTl8aFK22TDwGdVRSr-HYWV9L0')