from collections import defaultdict


def neighbors(position):
    i, j = position
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]


def read_map(file_name):
    lines = open(file_name, "r").read().splitlines()

    # can be any number higher than 8
    heightmap = defaultdict(lambda: 9)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            heightmap[(i, j)] = int(c)

    return heightmap


def find_local_minima(heightmap):
    local_minima = []
    for (k, v) in list(heightmap.items()):
        if all([v < heightmap[n] for n in neighbors(k)]):
            local_minima.append(k)
    return local_minima


def num_neighbors_below_9(position, heightmap):
    # we turn current position to 9 to make sure the recursion does not visit
    # this position again
    n = 1
    heightmap[position] = 9
    for neighbor in neighbors(position):
        if heightmap[neighbor] < 9:
            n += num_neighbors_below_9(neighbor, heightmap)
    return n


if __name__ == "__main__":
    heightmap = read_map("input.txt")

    local_minima = find_local_minima(heightmap)

    print("part 1:", sum([heightmap[k] + 1 for k in local_minima]))

    basin_sizes = map(lambda p: num_neighbors_below_9(p, heightmap), local_minima)
    a, b, c, *_ = list(sorted(basin_sizes, reverse=True))

    print("part 2:", a * b * c)
