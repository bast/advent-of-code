import sys
from itertools import permutations, combinations
from more_itertools import windowed

sys.path.append("../..")

from pathfinder import find_path
from read import read_positions


def neighbors(position):
    row, col = position
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def read_number_locations(file_name):
    locations = {}
    with open(file_name, "r") as f:
        for row, line in enumerate(f.read().splitlines()):
            for col, c in enumerate(line):
                if c not in ["#", "."]:
                    locations[int(c)] = (row, col)
    return locations


def possible_sequences(highest_waypoint, back_to_start):
    sequences = []
    for p in permutations(range(1, highest_waypoint + 1)):
        l = [0] + list(p)
        if back_to_start:
            l += [0]
        sequences.append(tuple(l))
    return sequences


def path_length(sequence, distances):
    l = 0
    for a, b in windowed(sequence, 2):
        l += distances[(a, b)]
    return l


if __name__ == "__main__":
    bad_positions = read_positions("input.txt", row_major=True)

    def position_is_allowed(position):
        return position not in bad_positions

    number_locations = read_number_locations("input.txt")
    n = max(number_locations.keys())

    distances = {}
    for a, b in combinations(range(n + 1), 2):
        origin = number_locations[a]
        destination = number_locations[b]
        path = find_path(origin, destination, position_is_allowed, neighbors)
        distances[(a, b)] = len(path) - 1
        distances[(b, a)] = distances[(a, b)]

    shortest_path = sys.maxsize
    for sequence in possible_sequences(n, back_to_start=False):
        shortest_path = min(shortest_path, path_length(sequence, distances))
    print("part 1:", shortest_path)

    shortest_path = sys.maxsize
    for sequence in possible_sequences(n, back_to_start=True):
        shortest_path = min(shortest_path, path_length(sequence, distances))
    print("part 2:", shortest_path)
