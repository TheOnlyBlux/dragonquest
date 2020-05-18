from items import *
room_shell = {
    "name":"",
    "desc":"",
    "size":"",
    "north":"",
    "south":"",
    "east":"",
    "west":"",
    "entities":{
    
        }
    }
    
rooms = {
    "entrance":{
        "name":"entrance",
        "desc":"you stand in in front of the doorway to the castle",
        "size":"1",
        "north":"main hall",
        "south":"",
        "east":"",
        "west":"",
        "entities":{
    
            }
        },
    "main hall":{
        "name":"main hall",
        "desc":"The hall is large with hallways leading east and west",
        "size":"2",
        "north":"",
        "south":"entrance",
        "east":"east hallway",
        "west":"west hallway",
        "entities":{
    
            }
        },
    "east hallway":{
        "name":"east hallway",
        "desc":"at the end of the hallway is a door",
        "size":"2",
        "north":"",
        "south":"entrance",
        "east":"room 1",
        "west":"main hallway",
        "entities":{
    
            }
        },
    "west hallway":{
        "name":"west hallway",
        "desc":"at the end of the hallway is a door",
        "size":"2",
        "north":"",
        "south":"entrance",
        "east":"main hall",
        "west":"room 2",
        "entities":{
    
            }
        }
    }
directions = ["north", "south", "east", "west"]    
def printRoom(room):
    print(rooms[room]["desc"])
    x = 0
    warbandCreation(randint(1, 5))
    while x < 4:
        if rooms[room][directions[x]] == "":
            x += 1
        else:
            print("to the " + directions[x] + " is the " + rooms[room][directions[x]])
            x += 1 

curRoom = "entrance"
def runRoom():
    global curRoom, action
    printRoom(curRoom)
    action = input("> ")
    try:
        action = action.split(" ")
        action[1] = action[1].lower()
        if action[0] == "go":
            if action[1] in directions:
                print("you go " + action[1])
                curRoom = rooms[curRoom][action[1]]
            else:
                print("valid command, wrong parameters \nTry: \nNorth\nSouth\nWest \nEast")
        else:
            print("that is not a valid command, \ntry: \ngo direction")
    except:
        print("that is not a valid command, \ntry: \ngo direction")
    