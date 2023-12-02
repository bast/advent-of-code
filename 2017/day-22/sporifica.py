import sys
from collections import defaultdict

sys.path.append("../..")

from read import read_positions, read_block_dimensions
from rotations import rotate_row_col


def new_position(position, direction):
    r, c = position
    vr, vc = direction
    return (r + vr, c + vc)


def count_infections(num_bursts, infected_positions, num_rows, num_cols, rules):
    infected_map = defaultdict(int)
    for position in infected_positions:
        # 0 for clean, 1 for weakened, 2 for infected, 3 for flagged
        infected_map[position] = 2

    position = (num_rows // 2, num_cols // 2)
    direction = (-1, 0)  # facing up

    num_infections = 0
    for _ in range(num_bursts):
        position, direction, infected_map, num_infections = rules(
            position, direction, infected_map, num_infections
        )
    return num_infections


# 0 for clean, 1 for weakened, 2 for infected, 3 for flagged
def burst_rules1(position, direction, infection_map, num_infections):
    if infection_map[position] == 2:
        direction = rotate_row_col(direction, "right")
        infection_map[position] = 0
    else:
        direction = rotate_row_col(direction, "left")
        infection_map[position] = 2
        num_infections += 1
    position = new_position(position, direction)
    return position, direction, infection_map, num_infections


# 0 for clean, 1 for weakened, 2 for infected, 3 for flagged
def burst_rules2(position, direction, infection_map, num_infections):
    match infection_map[position]:
        case 0:
            direction = rotate_row_col(direction, "left")
            infection_map[position] = 1
        case 1:
            infection_map[position] = 2
            num_infections += 1
        case 2:
            direction = rotate_row_col(direction, "right")
            infection_map[position] = 3
        case 3:
            direction = rotate_row_col(direction, "back")
            infection_map[position] = 0
    position = new_position(position, direction)
    return position, direction, infection_map, num_infections


infected_positions = read_positions("input.txt", row_major=True)
num_rows, num_cols = read_block_dimensions("input.txt")


print(
    "part 1:",
    count_infections(10000, infected_positions, num_rows, num_cols, burst_rules1),
)
print(
    "part 2:",
    count_infections(10000000, infected_positions, num_rows, num_cols, burst_rules2),
)
