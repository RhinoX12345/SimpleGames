#virtual environment: venv/Script/activate
#import pygame
import random, time

#functions
def hint(correct):
    hints = {
        "1,2": "x=1,2",
        "1,3": "x=1,3",
        "1,4": "x=1,4",
        "1,5": "x=1,5",
        "1,6": "x=1,6",
        "1,7": "x=1,7",
        "1,8": "x=1,8",
        "2,3": "x=2,3",
        "2,4": "x=2,4",
        "2,5": "x=2,5",
        "2,6": "x=2,6",
        "2,7": "x=2,7",
        "2,8": "x=2,8",
        "3,4": "x=3,4",
        "3,5": "x=3,5",
        "3,6": "x=3,6",
        "3,7": "x=3,7",
        "3,8": "x=3,8",
        "4,5": "x=4,5",
        "4,6": "x=4,6",
        "4,7": "x=4,7",
        "4,8": "x=4,8",
        "5,6": "x=5,6",
        "5,7": "x=5,7",
        "5,8": "x=5,8",
        "6,7": "x=6,7",
        "6,8": "x=6,8",
        "7,8": "x=7,8"
        }
    correct = int(correct)
    n = random.randint(1, 8)
    while n == correct:
        n = random.randint(1, 8)
    if n < correct:
        msg = str(n) + "," + str(correct)
    else:
        msg = str(correct) + "," + str(n)
    return hints[msg]

def positionCheck(position):
    if len(playerPos) != 9:
        print("Incorrect number of positions")
        return False
    for i in playerPos:
        if i not in coordList:
            print("Invalid input")
            return False
    return True

#default values
defPos = [
    ["E5","E6","E3","F3","G3","B2","B3","B4","B5"],
    ["D4","D5","H2","H3","H4","B7","C7","D7","E7"],
    ["B8","C8","H5","H6","H7","E1","E2","E3","E4"]]
ltnConvert = str.maketrans("ABCDEFGH", "12345678")
coordList = [
    'A1','A2','A3','A4','A5','A6','A7','A8',
    'B1','B2','B3','B4','B5','B6','B7','B8',
    'C1','C2','C3','C4','C5','C6','C7','C8',
    'D1','D2','D3','D4','D5','D6','D7','D8',
    'E1','E2','E3','E4','E5','E6','E7','E8',
    'F1','F2','F3','F4','F5','F6','F7','F8',
    'G1','G2','G3','G4','G5','G6','G7','G8',
    'H1','H2','H3','H4','H5','H6','H7','H8']
instructions= "Instructions:\nplaceholder"
playerTargeted = []
botTargeted = []
playerPos = ""

botPos = defPos[random.randint(0,2)]
print(botPos)
print(instructions)
while playerPos == "":
    playerPos = input("Set your positions: ")
    playerPos = playerPos.split(",")
    valid = positionCheck(playerPos)
    if valid == True:
        break
    else:
        playerPos = ""

while botPos != [] or playerPos != []:
    hintType = ""
    check = ""
    while hintType == "":
        hintType = input("Hint (Row/Column): ")
        hintType = hintType.lower()
        if hintType == "row":
            posTarget = random.choice(botPos)
            temp = posTarget[0]
            temp = temp.translate(ltnConvert)
        elif hintType == "column":
            posTarget = random.choice(botPos)
            temp = posTarget[1]
        else:
            print("Invalid input")
            hintType = ""
    print(posTarget)
    print(hint(temp))
    while check == "":
        check = input("Pick a target coordinate: ")
        check = check.upper()
        if check in coordList:
            if check not in playerTargeted:
                if check in botPos:
                    botPos.remove(check)
                    print("-Hit")
                else:
                    print("-Miss")
                playerTargeted.append(check)
            else:
                print("Already chosen previously")
                check = ""
        else:
            print("Invalid input")
            check = ""
    print("Bot thinking...")
    botTarget = random.choice(coordList)
    while botTarget in botTargeted:
        botTarget = random.choice(coordList)
    time.sleep(2)
    print(f"Bot Target: {botTarget}")
    if botTarget in playerPos:
        playerPos.remove(botTarget)
        print("-Hit")
    else:
        print("-Miss")
    botTargeted.append(botTarget)
    time.sleep(1)
if botPos == []:
    print("You Win!")
elif playerPos == []:
    print("Bot Wins!")