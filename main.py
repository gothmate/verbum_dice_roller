import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import random
from CONSTANTS import *

# Defina URLs das imagens para cada resultado
IMAGES = {
    "natural": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/d8.jpg",
    "social": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/d8.jpg",
    "racional": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/d8.jpg"
}

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("-----------------------------------------")

ServerID = 1270162128992600155

@client.slash_command(name='hello', description="Diz Olá", guild_ids=[ServerID])
async def hellocommand(interaction: Interaction):
    await interaction.response.send_message(f'Olá.')

@client.slash_command(name='roll-nr4', description="rola 3 dados de 8 lados.", guild_ids=[ServerID])
async def rollcommand(interaction: Interaction):
    firstDie = random.randint(1, 8)
    secondDie = random.randint(1, 8)
    thirdDie = random.randint(1, 8)

    if firstDie == 4 or firstDie == 8:
      sucessOne = True 
    else: 
      sucessOne = False
    if secondDie == 4 or secondDie == 8:
      sucessTwo = True 
    else: 
      sucessTwo = False
    if thirdDie == 4 or thirdDie == 8:
      sucessThree = True 
    else: 
      sucessThree = False

    diceList = {
        "natural": [firstDie, sucessOne],
        "social": [secondDie, sucessTwo],
        "racional": [thirdDie, sucessThree],
    }

    numero_de_sucessos = contar_sucessos(diceList)
    if numero_de_sucessos > 1:
        resultado = "Maravilha!!!"
    elif numero_de_sucessos == 1:
        resultado = "Foi bem."
    else:
        resultado = "Falhou miseravelmente."

    # Criando os embeds com imagens diferentes
    embeds = []
    for key, value in diceList.items():
        embed = nextcord.Embed(
            title=f"Resultado {key}",
            description=f"{key}: {value[0]} - {"Sucesso" if value[1] == True else "Falha"}",
            color=0x00ff00 if value[1] == True else 0xff0000
        )
        embed.set_image(url=IMAGES[key])
        embeds.append(embed)

    # Enviando os embeds
    for embed in embeds:
        await interaction.channel.send(embed=embed)
    
    # Enviando a mensagem final com o resultado
    await interaction.channel.send(
        f'{numero_de_sucessos} sucessos!\n{resultado}'
    )
    
@client.slash_command(name='roll-nr7', description="rola 3 dados de 8 lados.", guild_ids=[ServerID])
async def rollcommand(interaction: Interaction):
    firstDie = random.randint(1, 8)
    secondDie = random.randint(1, 8)
    thirdDie = random.randint(1, 8)

    if firstDie == 7 or firstDie == 8:
      sucessOne = True 
    else: 
      sucessOne = False
    if secondDie == 7 or secondDie == 8:
      sucessTwo = True 
    else: 
      sucessTwo = False
    if thirdDie == 7 or thirdDie == 8:
      sucessThree = True 
    else: 
      sucessThree = False

    diceList = {
        "natural": [firstDie, sucessOne],
        "social": [secondDie, sucessTwo],
        "racional": [thirdDie, sucessThree],
    }

    numero_de_sucessos = contar_sucessos(diceList)
    if numero_de_sucessos > 1:
        resultado = "Maravilha!!!"
    elif numero_de_sucessos == 1:
        resultado = "Foi bem."
    else:
        resultado = "Falhou miseravelmente."

    # Criando os embeds com imagens diferentes
    embeds = []
    for key, value in diceList.items():
        embed = nextcord.Embed(
            title=f"Resultado {key}",
            description=f"{key}: {value[0]} - {"Sucesso" if value[1] == True else "Falha"}",
            color=0x00ff00 if value[1] == True else 0xff0000
        )
        embed.set_image(url=IMAGES[key])
        embeds.append(embed)

    # Enviando os embeds
    for embed in embeds:
        await interaction.channel.send(embed=embed)
    
    # Enviando a mensagem final com o resultado
    await interaction.channel.send(
        f'{numero_de_sucessos} sucessos!\n{resultado}'
    )
    
@client.slash_command(name='roll-one', description="rola 1 dado de 8 lados.", guild_ids=[ServerID])
async def rollcommand(interaction: Interaction):
    roll = random.randint(1, 8)

    if roll == 4 or roll == 8:
      sucess = True 
    else: 
      sucess = False
    
    
    msg = ''
    if sucess == True:
        msg="Sucesso"
    else:
        msg="Falha"
        
    embed = nextcord.Embed(
        title=f"Resultado {roll}",
        description=f"O rolamento do dado resultou em {roll} - {msg}",
        color=0x00ff00 if sucess == True else 0xff0000
    )
    embed.set_image(url='https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/d8.jpg')

    # Enviando os embeds
    await interaction.channel.send(embed=embed)
    

def contar_sucessos(dice_list):
    return sum(1 for result in dice_list.values() if result[1] == True)

client.run(BOT_TOKEN)
