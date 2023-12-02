import re
from collections import defaultdict


def extract_numbers(pattern, line):
    i, j = tuple(map(int, pattern.search(line).groups()))
    return i, j


def create_rect(x, y, screen):
    for ix in range(x):
        for iy in range(y):
            screen[(ix, iy)] = 1
    return screen


def rotate_col(x, n, screen, num_rows):
    col = [screen[(x, y)] for y in range(num_rows)]
    for y in range(num_rows):
        screen[(x, y)] = col[(y - n) % num_rows]
    return screen


def rotate_row(y, n, screen, num_cols):
    row = [screen[(x, y)] for x in range(num_cols)]
    for x in range(num_cols):
        screen[(x, y)] = row[(x - n) % num_cols]
    return screen


def print_block(screen, num_rows, num_cols):
    for y in range(num_rows):
        for x in range(num_cols):
            if screen[(x, y)]:
                print("#", end="")
            else:
                print(" ", end="")
        print("")


num_rows = 6
num_cols = 50
screen = defaultdict(int)


lines = open("input.txt", "r").read().splitlines()

pattern_rect = re.compile(r"rect (\d+)x(\d+)")
pattern_col = re.compile(r"rotate column x=(\d+) by (\d+)")
pattern_row = re.compile(r"rotate row y=(\d+) by (\d+)")


for line in lines:
    if "rect" in line:
        x, y = extract_numbers(pattern_rect, line)
        screen = create_rect(x, y, screen)
    elif "column" in line:
        x, n = extract_numbers(pattern_col, line)
        screen = rotate_col(x, n, screen, num_rows)
    elif "row" in line:
        y, n = extract_numbers(pattern_row, line)
        screen = rotate_row(y, n, screen, num_cols)


print("part 1:", sum(screen.values()))

print_block(screen, num_rows, num_cols)
