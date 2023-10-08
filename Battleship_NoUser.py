import random, pyscript
from pyscript import document

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
def botPosMaker(bBoatLength):
    botPos = {}
    botPosList = []
    z = 0
    while len(bBoatLength) > 0:
        direction = random.choice("12")
        if direction == "1":
            boat, loop = horizontal(bBoatLength[0], botPosList)
        if direction == "2":
            boat, loop = vertical(bBoatLength[0], botPosList)
        botPos[z] = boat
        for i in boat:
            botPosList.append(i)
        bBoatLength.pop(0)
        z+=1
    return botPos, botPosList

#default values
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
boatLength = [2, 2, 2, 2]

botPos, botPosList = botPosMaker(boatLength.copy())

document.querySelector("#bot").innerText = f"{botPos}/{botPosList}"
msg = ""
for i in boatLength:
    msg += str(i) + "/"
msg = msg.strip("/")
document.querySelector("#boatlength").innerText = msg