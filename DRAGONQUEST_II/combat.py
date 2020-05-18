from functions import *
from setup import *
from random import randint, choice
from json import dumps

"""decided to make a whole file for combat,
because this could a big chunk of the code """

def playerCombatPhase():
    print("you have <" + equiped + "< equiped")
    commands = ["attack", "use magic", "equip an item", \
                "read inventory", "heal"]
    print(commands)

    action = input(">")
    if action == commands[0]:
        print("you swing your weapon at the enemy")

    elif action == commands[1]:
        if inventory[equiped]["type"] == "magic":
            print("you do magical stuff")
        else:
            print("you do not have a magical item")
        
    elif action == commands[2]:
        equipItem()

    elif action == commands[3]:
        readInventory()
        
    elif action == commands[4]:
        heal()
    else:
        print("that is not a valid command, \
you lost your chance to attack")
