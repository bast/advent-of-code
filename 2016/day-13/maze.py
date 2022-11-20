import sys

sys.path.append("../..")

from pathfinder import find_path, visited_positions, print_block


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
