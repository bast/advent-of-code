import sys
from collections import defaultdict

sys.path.append("../..")

from read import read_regex_and_parse


def toggle(n: int) -> int:
    if n == 1:
        return 0
    else:
        return 1


def apply1(d, instruction, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            position = (x, y)
            match instruction:
                case "on":
                    d[position] = 1
                case "off":
                    d[position] = 0
                case "toggle":
                    d[position] = toggle(d[position])


def apply2(d, instruction, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            position = (x, y)
            match instruction:
                case "on":
                    d[position] += 1
                case "off":
                    d[position] = max(0, d[position] - 1)
                case "toggle":
                    d[position] += 2


instructions = read_regex_and_parse(
    "input.txt", r"(\w+) (\d+),(\d+) through (\d+),(\d+)", (str, int, int, int, int)
)

d = defaultdict(int)
for instruction, x1, y1, x2, y2 in instructions:
    apply1(d, instruction, x1, y1, x2, y2)
print("part 1:", sum(d.values()))

d = defaultdict(int)
for instruction, x1, y1, x2, y2 in instructions:
    apply2(d, instruction, x1, y1, x2, y2)
print("part 2:", sum(d.values()))
