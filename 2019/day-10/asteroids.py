import sys
import math
from collections import defaultdict

sys.path.append("../..")

from read import read_positions


def get_direction(dx: int, dy: int) -> int:
    d = math.atan2(dx, dy)
    if d < 0.0:
        d = 2.0 * math.pi + d
    return int(d * 10000)


def get_distance(dx: int, dy: int) -> int:
    d = math.sqrt(dx * dx + dy * dy)
    return int(d * 10000)


positions = read_positions("input.txt", row_major=False)


direction_map = defaultdict(set)
for i, (ax, ay) in enumerate(positions):
    for j, (bx, by) in enumerate(positions):
        if i != j:
            direction = get_direction(bx - ax, ay - by)  # y reversed
            direction_map[(ax, ay)].add(direction)

map_num_visible = map(lambda t: (t[0], len(t[1])), direction_map.items())
map_num_visible = sorted(map_num_visible, key=lambda t: t[1], reverse=True)

(lx, ly), num_visible = map_num_visible[0]
print(f"part 1: {num_visible} from {lx, ly}")


directions = set()
positions_map = defaultdict(list)
for (x, y) in positions:
    if (x, y) != (lx, ly):
        direction = get_direction(x - lx, ly - y)  # y reversed
        distance = get_distance(x - lx, y - ly)
        directions.add(direction)
        positions_map[direction].append((distance, (x, y)))
directions = sorted(list(directions))

# sort positions to distance
for direction in directions:
    l = positions_map[direction]
    positions_map[direction] = sorted(l, reverse=True)

positions_vaporized = []
while positions_map:  # shoot until the dictionary is empty
    for direction in directions:
        if direction in positions_map:
            _, (x, y) = positions_map[direction].pop()
            if len(positions_map[direction]) == 0:
                del positions_map[direction]
            positions_vaporized.append((x, y))

(x, y) = positions_vaporized[199]
print(f"part 2: {x*100 + y}")
