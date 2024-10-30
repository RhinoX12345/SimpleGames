import math

cells = [
    '11', '21', '31', '41', '51', '61', '71', '81', '91', 
    '12', '22', '32', '42', '52', '62', '72', '82', '92', 
    '13', '23', '33', '43', '53', '63', '73', '83', '93', 
    '14', '24', '34', '44', '54', '64', '74', '84', '94', 
    '15', '25', '35', '45', '55', '65', '75', '85', '95', 
    '16', '26', '36', '46', '56', '66', '76', '86', '96', 
    '17', '27', '37', '47', '57', '67', '77', '87', '97', 
    '18', '28', '38', '48', '58', '68', '78', '88', '98', 
    '19', '29', '39', '49', '59', '69', '79', '89', '99']
groups = {
    1: ['11', '21', '31', '12', '22', '32', '13', '23', '33'], 
    2: ['41', '51', '61', '42', '52', '62', '43', '53', '63'], 
    3: ['71', '81', '91', '72', '82', '92', '73', '83', '93'], 
    4: ['14', '24', '34', '15', '25', '35', '16', '26', '36'], 
    5: ['44', '54', '64', '45', '55', '65', '46', '56', '66'], 
    6: ['74', '84', '94', '75', '85', '95', '76', '86', '96'], 
    7: ['17', '27', '37', '18', '28', '38', '19', '29', '39'], 
    8: ['47', '57', '67', '48', '58', '68', '49', '59', '69'], 
    9: ['77', '87', '97', '78', '88', '98', '79', '89', '99']}
         
         
fill = obviousPair = obviousTriple = obviousQuad = hiddenSingle = hiddenPair = hiddenTriple = hiddenQuad = pointingPairTriple = boxLineReduc = rectElim = xWing = yWing = swordfish = True

