from collections import defaultdict
import math


def read_input(file_name):
    lines = open(file_name).read().splitlines()
    pair_counts = defaultdict(int)
    for pair in zip(lines[0], lines[0][1:]):
        pair_counts[pair] += 1
    substitutions = {}
    for line in lines:
        if "->" in line:
            left, right = line.split(" -> ")
            (a, b) = left[0], left[1]
            substitutions[(a, b)] = [(a, right), (right, b)]
    return pair_counts, substitutions


def count_characters(pair_counts):
    c = defaultdict(int)
    for ((a, b), v) in pair_counts.items():
        c[a] += v
        c[b] += v
    d = {math.ceil(v / 2): k for (k, v) in c.items()}
    return sorted(d.items())


def grow(file_name, num_steps):
    pair_counts, substitutions = read_input(file_name)
    for _ in range(num_steps):
        for k, v in list(pair_counts.items()):
            pair_counts[k] -= v
            for s in substitutions[k]:
                pair_counts[s] += v
    return count_characters(pair_counts)


character_counts = grow("input.txt", 10)
print("part 1:", character_counts[-1][0] - character_counts[0][0])

character_counts = grow("input.txt", 40)
print("part 2:", character_counts[-1][0] - character_counts[0][0])
