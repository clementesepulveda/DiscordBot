# bot.py
import os
import random

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
client_states = {}

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name not in client_states:
        client_states[message.author.name] = 0
        response = f"Lets start this journey, {message.author.name}"
        await message.channel.send(response)

    response = client_states[message.author.name]
    await message.channel.send(response)

client.run(TOKEN)