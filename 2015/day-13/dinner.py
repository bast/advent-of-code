import sys
from itertools import permutations

sys.path.append("../..")

from read import read_regex_and_parse


def cyclic_pairs(l):
    pairs = list(zip(l, l[1:]))
    pairs.append((l[-1], l[0]))
    return pairs


def happiness_change(arrangement, happiness) -> int:
    pairs = cyclic_pairs(arrangement)
    return sum(map(lambda t: happiness[t], pairs))


names = set()
happiness = {}
for name_a, gain_or_lose, n, name_b in read_regex_and_parse(
    "input.txt",
    r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).",
    (str, str, int, str),
):
    num_units = n
    if gain_or_lose == "lose":
        num_units *= -1

    names.add(name_a)
    happiness[(name_a, name_b)] = num_units


def change(arrangement):
    return happiness_change(arrangement, happiness) + happiness_change(
        list(reversed(arrangement)), happiness
    )


result = max(map(change, permutations(names)))
print(f"part 1: {result}")


for name in names:
    happiness[("ego", name)] = 0
    happiness[(name, "ego")] = 0
names.add("ego")

result = max(map(change, permutations(names)))
print(f"part 2: {result}")
