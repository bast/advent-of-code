instructions = open("input.txt", "r").read().strip().split(", ")


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 0
x, y = 0, 0
visited = set()
part2_location = None


for instruction in instructions:
    turn, distance = instruction[0], int(instruction[1:])

    if turn == "R":
        current_direction = (current_direction + 1) % 4
    else:
        current_direction = (current_direction - 1) % 4

    dx, dy = directions[current_direction]

    for _ in range(distance):
        x += dx
        y += dy
        if part2_location is None:
            if (x, y) in visited:
                part2_location = (x, y)
            visited.add((x, y))


print("part 1:", abs(x) + abs(y))

x, y = part2_location
print("part 2:", abs(x) + abs(y))
