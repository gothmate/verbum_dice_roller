import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import random
from CONSTANTS import *

# Defina URLs das imagens para cada resultado
IMAGES = {
    "res1": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/1.png",
    "res2": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/2.png",
    "res3": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/3.png",
    "res4": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/4.png",
    "res5": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/5.png",
    "res6": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/6.png",
    "res7": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/7.png",
    "res8": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/8.png",
}

emoji_custom = "<:VerbumRPG:1158569919424774236>"
emotive = ":face_holding_back_tears:"

resp_falha = ["Ihhhh....", "Corre que deu ruim!", "Daí pra pior."]
resp_1_successo = ["Podia ser melhor.", "É, dá pro gasto.", "Entrou raspando."]
resp_2_successos = ["Se deu bem.", "Bom demais.", "A sorte está do seu lado."]
resp_3_successos = ["Melhor dos melhores.", "Vez ou outra, o universo se alinha.", "Esse resultado nunca mais... :O"]

intents = nextcord.Intents.default()
intents.members = True
intents.emojis = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("-----------------------------------------")

ServerID = 1270162128992600155

@client.slash_command(name='hello', description="Diz Olá", guild_ids=[ServerID])
async def hellocommand(interaction: Interaction):
    print(interaction.channel)
    await interaction.response.send_message(f'Olá.')

@client.slash_command(name='roll-nr4', description="rola 3 dados de 8 lados.")
async def rollcommand1(interaction: Interaction):

    username = interaction.user.name
    channel = interaction.channel

    firstDie = random.randint(1, 8)
    secondDie = random.randint(1, 8)
    thirdDie = random.randint(1, 8)

    sucessOne = sucess_decision(firstDie, 4)
    sucessTwo = sucess_decision(secondDie, 4)
    sucessThree = sucess_decision(thirdDie, 4)

    diceList = {
        "natural": [firstDie, sucessOne],
        "social": [secondDie, sucessTwo],
        "racional": [thirdDie, sucessThree],
    }

    numero_de_sucessos = contar_sucessos(diceList)
    resultado = select_response(numero_de_sucessos)

    # Criando os embeds com imagens diferentes
    embeds = []
    for key, value in diceList.items():
        embed = nextcord.Embed(
            title=f"Resultado NR-4 para {username} em #{channel}",
            description=f"{key}: {
                value[0]} - {f'Atingiu o N.R.  {emoji_custom}' if value[1] == True else f'Não atingiu o N.R. {emotive}'}",
            color=0x00ff00 if value[1] == True else 0xff0000
        )
        for key in IMAGES:
            if int(key[-1]) == value[0]:
                embed.set_image(url=IMAGES[key])
                embeds.append(embed)

    # Enviando os embeds
    for embed in embeds:
        print(f'{embed.title}')
        print(f'{embed.description}')
        await interaction.channel.send(embed=embed)

    # Enviando a mensagem final com o resultado
    print(f'\n{numero_de_sucessos} sucessos!\n{resultado}')
    await interaction.channel.send(
        f'{numero_de_sucessos} sucessos!\n{resultado}'
    )

@client.slash_command(name='roll-nr7', description="rola 3 dados de 8 lados.")
async def rollcommand2(interaction: Interaction):

    username = interaction.user.name
    channel = interaction.channel

    firstDie = random.randint(1, 8)
    secondDie = random.randint(1, 8)
    thirdDie = random.randint(1, 8)

    sucessOne = sucess_decision(firstDie, 7)
    sucessTwo = sucess_decision(secondDie, 7)
    sucessThree = sucess_decision(thirdDie, 7)
    
    diceList = {
        "natural": [firstDie, sucessOne],
        "social": [secondDie, sucessTwo],
        "racional": [thirdDie, sucessThree],
    }

    numero_de_sucessos = contar_sucessos(diceList)
    resultado = select_response(numero_de_sucessos)
        
    # Criando os embeds com imagens diferentes
    embeds = []
    for key, value in diceList.items():
        embed = nextcord.Embed(
            title=f"Resultado NR-7 para {username} em #{channel}",
            description=f"{key}: {value[0]} - {f'Atingiu o N.R. {emoji_custom}' if value[1]
                                               == True else f'Não atingiu o N.R. {emotive}'}",
            color=0x00ff00 if value[1] == True else 0xff0000
        )
        for key in IMAGES:
            if int(key[-1]) == value[0]:
                embed.set_image(url=IMAGES[key])
                embeds.append(embed)

    # Enviando os embeds
    for embed in embeds:
        print(f'{embed.title}')
        print(f'{embed.description}')
        await interaction.channel.send(embed=embed)

    # Enviando a mensagem final com o resultado
    print(f'\n{numero_de_sucessos} sucessos!\n{resultado}')
    await interaction.channel.send(
        f'{numero_de_sucessos} sucessos!\n{resultado}'
    )

@client.slash_command(name='roll-one', description="rola 1 dado de 8 lados.")
async def rollcommand3(interaction: Interaction):

    username = interaction.user.name
    channel = interaction.channel

    roll = random.randint(1, 8)

    if roll == 4 or roll == 8:
        sucess = True
    else:
        sucess = False

    msg = ''
    if sucess == True:
        msg = "Atingiu o N.R."
    else:
        msg = "Não atingiu o N.R."

    embed = nextcord.Embed(
        title="Resultado",
        description=f"O dado rolado por {username} em #{channel}, resultou em {roll} - {msg}",
        color=0x00ff00 if sucess == True else 0xff0000
    )
    for key in IMAGES:
        if int(key[-1]) == roll:
            embed.set_image(url=IMAGES[key])

    # Enviando os embeds
    await interaction.channel.send(embed=embed)

def contar_sucessos(dice_list):
    return sum(1 for result in dice_list.values() if result[1] == True)

def sucess_decision(die_result, dif):
    if die_result == dif or die_result == 8:
        return True
    else:
        return False
    
def select_response(sucessos):
    if sucessos == 0:
        res_aleatorio = random.randint(0, 2)
        resultado = resp_falha[res_aleatorio]
    if sucessos == 1:
        res_aleatorio = random.randint(0, 2)
        resultado = resp_1_successo[res_aleatorio]
    if sucessos == 2:
        res_aleatorio = random.randint(0, 2)
        resultado = resp_2_successos[res_aleatorio]
    if sucessos == 3:
        res_aleatorio = random.randint(0, 2)
        resultado = resp_3_successos[res_aleatorio]
        
    return resultado


client.run(BOT_TOKEN)
