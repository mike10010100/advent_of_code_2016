file = open("input.txt")

current_direction = 0
x = 0
y = 0

for line in file:
    for command in [com.strip() for com in line.split(',')]:
        direction = command[0]
        distance = int(command[1:])
        new_dir = 90 if direction == "R" else -90
        current_direction = (current_direction + new_dir) % 360
        if current_direction == 0:
            y += distance
        elif current_direction == 90:
            x += distance
        elif current_direction == 180:
            y -= distance
        else:
            x -= distance

    dist = abs(x) + abs(y)
    print dist
