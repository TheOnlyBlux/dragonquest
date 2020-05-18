from json import dumps
from random import randint
#stats
""" 
-DEX:Dextarity
-STR:Strength
-CON:Consitution
-Int:Intelect
-WIS:Wisdom
-RES:Reserve
"""

#classes
classesList = [
    "Warrior",
    "Crusader",
    "Wizard",
    "Barbarian",
    "Archer",
    "Ranger",
    "Rogue",
    "Bard" 
    ]
racesList = [
    "Human",
    "Elf",
    "Dwarf",
    "Halfling",
    "Angrador",
    "Salvidua" 
    ]
statsList = [
    "DEX",
    "STR",
    "CON",
    "INT",
    "WIS",
    "RES" 
    ]
races = {
    "Human": {
        "CON":2,
        "STR":2,
        "DEX":2,
        "WIS":2,
        "INT":2,
        "RES":2
        },
    "Dwarf": {
        "CON":4,
        "STR":3,
        "DEX":1,
        "WIS":1,
        "INT":1,
        "RES":0
        },
    "Elf": {
        "CON":2,
        "STR":2,
        "DEX":3,
        "WIS":2,
        "INT":2,
        "RES":0
        },
    "Halfling": {
        "CON":2,
        "STR":1,
        "DEX":4,
        "WIS":2,
        "INT":2,
        "RES":0
        },
    "Angrador": {
        "CON":3,
        "STR":4,
        "DEX":1,
        "WIS":1,
        "INT":1,
        "RES":0
        },
    "Salvidua": {
        "CON":1,
        "STR":1,
        "DEX":1,
        "WIS":3,
        "INT":3,
        "RES":3
        },
    
        
    }
classes = {
    "Warrior": {
        "CON":3,
        "STR":2,
        "DEX":1,
        "WIS":1,
        "INT":1,
        "RES":0
        },
    "Crusader": {
        "CON":2,
        "STR":2,
        "DEX":1,
        "WIS":3,
        "INT":2,
        "RES":0
        },
    "Wizard": {
        "CON":3,
        "STR":1,
        "DEX":1,
        "WIS":3,
        "INT":3,
        "RES":4
        },
    "Barbarian": {
        "CON":5,
        "STR":3,
        "DEX":1,
        "WIS":1,
        "INT":1,
        "RES":0
        },
    "Archer": {
        "CON":1,
        "STR":3,
        "DEX":4,
        "WIS":1,
        "INT":1,
        "RES":0
        },
    "Ranger": {
        "CON":3,
        "STR":2,
        "DEX":3,
        "WIS":1,
        "INT":1,
        "RES":0
        },
    "Rogue": {
        "CON":2,
        "STR":2,
        "DEX":5,
        "WIS":1,
        "INT":1,
        "RES":0
        },
    "Bard": {
        "CON":3,
        "STR":1,
        "DEX":2,
        "WIS":3,
        "INT":1,
        "RES":2
        }
    }
cast = {

    "fireball I": {
        "type":"fire",
        "sap":3,
        "damage":3
        },
    "fireball II": {
        "type":"fire",
        "sap":2,
        "damage":3
        },
    "fireball III": {
        "type":"fire",
        "sap":2,
        "damage":5
        },
    "heal I": {
        "type":"health",
        "sap":2,
        "heal":3
        },
    "heal II": {
        "type":"health",
        "sap":2,
        "heal":5
        },
    "great bolt I": {
        "type":"lightning",
        "sap":10,
        "damage":10
        },
    "great bolt II": {
        "type":"lightning",
        "sap":10,
        "damage":15
        },
    "great bolt III": {
        "type":"lightning",
        "sap":15,
        "damage":20
        },
    "great bolt IV": {
        "type":"lightning",
        "sap":10,
        "damage":20
        },
    "great bolt V": {
        "type":"lightning",
        "sap":5,
        "damage":20
        }
    }
        
