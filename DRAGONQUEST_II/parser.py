from items import playerRow, playerCol
def parse():
    global playerRow
    global playerCol
    verbs = ["go", "fight", "shoot", "read"]
    nouns = ["forward", "backward", "left", "right"]
    prompt = input("> ")
    prompt = prompt.split(" ")
    print(prompt[1])
    if prompt[0] == verbs[0]:
        print("you " + prompt[0] + " " + prompt[1])
        if prompt[1] == 'forward':
            playerRow += 1
        elif prompt[1] == 'backward':
            playerRow -= 1
        elif prompt[1] == 'right':
            playerCol += 1
        elif prompt[1] == 'left':
            playerCol -= 1
        else:
            print("check the command")
        
            
    else:
        print("check the command")

parse()