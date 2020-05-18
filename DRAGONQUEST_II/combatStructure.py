"""
structure = {
        Determine Order
        1st attack {
            numOfActions = int(DEX/3)
            declare action
            declare Target if attacking
        }
        repeat for others
        repeat until player or monsters win
        
}
"""
from items import *

characterCreation()
listedMonsters = []
warbandCreation(2)
def playerAction():
    numOfActions = player["stats"]["DEX"]/3
    actions = ["attack [target]", "cast [thing] [target] ", "equip [item] ", "use [item] [target]"]
    print(actions)
    actionTaken = input("> ")
    actionTaken = actionTaken.split(" ")
    if actionTaken[0] == "equip":
        player["equipped"] += actionTaken[1]
        print(player)
        
playerAction
    