import sys
from collections import defaultdict

sys.path.append("../..")

from pathfinder import find_path2


def read_positions(file_name):
    allowed_positions = []
    markers = {}
    with open(file_name, "r") as f:
        for row, line in enumerate(f.read().splitlines()):
            for col, c in enumerate(line):
                if c == ".":
                    allowed_positions.append((row, col))
                if c.isupper():
                    markers[(row, col)] = c
    return allowed_positions, markers


def _neighbors(position):
    row, col = position
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def locate_teleports(markers, allowed_positions):
    d = defaultdict(list)
    for (row, col), c in markers.items():
        for row_n, col_n in _neighbors((row, col)):
            if (row_n, col_n) in allowed_positions:
                row_d, col_d = row_n - row, col_n - col
                c_other = markers[(row - row_d, col - col_d)]
                teleport_name = "".join(sorted([c, c_other]))
                d[teleport_name].append((row_n, col_n))

    origin = d["AA"][0]
    destination = d["ZZ"][0]

    teleports = {}
    for v in d.values():
        if len(v) == 2:
            teleports[v[0]] = v[1]
            teleports[v[1]] = v[0]

    return origin, destination, teleports


def _neighbors(position):
    row, col = position
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def shortest_path_length(file_name):
    allowed_positions, markers = read_positions(file_name)
    origin, destination, teleports = locate_teleports(markers, allowed_positions)

    def neighbors(position):
        result = []
        for neighbor in _neighbors(position):
            if position in allowed_positions:
                result.append(neighbor)
        if position in teleports:
            result.append(teleports[position])
        return result

    path = find_path2(origin, destination, neighbors)
    return len(path) - 1


print("small:", shortest_path_length("small.txt"))
print("medium:", shortest_path_length("medium.txt"))
print("part 1:", shortest_path_length("input.txt"))
