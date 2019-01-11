import discord
import asyncio
import youtube_dl
from discord.ext import commands
from discord.utils import find
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "-")


players = {}

@client.event
async def on_ready():
     print("Bot Ready")

@client.command(pass_context=True)
async def join(ctx):
     channel = ctx.message.author.voice.voice_channel
     await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
     server = ctx.message.server
     voice_client = client.voice_client_in(server)
     await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx):
     server = ctx.message.server
     voice_client = client.voice_client_in(server)
     player = await voice_client.create_ytdl_player('https://www.youtube.com/watch?v=1QQlUah25UI')
     players[server.id] = player
     player.start()

client.run(os.environ['BOT_TOKEN']) #do not post your bot token publically 
