"""this sets up the game varibles"""

""" all gear in the game """
gear = {
    "ancient staff": {
        "power":2,
        "sap":2,
        "strength":250,
        "type":"magic",
        "quantity":0,
        "rarity":1
        },
    "staff of power": {
        "power":5,
        "sap":3,
        "strength":150,
        "type":"magic",
        "quantity":0,
        "rarity":5
        },
    "staff of light": {
        "power":10,
        "sap":3,
        "strength":300,
        "type":"magic",
        "quantity":0,
        "rarity":8
        },
    "amulet of dawn": {
        "power":5,
        "sap":4,
        "strength":200,
        "type":"magic",
        "quantity":0,
        "rarity":4
        },
    "gauntlet of flame": {
        "power":2,
        "sap":1,
        "strength":200,
        "type":"magic",
        "quantity":0,
        "rarity":3
        },
    "gauntlet of infinity": {
        "power":20,
        "sap":2,
        "strength":500,
        "type":"magic",
        "quantity":0,
        "rarity":10
        },
    "sword": {
        "damage": 5,
        "range":2,
        "strength":100,
        "type":"melee",
        "quantity":0,
        "rarity":1
        },
    "axe": {
        "damage":6,
        "range":2,
        "strength":75,
        "type":"melee",
        "quantity":0,
        "rarity":3
        },
    "sword of ancients": {
        "damage":10,
        "range":3,
        "strength":300,
        "type":"melee",
        "quantity":0,
        "rarity":8
        },
    "knife": {
        "damage":6,
        "range":1,
        "strength":100,
        "type":"melee",
        "quantity":0,
        "rarity":1
        },
    "long sword": {
        "damage":6,
        "range":3,
        "strength":100,
        "type":"melee",
        "quantity":0,
        "rarity":2
        },
    "flaming sword": {
        "damage":8,
        "range":2,
        "strength":150,
        "type":"melee",
        "quantity":0,
        "rarity":7
        },
    "bow": {
        "damage":6,
        "range":10,
        "strength":75,
        "type":"ranged",
        "quantity":0,
        "rarity":3
        },
    "leather cap": {
        "area":"head",
        "soak": 1,
        "strength": 50,
        "type":"armor",
        "quantity":0,
        "rarity":1
        },
    "heavy cloak": {
        "area":"chest",
        "soak":1,
        "strength":9999,
        "type":"armor",
        "quantity":0,
        "rarity":1
        },
    "iron plate": {
        "area":"chest",
        "soak":3,
        "strength":75,
        "type":"armor",
        "quantity":0,
        "rarity":5
        },
    "iron helm": {
        "area":"head",
        "soak":3,
        "strength":75,
        "type":"armor",
        "quantity":0,
        "rarity":5
        },
    "iron pants": {
        "area":"legs",
        "soak":2,
        "strength":50,
        "type":"armor",
        "quantity":0,
        "rarity":5
        },
    "cloak of protection": {
        "area":"chest",
        "soak":5,
        "strength":300,
        "type":"armor",
        "quantity":0,
        "rarity": 8
        },
    "helm of protection": {
        "area":"head",
        "soak":5,
        "strength":200,
        "type":"armor",
        "quantity":0,
        "rarity":10
        },
	"magician's robes": {
        "area":"chest",
        "soak":3,
        "strength":300,
        "type":"armor",
        "quantity":0,
        "rarity":5
        }
    }


inventory = {
    
    }
armor = {
    "head":"",
    "chest":"",
    "legs":"",
    "arms":""
    }

""" defines hit zones, where players
and entities can be hit """
hitZones = {
    "head":2,
    "chest":1,
    "legs":0.5,
    "arms":0.5
    }

#defines classes and races a player can be

races = {
    "human": {
        "hp":20,
        "strength":2,
        "speed":2,
        "will":2,
        "magic":0,
        "magEnergy":0
        },
    "dwarf": {
        "hp":25,
        "strength":4,
        "speed":1,
        "will":3,
        "magic":0,
        "magEnergy":0
        },
    "elf": {
        "hp":20,
        "strength":2,
        "speed":3,
        "will":3,
        "magic":1,
        "magEnergy":3
        },
    "halfling": {
        "hp":20,
        "strength":1,
        "speed":4,
        "will":2,
        "magic":0,
        "magEnergy":0
        }
    }

classes = {
    "warrior": {
        "hp":5,
        "strength":1,
        "speed":0,
        "will":1,
        "magic":0,
        "magEnergy":0
        },
    "rogue": {
        "hp":0,
        "strength":0,
        "speed":2,
        "will":0,
        "magic":1,
        "magEnergy":1
        },
    "wizard": {
        "hp":-5,
        "strength":0,
        "speed":0,
        "will":4,
        "magic":2,
        "magEnergy":3
        },
    "archer": {
        "hp":0,
        "strength":-1,
        "speed":2,
        "will":2,
        "magic":0,
        "magEnergy":0
        },
    "ranger": {
        "hp":0,
        "strength":0,
        "speed":2,
        "will":3,
        "magic":1,
        "magEnergy":3
        }
    }

"""foes a player can encounter"""
foes = {
    "slime": {
        "hp":5,
        "strength":2,
        "speed":10,
        "will":2
        },
    "goblin warrior": {
        "hp":15,
        "strength":5,
        "speed":5,
        "will":4
        },
    "goblin sniper": {
        "hp":15,
        "strength":10,
        "speed":2,
        "will":4
        },
    "orc": {
        "hp":20,
        "strength":7,
        "speed":3,
        "will":4
        },
    "orc archer": {
        "hp":20,
        "strength":15,
        "speed":2,
        "will":4
        },
    "troll": {
        "hp":30,
        "strength":15,
        "speed":5,
        "will":1
        },
    "group of rock pelters": {
        "hp":10,
        "strength":5,
        "speed":2,
        "will":3
        },
    "spider": {
        "hp":20,
        "strength":10,
        "speed":10,
        "will":1
        },
    }
"""adjitives to describe foes"""
foeAdj = ["big", "smelly", "pot-bellied", "huge", "short", \
          "stout", "green", "grey", "blue", "red", "towering", \
          "dreadful", "brown", "spikey", "scaley", "slimey"]
