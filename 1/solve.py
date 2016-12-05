file = open("input.txt")

current_direction = 0
x = 0
y = 0

visit_map = [(0, 0)]

for line in file:
    for command in [com.strip() for com in line.split(',')]:
        direction = command[0]
        distance = int(command[1:])
        new_dir = 90 if direction == "R" else -90
        current_direction = (current_direction + new_dir) % 360
        for i in range(distance):
            if current_direction == 0:
                y += 1
            elif current_direction == 90:
                x += 1
            elif current_direction == 180:
                y -= 1
            else:
                x -= 1

            if (x, y) in visit_map:
                dist = abs(x) + abs(y)
                print dist
                exit()
            else:
                visit_map.append((x, y))
