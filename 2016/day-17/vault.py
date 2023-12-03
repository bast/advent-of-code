import hashlib
import sys
from collections import deque


def path_to_directions(path):
    directions = ""
    for (a, b) in zip(path, path[1:]):
        if a[0] < b[0]:
            directions += "D"
        elif a[0] > b[0]:
            directions += "U"
        elif a[1] < b[1]:
            directions += "R"
        elif a[1] > b[1]:
            directions += "L"
    return directions


def compute_md5_hash(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def door_open(c) -> bool:
    return c in "bcdef"


def position_is_allowed(position):
    x, y = position
    if x < 0:
        return False
    if x > 3:
        return False
    if y < 0:
        return False
    if y > 3:
        return False
    return True


def neighbors(position, passcode, path):
    row, col = position
    directions = path_to_directions(path)
    result = []
    up, down, left, right = compute_md5_hash(passcode + directions)[:4]
    if door_open(up):
        result.append((row - 1, col))
    if door_open(down):
        result.append((row + 1, col))
    if door_open(left):
        result.append((row, col - 1))
    if door_open(right):
        result.append((row, col + 1))
    return result


def find_path(passcode, origin, destination):
    queue = deque()
    queue.append([origin])

    while queue:
        path = queue.popleft()
        directions = path_to_directions(path)
        position = path[-1]

        if position == destination:
            return path

        for neighbor in neighbors(position, passcode, path):
            if position_is_allowed(neighbor):
                queue.append(path + [neighbor])

    return []  # no path exists


def find_all_paths(passcode, origin, destination):
    queue = deque()
    queue.append([origin])
    paths = []

    while queue:
        path = queue.popleft()
        directions = path_to_directions(path)
        position = path[-1]

        for neighbor in neighbors(position, passcode, path):
            if position_is_allowed(neighbor):
                new_path = path + [neighbor]
                if neighbor == destination:
                    paths.append(new_path)
                else:
                    queue.append(new_path)

    return paths


passcode = "ioramepc"
origin = (0, 0)
destination = (3, 3)

path = find_path(passcode, origin, destination)
print("part 1:", path_to_directions(path))

longest = 0
for path in find_all_paths(passcode, origin, destination):
    longest = max(longest, len(path))
print("part 2:", longest - 1)
