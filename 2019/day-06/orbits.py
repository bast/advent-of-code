from collections import defaultdict
import re


def read_data(file_name: str):
    d = defaultdict(list)
    with open(file_name, "r") as f:
        for line in f.read().splitlines():
            groups = re.search(r"(\w+)\)(\w+)", line).groups()
            k, v = tuple(groups)
            d[k].append(v)
    return d


def num_orbits(data, k) -> int:
    n = 0
    for v in data[k]:
        n += 1
        if v in data.keys():
            n += num_orbits(data, v)
    return n


data = read_data("input.txt")

sum_all_orbits = sum([num_orbits(data, k) for k in data.keys()])

print("part 1:", sum_all_orbits)
