from statistics import median
with open('Dec7/Dec7-data.txt') as f:
    inp = list(map(lambda x: int(x), f.read().split(",")))
spot = int(median(inp))
total = 0
for _ in inp:
    total += abs(_ - spot)
print(total)
