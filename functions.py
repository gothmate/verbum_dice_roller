import random

def rollDice():
  firstDie = random.randint(1, 8)
  secondDie = random.randint(1, 8)
  thirdDie = random.randint(1, 8)

  sucessOne = sucess_decision(firstDie, 4)
  sucessTwo = sucess_decision(secondDie, 4)
  sucessThree = sucess_decision(thirdDie, 4)

  diceList = {
      "natural": [firstDie, sucessOne],
      "racional": [thirdDie, sucessThree],
      "social": [secondDie, sucessTwo],
  }

  return diceList


def contar_sucessos(dice_list):
    return sum(1 for result in dice_list.values() if result[1] == True)


def sucess_decision(die_result, dif):
    if die_result == dif or die_result == 8:
        return True
    else:
        return False
