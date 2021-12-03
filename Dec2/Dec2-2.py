with open("Dec2/Dec2-data.txt") as f:
    lines = f.read().splitlines()
depth = 0
hp = 0  # horizontal position
aim = 0


def down(num):
    global aim
    aim += num


def up(num):
    global aim
    aim -= num


def forward(num):
    global depth
    global hp
    global aim
    hp += num
    depth += aim * num


for x in lines:
    inputs = x.split(" ")
    direction = inputs[0]
    distance = inputs[1]
    options = {"forward": forward,
               "up": up,
               "down": down, }
    options[direction](int(distance))
print(depth)
print(depth * hp)
