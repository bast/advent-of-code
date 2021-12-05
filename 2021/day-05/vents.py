from collections import defaultdict
import re


def num_overlaps(file_name: str, consider_diagonals: bool) -> int:
    diagram = defaultdict(int)

    with open(file_name, "r") as f:
        for line in f.read().splitlines():
            groups = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line).groups()
            x1, y1, x2, y2 = tuple(map(int, groups))
            num_steps = max(abs(x2 - x1), abs(y2 - y1))
            if x1 != x2 and y1 != y2 and not consider_diagonals:
                continue
            x = x1
            y = y1
            diagram[(x, y)] += 1
            sx = (x2 - x1) / num_steps
            sy = (y2 - y1) / num_steps
            for _ in range(num_steps):
                x += sx
                y += sy
                diagram[(x, y)] += 1

    return len(list(filter(lambda t: t[1] > 1, diagram.items())))


print("part 1:", num_overlaps("input.txt", False))
print("part 2:", num_overlaps("input.txt", True))
