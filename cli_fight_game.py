import os, time, random

def health_stats():
  health = (rollDice(6)*rollDice(12))/2+10
  return health

def strength_stats():
  strength = (rollDice(6)*rollDice(8))/2+12
  return strength

def character_builder():
  character = input("Name your Legend:")
  char_type = input("Character type (human, elf, wizard, orc):")
  return character

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def damage(strength_1, strength_2):
  if strength_1 > strength_2:
    return strength_1 - strength_2 + 5
  else:
    return strength_2 - strength_1 + 5





playGame = "yes"

while True:
  os.system("clear")
  time.sleep(1)
  
  print("⚔️ Character Generator ⚔️")
  time.sleep(1)
  character_1 = character_builder()
  health_1 = health_stats()
  strength_1 = strength_stats()
  print(character_1)
  time.sleep(1)
  print("HEALTH:", health_1)
  time.sleep(1)
  print("STRENGTH:", strength_1)
  time.sleep(1)
  
  print("Who are they battling?")
  time.sleep(1)
  character_2 = character_builder()
  health_2 = health_stats()
  strength_2 = strength_stats()
  print(character_2)
  time.sleep(1)
  print("HEALTH:", health_2)
  time.sleep(1)
  print("STRENGTH:", strength_2)
  time.sleep(1)
  
  battle_counter = 0

  while True:
    battle_counter += 1
    os.system("clear")
    print("⚔️ Battle time ⚔️")
    time.sleep(1)
    
    if battle_counter == 1:
      print("The battle begins!")
    else :
      print("The battle continues")
    
    time.sleep(2)
  
    character_1_dice = rollDice(6)
    character_2_dice = rollDice(6)
    health_damage = damage(strength_1, strength_2)
  
    if character_1_dice > character_2_dice :
      print(character_1," wins round ",battle_counter)
      print(character_2," takes a hit with ",health_damage," damage")
      health_2 -= health_damage
    elif character_2_dice > character_1_dice :
      print(character_2," wins round ",battle_counter)
      print(character_1," takes a hit with ",health_damage," damage")
      health_1 -= health_damage
    else:
      print("It's a draw")

    time.sleep(2)

    print(character_1)
    print("HEALTH : ", health_1)
    time.sleep(2)
    print(character_2)
    print("HEALTH : ", health_2)

    time.sleep(2)

    if health_1 <= 0 :
      print("Oh no ", character_1, " has died!")
      print(character_2," has destroyed ", character_1, " in ",battle_counter," rounds")
      break
    elif health_2 <= 0:
      print("Oh no ", character_2, " has died!")
      print(character_1," has destroyed ", character_2, " in ",battle_counter," rounds")
      break
    else :
      print("And they are both standing for the next round!")
      
      time.sleep(2)
      continue
  
  playGame = input("Start over?:")
  if playGame == "yes":
    continue
  else:
    break
