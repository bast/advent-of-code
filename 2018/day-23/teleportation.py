import sys
from z3 import *

sys.path.append("../..")

from read import read_regex_and_parse


def _abs(x):
    return If(x >= 0, x, -x)


def manhattan_distance(bot1, bot2) -> int:
    _, x1, y1, z1 = bot1
    _, x2, y2, z2 = bot2
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


nanobots = []
for x, y, z, r in read_regex_and_parse(
    "input.txt",
    r"pos=<(-*\d+),(-*\d+),(-*\d+)>, r=(\d+)",
    (int, int, int, int),
):
    nanobots.append((r, x, y, z))

strongest = sorted(nanobots, reverse=True)[0]

distances = map(lambda b: manhattan_distance(b, strongest), nanobots)

r, x, y, z = strongest
in_range = filter(lambda d: d <= r, distances)
print("part 1:", len(list(in_range)))

x0, y0, z0 = Int("x"), Int("y"), Int("z")

o = Optimize()

in_ranges = [Int(f"in_range_{i}") for i in range(len(nanobots))]
for i, nanobot in enumerate(nanobots):
    r, x, y, z = nanobot
    o.add(in_ranges[i] == If(_abs(x - x0) + _abs(y - y0) + _abs(z - z0) <= r, 1, 0))

range_count = Int("sum")
o.add(range_count == sum(in_ranges))

dist_from_zero = Int("dist")
o.add(dist_from_zero == _abs(x0) + _abs(y0) + _abs(z0))

_ = o.maximize(range_count)
f = o.minimize(dist_from_zero)

_ = o.check()
print("part 2:", o.lower(f))
