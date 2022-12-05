import re
from more_itertools import windowed


def inside_brackets(s: str) -> list[str]:
    return re.findall(r"\[(.*?)\]", s)


def outside_brackets(s: str) -> list[str]:
    return re.findall(r"([^[\]]+)(?:$|\[)", s)


def contains_abba(s: str) -> bool:
    for a, b, c, d in windowed(s, 4):
        if a != b and a == d and b == c:
            return True
    return False


n = 0
for line in open("input.txt", "r").read().splitlines():
    inside = inside_brackets(line)
    n_inside = len(list(filter(contains_abba, inside)))
    if n_inside == 0:
        outside = outside_brackets(line)
        n_outside = len(list(filter(contains_abba, outside)))
        if n_outside > 0:
            n += 1

print("part 1:", n)
