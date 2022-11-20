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


def print_block(legend, row_range, col_range):
    print()
    for ir in range(row_range[0], row_range[1] + 1):
        chars = []
        for ic in range(col_range[0], col_range[1] + 1):
            position = (ir, ic)
            chars.append(legend(position))
        print("".join(chars))