items = {
    "sword": {
        "type":"weapon",
        "damage":5,
        "last":100,
        "range":1
        },
    "short sword": {
        "type":"weapon",
        "damage":4,
        "last":150,
        "range":1
        },
    "long bow": {
        "type":"weapon",
        "damage":5,
        "last":75,
        "range":4
        },
    "heater shield": {
        "type":"shield",
        "soak":4,
        "last":100
        },
    "wand": {
        "type":"magic",
        "cast": {
            "type":"none",
            "bonus":0
            },
        "last":100
        },
    "iron platelet": {
        "type":"armor",
        "area":"chest",
        "soak":2,
        "last":100
        }
    }
hitZones = {
    "head":2,
    "chest":1,
    "legs":0.5,
    "arms":0.5
    }
player = {
        "name":'',
        "race":'',
        "class":'',
        "hp":"",
        "soak":"",
        "stats": {
        
            },
        "inventory": {
        
            },
        "cast": {
        
            },
        "equipped":""
    }

monsterRaces = {
    "Goblin": {
        "CON":2,
        "STR":1,
        "DEX":3,
        "WIS":1,
        "INT":2,
        "RES":0
        },
    "Troll": {
        "CON":3,
        "STR":4,
        "DEX":1,
        "WIS":1,
        "INT":1,
        "RES":0
        },
    "Orc": {
        "CON":2,
        "STR":2,
        "DEX":2,
        "WIS":2,
        "INT":2,
        "RES":2
        }
    }
monsterRaceList = [
    "Goblin",
    "Troll",
    "Orc"
]
warband = {
}
def addItem(item):
    global player
    player["inventory"][item] = {
            "strength":items[item]["last"]
        }
def readyType(type):
    global classes, player, races
    player[type] = input("what " + type + "?\n>").lower()
    player[type] = player[type][0].upper() + player[type][1:len(player[type])]
    print(player[type])
    
def characterCreation():
    global player
    player["name"] = input("what is your name? \n>")
    print(dumps(classesList, indent=4))
    readyType("class")
    print(dumps(racesList, indent=4))
    readyType("race")
    x = 0
    while x < len(statsList):
        player["stats"][statsList[x]] = races[player["race"]][statsList[x]] + classes[player["class"]][statsList[x]]
        x += 1
    if player["class"] == "Wizard":
        player["cast"] = ["fireball I", "heal I"]
        player["inventory"] = ["wand"]
    elif player["class"] == "Archer":
        player["inventory"] = ["long bow"]
    else:
        player["inventory"] = ["sword"]
    
    print(dumps(player, indent=4))
        
def warbandCreation(size):
    global monsterRaces, monsterRaceList,classesList, listedMonsters
    listedMonsters = []
    y = 0 
    x = 0
    while y <= size:
        warband[str(y)] = {
            "race":'',
            "class":'',
            "stats": {
        
                },
            "inventory": {
        
                },
            "cast": {
        
                },
            "equipped":""
        }
        warband[str(y)]["race"] = monsterRaceList[randint(0, 2)]
        warband[str(y)]["class"] = classesList[randint(0, 6)]
        while x < len(statsList):
            warband[str(y)]["stats"][statsList[x]] = monsterRaces[warband[str(y)]["race"]][statsList[x]] + classes[warband[str(y)]["class"]][statsList[x]]
            x += 1
        if warband[str(y)]["class"] == "Wizard":
            warband[str(y)]["cast"] = ["fireball I", "heal I"]
            warband[str(y)]["inventory"] = ["wand"]
        elif warband[str(y)]["class"] == "Archer":
            warband[str(y)]["inventory"] = ["long bow"]
        else:
            warband[str(y)]["inventory"] = ["sword"]
        listedMonsters.append(warband[str(y)]["race"] + " " + warband[str(y)]["class"])
        x = 0
        y += 1
    print("There are Monsters inside")
    print(listedMonsters)
        

