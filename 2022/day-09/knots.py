import sys

sys.path.append("../..")

from read import read_regex_and_parse


def move(position, direction):
    x, y = position
    match direction:
        case "R":
            return x + 1, y
        case "L":
            return x - 1, y
        case "U":
            return x, y + 1
        case "D":
            return x, y - 1


def follow(position, parent):
    tx, ty = position
    hx, hy = parent
    dx, dy = (hx - tx, hy - ty)

    match (abs(dx), abs(dy)):
        case (2, 0):
            return (tx + dx // 2, ty)
        case (0, 2):
            return (tx, ty + dy // 2)
        case (2, _) | (_, 2):
            return (tx + dx // abs(dx), ty + dy // abs(dy))
        case _:
            return position


def num_visited(instructions, num_knots):
    visited = set()
    positions = [(0, 0) for _ in range(num_knots)]
    visited.add(positions[-1])
    for direction, n in instructions:
        for _ in range(n):
            positions[0] = move(positions[0], direction)
            for m in range(1, num_knots):
                positions[m] = follow(positions[m], positions[m - 1])
            visited.add(positions[-1])
    return len(visited)


instructions = read_regex_and_parse("input.txt", r"(\w+) (\d+)", (str, int))

print("part 1:", num_visited(instructions, 2))
print("part 2:", num_visited(instructions, 10))
