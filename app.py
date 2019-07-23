# Work with Python xxx
import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from itertools import cycle

client = commands.Bot(command_prefix='!')
#client = discord.Client()

        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(os.getenv('BOT_TOKEN'))
