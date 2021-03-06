import discord
from discord.ext import commands
import music
from music import music_cog
import os
from dotenv import load_dotenv

cogs = [music]

client = discord.Client()
client = commands.Bot(command_prefix='+',intents = discord.Intents.all())

client.remove_command('help')

client.add_cog(music_cog(client))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run(os.environ.get("TOKEN"))