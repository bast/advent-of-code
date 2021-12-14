def read_input(file_name):
    lines = open(file_name).read().splitlines()
    positions = set()
    folds = []
    for line in lines:
        if "," in line:
            x, y = tuple(map(int, line.split(",")))
            positions.add((x, y))
        if "fold" in line:
            n = int(line.split("=")[-1])
            if "along x" in line:
                folds.append((0, n))
            if "along y" in line:
                folds.append((1, n))
    return positions, folds


def fold_position(p, fold):
    axis, n = fold
    new_p = list(p)
    if new_p[axis] > n:
        new_p[axis] = n - (new_p[axis] - n)
    return tuple(new_p)


def print_message(positions):
    xs, ys = zip(*positions)
    num_rows, num_cols = max(ys), max(xs)
    message = []
    for i in range(num_rows + 1):
        line = ""
        for j in range(num_cols + 1):
            if (j, i) in positions:
                line += "*"
            else:
                line += " "
        message.append(line)
    print("\n".join(message))


if __name__ == "__main__":
    positions, folds = read_input("input.txt")
    positions_save = list(positions)

    positions = {fold_position(p, folds[0]) for p in positions}
    print("part 1:", len(positions))

    positions = positions_save
    for fold in folds:
        positions = {fold_position(p, fold) for p in positions}

    print("part 2:")
    print_message(positions)
