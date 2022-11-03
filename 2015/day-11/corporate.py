import re
import string
from more_itertools import windowed


def num_repeating_pairs(s: str) -> int:
    matcher = re.compile(r"(.)\1{1}")
    l = [match.group() for match in matcher.finditer(s)]
    return len(l)


def int_to_str(i, digits):
    base = len(digits)
    if i < 0:
        return "-" + int_to_str(-i, digits)
    return ("" if i < base else int_to_str(i // base, digits)) + digits[i % base]


def str_to_int(s, digits):
    base = len(digits)
    position = {k: v for (k, v) in zip(digits, range(len(digits)))}
    i = 0
    for m, c in enumerate(reversed(s)):
        i += position[c] * base**m
    return i


def contains_straight(s: str, digits) -> bool:
    position = {k: v for (k, v) in zip(digits, range(len(digits)))}
    for a, b, c in windowed(s, 3):
        if (position[a] + 1 == position[b]) and (position[b] + 1 == position[c]):
            return True
    return False


def contains_valid_characters(s: str) -> bool:
    if "i" in s:
        return False
    if "o" in s:
        return False
    if "l" in s:
        return False
    return True


def is_valid(s: str) -> bool:
    digits = string.ascii_lowercase
    if not contains_valid_characters(s):
        return False
    if not contains_straight(s, digits):
        return False
    if num_repeating_pairs(s) < 2:
        return False
    return True


def find_next(s: str) -> str:
    digits = string.ascii_lowercase
    i = str_to_int(s, digits)
    while True:
        i += 1
        s_new = int_to_str(i, digits)
        if is_valid(s_new):
            return s_new


p = find_next("vzbxkghb")
print("part 1:", p)
print("part 2:", find_next(p))
