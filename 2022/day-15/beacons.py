import sys
from collections import Counter
from tqdm import tqdm

sys.path.append("../..")

from read import read_regex_and_parse


def manhattan_distance(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)


def get_range(d, sx, sy, y):
    dy = abs(y - sy)
    if dy > d:
        return []

    dx = d - dy
    return list(range(sx - dx, sx + dx + 1))


def connect_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x2 > x1:
        dx = 1
    else:
        dx = -1

    if y2 > y1:
        dy = 1
    else:
        dy = -1

    x = x1
    y = y1

    l = []
    while True:
        l.append((x, y))
        if (x, y) == (x2, y2):
            return l
        x += dx
        y += dy


def get_outline(d, sx, sy):
    north = (sx, sy - d)
    south = (sx, sy + d)
    east = (sx + d, sy)
    west = (sx - d, sy)

    ne = connect_points(north, east)
    es = connect_points(east, south)
    sw = connect_points(south, west)
    wn = connect_points(west, north)

    return set(ne + es + sw + wn)


row = 2000000
m = 4000000
positions = set()
intersections = Counter()

for sx, sy, bx, by in tqdm(
    read_regex_and_parse(
        "input.txt",
        r"Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)",
        (int, int, int, int),
    )
):
    d = manhattan_distance(bx, by, sx, sy)

    for p in get_range(d, sx, sy, row):
        if p != bx or row != by:
            positions.add(p)

    for (x, y) in get_outline(d + 1, sx, sy):
        if 0 <= x < m and 0 <= y < m:
            intersections[(x, y)] += 1

print("part 1:", len(positions))

x, y = intersections.most_common(1)[0][0]
print("part 2:", x * 4000000 + y)
