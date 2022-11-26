def read_positions(file_name):
    east = set()
    south = set()
    with open(file_name, "r") as f:
        num_rows = 0
        for row, line in enumerate(f.read().splitlines()):
            num_rows += 1
            num_cols = 0
            for col, c in enumerate(line):
                num_cols += 1
                match c:
                    case ">":
                        east.add((row, col))
                    case "v":
                        south.add((row, col))
    return east, south, num_rows, num_cols


def step(east, south, num_rows, num_cols):
    new_east = set()
    for row, col in east:
        mod_col = (col + 1) % num_cols
        if (row, mod_col) not in east and (row, mod_col) not in south:
            new_east.add((row, mod_col))
        else:
            new_east.add((row, col))
    east_changed = new_east != east
    east = new_east

    new_south = set()
    for row, col in south:
        mod_row = (row + 1) % num_rows
        if (mod_row, col) not in east and (mod_row, col) not in south:
            new_south.add((mod_row, col))
        else:
            new_south.add((row, col))
    south_changed = new_south != south
    south = new_south

    changed = east_changed or south_changed
    return east, south, changed


def print_data(east, south, num_rows, num_cols):
    print()
    for row in range(num_rows):
        line = ""
        for col in range(num_cols):
            if (row, col) in east:
                line += ">"
            elif (row, col) in south:
                line += "v"
            else:
                line += "."
        print(line)


east, south, num_rows, num_cols = read_positions("input.txt")
# print_data(east, south, num_rows, num_cols)

n = 0
while True:
    n += 1
    east, south, changed = step(east, south, num_rows, num_cols)
    if not changed:
        break

print("part 1:", n)
