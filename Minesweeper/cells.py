row = 9
col = 9

cells = []

for i in range(row):
    for j in range(col):
        cells.append(str(chr(65+i))+str(j+1))
print(cells)

cells2 = []
for i in range(row):
    for j in range(col):
        cells2.append(str(i+1)+str(j+1))
print(cells2)