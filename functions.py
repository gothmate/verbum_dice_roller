def roller():
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
  
  return diceList