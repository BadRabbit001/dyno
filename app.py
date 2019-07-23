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
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('pass:88-unhide'):
        msg = 'Fuck you! I am hiding you dickhead!'.format(message)
        await message.channel.send(msg)
bot = commands.Bot(command_prefix = "!")

@bot.command(pass_context = True)
async def ban(member: discord.Member, days: int = 1):
    if "449706643710541824" in [role.id for role in message.author.roles]:
        await bot.ban(member, days)
    else:
        await bot.say("You don't have permission to use this command.")
       
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
