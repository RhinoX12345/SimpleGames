#virtual environment: venv/Script/activate
#import pygame
import random, time

#functions
def horizontal(length, current):
    rangeMax = 9-length
    loop = True
    while loop:
        column = str(random.randint(1, rangeMax))
        startCoord = random.choice(colList[column])
        index = coordList.index(startCoord)
        boat = []
        for i in range(length):
            pos = coordList[index+i]
            if pos not in current:
                boat.append(pos)
                loop = False
            else:
                boat.clear()
                loop = True
                break
    return boat, True

def vertical(length, current):
    ltrRange = "ABCDEFGH"
    rangeMax = 9-length
    row = ltrRange[:rangeMax]
    loop = True
    while loop:
        startCoord = random.choice(rowList[str(random.choice(row))])
        index = coordList.index(startCoord)
        boat = []
        for i in range(length):
            pos = coordList[index+i*8]
            if pos not in current:
                boat.append(pos)
                loop = False
            else:
                boat.clear()
                loop = True
                break
    return boat, True

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

def positionCheck(position, length):
    if len(position) != length:#check number of positions
        print("Incorrect number of positions")
        return False
    for i in position:#check for valid coordinates
        if i not in coordList:
            print("Invalid input")
            return False
    tempList = []
    for i in position:#check duplicates
        if i in tempList:
            print("Duplicate input")
            return False
        else:
            tempList.append(i)
    return boatCheck(position, length)

def paramMaker(length):
    ltr = "ABCDEFGH"
    row = ltr[:(length)]
    col = ""
    for i in range(1,9-length):
        col += str(i)
    return row, col

def boatCheck(position, length):
    startRowRange, startColRange = paramMaker(length)
    pos1 = position[0]
    pos2 = position[1]
    if pos1[0] not in startRowRange:
        return False
    if pos1[1] not in startColRange:
        return False
    if coordList.index(pos2) == (coordList.index(pos1)+1):
        for i in position:
            check = (coordList.index(i) - coordList.index(pos1)) == (position.index(pos1) + position.index(i))
            if check:
                continue
            else:
                return False
    elif coordList.index(pos2) == (coordList.index(pos1)+8):
        for i in position:
            check = (coordList.index(i) - coordList.index(pos1)) == (position.index(pos1) + position.index(i)*8)
            if check:
                continue
            else:
                return False
    else: 
        return False
    return True
    
#default values
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
rowList = {
    "A":['A1','A2','A3','A4','A5','A6','A7','A8'],
    "B":['B1','B2','B3','B4','B5','B6','B7','B8'],
    "C":['C1','C2','C3','C4','C5','C6','C7','C8'],
    "D":['D1','D2','D3','D4','D5','D6','D7','D8'],
    "E":['E1','E2','E3','E4','E5','E6','E7','E8'],
    "F":['F1','F2','F3','F4','F5','F6','F7','F8'],
    "G":['G1','G2','G3','G4','G5','G6','G7','G8'],
    "H":['H1','H2','H3','H4','H5','H6','H7','H8']}
colList = {
    "1":['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
    "2":['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
    "3":['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
    "4":['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
    "5":['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
    "6":['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
    "7":['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
    "8":['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']}
instructions= "Instructions:\nplaceholder"
playerTargeted = []
botTargeted = []
playerPos = []

botPos = {}
botPosList = []
boatLength = [3, 3, 3]
pBoatLength = boatLength.copy()
z = 0
while len(boatLength) > 0:
    direction = random.choice("12")
    if direction == "1":
        boat, loop = horizontal(boatLength[0], botPosList)
    if direction == "2":
        boat, loop = vertical(boatLength[0], botPosList)
    botPos[str(z)] = boat
    for i in boat:
        botPosList.append(i)
    boatLength.pop(0)
    z+=1
print(botPos)
print(botPosList)
print(instructions)

for i in pBoatLength:
    print()
    loop = True
    while loop:
        temp = input(f"Set 1 boat (length:{i}): ")
        temp.upper()
        temp = temp.split(",")
        temp.sort()
        valid = positionCheck(temp, i)
        if valid == True:
            for a in temp:
                playerPos.append(a)
            loop = False
        else:
            loop = True
    
while botPos != [] or playerPos != []:
    hintType = ""
    check = ""
    while hintType == "":#Hint
        hintType = input("Hint (Row/Column): ")
        hintType = hintType.lower()
        if hintType == "row":
            posTarget = random.choice(botPosList)
            temp = posTarget[0]
            temp = temp.translate(ltnConvert)
        elif hintType == "column":
            posTarget = random.choice(botPosList)
            temp = posTarget[1]
        else:
            print("Invalid input")
            hintType = ""
    print(posTarget)
    print(hint(temp))
    while check == "":#Player Check
        check = input("Pick a target coordinate: ")
        check = check.upper()
        if check in coordList:
            if check not in playerTargeted:
                key = "miss"
                playerTargeted.append(check)
                for boat, i in botPos.items():
                    if check in i:
                        botPosList.remove(check)
                        i.remove(check)
                        botPos[boat] = i
                        if i == []:
                            print("-Sink!")
                            key = "skip"
                            break
                        else:
                            print("-Hit!")
                            key = "skip"
                            break
                if key == "miss":
                    print("-Miss!")
            else:
                print("Already chosen previously")
                check = ""
        else:
            print("Invalid input")
            check = ""
    if botPosList == []:
        print("You Win!")
        break
    print("Bot thinking...")
    botTarget = random.choice(coordList)
    while botTarget in botTargeted:
        botTarget = random.choice(coordList)
    time.sleep(2)
    print(f"Bot Target: {botTarget}")
    if botTarget in playerPos:
        playerPos.remove(botTarget)
        print("-Hit!")
    else:
        print("-Miss!")
    botTargeted.append(botTarget)
    if playerPos == []:
        print("Bot Wins!")
        break
    time.sleep(1)

"""
Bugs:
-

To-do:
-Fix bugs
-Finish position checker
"""