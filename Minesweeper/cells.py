row = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
cells = []
rows,cols = {}

for i in row:
    for j in range(len(row)):
        col = str(j+1)
        cell = i + col
        cells.append(cell)
print(cells)
print()

for i in row:
    tempcells = []
    for j in range(len(row)):
        col = str(j+1)
        cell = i + col
        tempcells.append(cell)
    rows[i] = tempcells
print(rows)
print()

for i in range(len(row)):
    col = str(i+1)
    tempcells = []
    for j in row:
        cell = j + col
        tempcells.append(cell)
    cols[col] = tempcells
print(cols)