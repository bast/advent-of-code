import re
import math
from functools import reduce
from itertools import cycle


def parse_line(line):
    m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
    return m.groups()


def least_common_multiple(num_list):
    return reduce(lambda a, b: a * b // math.gcd(a, b), num_list)


def num_steps(start, end_predicate, instructions):
    n = 0
    position = start
    for instruction in cycle(instructions):
        n += 1
        l, r = d[position]
        if instruction == "L":
            position = l
        else:
            position = r
        if end_predicate(position):
            return n


lines = open("input.txt").read().splitlines()

d = {}
for i, line in enumerate(lines):
    if i == 0:
        instructions = line
    if "=" in line:
        a, b, c = parse_line(line)
        d[a] = (b, c)

n = num_steps("AAA", lambda p: p == "ZZZ", instructions)
print("part 1:", n)

ghosts = [p for p in d.keys() if p.endswith("A")]
periods = map(lambda p: num_steps(p, lambda p: p.endswith("Z"), instructions), ghosts)
print("part 2:", least_common_multiple(periods))
