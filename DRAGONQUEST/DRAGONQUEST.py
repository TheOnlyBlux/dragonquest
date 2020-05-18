from random import randint

gameOn = True
transitions = ["you turn the corner... ",
               "you slide open a padlock and step inside... ",
               "you crawl through an opening in the wall... "]
floor = 0
statDictionary = {
    "warrior" : { #class layer
        "strength" : 3, #stat layer
        "speed" : 3,
        "soak" : 3,
        "hp" : 12,
        "magic": 0
        },
    "rogue" : {
        "strength" : 3,
        "speed" : 4,
        "soak" : 2,
        "hp" : 10,
        "magic": 0
        },
    "wizard" : {
        "strength" : 2,
        "speed" : 2,
        "soak" : 2,
        "hp" : 9,
        "magic": 4 
        },
    }

enemyDictionary = {
    "goblin" : {
        "strength" : 2,
        "speed" : 2,
        "soak" : 2,
        "hp" : 5,
        "magic": 1
        },
    "troll": {
        "strength": 4,
        "speed": 1,
        "soak" : 4,
        "hp": 10,
        "magic": 0
        },
    "orc" : {
        "strength" : 3,
        "speed" : 3,
        "soak" : 4,
        "hp" : 12,
        "magic": 2
        },
    "dragon" : {
        "strength" : 6,
        "speed" : 6,
        "soak" : 4,
        "hp" : 25,
        "magic": 5
        },
}

        
playerClass = input("Wizard, Warrior, or Rogue? \n> ")
playerClass = playerClass.lower()
print("You are a", playerClass)
playerName = input("What is your name? \n> ")
print("Hello,", playerName)
print(statDictionary[playerClass])
print("You enter a dark dungeon to defeat the \n\
evil dragon that lurks within... ")
playerStats = {playerClass:statDictionary[playerClass]}
while gameOn:
    print(transitions[randint(0, 2)])
    input("[press enter]")
    diceRoll = randint(1, 20)
    if diceRoll >= 5 and floor >= 10:
        enemy = "dragon"
        chosenEnemy = {"dragon":enemyDictionary["dragon"]}
        print("you have reached the final floor, \
home to the final boss, the evil dragon \
Morgatroth the Nacho breather")
        print("you hear a roar in front of you")
        print("a booming voice says, 'you shall not defeat me puny human", playerClass, "'")
        print(playerName, "what will you do?")
        while playerStats[playerClass]["hp"] > 0 and chosenEnemy["dragon"]["hp"] > 0:
            print("1. attack")
            print("2. use magic")
            print("3. heal")
            print("4. access situation")
            query = input("> ")
            if query == "1":
                    print("you swing your weapon at the monster")
                    roll = randint(1, 20)
                    if roll > 2*chosenEnemy[enemy]["speed"]:
                        if roll == 20:
                            print("you score a direct hit")
                            chosenEnemy[enemy]["hp"] -= 2*playerStats[playerClass]["strength"]
                        else:
                            print("you score a hit")
                            chosenEnemy[enemy]["hp"] -= playerStats[playerClass]["strength"]
                    else:
                        print("The", enemy, "dodges out of the way")
            elif query == "2":
                print("what would you like to do with magic?")
                print("1. attack")
                print("2. heal")
                magicQuery = input("> ")
                if magicQuery == "1":
                    print("you fire a burst of fiery magic at the", enemy)
                    roll = randint(1, 20)
                    if roll > playerStats[playerClass]["magic"]:
                        if roll == 20:
                            print("you score a direct hit")
                            chosenEnemy[enemy]["hp"] -= playerStats[playerClass]["magic"]
                        else:
                            print("you score a hit")
                            chosenEnemy[enemy]["hp"] -= playerStats[playerClass]["magic"]/2
                    else:
                        print("the blast misses the monster")
                elif magicQuery == "2":
                    playerStats[playerClass]["hp"] += playerStats[playerClass]["magic"]
                    print("you begin to feel better")

            elif query == "3":
                print("you begin to feel better")
                playerStats[playerClass]["hp"] += 2

            elif query == "4":
                print(enemy, ":", chosenEnemy[enemy])
                print(playerName, ":", playerStats[playerClass])
                
            roll = randint(1, 20)
            if roll > 5 and roll <= 10:
                print("The dragon takes breath and fiery flame rushes over you")
                roll = randint(1, 20)
                if roll > playerStats[playerClass]["speed"]*2:
                    print("you the monsters fiery breath hit your skin")
                    playerStats[playerClass]["hp"] -= chosenEnemy[enemy]["magic"]
                else:
                    print("the nacho-y fire barely misses you")
            elif roll <= 5:
                print("The dragon heals")
                chosenEnemy[enemy]["hp"] += 2
            else:
                print("the dragon swings a claw at you")
                roll = randint(1, 20)
                if roll > playerStats[playerClass]["speed"]*2:
                    print("you feel the claw puncture your armor")
                    playerStats[playerClass]["hp"] -= chosenEnemy[enemy]["strength"]
                else:
                    print("you narrowly avoid the dragons nasty claws")
        if playerStats[playerClass]["hp"] <= 0:
            print("you died")
            gameOn = False
            input("[press enter]")
            exit()
