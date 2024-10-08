import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from functions import *
from CONSTANTS import *

IMAGES = {
    "natural": {
        "res1": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/amarelo/1.png",
        "res2": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/amarelo/2.png",
        "res3": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/amarelo/3.png",
        "res4": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/amarelo/4.png",
        "res5": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/amarelo/5.png",
        "res6": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/amarelo/6.png",
        "res7": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/amarelo/7.png",
        "res8": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/amarelo/8.png",
    },
    "social": {
        "res1": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/preto/1.png",
        "res2": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/preto/2.png",
        "res3": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/preto/3.png",
        "res4": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/preto/4.png",
        "res5": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/preto/5.png",
        "res6": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/preto/6.png",
        "res7": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/preto/7.png",
        "res8": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/preto/8.png",
    },
    "racional": {
        "res1": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/vermelho/1.png",
        "res2": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/vermelho/2.png",
        "res3": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/vermelho/3.png",
        "res4": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/vermelho/4.png",
        "res5": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/vermelho/5.png",
        "res6": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/vermelho/6.png",
        "res7": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/vermelho/7.png",
        "res8": "https://raw.githubusercontent.com/gothmate/verbum_dice_roller/dev/images/vermelho/8.png",
    }
    
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

@client.slash_command(name='roll-nr4', description="rola 3 dados de 8 lados.")
async def rollcommand1(interaction: Interaction):
    username = interaction.user.name
    channel = interaction.channel
    diceList = rollDice()
    numero_de_sucessos = contar_sucessos(diceList)
    embeds = []
    
    await interaction.channel.send(f"Resultado NR-4 para {username} em #{channel}")
    for key, value in diceList.items():
        if numero_de_sucessos == 0:
            nivel = 'Resultado Irrelevante'
        if numero_de_sucessos == 1:
            nivel = 'Resultado Medíocre'
        if numero_de_sucessos == 2:
            nivel = 'Resultado Satisfatório'
        if numero_de_sucessos == 3:
            nivel = 'Resultado Excepcional'

        embed = nextcord.Embed(
            title='',
            description=f"{key}: {
                value[0]} - {'Atingiu o N.R.' if value[1] == True else 'Não atingiu o N.R.'}",
            color=0x00ff00 if value[1] == True else 0xff0000
        )
        for chave in IMAGES[key]:
            if int(chave[-1]) == value[0]:
                embed.set_image(url=IMAGES[key][chave])
                embeds.append(embed)

    for embed in embeds:
       await interaction.channel.send(embed=embed)

    await interaction.channel.send(nivel)


@client.slash_command(name='roll-nr7', description="rola 3 dados de 8 lados.")
async def rollcommand1(interaction: Interaction):
    username = interaction.user.name
    channel = interaction.channel
    diceList = rollDice()
    numero_de_sucessos = contar_sucessos(diceList)
    embeds = []
    
    await interaction.channel.send(f"Resultado NR-7 para {username} em #{channel}")
    for key, value in diceList.items():
        if numero_de_sucessos == 0:
            nivel = 'Resultado Irrelevante'
        if numero_de_sucessos == 1:
            nivel = 'Resultado Medíocre'
        if numero_de_sucessos == 2:
            nivel = 'Resultado Satisfatório'
        if numero_de_sucessos == 3:
            nivel = 'Resultado Excepcional'

        embed = nextcord.Embed(
            title='',
            description=f"{key}: {
                value[0]} - {'Atingiu o N.R.' if value[1] == True else 'Não atingiu o N.R.'}",
            color=0x00ff00 if value[1] == True else 0xff0000
        )
        for chave in IMAGES[key]:
            if int(chave[-1]) == value[0]:
                embed.set_image(url=IMAGES[key][chave])
                embeds.append(embed)

    for embed in embeds:
       await interaction.channel.send(embed=embed)

    await interaction.channel.send(nivel)


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
        title="",
        description=f"O dado rolado por {username} em #{channel} {msg}",
        color=0x00ff00 if sucess == True else 0xff0000
    )
    for key in IMAGES['racional']:
        if int(key[-1]) == roll:
            embed.set_image(url=IMAGES['racional'][key])

    await interaction.channel.send(embed=embed)

client.run(BOT_TOKEN)
