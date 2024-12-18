import sys

sys.path.append("../..")

from pathfinder import find_path
from collections import defaultdict


def read_positions(file_name):
    positions = []
    for line in open(file_name, "r").read().splitlines():
        x, y = map(int, line.split(","))
        positions.append((x, y))
    return positions


def neighbors(position):
    row, col = position
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def base_grid(x_max):
    grid = defaultdict(bool)
    for x in range(x_max + 1):
        for y in range(x_max + 1):
            grid[(x, y)] = True
    return grid


x_max = 70
num_steps = 1024

origin = (0, 0)
destination = (x_max, x_max)

positions = read_positions("input.txt")
grid = base_grid(x_max)

for i, position in enumerate(positions):
    grid[position] = False

    path = find_path(origin, destination, lambda position: grid[position], neighbors)

    if i + 1 == num_steps:
        print("part 1:", len(path) - 1)

    if len(path) == 0:
        print("part 2:", position)
        break
