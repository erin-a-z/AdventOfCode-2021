with open('Dec1/Dec1-data.txt') as f:
    lines = f.read().splitlines()
counter = 0
for i in range(len(lines)):
    if i == 0:
        continue
    elif int(lines[i]) > int(lines[i-1]):
        counter += 1
print(counter)
