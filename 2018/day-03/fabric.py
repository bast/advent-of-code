import sys
from collections import defaultdict

sys.path.append("../..")

from read import read_regex_and_parse


def read_data(file_name):
    d = defaultdict(int)
    for _, col, row, wide, tall in read_regex_and_parse(
        file_name,
        r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)",
        (int, int, int, int, int),
    ):
        for r in range(row, row + tall):
            for c in range(col, col + wide):
                d[(r, c)] += 1
    return d


def find_layer(file_name, d):
    for identification, col, row, wide, tall in read_regex_and_parse(
        file_name,
        r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)",
        (int, int, int, int, int),
    ):
        all_are_1 = True
        for r in range(row, row + tall):
            for c in range(col, col + wide):
                if d[(r, c)] != 1:
                    all_are_1 = False
        if all_are_1:
            return identification


d = read_data("input.txt")
print("part 1:", len(list(filter(lambda v: v > 1, d.values()))))
print("part 2:", find_layer("input.txt", d))
