from more_itertools import chunked
from collections import Counter


def get_part1(layers):
    counts = map(lambda l: dict(Counter(l)), layers)
    counts = sorted(counts, key=lambda c: c[0], reverse=True)
    solution = counts[-1]
    return solution[1] * solution[2]


def print_part2(layers, num_rows, num_cols):
    print("part 2:")
    for row in range(num_rows):
        s = ""
        for col in range(num_cols):
            for layer in layers:
                char = layer[row * num_cols + col]
                if char != 2:
                    if char == 1:
                        c = "*"
                    else:
                        c = " "
                    break
            s += c
        print(s)


text = open("input.txt", "r").read()
numbers = map(int, list(text[:-1]))
num_rows, num_cols = 6, 25

layers = list(chunked(numbers, num_rows * num_cols))

print("part 1:", get_part1(layers))

print_part2(layers, num_rows, num_cols)
