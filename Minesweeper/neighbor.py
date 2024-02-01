cells = [
    'A1','A2','A3','A4','A5','A6','A7','A8',
    'B1','B2','B3','B4','B5','B6','B7','B8',
    'C1','C2','C3','C4','C5','C6','C7','C8',
    'D1','D2','D3','D4','D5','D6','D7','D8',
    'E1','E2','E3','E4','E5','E6','E7','E8',
    'F1','F2','F3','F4','F5','F6','F7','F8',
    'G1','G2','G3','G4','G5','G6','G7','G8',
    'H1','H2','H3','H4','H5','H6','H7','H8']
rows = ["A","B","C","D","E","F","G","H"]
neighborDict = {}
for i in cells:
    neighbors = []
    index = cells.index(i)
    row = rows.index(i[0])
    if (index-9)>=0 and rows.index(cells[index-9][0])==row-1:
        neighbors.append(cells[index-9])
    if (index-8)>=0 and rows.index(cells[index-8][0])==row-1:
        neighbors.append(cells[index-8])
    if (index-7)>=0 and rows.index(cells[index-7][0])==row-1:
        neighbors.append(cells[index-7])
    if (index-1)>=0 and rows.index(cells[index-1][0])==row:
        neighbors.append(cells[index-1])
    if (index+1)<=len(cells)-1 and rows.index(cells[index+1][0])==row:
        neighbors.append(cells[index+1])
    if (index+7)<=len(cells)-1 and rows.index(cells[index+7][0])==row+1:
        neighbors.append(cells[index+7])
    if (index+8)<=len(cells)-1 and rows.index(cells[index+8][0])==row+1:
        neighbors.append(cells[index+8])
    if (index+9)<=len(cells)-1 and rows.index(cells[index+9][0])==row+1:
        neighbors.append(cells[index+9])
    neighborDict[i] = neighbors
print(neighborDict)