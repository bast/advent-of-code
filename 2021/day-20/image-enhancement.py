from collections import defaultdict


def read_input(file_name):
    interpret = {"#": 1, ".": 0}
    data = defaultdict(int)
    with open(file_name, "r") as f:
        algorithm = [interpret[c] for c in f.readline().strip()]
        _ = next(f)
        for row, line in enumerate(f.read().splitlines()):
            for col, c in enumerate(line):
                data[(row, col)] = interpret[c]
    return algorithm, data


def bounds(data):
    rows, cols = zip(*data.keys())
    return min(rows), max(rows), min(cols), max(cols)


def stencil(row, col):
    return [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]


def compute_pixel(row, col, data, algorithm) -> int:
    s = "".join([str(data[e]) for e in stencil(row, col)])
    n = int(s, 2)
    return algorithm[n]


def enhance(data, algorithm, default):
    row_min, row_max, col_min, col_max = bounds(data)
    new_data = defaultdict(lambda: default)
    for row in range(row_min - 2, row_max + 2):
        line = ""
        for col in range(col_min - 2, col_max + 2):
            new_data[(row, col)] = compute_pixel(row, col, data, algorithm)
    return new_data


def result(data, algorithm, num_steps) -> int:
    for i in range(num_steps):
        if i % 2 == 0:
            default = algorithm[0]
        else:
            default = algorithm[-1]
        data = enhance(data, algorithm, default)
    return sum(data.values())


algorithm, data = read_input("input.txt")
print("part 1:", result(data, algorithm, 2))
print("part 2:", result(data, algorithm, 50))
