import sys

sys.path.append("..")

from read import read_regex_and_parse


def compute_fuel1(mass: int) -> int:
    return mass // 3 - 2


def compute_fuel2(mass: int) -> int:
    fuel = compute_fuel1(mass)
    if fuel < 0:
        return 0
    else:
        return fuel + compute_fuel2(fuel)


masses = read_regex_and_parse("input.txt", r"(\d+)", int)

result = sum(map(compute_fuel1, masses))
print(f"part 1: {result}")

result = sum(map(compute_fuel2, masses))
print(f"part 2: {result}")
