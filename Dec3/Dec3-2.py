with open('Dec3/Dec3-data.txt') as f:
    lines = f.read().splitlines()


length = len(lines[0])
numOfLines = len(lines)

mc = [0] * length  # most common

for l in lines:
    for i in range(length):
        if int(l[i]) == 1:
            mc[i] += 1

mc1 = [0] * length  # most common 1s
mc0 = [0] * length  # inverse of mc1

for i in range(length):
    if mc[i] > numOfLines / 2:
        mc1[i] = 1
        mc0[i] = 0
    else:
        mc1[i] = 0
        mc0[i] = 1

# calculating  oxygen generator rating
ogr = 0  # oxygen generator rating
cb = 0  # current bit
numbersLeft = lines
while cb < length and len(numbersLeft) > 1:
    numberOf1s = 0
    for l in numbersLeft:
        if int(l[cb]) == 1:
            numberOf1s += 1
    if numberOf1s > len(numbersLeft) / 2:
        numbersLeft = [l for l in numbersLeft if int(l[cb]) == 1]
    elif numberOf1s < len(numbersLeft) / 2:
        numbersLeft = [l for l in numbersLeft if int(l[cb]) == 0]
    else:
        numbersLeft = [l for l in numbersLeft if int(l[cb]) == 1]
    cb += 1

ogr = int(numbersLeft[0], 2)

# calculating CO2 scrubber rating
csr = 0  # CO2 scrubber rating
cb = 0  # current bit
numbersLeft = lines
while cb < length and len(numbersLeft) > 1:
    numberOf0s = 0
    for l in numbersLeft:
        if int(l[cb]) == 0:
            numberOf0s += 1
    if numberOf0s > len(numbersLeft) / 2:
        numbersLeft = [l for l in numbersLeft if int(l[cb]) == 1]
    elif numberOf0s < len(numbersLeft) / 2:
        numbersLeft = [l for l in numbersLeft if int(l[cb]) == 0]
    else:
        numbersLeft = [l for l in numbersLeft if int(l[cb]) == 0]
    cb += 1
csr = int(numbersLeft[0], 2)

lsr = ogr * csr  # life support rating
print(lsr)
