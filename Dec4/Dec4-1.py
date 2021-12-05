with open('Dec4/Dec4-data.txt') as f:
    lines = f.read().splitlines()

numOfLines = len(lines)

inputs = [int(num) for num in lines[0].split(",")]
print(inputs)

grids = []
for i in range(numOfLines):
    if lines[i] == "":
        grid = [[int(x) for x in lines[i + 1].split(" ") if x],[int(x) for x in lines[i + 2].split(" ") if x], [int(x) for x in lines[i + 3].split(" ") if x], [int(x) for x in lines[i + 4].split(" ") if x], [int(x) for x in lines[i + 5].split(" ") if x]]
        grids.append(grid)

print(grids)
win = False
row_same = False
column_same = False
count = 0
updatedGrid = grids
fc = 0 #final score
notCalled = []
while win == False and count < len(grids):
    input = inputs[count]
    updatedGrid = [[[True if num == input else num for num in row ] for row in singleGrid] for singleGrid in updatedGrid]
    for singleGrid in updatedGrid:
        row_same = [index if all(map(lambda x: x==True, i)) else -1 for index, i in enumerate(singleGrid)]
        column_same = [j if all(map(lambda x: x==True, [i[j] for i in singleGrid])) else -1 for j in range(len(singleGrid[0]))]
        if [x for x in row_same if x != -1] != [] or [x for x in column_same if x != -1] != []:
            notCalled = [num for row in singleGrid for num in row if num != True]
            win = True

    count += 1
# calculate score
total = sum(notCalled)
fc = total * input
print(fc)
