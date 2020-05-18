import items, character, monsters

inpt = input("are you a Warrior or Rogue? >")
if inpt == "Warrior" or inpt == "warrior":
    player = character.Warrior()

else:
    player = character.Rogue()

player.Stats
