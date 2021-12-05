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

print(mc1)
print(mc0)
gr = int(''.join(map(str, mc1)), 2)
er = int(''.join(map(str, mc0)), 2)
print(gr)
print(er)
print(gr * er)  # consumption
