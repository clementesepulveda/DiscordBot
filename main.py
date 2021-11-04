# bot.py
import os
import random
import discord
from nodos import NODOS # diccionario con id:Nodo


load_dotenv()
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

    if message.content.startswith("$instrucciones"):
        response = "$instrucciones"+
                   "$jugar"+
                   "$reiniciar"+
                   "$repetir"
        await message.channel.send(response)
    elif message.content.startswith("$jugar"):
        if message.author.name not in client_states:
            client_states[message.author.name] = 0
            response = f"Lets start this journey, {message.author.name}"
            await message.channel.send(response)
    elif message.content.startswith("$reiniciar"):
        pass
    elif message.content.startswith("$repetir"):
        pass

    
    
    

client.run(TOKEN)