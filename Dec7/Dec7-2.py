with open('Dec7/Dec7-data.txt') as f:
    inp = list(map(lambda x: int(x), f.read().split(",")))
min = False
for x in range(max(inp)):
    totalCost = 0
    for _ in inp:
        change = abs(_ - x)
        totalCost += change * (change + 1) // 2
    if not min or totalCost < min:
        min = totalCost
print(min)
