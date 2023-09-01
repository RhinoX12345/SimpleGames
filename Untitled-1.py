ltrList = "ABCDEFGH"
numList = "12345678"
coordList = []
for a in ltrList:
    for b in numList:
        coord = a + b
        coordList.append(coord)
print(coordList)
#test