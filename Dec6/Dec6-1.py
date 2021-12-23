inp = []
with open('Dec6/Dec6-data.txt') as f:
    inp = list(map(lambda x: int(x), f.read().split(",")))
count = 0
while count < 80:
    inp = [x - 1 for x in inp]
    length = len(inp)
    for x in range(len(inp)):
        if inp[x] == -1:
            inp[x] = 6
            inp.append(8)
    count += 1
print(len(inp))
