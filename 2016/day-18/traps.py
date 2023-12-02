from more_itertools import sliding_window
from tqdm import tqdm


def new_character(left, center, right):
    match (left, center, right):
        case ("^", "^", "."):
            return "^"
        case (".", "^", "^"):
            return "^"
        case ("^", ".", "."):
            return "^"
        case (".", ".", "^"):
            return "^"
        case _:
            return "."


def new_row(row):
    extended_row = "." + row + "."
    l = []
    for left, center, right in sliding_window(extended_row, 3):
        l.append(new_character(left, center, right))
    return "".join(l)


def num_safe(row):
    return row.count(".")


def count_safe_places(row, num_rows):
    n = num_safe(row)
    for _ in tqdm(range(num_rows - 1)):
        row = new_row(row)
        n += num_safe(row)
    return n


row = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
print("part 1:", count_safe_places(row, 40))
print("part 2:", count_safe_places(row, 400000))
