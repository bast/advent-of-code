import sys


def parse_line(line):
    instructions = []
    for word in line.split(","):
        instructions.append((word[0], int(word[1:])))
    return instructions


def read_data(file_name):
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
        return tuple(map(parse_line, lines))


def visited_coordinates(instructions):
    coordinates = set()
    steps = {}
    x, y, num_steps = 0, 0, 0
    for direction, n in instructions:
        match direction:
            case "R":
                for (j, k) in enumerate(range(x + 1, x + n + 1)):
                    coordinates.add((k, y))
                    num_steps += 1
                    steps[(k, y)] = num_steps
                x += n
            case "L":
                for (j, k) in enumerate(range(x - 1, x - n - 1, -1)):
                    coordinates.add((k, y))
                    num_steps += 1
                    steps[(k, y)] = num_steps
                x -= n
            case "U":
                for (j, k) in enumerate(range(y + 1, y + n + 1)):
                    coordinates.add((x, k))
                    num_steps += 1
                    steps[(x, k)] = num_steps
                y += n
            case "D":
                for (j, k) in enumerate(range(y - 1, y - n - 1, -1)):
                    coordinates.add((x, k))
                    num_steps += 1
                    steps[(x, k)] = num_steps
                y -= n
            case _:
                sys.exit("unexpected input")
    return coordinates, steps


if __name__ == "__main__":
    instructions1, instructions2 = read_data("input.txt")

    coordinates1, steps1 = visited_coordinates(instructions1)
    coordinates2, steps2 = visited_coordinates(instructions2)

    crosses = coordinates1.intersection(coordinates2)

    manhattan_distances = sorted([abs(x) + abs(y) for (x, y) in crosses])
    print("part 1:", manhattan_distances[1])

    steps = sorted([steps1[(x, y)] + steps2[(x, y)] for (x, y) in crosses])
    print("part 2:", steps[0])
