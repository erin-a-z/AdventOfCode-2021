with open("Dec2/Dec2-data.txt") as f:
    lines = f.read().splitlines()
depth = 0
hp = 0  # horizontal position


def forward(num):
    global hp
    hp += num


def down(num):
    global depth
    depth += num


def up(num):
    global depth
    depth -= num


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
