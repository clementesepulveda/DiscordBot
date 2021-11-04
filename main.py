# bot.py
import os
from dotenv import load_dotenv
import discord
from nodos import NODOS # diccionario con id:Nodo


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
client_states = {}

async def describir_opciones(id_nodo):
    response = "```"+ NODOS[id_nodo].msg_entreda + "\n\n"

    if len(NODOS[id_nodo].next) != 0:
        response += "Opciones:\n"
        for i, path in enumerate(NODOS[id_nodo].next):
            response += f"  Opcion {i+1}: {path.option}\n"
    else:
        response += "Para jugar de nuevo usa el comando $jugar."

    return response + "```"


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name not in client_states:
        client_states[message.author.name] = -1 # para saber cuando juega o no


    if message.content.startswith("$instrucciones"):
        response = "```Instrucciones:\n" + \
                   "  $jugar: para empezar una nueva partida.\n" + \
                   "  $reiniciar: para reiniciar la partida que tienes.\n" + \
                   "  $repetir: tal vez no juegas desde varios días y necesitas saber donde habías quedado.\n" + \
                   "  $elegir X: cuando te den la opción de elegir, se usa este comando reemplazando X por la opción que desees.```"
    

    if message.content.startswith("$elegir"):
        if client_states[message.author.name] == -1:
            response = "```Necesitas empezar una partida primero, con el comando $jugar. " + \
                       "Para más instrucciones, ocupa el comando $instrucciones.```"

        else:
            try:
                opcion = int(message.content.split(' ')[1]) - 1

                if 0 <= opcion < len(NODOS[client_states[message.author.name]].next): # opcion valida
                    client_states[message.author.name] = NODOS[client_states[message.author.name]].next[opcion].id

                    response = await describir_opciones(client_states[message.author.name])

                    if len(NODOS[client_states[message.author.name]].next) == 0: # es termino de juego
                        client_states[message.author.name] = -1

                else: # opcion invalida
                    response = "```La opcion escrita no existe.```"
            except:
                response = "```Opcion elegida no es de la forma correcta. " + \
                           "Se tiene que escribir: $elegir X```"

    elif message.content.startswith("$jugar"):
        if client_states[message.author.name] == -1:
            client_states[message.author.name] = 0
            response = await describir_opciones(client_states[message.author.name])
        else: # ya esta en una partida
            response = "```Ya estas en una partida. Para saber donde quedaste ocupa el comando $repetir. " + \
                       "Para más instrucciones, ocupa el comando $instrucciones```"

    elif message.content.startswith("$reiniciar"):
        if client_states[message.author.name] == -1: # no se puede reiniciar si todavia no empieza
            response = "```Necesitas empezar una partida primero, con el comando $jugar. " + \
                        "Para más instrucciones, ocupa el comando $instrucciones.```"
        else:
            client_states[message.author.name] = 0
            response = await describir_opciones(client_states[message.author.name])

    elif message.content.startswith("$repetir"):
        if client_states[message.author.name] >= 0:
            response = await describir_opciones(client_states[message.author.name])
        else:
            response = "```Necesitas empezar una partida primero, con el comando $jugar. " + \
                       "Para más instrucciones, ocupa el comando $instrucciones```"

    await message.channel.send(response)



client.run(TOKEN)