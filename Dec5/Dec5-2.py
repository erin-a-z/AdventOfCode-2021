with open('Dec5/Dec5-data.txt') as f:
    lines = f.read().splitlines()

numOfLines = len(lines)
gridSize = 1000
grid = [[0] * gridSize for _ in range(gridSize)]
for l in lines:
    point1, point2 = l.split("->")
    x1, y1 = point1.strip().split(",")
    x2, y2 = point2.strip().split(",")
    x1 = int(x1) - 1
    x2 = int(x2) - 1
    y1 = int(y1) - 1
    y2 = int(y2) - 1
    if x1 == x2:
        if y2 > y1:
            for y in range(y1, y2 + 1):
                grid[y][x1] += 1
        else:
            for y in range(y2, y1 + 1):
                grid[y][x1] += 1
    elif y1 == y2:
        if x2 > x1:
            for x in range(x1, x2 + 1):
                grid[y1][x] += 1
        else:
            for x in range(x2, x1 + 1):
                grid[y1][x] += 1
    else:  # diagonal
        xRange = abs(x1 - x2) + 1
        x = min(x1, x2)
        y = y1 if x == x1 else y2
        direction = int((y1 - y2) / (x1 - x2))
        for i in range(xRange):
            grid[y][x] += 1
            x += 1
            y += direction

print(sum(map(lambda x: x > 1, [item for row in grid for item in row])))