def solver(key):
    def link(primary, secondary, n):  # return array[row/col, group]; key: true (strong link), false (weak link), undefined (no link)
        if primary == secondary:
            return [None]
        if primary not in numberProfile[n] or secondary not in numberProfile[n]:
            return [None]
        returnVal = []
        if primary[0] == secondary[0]:
            strong = True
            for t in range(1, 10):
                check = f"{primary[0]}{t}"
                if check not in [primary, secondary] and check in numberProfile[n]:
                    strong = False
            returnVal.append(strong)
        elif primary[1] == secondary[1]:
            strong = True
            for t in range(1, 10):
                check = f"{t}{primary[1]}"
                if check not in [primary, secondary] and check in numberProfile[n]:
                    strong = False
            returnVal.append(strong)
        gPrim = math.ceil(int(primary[1])/3) * 3 - 3 + math.ceil(int(primary[0])/3)
        gSec = math.ceil(int(secondary[1])/3) * 3 - 3 + math.ceil(int(secondary[0])/3)
        if gPrim == gSec:
            strong = True
            for t in groups[gPrim]:
                if check not in [primary, secondary] and check in numberProfile[n]:
                    strong = False
            returnVal.append(strong)
        return returnVal

    def check():
        for i in range(1, 10):
            for j in range(1, 10):
                if boardLayout[f"{j}{i}"] == 0 and f"{j}{i}" not in cellProfile and False:
                    return "Incorrect"
        for i in range(1, 10):
            rowNumbers = []
            colNumbers = []
            for j in range(1, 10):
                number = boardLayout[f"{j}{i}"]
                if number != 0:
                    if number not in rowNumbers:
                        rowNumbers.append(number)
                    else:
                        return "Incorrect"
                number = boardLayout[f"{i}{j}"]
                if number != 0:
                    if number not in colNumbers:
                        colNumbers.append(number)
                    else:
                        return "Incorrect"
        return "Success"

    cellProfile = {}
    numberProfile = {i: [] for i in range(1, 10)}
    boardLayout = {}
    snapShot = {}
    for i in range(len(key)):
        boardLayout[cells[i]] = int(key[i])
    for i in boardLayout:
        if boardLayout[i] == 0:
            cellProfile[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in cellProfile:
        for j in cellProfile[i]:
            numberProfile[j] = [*numberProfile[j], i]
            numberProfile[j] = list(filter(lambda value: value is not None, numberProfile[j]))
    change = 0
    step = 0
    log = []
    try:
        while True and step < 100:
            if fill:
                if change > 0:
                    cellOutput = {}
                    for i in cellProfile:  # sets tiles for only possible number
                        if len(cellProfile[i]) == 1:
                            boardLayout[i] = cellProfile[i][0]
                            cellOutput[i] = cellProfile[i][0]
                            try:
                                numberProfile[cellProfile[i][0]].remove(i)
                            except:
                                #print("numProfile Desync")
                                return ["Incorrect", "", log, step]
                            cellProfile[i] = []
                    if cellOutput:
                        log.append(cellOutput)
            if change > 0:
                #print(cellProfile)
                #print({key:len(value) for key,value in numberProfile.items()})
                change = 0
            step += 1
            #print("Step", step)
            lastStep = step - 1
            
            for i in range(1):  # removes empty cells from cellProfile
                tempObj = cellProfile.copy()
                for j in cellProfile:
                    if cellProfile[j] == []:
                        del tempObj[j]
                cellProfile = tempObj.copy()

            if True:
                temp = check()
                if temp == "Incorrect":
                    return ["Incorrect", "", log, step]
            
            for i in cellProfile:  # Obvious single
                localChange = 0
                values = cellProfile[i]
                group = math.ceil(int(i[1])/3) * 3 - 3 + math.ceil(int(i[0])/3)
                for j in range(1, 10):  # row
                    tempValue = boardLayout[f"{i[0]}{j}"]
                    if tempValue != 0:
                        if tempValue in cellProfile[i]:
                            cellProfile[i].remove(tempValue)
                            numberProfile[tempValue].remove(i)
                            change += 1
                            localChange += 1
                for j in range(1, 10):  # col
                    tempValue = boardLayout[f"{j}{i[1]}"]
                    if tempValue != 0:
                        if tempValue in cellProfile[i]:
                            cellProfile[i].remove(tempValue)
                            numberProfile[tempValue].remove(i)
                            change += 1
                            localChange += 1
                for j in filter(lambda val: val != i, groups[group]):  # group
                    tempValue = boardLayout[j]
                    if tempValue != 0:
                        if tempValue in cellProfile[i]:
                            cellProfile[i].remove(tempValue)
                            numberProfile[tempValue].remove(i)
                            change += 1
                            localChange += 1
                if localChange > 0:
                    pass  # print("Obvious Single")
            if change > 0:
                log.append(["ObvSingle", change])
                continue
            # Obvious Pairs
            if obviousPair:
                for i in range(1, 10):  # eliminate options if there are twins in a group
                    numList = list(groups[i])
                    for j in range(len(numList)):
                        cell = numList[j]
                        if cell in cellProfile and len(cellProfile[cell]) == 2:
                            for k in range(len(numList)):
                                neighbor = numList[k]
                                if neighbor in cellProfile and len(cellProfile[neighbor]) == 2 and int(cell) < int(neighbor):
                                    if str(cellProfile[cell]) == str(cellProfile[neighbor]):
                                        twins = [cell, neighbor]
                                        elim = cellProfile[twins[0]]
                                        for l in elim:
                                            for target in numList:
                                                if target not in twins and target in cellProfile and l in cellProfile[target]:
                                                    change += 1
                                                    cellProfile[target].remove(l)
                                                    numberProfile[l].remove(target)
                for i in range(1, 10):  # eliminate options if there are twins in a col
                    for j in range(1, 10):
                        cell = f"{i}{j}"
                        if cell in cellProfile and len(cellProfile[cell]) == 2:
                            for k in range(1, 10):
                                neighbor = f"{i}{k}"
                                if neighbor in cellProfile and len(cellProfile[neighbor]) == 2 and int(cell) < int(neighbor):
                                    if str(cellProfile[cell]) == str(cellProfile[neighbor]):
                                        twins = [cell, neighbor]
                                        elim = cellProfile[twins[0]]
                                        for l in elim:
                                            for m in range(1, 10):
                                                target = f"{i}{m}"
                                                if target not in twins and target in cellProfile and l in cellProfile[target]:
                                                    change += 1
                                                    cellProfile[target].remove(l)
                                                    numberProfile[l].remove(target)
                for i in range(1, 10):  # eliminate options if there are twins in a row
                    for j in range(1, 10):
                        cell = f"{j}{i}"
                        if cell in cellProfile and len(cellProfile[cell]) == 2:
                            for k in range(1, 10):
                                neighbor = f"{k}{i}"
                                if neighbor in cellProfile and len(cellProfile[neighbor]) == 2 and int(cell) < int(neighbor):
                                    if str(cellProfile[cell]) == str(cellProfile[neighbor]):
                                        twins = [cell, neighbor]
                                        elim = cellProfile[twins[0]]
                                        for l in elim:
                                            for m in range(1, 10):
                                                target = f"{m}{i}"
                                                if target not in twins and target in cellProfile and l in cellProfile[target]:
                                                    change += 1
                                                    cellProfile[target].remove(l)
                                                    numberProfile[l].remove(target)
                if change > 0:
                    log.append(["ObvPair", change])
                    continue
                
            # Obvious Triple
            if obviousTriple:
                for i in range(1, 10):  # eliminate options if there are triples in a group
                    placeholder = [(key, value) for key, value in cellProfile.items() if key in groups[i] and 1 < len(value) <= 3]
                    candidates = {key: value for key, value in placeholder}
                    for j in range(len(candidates)):
                        for k in range(j + 1, len(candidates)):
                            for l in range(k + 1, len(candidates)):
                                n1, n2, n3 = list(candidates.keys())[j], list(candidates.keys())[k], list(candidates.keys())[l]
                                temp = []
                                temp2 = sorted([*candidates[n1], *candidates[n2], *candidates[n3]])
                                for val in temp2:
                                    if val not in temp:
                                        temp.append(val)
                                if len(temp) == 3:
                                    c1 = temp2.count(temp[0])
                                    c2 = temp2.count(temp[1])
                                    c3 = temp2.count(temp[2])
                                    if c1 >= 2 and c2 >= 2 and c3 >= 2:
                                        for m in [key for key in cellProfile if key in groups[i]]:
                                            if m not in [n1, n2, n3]:
                                                for n in cellProfile[m]:
                                                    if n in temp:
                                                        # console.log("Obvious Triple Group")
                                                        change += 1
                                                        cellProfile[m].remove(n)
                                                        numberProfile[n].remove(m)
                for i in range(1, 10):  # eliminate options if there are triples in a col
                    candidates = {key: value for key, value in cellProfile.items() if key[0] == str(i) and 1 < len(value) <= 3}
                    for j in range(len(candidates)):
                        for k in range(j + 1, len(candidates)):
                            for l in range(k + 1, len(candidates)):
                                n1, n2, n3 = list(candidates.keys())[j], list(candidates.keys())[k], list(candidates.keys())[l]
                                temp = []
                                temp2 = sorted([*candidates[n1], *candidates[n2], *candidates[n3]])
                                for val in temp2:
                                    if val not in temp:
                                        temp.append(val)
                                if len(temp) == 3:
                                    c1 = temp2.count(temp[0])
                                    c2 = temp2.count(temp[1])
                                    c3 = temp2.count(temp[2])
                                    if c1 >= 2 and c2 >= 2 and c3 >= 2:
                                        for m in [key for key in cellProfile if key[0] == str(i)]:
                                            if m not in [n1, n2, n3]:
                                                for n in cellProfile[m]:
                                                    if n in temp:
                                                        # console.log("Obvious Triple Col")
                                                        change += 1
                                                        cellProfile[m].remove(n)
                                                        numberProfile[n].remove(m)
                for i in range(1, 10):  # eliminate options if there are triples in a row
                    candidates = {key: value for key, value in cellProfile.items() if key[1] == str(i) and 1 < len(value) <= 3}
                    for j in range(len(candidates)):
                        for k in range(j + 1, len(candidates)):
                            for l in range(k + 1, len(candidates)):
                                n1, n2, n3 = list(candidates.keys())[j], list(candidates.keys())[k], list(candidates.keys())[l]
                                temp = []
                                temp2 = sorted([*candidates[n1], *candidates[n2], *candidates[n3]])
                                for val in temp2:
                                    if val not in temp:
                                        temp.append(val)
                                if len(temp) == 3:
                                    c1 = temp2.count(temp[0])
                                    c2 = temp2.count(temp[1])
                                    c3 = temp2.count(temp[2])
                                    if c1 >= 2 and c2 >= 2 and c3 >= 2:
                                        for m in [key for key in cellProfile if key[1] == str(i)]:
                                            if m not in [n1, n2, n3]:
                                                for n in cellProfile[m]:
                                                    if n in temp:
                                                        # console.log("Obvious Triple Row")
                                                        change += 1
                                                        cellProfile[m].remove(n)
                                                        numberProfile[n].remove(m)
                if change > 0:
                    log.append(["ObvTriple", change])
                    continue

            # Obvious Quad
            if obviousQuad:
                for i in range(1, 10):  # eliminate options if there are quadruples in a group
                    candidates = {key: value for key, value in cellProfile.items() if key in groups[i] and 1 < len(value) <= 4}
                    for j in range(len(candidates)):
                        for k in range(j + 1, len(candidates)):
                            for l in range(k + 1, len(candidates)):
                                for m in range(l + 1, len(candidates)):
                                    n1, n2, n3, n4 = list(candidates.keys())[j], list(candidates.keys())[k], list(candidates.keys())[l], list(candidates.keys())[m]
                                    temp = []
                                    temp2 = sorted([*candidates[n1], *candidates[n2], *candidates[n3], *candidates[n4]])
                                    for val in temp2:
                                        if val not in temp:
                                            temp.append(val)
                                    if len(temp) == 4:
                                        c1 = temp2.count(temp[0])
                                        c2 = temp2.count(temp[1])
                                        c3 = temp2.count(temp[2])
                                        c4 = temp2.count(temp[3])
                                        if c1 >= 2 and c2 >= 2 and c3 >= 2 and c4 >= 2:
                                            for n in [key for key in cellProfile if key in groups[i]]:
                                                if n not in [n1, n2, n3, n4]:
                                                    for o in [val for val in cellProfile[n] if val in temp]:
                                                        # console.log("Obvious Quad Group")
                                                        change += 1
                                                        cellProfile[n].remove(o)
                                                        numberProfile[o].remove(n)
                for i in range(1, 10):  # eliminate options if there are quadruples in a col
                    candidates = {key: value for key, value in cellProfile.items() if key[0] == str(i) and 1 < len(value) <= 4}
                    for j in range(len(candidates)):
                        for k in range(j + 1, len(candidates)):
                            for l in range(k + 1, len(candidates)):
                                for m in range(l + 1, len(candidates)):
                                    n1, n2, n3, n4 = list(candidates.keys())[j], list(candidates.keys())[k], list(candidates.keys())[l], list(candidates.keys())[m]
                                    temp = []
                                    temp2 = sorted([*candidates[n1], *candidates[n2], *candidates[n3], *candidates[n4]])
                                    for val in temp2:
                                        if val not in temp:
                                            temp.append(val)
                                    if len(temp) == 4:
                                        c1 = temp2.count(temp[0])
                                        c2 = temp2.count(temp[1])
                                        c3 = temp2.count(temp[2])
                                        c4 = temp2.count(temp[3])
                                        if c1 >= 2 and c2 >= 2 and c3 >= 2 and c4 >= 2:
                                            for n in [key for key in cellProfile if key[0] == str(i)]:
                                                if n not in [n1, n2, n3, n4]:
                                                    for o in [val for val in cellProfile[n] if val in temp]:
                                                        # console.log("Obvious Quad Col")
                                                        change += 1
                                                        cellProfile[n].remove(o)
                                                        numberProfile[o].remove(n)
                for i in range(1, 10):  # eliminate options if there are quadruples in a row
                    candidates = {key: value for key, value in cellProfile.items() if key[1] == str(i) and 1 < len(value) <= 4}
                    for j in range(len(candidates)):
                        for k in range(j + 1, len(candidates)):
                            for l in range(k + 1, len(candidates)):
                                for m in range(l + 1, len(candidates)):
                                    n1, n2, n3, n4 = list(candidates.keys())[j], list(candidates.keys())[k], list(candidates.keys())[l], list(candidates.keys())[m]
                                    temp = []
                                    temp2 = sorted([*candidates[n1], *candidates[n2], *candidates[n3], *candidates[n4]])
                                    for val in temp2:
                                        if val not in temp:
                                            temp.append(val)
                                    if len(temp) == 4:
                                        c1 = temp2.count(temp[0])
                                        c2 = temp2.count(temp[1])
                                        c3 = temp2.count(temp[2])
                                        c4 = temp2.count(temp[3])
                                        if c1 >= 2 and c2 >= 2 and c3 >= 2 and c4 >= 2:
                                            for n in [key for key in cellProfile if key[1] == str(i)]:
                                                if n not in [n1, n2, n3, n4]:
                                                    for o in [val for val in cellProfile[n] if val in temp]:
                                                        # console.log("Obvious Quad Row")
                                                        change += 1
                                                        cellProfile[n].remove(o)
                                                        numberProfile[o].remove(n)
                if change > 0:
                    log.append(["ObvQuad", change])
                    continue

            # Hidden Single
            if hiddenSingle:
                for i in range(1, 10):  # set for tile with the only number possibility in group
                    group = list(groups[i])
                    unfilled = [val for val in group if val in cellProfile]
                    for j in unfilled:
                        temp = []
                        for k in [val for val in group if val != j]:
                            if k in cellProfile:
                                temp.extend(cellProfile[k])
                            else:
                                temp.append(boardLayout[k])
                        temp2 = []
                        for k in sorted(temp):
                            if k not in temp2:
                                temp2.append(k)
                        for k in cellProfile[j]:
                            if k not in temp2:
                                # console.log(("Hidden Single Group", j, k, cellProfile[j], temp2)
                                for l in [val for val in cellProfile[j] if val != k]:
                                    numberProfile[l].remove(j)
                                cellProfile[j] = [k]
                                change += 1
                for i in range(1, 10):  # set for tile with the only number possibility in col
                    col = [f"{i}{j}" for j in range(1, 10)]
                    unfilled = [val for val in col if val in cellProfile]
                    for j in unfilled:
                        temp = []
                        for k in [val for val in col if val != j]:
                            if k in cellProfile:
                                temp.extend(cellProfile[k])
                            else:
                                temp.append(boardLayout[k])
                        temp2 = []
                        for k in sorted(temp):
                            if k not in temp2:
                                temp2.append(k)
                        for k in cellProfile[j]:
                            if k not in temp2:
                                # console.log(("Hidden Single Col", j, k, cellProfile[j], temp2)
                                for l in [val for val in cellProfile[j] if val != k]:
                                    numberProfile[l].remove(j)
                                cellProfile[j] = [k]
                                change += 1
                for i in range(1, 10):  # set for tile with the only number possibility in row
                    row = [f"{j}{i}" for j in range(1, 10)]
                    unfilled = [val for val in row if val in cellProfile]
                    for j in unfilled:
                        temp = []
                        for k in [val for val in row if val != j]:
                            if k in cellProfile:
                                temp.extend(cellProfile[k])
                            else:
                                temp.append(boardLayout[k])
                        temp2 = []
                        for k in sorted(temp):
                            if k not in temp2:
                                temp2.append(k)
                        for k in cellProfile[j]:
                            if k not in temp2:
                                # console.log(("Hidden Single Row", j, k, cellProfile[j], temp2)
                                for l in [val for val in cellProfile[j] if val != k]:
                                    numberProfile[l].remove(j)
                                cellProfile[j] = [k]
                                change += 1
                if change > 0:
                    log.append(["HiddenSingle", change])
                    continue

            # Hidden Pairs
            if hiddenPair:
                for i in range(1, 10):  # group
                    possibleNum = []
                    for j in groups[i]:
                        if j in cellProfile:
                            possibleNum.extend(cellProfile[j])
                    possibleNum = sorted(possibleNum)
                    for j in range(1, 10):
                        for k in range(1, 10):
                            if j < k:
                                amount1 = 0
                                amount2 = 0
                                if j in possibleNum:
                                    amount1 = possibleNum.count(j)
                                if k in possibleNum:
                                    amount2 = possibleNum.count(k)
                                if amount1 == 2 and amount2 == 2:
                                    for l in range(len(groups[i])):
                                        for m in range(len(groups[i])):
                                            cell1 = groups[i][l]
                                            cell2 = groups[i][m]
                                            empty = cell1 in cellProfile and cell2 in cellProfile
                                            if l < m and empty:
                                                has1 = j in cellProfile[cell1] and k in cellProfile[cell1]
                                                has2 = j in cellProfile[cell2] and k in cellProfile[cell2]
                                                if has1 and has2:
                                                    if str(cellProfile[cell1]) != str([j, k]) or str(cellProfile[cell2]) != str([j, k]):
                                                        # console.log(("Hidden Pair Group")
                                                        change += 1
                                                        cellProfile[cell1] = [j, k]
                                                        cellProfile[cell2] = [j, k]
                                                        for m in numberProfile:
                                                            m = int(m)
                                                            if cell1 in numberProfile[m] and m != j and m != k:
                                                                numberProfile[m].remove(cell1)
                                                            if cell2 in numberProfile[m] and m != j and m != k:
                                                                numberProfile[m].remove(cell2)
                for i in range(1, 10):  # col
                    possibleNum = []
                    for j in range(1, 10):
                        cell = f"{i}{j}"
                        if cell in cellProfile:
                            possibleNum.extend(cellProfile[cell])
                    possibleNum = sorted(possibleNum)
                    for j in range(1, 10):
                        for k in range(1, 10):
                            if j < k:
                                amount1 = 0
                                amount2 = 0
                                if j in possibleNum:
                                    amount1 = possibleNum.count(j)
                                if k in possibleNum:
                                    amount2 = possibleNum.count(k)
                                if amount1 == 2 and amount2 == 2:
                                    for l in range(1, 10):
                                        for m in range(1, 10):
                                            cell1 = f"{i}{l}"
                                            cell2 = f"{i}{m}"
                                            empty = cell1 in cellProfile and cell2 in cellProfile
                                            if l < m and empty:
                                                has1 = j in cellProfile[cell1] and k in cellProfile[cell1]
                                                has2 = j in cellProfile[cell2] and k in cellProfile[cell2]
                                                if has1 and has2:
                                                    if str(cellProfile[cell1]) != str([j, k]) or str(cellProfile[cell2]) != str([j, k]):
                                                        # console.log(("Hidden Pair Row")
                                                        change += 1
                                                        cellProfile[cell1] = [j, k]
                                                        cellProfile[cell2] = [j, k]
                                                        for m in numberProfile:
                                                            m = int(m)
                                                            if cell1 in numberProfile[m] and m != j and m != k:
                                                                numberProfile[m].remove(cell1)
                                                            if cell2 in numberProfile[m] and m != j and m != k:
                                                                numberProfile[m].remove(cell2)
                for i in range(1, 10):  # row
                    possibleNum = []
                    for j in range(1, 10):
                        cell = f"{j}{i}"
                        if cell in cellProfile:
                            possibleNum.extend(cellProfile[cell])
                    possibleNum = sorted(possibleNum)
                    for j in range(1, 10):
                        for k in range(1, 10):
                            if j < k:
                                amount1 = 0
                                amount2 = 0
                                if j in possibleNum:
                                    amount1 = possibleNum.count(j)
                                if k in possibleNum:
                                    amount2 = possibleNum.count(k)
                                if amount1 == 2 and amount2 == 2:
                                    for l in range(1, 10):
                                        for m in range(1, 10):
                                            cell1 = f"{l}{i}"
                                            cell2 = f"{m}{i}"
                                            empty = cell1 in cellProfile and cell2 in cellProfile
                                            if l < m and empty:
                                                has1 = j in cellProfile[cell1] and k in cellProfile[cell1]
                                                has2 = j in cellProfile[cell2] and k in cellProfile[cell2]
                                                if has1 and has2:
                                                    if str(cellProfile[cell1]) != str([j, k]) or str(cellProfile[cell2]) != str([j, k]):
                                                        # console.log(("Hidden Pair Col")
                                                        change += 1
                                                        cellProfile[cell1] = [j, k]
                                                        cellProfile[cell2] = [j, k]
                                                        for m in numberProfile:
                                                            m = int(m)
                                                            if cell1 in numberProfile[m] and m != j and m != k:
                                                                numberProfile[m].remove(cell1)
                                                            if cell2 in numberProfile[m] and m != j and m != k:
                                                                numberProfile[m].remove(cell2)
                if change > 0:
                    log.append(["HiddenPair", change])
                    continue

            # Hidden Triple
            if hiddenTriple:
                for i in range(1, 10):  # group
                    placeholder = {key: value for key, value in cellProfile.items() if any(k in groups[i] for k in key)}
                    candidates = {}
                    for j in placeholder:
                        candidates[j] = placeholder[j]

                    temp = []
                    temp2 = []
                    for cell in candidates:
                        temp2.extend(cellProfile[cell])

                    temp2.sort()
                    temp = list(set(temp2))

                    for j in range(len(temp)):
                        for k in range(j + 1, len(temp)):
                            for l in range(k + 1, len(temp)):
                                cj = temp2.count(temp[j])
                                ck = temp2.count(temp[k])
                                cl = temp2.count(temp[l])
                                if 2 <= cj <= 3 and 2 <= ck <= 3 and 2 <= cl <= 3:
                                    potential = []
                                    for value in candidates:
                                        if temp[j] in cellProfile[value]:
                                            if value not in potential:
                                                potential.append(value)
                                        if temp[k] in cellProfile[value]:
                                            if value not in potential:
                                                potential.append(value)
                                        if temp[l] in cellProfile[value]:
                                            if value not in potential:
                                                potential.append(value)

                                    if len(potential) == 3:
                                        for cell in potential:
                                            if (temp[j] in cellProfile[cell] and temp[k] in cellProfile[cell]) or (temp[j] in cellProfile[cell] and temp[l] in cellProfile[cell]) or (temp[k] in cellProfile[cell] and temp[l] in cellProfile[cell]):
                                                for m in cellProfile[cell]:
                                                    if m not in [temp[j], temp[k], temp[l]]:
                                                        # console.log("Hidden Triple Group")
                                                        change += 1
                                                        cellProfile[cell].remove(m)
                                                        numberProfile[m].remove(cell)
                for i in range(1, 10):  # col
                    placeholder = {key: value for key, value in cellProfile.items() if key[0] == str(i)}
                    candidates = {}
                    for j in placeholder:
                        candidates[j] = placeholder[j]

                    temp = []
                    temp2 = []
                    for cell in candidates:
                        temp2.extend(cellProfile[cell])

                    temp2.sort()
                    temp = list(set(temp2))

                    for j in range(len(temp)):
                        for k in range(j + 1, len(temp)):
                            for l in range(k + 1, len(temp)):
                                cj = temp2.count(temp[j])
                                ck = temp2.count(temp[k])
                                cl = temp2.count(temp[l])
                                if 2 <= cj <= 3 and 2 <= ck <= 3 and 2 <= cl <= 3:
                                    potential = []
                                    for value in candidates:
                                        if temp[j] in cellProfile[value]:
                                            if value not in potential:
                                                potential.append(value)
                                        if temp[k] in cellProfile[value]:
                                            if value not in potential:
                                                potential.append(value)
                                        if temp[l] in cellProfile[value]:
                                            if value not in potential:
                                                potential.append(value)

                                    if len(potential) == 3:
                                        for cell in potential:
                                            if (temp[j] in cellProfile[cell] and temp[k] in cellProfile[cell]) or (temp[j] in cellProfile[cell] and temp[l] in cellProfile[cell]) or (temp[k] in cellProfile[cell] and temp[l] in cellProfile[cell]):
                                                for m in cellProfile[cell]:
                                                    if m not in [temp[j], temp[k], temp[l]]:
                                                        # console.log("Hidden Triple Col")
                                                        change += 1
                                                        cellProfile[cell].remove(m)
                                                        numberProfile[m].remove(cell)
                for i in range(1, 10):  # row
                    placeholder = {key: value for key, value in cellProfile.items() if key[1] == str(i)}
                    candidates = {}
                    for j in placeholder:
                        candidates[j] = placeholder[j]

                    temp = []
                    temp2 = []
                    for cell in candidates:
                        temp2.extend(cellProfile[cell])

                    temp2.sort()
                    temp = list(set(temp2))

                    for j in range(len(temp)):
                        for k in range(j + 1, len(temp)):
                            for l in range(k + 1, len(temp)):
                                cj = temp2.count(temp[j])
                                ck = temp2.count(temp[k])
                                cl = temp2.count(temp[l])
                                if 2 <= cj <= 3 and 2 <= ck <= 3 and 2 <= cl <= 3:
                                    potential = []
                                    for value in candidates:
                                        if temp[j] in cellProfile[value]:
                                            if value not in potential:
                                                potential.append(value)
                                        if temp[k] in cellProfile[value]:
                                            if value not in potential:
                                                potential.append(value)
                                        if temp[l] in cellProfile[value]:
                                            if value not in potential:
                                                potential.append(value)

                                    if len(potential) == 3:
                                        for cell in potential:
                                            if (temp[j] in cellProfile[cell] and temp[k] in cellProfile[cell]) or (temp[j] in cellProfile[cell] and temp[l] in cellProfile[cell]) or (temp[k] in cellProfile[cell] and temp[l] in cellProfile[cell]):
                                                for m in cellProfile[cell]:
                                                    if m not in [temp[j], temp[k], temp[l]]:
                                                        # console.log("Hidden Triple Row", cell, m, [temp[j], temp[k], temp[l]])
                                                        change += 1
                                                        cellProfile[cell].remove(m)
                                                        numberProfile[m].remove(cell)
                if change > 0:
                    log.append(["HiddenTriple", change])
                    continue

            # Hidden Quads
            if hiddenQuad:
                for i in range(1, 10):  # group
                    placeholder = {key: value for key, value in cellProfile.items() if any(k in groups[i] for k in key)}
                    candidates = {}
                    for j in placeholder:
                        candidates[j] = placeholder[j]

                    temp = []
                    temp2 = []
                    for cell in candidates:
                        temp2.extend(cellProfile[cell])

                    temp2.sort()
                    temp = list(set(temp2))

                    for j in range(len(temp)):
                        for k in range(j + 1, len(temp)):
                            for l in range(k + 1, len(temp)):
                                for m in range(l + 1, len(temp)):
                                    cj = temp2.count(temp[j])
                                    ck = temp2.count(temp[k])
                                    cl = temp2.count(temp[l])
                                    cm = temp2.count(temp[m])
                                    if 2 <= cj <= 4 and 2 <= ck <= 4 and 2 <= cl <= 4 and 2 <= cm <= 4:
                                        potential = []
                                        for value in candidates:
                                            if temp[j] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)
                                            if temp[k] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)
                                            if temp[l] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)
                                            if temp[m] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)

                                        if len(potential) == 4:
                                            for cell in potential:
                                                conj = temp[j] in cellProfile[cell]
                                                conk = temp[k] in cellProfile[cell]
                                                conl = temp[l] in cellProfile[cell]
                                                conm = temp[m] in cellProfile[cell]
                                                if (conj and conk) or (conj and conl) or (conj and conm) or (conk and conl) or (conk and conm) or (conl and conm):
                                                    for n in cellProfile[cell]:
                                                        if n not in [temp[j], temp[k], temp[l], temp[m]]:
                                                            # console.log("Hidden Quad Group")
                                                            change += 1
                                                            cellProfile[cell].remove(n)
                                                            numberProfile[n].remove(cell)
                for i in range(1, 10):  # col
                    placeholder = {key: value for key, value in cellProfile.items() if key[0] == str(i)}
                    candidates = {}
                    for j in placeholder:
                        candidates[j] = placeholder[j]

                    temp = []
                    temp2 = []
                    for cell in candidates:
                        temp2.extend(cellProfile[cell])

                    temp2.sort()
                    temp = list(set(temp2))

                    for j in range(len(temp)):
                        for k in range(j + 1, len(temp)):
                            for l in range(k + 1, len(temp)):
                                for m in range(l + 1, len(temp)):
                                    cj = temp2.count(temp[j])
                                    ck = temp2.count(temp[k])
                                    cl = temp2.count(temp[l])
                                    cm = temp2.count(temp[m])
                                    if 2 <= cj <= 4 and 2 <= ck <= 4 and 2 <= cl <= 4 and 2 <= cm <= 4:
                                        potential = []
                                        for value in candidates:
                                            if temp[j] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)
                                            if temp[k] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)
                                            if temp[l] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)
                                            if temp[m] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)

                                        if len(potential) == 4:
                                            for cell in potential:
                                                conj = temp[j] in cellProfile[cell]
                                                conk = temp[k] in cellProfile[cell]
                                                conl = temp[l] in cellProfile[cell]
                                                conm = temp[m] in cellProfile[cell]
                                                if (conj and conk) or (conj and conl) or (conj and conm) or (conk and conl) or (conk and conm) or (conl and conm):
                                                    for n in cellProfile[cell]:
                                                        if n not in [temp[j], temp[k], temp[l], temp[m]]:
                                                            # console.log("Hidden Quad Col")
                                                            change += 1
                                                            cellProfile[cell].remove(n)
                                                            numberProfile[n].remove(cell)
                for i in range(1, 10):  # row
                    placeholder = {key: value for key, value in cellProfile.items() if key[1] == str(i)}
                    candidates = {}
                    for j in placeholder:
                        candidates[j] = placeholder[j]

                    temp = []
                    temp2 = []
                    for cell in candidates:
                        temp2.extend(cellProfile[cell])

                    temp2.sort()
                    temp = list(set(temp2))

                    for j in range(len(temp)):
                        for k in range(j + 1, len(temp)):
                            for l in range(k + 1, len(temp)):
                                for m in range(l + 1, len(temp)):
                                    cj = temp2.count(temp[j])
                                    ck = temp2.count(temp[k])
                                    cl = temp2.count(temp[l])
                                    cm = temp2.count(temp[m])
                                    if 2 <= cj <= 4 and 2 <= ck <= 4 and 2 <= cl <= 4 and 2 <= cm <= 4:
                                        potential = []
                                        for value in candidates:
                                            if temp[j] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)
                                            if temp[k] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)
                                            if temp[l] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)
                                            if temp[m] in cellProfile[value]:
                                                if value not in potential:
                                                    potential.append(value)

                                        if len(potential) == 4:
                                            for cell in potential:
                                                conj = temp[j] in cellProfile[cell]
                                                conk = temp[k] in cellProfile[cell]
                                                conl = temp[l] in cellProfile[cell]
                                                conm = temp[m] in cellProfile[cell]
                                                if (conj and conk) or (conj and conl) or (conj and conm) or (conk and conl) or (conk and conm) or (conl and conm):
                                                    for n in cellProfile[cell]:
                                                        if n not in [temp[j], temp[k], temp[l], temp[m]]:
                                                            # console.log("Hidden Quad Col")
                                                            change += 1
                                                            cellProfile[cell].remove(n)
                                                            numberProfile[n].remove(cell)
                if change > 0:
                    log.append(["HiddenQuad", change])
                    continue

            # Pointing Pairs & Pointing Triple
            if pointingPairTriple:
                for i in groups:
                    possibleNum = []
                    temp = [val for val in groups[i] if val in cellProfile]
                    for j in temp:
                        possibleNum.extend(cellProfile[j])

                    possibleNum.sort()
                    temp2 = list(set(possibleNum))

                    for j in temp2:
                        amount = possibleNum.count(j)
                        if amount == 2:
                            neighbors = [val for val in temp if j in cellProfile[val]]
                            if neighbors[0][0] == neighbors[1][0]:
                                for k in range(1, 10):
                                    cell = f"{neighbors[0][0]}{k}"
                                    if cell in cellProfile and cell not in neighbors and len(cellProfile[cell]) != 1 and j in cellProfile[cell]:
                                        # console.log("Pointing Pair Row")
                                        change += 1
                                        cellProfile[cell].remove(j)
                                        numberProfile[j].remove(cell)
                            elif neighbors[0][1] == neighbors[1][1]:
                                for k in range(1, 10):
                                    cell = f"{k}{neighbors[0][1]}"
                                    if cell in cellProfile and cell not in neighbors and len(cellProfile[cell]) != 1 and j in cellProfile[cell]:
                                        # console.log("Pointing Pair Col")
                                        change += 1
                                        cellProfile[cell].remove(j)
                                        numberProfile[j].remove(cell)
                        elif amount == 3:
                            neighbors = [val for val in temp if j in cellProfile[val]]
                            if neighbors[0][0] == neighbors[1][0] and neighbors[1][0] == neighbors[2][0]:
                                for k in range(1, 10):
                                    cell = f"{neighbors[0][0]}{k}"
                                    if cell in cellProfile and cell not in neighbors and len(cellProfile[cell]) != 1 and j in cellProfile[cell]:
                                        # console.log("Pointing Triple Row")
                                        change += 1
                                        cellProfile[cell].remove(j)
                                        numberProfile[j].remove(cell)
                            elif neighbors[0][1] == neighbors[1][1] and neighbors[1][1] == neighbors[2][1]:
                                for k in range(1, 10):
                                    cell = f"{k}{neighbors[0][1]}"
                                    if cell in cellProfile and cell not in neighbors and len(cellProfile[cell]) != 1 and j in cellProfile[cell]:
                                        # console.log("Pointing Triple Col")
                                        change += 1
                                        cellProfile[cell].remove(j)
                                        numberProfile[j].remove(cell)
                if change > 0:
                    log.append(["PointingPairTriple", change])
                    continue

            # Box Line Reduction
            if boxLineReduc:
                # iter through rows per group
                # for each number, save group & row
                # for each row, if num of groups == 1: remove other rows in that group
                for i in range(1, 9, 3):
                    g1, g2, g3 = i, i + 1, i + 2
                    for j in numberProfile:
                        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        for k in numberProfile[j]:
                            if k in groups[g1] or k in groups[g2] or k in groups[g3]:
                                group = math.ceil(int(k[0])/3) -1
                                row = (int(k[1]) % 3) - 1 if int(k[1]) % 3 != 0 else 2
                                c[row][group] += 1
                        for row in range(len(c)):
                            total = sum(c[row])
                            max_val = max(c[row])
                            if total == max_val and max_val > 0:
                                for k in sorted(numberProfile[j]):
                                    group = math.ceil(int(k[1])/3)*3 - 3 + math.ceil(int(k[0])/3)
                                    tRow = int(k[1])
                                    if [g1, g2, g3][c[row].index(total)] == group:
                                        if tRow == row + g1:
                                            continue
                                        #print("Box Line Reduction Horizontal", k, j)
                                        change += 1
                                        cellProfile[k].remove(j)
                                        numberProfile[j].remove(k)
                # Iterate through cols per group
                for i in range(1, 4):
                    g1, g2, g3 = i, i + 3, i + 6
                    for j in numberProfile.keys():
                        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        for k in numberProfile[j]:
                            if k in groups[g1] or k in groups[g2] or k in groups[g3]:
                                group = math.ceil(int(k[1]) / 3) - 1
                                col = (int(k[0]) % 3) - 1 if int(k[0]) % 3 != 0 else 2
                                c[col][group] += 1
                        for col in range(3):
                            total = sum(c[col])
                            max_val = max(c[col])
                            if total == max_val and max_val > 0:
                                for k in sorted(numberProfile[j]):
                                    group = math.ceil(int(k[1]) / 3) * 3 - 3 + math.ceil(int(k[0]) / 3)
                                    tCol = int(k[0])
                                    if [g1, g2, g3][c[col].index(total)] == group:
                                        if tCol == g1 * 3 - 2 + col:
                                            continue
                                        # console.log(("Box Line Reduction Vertical", k))
                                        change += 1
                                        cellProfile[k].remove(j)
                                        numberProfile[j].remove(k)
                if change > 0:
                    log.append(["Box Line Reduction", change])
                    continue

            # Rectangle Elimination
            if rectElim:
                for i in numberProfile:
                    for hinge in sorted(numberProfile[i]):
                        hGroup = math.ceil(int(hinge[1]) / 3) * 3 - 3 + math.ceil(int(hinge[0]) / 3)
                        colN = [value for value in numberProfile[i] if value[0] == hinge[0] and value != hinge and value not in groups[hGroup]]
                        rowN = [value for value in numberProfile[i] if value[1] == hinge[1] and value != hinge and value not in groups[hGroup]]
                        for k in range(len(colN)):
                            for l in range(len(rowN)):
                                tGroup = math.ceil(int(colN[k][1]) / 3) * 3 - 3 + math.ceil(int(rowN[l][0]) / 3)
                                checkL = [value for value in numberProfile[i] if value in groups[tGroup]]
                                cond = len(checkL) > 0
                                for m in checkL:
                                    if m[0] != rowN[l][0] and m[1] != colN[k][1]:
                                        cond = False
                                if cond:
                                    rStr = link(hinge, rowN[l], i)[0]
                                    cStr = link(hinge, colN[k], i)[0]
                                    if rStr:
                                        #print("Rectangle Elimination", colN[k], hinge, rowN[l])
                                        cellProfile[colN[k]].remove(i)
                                        numberProfile[i].remove(colN[k])
                                        change += 1
                                    if cStr:
                                        #print("Rectangle Elimination", rowN[l], hinge, colN[k])
                                        cellProfile[rowN[l]].remove(i)
                                        numberProfile[i].remove(rowN[l])
                                        change += 1
                if change > 0:
                    log.append(["Rectangle Elimination", change])
                    continue

            # X-wing
            if xWing:
                for cell1 in cellProfile.keys():
                    for j in range(1, 10):
                        if int(j) <= int(cell1[0]):
                            continue
                        for k in range(1, 10):
                            if int(k) <= int(cell1[1]):
                                continue
                            cell2 = f"{j}{cell1[1]}"
                            if cell2 not in cellProfile:
                                continue
                            cell3 = f"{cell1[0]}{k}"
                            if cell3 not in cellProfile:
                                continue
                            cell4 = f"{j}{k}"
                            if cell4 not in cellProfile:
                                continue
                            possibility = []
                            for l in range(1, 10):
                                if l in cellProfile[cell1] and l in cellProfile[cell2] and l in cellProfile[cell3] and l in cellProfile[cell4]:
                                    possibility.append(l)
                            if len(possibility) == 1:
                                conditionRow = True
                                conditionCol = True
                                n = possibility[0]
                                for l in range(1, 10):
                                    target = f"{l}{cell1[1]}"
                                    if target not in [cell1, cell2] and target in cellProfile:
                                        if n in cellProfile[target]:
                                            conditionRow = False
                                    target = f"{l}{cell3[1]}"
                                    if target not in [cell3, cell4] and target in cellProfile:
                                        if n in cellProfile[target]:
                                            conditionRow = False
                                    target = f"{cell1[0]}{l}"
                                    if target not in [cell1, cell3] and target in cellProfile:
                                        if n in cellProfile[target]:
                                            conditionCol = False
                                    target = f"{cell2[0]}{l}"
                                    if target not in [cell2, cell4] and target in cellProfile:
                                        if n in cellProfile[target]:
                                            conditionCol = False
                                if conditionRow != conditionCol:
                                    if conditionRow:
                                        for l in range(1, 10):
                                            target = f"{cell1[0]}{l}"
                                            if target not in [cell1, cell3] and target in cellProfile:
                                                if n in cellProfile[target]:
                                                    # console.log(("X-Wing", target, n))
                                                    change += 1
                                                    cellProfile[target].remove(n)
                                                    numberProfile[n].remove(target)
                                            target = f"{cell2[0]}{l}"
                                            if target not in [cell2, cell4] and target in cellProfile:
                                                if n in cellProfile[target]:
                                                    # console.log(("X-Wing", target, n))
                                                    change += 1
                                                    cellProfile[target].remove(n)
                                                    numberProfile[n].remove(target)
                                    if conditionCol:
                                        for l in range(1, 10):
                                            target = f"{l}{cell1[1]}"
                                            if target not in [cell1, cell2] and target in cellProfile:
                                                if n in cellProfile[target]:
                                                    # console.log(("X-Wing", target, n))
                                                    change += 1
                                                    cellProfile[target].remove(n)
                                                    numberProfile[n].remove(target)
                                            target = f"{l}{cell3[1]}"
                                            if target not in [cell3, cell4] and target in cellProfile:
                                                if n in cellProfile[target]:
                                                    # console.log(("X-Wing", target, n))
                                                    change += 1
                                                    cellProfile[target].remove(n)
                                                    numberProfile[n].remove(target)
                if change > 0:
                    log.append(["X-Wing", change])
                    continue

            # Y-wing
            if yWing:
                for cell1 in cellProfile.keys():
                    if len(cellProfile[cell1]) != 2:
                        continue
                    group1 = math.ceil(int(cell1[1]) / 3) * 3 - 3 + math.ceil(int(cell1[0]) / 3)
                    checkRow = [val for val in groups[group1] if val in cellProfile]
                    checkCol = [val for val in groups[group1] if val in cellProfile]
                    for j in range(1, 10):
                        cell2 = f"{j}{cell1[1]}"
                        if cell2 in cellProfile and cell2 not in checkRow:
                            checkRow.append(cell2)
                        cell3 = f"{cell1[0]}{j}"
                        if cell3 in cellProfile and cell3 not in checkCol:
                            checkCol.append(cell3)
                    checkRow = [val for val in checkRow if val != cell1 and len(cellProfile[val]) == 2 and (cellProfile[val][0] != cellProfile[cell1][0] or cellProfile[val][1] != cellProfile[cell1][1])]
                    checkCol = [val for val in checkCol if val != cell1 and len(cellProfile[val]) == 2 and (cellProfile[val][0] != cellProfile[cell1][0] or cellProfile[val][1] != cellProfile[cell1][1])]
                    for cell2 in checkRow:
                        for cell3 in checkCol:
                            if cell2[0] == cell3[0] or cell2[1] == cell3[1]:
                                continue
                            if cellProfile[cell2][0] == cellProfile[cell3][0] and cellProfile[cell2][1] == cellProfile[cell3][1]:
                                continue
                            temp = list(set(cellProfile[cell1] + cellProfile[cell2] + cellProfile[cell3]))
                            temp.sort()
                            if len(temp) != 3:
                                continue
                            group2 = math.ceil(int(cell2[1]) / 3) * 3 - 3 + math.ceil(int(cell2[0]) / 3)
                            group3 = math.ceil(int(cell3[1]) / 3) * 3 - 3 + math.ceil(int(cell3[0]) / 3)
                            if group2 != group3:
                                set2 = [val for val in groups[group2] if val in cellProfile]
                                set3 = [val for val in groups[group3] if val in cellProfile]
                                for i in range(1, 10):
                                    if f"{cell2[0]}{i}" not in set2:
                                        set2.append(f"{cell2[0]}{i}")
                                    if f"{i}{cell2[1]}" not in set2:
                                        set2.append(f"{i}{cell2[1]}")
                                    if f"{cell3[0]}{i}" not in set3:
                                        set3.append(f"{cell3[0]}{i}")
                                    if f"{i}{cell3[1]}" not in set3:
                                        set3.append(f"{i}{cell3[1]}")
                                set2 = [val for val in set2 if val in cellProfile]
                                set3 = [val for val in set3 if val in cellProfile]
                                numCheck = [val for val in temp if val not in cellProfile[cell1]][0]
                                setCheck = [val for val in set2 if val in set3 and numCheck in cellProfile[val]]
                                for i in setCheck:
                                    # console.log(("Y-Wing", i, cellProfile[i], numCheck, [cell1, cell2, cell3], cellProfile[cell1], cellProfile[cell2], cellProfile[cell3]))
                                    cellProfile[i].remove(numCheck)
                                    numberProfile[numCheck].remove(i)
                                    change += 1
                if change > 0:
                    log.append(["Y-Wing", change])
                    continue

            # Swordfish
            if swordfish:
                for i in numberProfile.keys():
                    conG = []
                    for j in range(1, 10):
                        temp = False
                        for k in filter(lambda val: val in cellProfile.keys(), groups[j]):
                            if i in cellProfile[k]:
                                temp = True
                        conG.append(temp)
                    if all(conG):
                        continue
                    if len(numberProfile[i]) >= 6:
                        for j in range(1, 10):
                            if len([val for val in numberProfile[i] if val[1] == str(j)]) < 2:
                                continue
                            for k in range(j + 1, 10):
                                if len([val for val in numberProfile[i] if val[1] == str(k)]) < 2:
                                    continue
                                for l in range(k + 1, 10):
                                    if len([val for val in numberProfile[i] if val[1] == str(l)]) < 2:
                                        continue
                                    for m in range(1, 10):
                                        if len([val for val in numberProfile[i] if val[0] == str(m)]) < 2:
                                            continue
                                        for n in range(m + 1, 10):
                                            if len([val for val in numberProfile[i] if val[0] == str(n)]) < 2:
                                                continue
                                            for o in range(n + 1, 10):
                                                if len([val for val in numberProfile[i] if val[0] == str(o)]) < 2:
                                                    continue
                                                temp = [[f"{m}{j}", f"{n}{j}", f"{o}{j}"],
                                                        [f"{m}{k}", f"{n}{k}", f"{o}{k}"],
                                                        [f"{m}{l}", f"{n}{l}", f"{o}{l}"],
                                                        [f"{m}{j}", f"{m}{k}", f"{m}{l}"],
                                                        [f"{n}{j}", f"{n}{k}", f"{n}{l}"],
                                                        [f"{o}{j}", f"{o}{k}", f"{o}{l}"]]
                                                check = []
                                                terminator = False
                                                for p in filter(lambda val: val in cellProfile.keys(), [item for sublist in temp for item in sublist]):
                                                    if i in cellProfile[p]:
                                                        check.append(p)
                                                    else:
                                                        terminator = False
                                                if terminator:
                                                    continue
                                                if len(check) >= 6:
                                                    conCol = True
                                                    conRow = True
                                                    for p in range(1, 10):
                                                        if (f"{p}{j}" in cellProfile and 
                                                            f"{p}{j}" in numberProfile[i] and 
                                                            f"{p}{j}" not in check):
                                                            conRow = False
                                                        if (f"{p}{k}" in cellProfile and 
                                                            f"{p}{k}" in numberProfile[i] and 
                                                            f"{p}{k}" not in check):
                                                            conRow = False
                                                        if (f"{p}{l}" in cellProfile and 
                                                            f"{p}{l}" in numberProfile[i] and 
                                                            f"{p}{l}" not in check):
                                                            conRow = False
                                                        if (f"{m}{p}" in cellProfile and 
                                                            f"{m}{p}" in numberProfile[i] and 
                                                            f"{m}{p}" not in check):
                                                            conCol = False
                                                        if (f"{n}{p}" in cellProfile and 
                                                            f"{n}{p}" in numberProfile[i] and 
                                                            f"{n}{p}" not in check):
                                                            conCol = False
                                                        if (f"{o}{p}" in cellProfile and 
                                                            f"{o}{p}" in numberProfile[i] and 
                                                            f"{o}{p}" not in check):
                                                            conCol = False
                                                        if not conCol and not conRow:
                                                            break
                                                    if conCol != conRow:
                                                        if conRow:
                                                            for p in range(1, 10):
                                                                for target in [f"{m}{p}", f"{n}{p}", f"{o}{p}"]:
                                                                    if target in cellProfile and target in numberProfile[i] and target not in check:
                                                                        change += 1
                                                                        cellProfile[target].remove(i)
                                                                        numberProfile[i].remove(target)
                                                        if conCol:
                                                            for p in range(1, 10):
                                                                for target in [f"{p}{j}", f"{p}{k}", f"{p}{l}"]:
                                                                    if target in cellProfile and target in numberProfile[i] and target not in check:
                                                                        change += 1
                                                                        cellProfile[target].remove(i)
                                                                        numberProfile[i].remove(target)
                if change > 0:
                    log.append(["Swordfish", change])
                    continue

            if change > 0:
                continue
            else:
                break
    except ValueError:
        print("ValErr")
    except KeyError:
        print("KeyErr")
    except ZeroDivisionError:
        print("zero")
    except TypeError:
        print("Type")
    except SyntaxError:
        print("Syntax")
    except ReferenceError:
        print("REf")
    except NameError:
        print("Name")
    except IndexError:
        print("Index")
    except ArithmeticError:
        print("Arith")
    except AttributeError:
        print("Attr")
    except:
        print("Error", log)
        return ["Incorrect"]
    if True:
        state = "Eval"
        outputBoard = ""
        for i in cells:
            outputBoard += str(boardLayout[i])
        
        groupProfile = {}
        for i in range(1, 10):
            for j in groups[i]:
                if j in cellProfile and cellProfile[j]:
                    groupProfile[j] = cellProfile[j]
        
        for i in cells:
            if boardLayout[i] == 0:
                state = "Incomplete"
        
        if state == "Incomplete":
            for i in cells:
                if boardLayout[i] == 0:
                    state = "Incorrect"
                    # print("Incorrect Empty Cell:", cells[i])
        else:
            for i in cells:
                if boardLayout[i] == 0:
                    state = "Incorrect"
                    # print("Incorrect Empty Cell:", cells[i])
            
            for i in range(1, 10):
                rowNumbers = []
                colNumbers = []
                for j in range(1, 10):
                    number = boardLayout[f"{j}{i}"]
                    if number not in rowNumbers:
                        rowNumbers.append(number)
                    else:
                        state = "Incorrect"
                        # print("Incorrect Row:", f"{j}{i}", number)
                    
                    number = boardLayout[f"{i}{j}"]
                    if number not in colNumbers:
                        colNumbers.append(number)
                    else:
                        state = "Incorrect"
                        # print("Incorrect Col:", f"{i}{j}", number)
        
        if state == "Eval":
            state = "Success"
        
        # print(state, outputBoard)
        c = sum(1 for i in outputBoard if i != "0")
        # print(f"{c}/81")
        # if state == "Success":
        #     print(log)
        
        return [state, outputBoard, log, step]

