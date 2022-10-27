from collections import deque


def find_path(origin, destination, position_is_allowed, neighbors):
    if not position_is_allowed(origin):
        return []
    if not position_is_allowed(destination):
        return []

    visited = set()
    visited.add(origin)

    queue = deque()
    queue.append([origin])

    while queue:
        path = queue.popleft()
        position = path[-1]

        if position == destination:
            return path

        for neighbor in neighbors(position):
            if neighbor not in visited:
                visited.add(neighbor)
                if position_is_allowed(neighbor):
                    queue.append(path + [neighbor])

    return []  # no path exists


def visited_positions(origin, num_steps_from_origin, position_is_allowed, neighbors):
    if not position_is_allowed(origin):
        return []

    visited = set()
    visited.add(origin)

    queue = deque()
    queue.append([origin])

    while queue:
        path = queue.popleft()
        position = path[-1]
        num_steps = len(path) - 1
        if num_steps < num_steps_from_origin:
            for neighbor in neighbors(position):
                if neighbor not in visited:
                    if position_is_allowed(neighbor):
                        visited.add(neighbor)
                        queue.append(path + [neighbor])

    return list(visited)


def _custom_is_allowed(x: int, y: int, number: int) -> bool:
    if x < 0:
        return False
    if y < 0:
        return False
    n = x * x + 3 * x + 2 * x * y + y + y * y + number
    binary_string = "{0:b}".format(n)
    if binary_string.count("1") % 2 == 0:
        return True
    else:
        return False


def position_is_allowed(position):
    x, y = position
    return _custom_is_allowed(x, y, 1352)


def neighbors(position):
    row, col = position
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def print_block(legend, row_range, col_range):
    print()
    for ir in range(row_range[0], row_range[1] + 1):
        chars = []
        for ic in range(col_range[0], col_range[1] + 1):
            position = (ir, ic)
            chars.append(legend(position))
        print("".join(chars))


origin = (1, 1)

destination = (31, 39)
path = find_path(origin, destination, position_is_allowed, neighbors)
print("part 1:", len(path) - 1)

num_steps_from_origin = 50
positions = visited_positions(
    origin, num_steps_from_origin, position_is_allowed, neighbors
)
print("part 2:", len(positions))


def legend_plain(position):
    if position_is_allowed(position):
        char = "."
    else:
        char = "#"
    return char


def legend(position):
    char = legend_plain(position)
    if position in positions:
        char = "o"
    if position in path:
        char = "x"
    return char


print_block(legend, (0, 40), (0, 40))
