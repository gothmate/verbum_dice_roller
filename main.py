import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import random

from CONSTANTS import *

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("-----------------------------------------")

testingServerID = 1270162128992600155

@client.slash_command(name='hello', description="Diz Olá", guild_ids=[testingServerID])
async def hellocommand(interaction: Interaction):
    await interaction.response.send_message(f'Olá.')

@client.slash_command(name='roll', description="rola 3 dados de 8 lados.", guild_ids=[testingServerID])
async def rollcommand(interaction: Interaction):
  firstDie = random.randint(1, 8)
  secondDie = random.randint(1, 8)
  thirdDie = random.randint(1, 8)
  
  if firstDie == 4 or firstDie == 8:
    sucessOne = "sucesso!"
  else:
    sucessOne = "falha!"
    
  if secondDie == 4 or secondDie == 8:
    sucessTwo = "sucesso!"
  else:
    sucessTwo = "falha!"
    
  if thirdDie == 4 or thirdDie == 8:
    sucessThree = "sucesso!"
  else:
    sucessThree = "falha!"
  
  diceList = {
    "firstpool": [firstDie, sucessOne],
    "secondpool": [secondDie, sucessTwo],
    "thirdpool": [thirdDie, sucessThree],
  }
  
  numero_de_sucessos = contar_sucessos(diceList)
  if numero_de_sucessos > 1: 
    resultado = "Maravilha!!!" 
  elif numero_de_sucessos == 1:
    resultado = "Foi bem."
  else:
    resultado = "Falhou miseravelmente."

  
  await interaction.response.send_message(
    f'Dado 1: {diceList["firstpool"][0]} {diceList["firstpool"][1]}\n'
    f'Dado 2: {diceList["secondpool"][0]} {diceList["secondpool"][1]}\n'
    f'Dado 3: {diceList["thirdpool"][0]} {diceList["thirdpool"][1]}\n\n'
    f'{numero_de_sucessos} sucessos!\n'
    f'{resultado}'
  )
  
def contar_sucessos(dice_list):
    return sum(1 for result in dice_list.values() if result[1] == "sucesso!")
  
client.run(BOT_TOKEN)