def checkUnique(key):
    b = []
    map = []
    for i in range(len(key)):
        b.append(int(key[i]))
        if key[i]=="0":
            map.append(i)
    def solver1(key):
        b = []
        for i in key:
            b.append(int(i))
        check = True
        for i in range(0,9):
            test1 = [1,2,3,4,5,6,7,8,9]
            test2 = [1,2,3,4,5,6,7,8,9]
            for j in range(0,9):
                if b[i*9+j]==0:
                    continue
                try:
                    test1.pop(test1.index(b[i*9+j]))
                except:
                    check = False
            for j in range(0,9):
                if b[j*9+i]==0:
                    continue
                try:
                    test2.pop(test2.index(b[j*9+i]))
                except:
                    check = False
            g = math.floor(i/3)*27+i%3*3
            test = [1,2,3,4,5,6,7,8,9]
            for j in range(0,3):
                for k in range(0,3):
                    if b[g+j*9+k]==0:
                        continue
                    try:
                        test.pop(test.index(b[g+j*9+k]))
                    except:
                        check = False
        if check==True:
            return ["Success"]
        else:
            return ["Incorrect"]
    def recurse(mt, bt, key, n):
        print("|"*n)
        while True:
            count = 0
            for i in mt:
                c = 0
                iter = [1,2,3,4,5,6,7,8,9]
                g = math.floor(i/27)*27+math.floor((i%9)/3)*3
                for j in range(0,3):
                    for k in range(0,3):
                        if (g+j+k*9!=i and iter.count(bt[g+j+k*9])!=0):
                            iter.remove(bt[g+j+k*9])
                for j in range(0,9):
                    if (i-i%9+j!=i and iter.count(bt[i-i%9+j])!=0):
                        iter.remove(bt[i-i%9+j])
                    if (i%9+9*j!=i and iter.count(bt[i%9+9*j])!=0):
                        iter.remove(bt[i%9+9*j])
                if len(iter)==1:
                    bt[i] = iter[0]
                    mt.remove(i)
                    count+=1
                if len(iter)==0:
                    return False
            if count==0:
                break
        if len(mt)>0:
            c = 0
            iter = [1,2,3,4,5,6,7,8,9]
            g = math.floor(mt[0]/27)*27+math.floor((mt[0]%9)/3)*3
            for j in range(0,3):
                for k in range(0,3):
                    if (g+j+k*9!=mt[0] and iter.count(bt[g+j+k*9])!=0):
                        iter.remove(bt[g+j+k*9])
            for j in range(0,9):
                if (mt[0]-mt[0]%9+j!=mt[0] and iter.count(bt[mt[0]-mt[0]%9+j])!=0):
                    iter.remove(bt[mt[0]-mt[0]%9+j])
                if (mt[0]%9+9*j!=mt[0] and iter.count(bt[mt[0]%9+9*j])!=0):
                    iter.remove(bt[mt[0]%9+9*j])
            for j in iter:
                copy = bt.copy()
                copy[mt[0]] = j
                test = ""
                for k in copy:
                    test += str(k)
                r = solver1(test)
                s = r[0]
                if s=="Success":
                    mt2 = mt.copy()
                    mt2.pop(0)
                    a = recurse(mt2, copy, key, n+1)
        else:
            check = True
            for i in range(0,9):
                test1 = [1,2,3,4,5,6,7,8,9]
                test2 = test1.copy()
                for j in range(0,9):
                    try:
                        test1.pop(test1.index(bt[i*9+j]))
                        test2.pop(test1.index(bt[j*9+i]))
                    except:
                        check = False
                g = math.floor(i/3)*27+i%3*3
                test = test1.copy()
                for j in range(0,3):
                    for k in range(0,3):
                        try:
                            test.pop(test.index(bt[g+j*9+k]))
                        except:
                            check = False
            t = ""
            for i in bt:
                t+=str(i)
            solutions.append(t)
            #print(t, len(history))
    solutions = []
    recurse(map, b, key, 1)
    if len(solutions)==0:
        return "No Solutions"
    elif len(solutions)==1:
        return f"1 Unique Solution: \n{solutions[0]}"
    elif len(solutions)>1:
        return f"Multiple Solutions: {len(solutions)}"
    

print(checkUnique("500000000000860000000751020008007093002093500000180070007216000000000830000000000"))
#print(solver("467281539153690004800003070720030100918000000530900000341067000270000008600020000"))