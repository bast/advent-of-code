import sys

sys.path.append("../..")

from read import read_regex_and_parse


def paper_area(dimensions):
    l, w, h = dimensions
    areas = [l * w, w * h, h * l]
    return 2 * sum(areas) + sorted(areas)[0]


def ribbon_length(dimensions):
    a, b, c = sorted(dimensions)
    return a + a + b + b + a * b * c


dimensions = read_regex_and_parse("input.txt", r"(\d+)x(\d+)x(\d+)", (int, int, int))

print("part 1:", sum(map(paper_area, dimensions)))
print("part 2:", sum(map(ribbon_length, dimensions)))
