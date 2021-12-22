with open('/Users/user1/Documents/Development/Python/Hydrogen/AdventOfCode 2021/Dec4/Dec4-data.txt') as f:
    lines = f.read().splitlines()

numOfLines = len(lines)

inps = [int(num) for num in lines[0].split(",")]
print(inps)

gridCount = 0
grids = []
for i in range(numOfLines):
    if lines[i] == "":
        grid = [[int(x) for x in lines[i + 1].split(" ") if x], [int(x) for x in lines[i + 2].split(" ") if x], [int(x)
                                                                                                                 for x in lines[i + 3].split(" ") if x], [int(x) for x in lines[i + 4].split(" ") if x], [int(x) for x in lines[i + 5].split(" ") if x]]
        gridCount += 1
        grids.append(grid)

print(grids)
win = [False] * gridCount
last = False
count = 0
updatedGrid = grids
total = 0
finalInp = 0
while last == False and count < gridCount:
    inp = inps[count]
    updatedGrid = [[[True if num == inp else num for num in row]
                    for row in singleGrid] for singleGrid in updatedGrid]
    for index, singleGrid in enumerate(updatedGrid):
        row_same = [index if all(map(lambda x: x == True, i))
                    else -1 for index, i in enumerate(singleGrid)]
        column_same = [j if all(map(lambda x: x == True, [
                                i[j] for i in singleGrid])) else -1 for j in range(len(singleGrid[0]))]
        if [x for x in row_same if x != -1] != [] or [x for x in column_same if x != -1] != []:
            win[index] = True
            if [w for w in win if w != True] == []:
                notCalled = [
                    num for row in singleGrid for num in row if num != True]
                finalInp = inp
                total = sum(notCalled)
                last = True
                break
    count += 1
# calculate score

fc = total * finalInp  # final score
print(fc)