####################################################################        
    elif diceRoll >= 5:
        direction = ["left", "right"]
        print("you enter a vast room full \n\
of treasure. to your", direction[randint(0,1)], "you hear a growl.")
        enemies = ["orc", "troll", "goblin"]
        enemy = enemies[randint(0, 2)]
        print("a", enemy, "steps into view")
        enemyDictionary = {
            "goblin" : {
                "strength" : 2,
                "speed" : 2,
                "soak" : 2,
                "hp" : 5,
                "magic": 1
                },
            "troll": {
                "strength": 4,
                "speed": 1,
                "soak" : 4,
                "hp": 10,
                "magic": 0
                },
            "orc" : {
                "strength" : 3,
                "speed" : 3,
                "soak" : 4,
                "hp" : 12,
                "magic": 2
                },
            "dragon" : {
                "strength" : 6,
                "speed" : 6,
                "soak" : 4,
                "hp" : 25,
                "magic": 5
                },
        }
        chosenEnemy = {}
        chosenEnemy.clear()
        chosenEnemy = {enemy:enemyDictionary[enemy]}
        chosenEnemy[enemy]["hp"] = enemyDictionary[enemy]["hp"]
        while playerStats[playerClass]["hp"] > 0 and chosenEnemy[enemy]["hp"] > 0:
            print(playerName, "what would you like to do?")
            print("1. attack")
            print("2. use magic")
            print("3. heal")
            print("4. access situation")
            query = input("> ")
            if query == "1":
                print("you swing your weapon at the monster")
                roll = randint(1, 20)
                if roll > 2*chosenEnemy[enemy]["speed"]:
                    if roll == 20:
                        print("you score a direct hit")
                        chosenEnemy[enemy]["hp"] -= 2*playerStats[playerClass]["strength"]
                    else:
                        print("you score a hit")
                        chosenEnemy[enemy]["hp"] -= playerStats[playerClass]["strength"]
                else:
                    print("The", enemy, "dodges out of the way")
            elif query == "2":
                print("what would you like to do with magic?")
                print("1. attack")
                print("2. heal")
                magicQuery = input("> ")
                if magicQuery == "1":
                    print("you fire a burst of fiery magic at the", enemy)
                    roll = randint(1, 20)
                    if roll > playerStats[playerClass]["magic"]:
                        if roll == 20:
                            print("you score a direct hit")
                            chosenEnemy[enemy]["hp"] -= playerStats[playerClass]["magic"]
                        else:
                            print("you score a hit")
                            chosenEnemy[enemy]["hp"] -= playerStats[playerClass]["magic"]/2
                    else:
                        print("the blast misses the monster")
                elif magicQuery == "2":
                    playerStats[playerClass]["hp"] += playerStats[playerClass]["magic"]
                    print("you begin to feel better")

            elif query == "3":
                print("you begin to feel better")
                playerStats[playerClass]["hp"] += 2

            elif query == "4":
                print(enemy, ":", chosenEnemy[enemy])
                print(playerName, ":", playerStats[playerClass])
                
            roll = randint(1, 20)
            if roll > 5:
                print("The monster takes a swing at you")
                roll = randint(1, 20)
                if roll > playerStats[playerClass]["strength"]*2:
                    print("The monster scores a hit against you")
                    playerStats[playerClass]["hp"] -= chosenEnemy[enemy]["strength"]
                else:
                    print("The monster swings nothing but air")
            elif roll <= 5:
                print("The monster heals")
                chosenEnemy[enemy]["hp"] += 1
        if chosenEnemy[enemy]["hp"] <= 0:
            print("you have defeated a", enemy)
            print("What skill would you like to upgrade?")
            print("strength")
            print("speed")
            print("magic")
            print("soak")
            upgrade = input("> ")
            playerStats[playerClass][upgrade] += 1
            print("your", upgrade, "is", playerStats[playerClass][upgrade])
            print("you begin to feel better")
            playerStats[playerClass]["hp"] += playerStats[playerClass]["soak"]
            print("you end the combat with", playerStats[playerClass]["hp"], "hp")
            floor += 1
        else:
            print("you died")
            gameOn = False
            input("[press enter]")
            exit()
################################################################
    else:
        print("you stumble upon an empty room")
        playerStats[playerClass]["hp"] += 2
