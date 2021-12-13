import sys
from collections import defaultdict


def neighbors(position):
    i, j = position
    return [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]


def read_input(file_name):
    lines = open(file_name, "r").read().splitlines()
    d = defaultdict(lambda: -sys.maxsize)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            d[(i, j)] = int(c)
    return d


def bump_neighbors(position, levels):
    levels[position] = 0
    for neighbor in neighbors(position):
        if levels[neighbor] > 0:
            levels[neighbor] += 1
        if levels[neighbor] > 9:
            bump_neighbors(neighbor, levels)


def step(levels):
    for position in levels:
        levels[position] += 1
    for position in list(levels.keys()):
        if levels[position] > 9:
            bump_neighbors(position, levels)
    return levels


def num_zeros(levels):
    return len(list(filter(lambda v: v == 0, levels.values())))


if __name__ == "__main__":
    levels = read_input("input.txt")
    s = 0
    for _ in range(100):
        levels = step(levels)
        s += num_zeros(levels)
    print("part 1:", s)

    levels = read_input("input.txt")
    i = 0
    while num_zeros(levels) < 100:
        levels = step(levels)
        i += 1
    print("part 2:", i)
