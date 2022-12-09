from operator import mul
from functools import reduce


def read_data(file_name):
    lines = open(file_name, "r").read().splitlines()
    data = {}
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            data[(row, col)] = int(c)
    return data, len(lines)


def plant_fake_trees(n):
    data = {}
    for i in range(n):
        data[(-1, i)] = 10
        data[(n, i)] = 10
        data[(i, -1)] = 10
        data[(i, n)] = 10
    return data


def trees_blocking_view(tree, data):
    h = data[tree]
    result = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = tree
        while True:
            x, y = x + dx, y + dy
            if data[(x, y)] >= h:
                result.append((x, y))
                break
    return result


def manhattan_distance(p1, p2, fake_tall_trees):
    x1, y1 = p1
    x2, y2 = p2
    d = abs(x2 - x1) + abs(y2 - y1)
    if p2 in fake_tall_trees:
        d -= 1  # ugly fix
    return d


input_trees, n = read_data("input.txt")


# these tall trees are planted around the perimeter so that we don't have to
# deal with the boundary
fake_tall_trees = plant_fake_trees(n)
all_trees = input_trees | fake_tall_trees


visible_trees = set()
scenic_score = {}
for p in input_trees:
    blocking_trees = trees_blocking_view(p, all_trees)
    if any(t in fake_tall_trees for t in blocking_trees):
        visible_trees.add(p)
    distances = map(
        lambda tree: manhattan_distance(p, tree, fake_tall_trees),
        blocking_trees,
    )
    scenic_score[p] = reduce(mul, distances, 1)

print("part 1:", len(visible_trees))
print("part 2:", max(scenic_score.values()))
