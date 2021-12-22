with open('Dec4/Dec4-data.txt') as f:
    lines = f.read().splitlines()

numOfLines = len(lines)

inps = [int(num) for num in lines[0].split(",")]
print(inps)

grids = []
for i in range(numOfLines):
    if lines[i] == "":
        grid = [[int(x) for x in lines[i + 1].split(" ") if x], [int(x) for x in lines[i + 2].split(" ") if x], [int(x)
                                                                                                                 for x in lines[i + 3].split(" ") if x], [int(x) for x in lines[i + 4].split(" ") if x], [int(x) for x in lines[i + 5].split(" ") if x]]
        grids.append(grid)

print(grids)
win = False
count = 0
updatedGrid = grids
total = 0
finalInp = 0
while win == False and count < len(grids):
    inp = inps[count]
    updatedGrid = [[[True if num == inp else num for num in row]
                    for row in singleGrid] for singleGrid in updatedGrid]
    for singleGrid in updatedGrid:
        row_same = [index if all(map(lambda x: x == True, i))
                    else -1 for index, i in enumerate(singleGrid)]
        column_same = [j if all(map(lambda x: x == True, [
                                i[j] for i in singleGrid])) else -1 for j in range(len(singleGrid[0]))]
        if [x for x in row_same if x != -1] != [] or [x for x in column_same if x != -1] != []:
            notCalled = [
                num for row in singleGrid for num in row if num != True]
            total = sum(notCalled)
            finalInp = inp
            win = True

    count += 1
# calculate score
fc = total * finalInp  # final score
print(fc)
