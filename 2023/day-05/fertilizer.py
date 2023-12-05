import re
import sys
from collections import defaultdict


def extract_integers(line):
    return [int(s) for s in re.findall(r"\b\d+\b", line)]


def lookup(l, key, reverse=False):
    for dest, src, count in l:
        if reverse:
            if dest <= key <= dest + count:
                return src + key - dest
        else:
            if src <= key <= src + count:
                return dest + key - src
    return key


def in_seed_range(l, key):
    for i in range(0, len(l), 2):
        (s, r) = tuple(l[i : i + 2])
        if s <= key < s + r:
            return True
    return False


def find_number(i, mapping, reverse=False):
    if reverse:
        l = reversed(mapping.keys())
    else:
        l = mapping.keys()
    for key in l:
        i = lookup(mapping[key], i, reverse)
    return i


def bisect_find_index(low, high, predicate):
    while True:
        mid = (low + high) // 2

        if mid == low or mid == high:
            if predicate(mid):
                return mid
            else:
                return mid + 1

        if predicate(mid):
            high = mid
        else:
            low = mid


mapping = defaultdict(list)
for line in open("input.txt", "r").read().splitlines():
    if line.startswith("seeds:"):
        seeds = extract_integers(line)
    if "map" in line:
        key = line.split()[0]
    numbers = extract_integers(line)
    if len(numbers) == 3:
        dest, src, count = numbers
        mapping[key].append((dest, src, count))


result = list(map(lambda x: find_number(x, mapping), seeds))
print("part 1:", sorted(result)[0])


# now use the mapping in reverse until we find a number that is in seed range
# this is brute-forced using bisect
i = bisect_find_index(
    0,
    100000000,
    lambda i: in_seed_range(seeds, find_number(i, mapping, reverse=True)),
)
print("part 2:", i)
