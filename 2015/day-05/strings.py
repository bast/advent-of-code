from more_itertools import windowed
from collections import defaultdict


def num_vowels(s: str) -> int:
    n = 0
    for c in s:
        if c in "aeiou":
            n += 1
    return n


def contains_repeating(s: str) -> bool:
    for (a, b) in windowed(s, 2):
        if a == b:
            return True
    return False


def string_is_nice1(s: str) -> bool:
    if "ab" in s:
        return False
    if "cd" in s:
        return False
    if "pq" in s:
        return False
    if "xy" in s:
        return False
    if not contains_repeating(s):
        return False
    if num_vowels(s) < 3:
        return False
    return True


def property1(s: str) -> bool:
    positions = defaultdict(set)
    for i, c in enumerate(s):
        if i > 0:
            pair = (s[i - 1], c)
            positions[pair].add(i - 1)
            positions[pair].add(i)
    for _, pos in positions.items():
        if len(pos) > 3:
            return True
    return False


def property2(s: str) -> bool:
    for (a, _, b) in windowed(s, 3):
        if a == b:
            return True
    return False


def string_is_nice2(s: str) -> bool:
    return property1(s) and property2(s)


lines = open("input.txt", "r").read().splitlines()

print("part 1:", len(list(filter(string_is_nice1, lines))))
print("part 2:", len(list(filter(string_is_nice2, lines))))
