from functools import cache
from itertools import cycle


@cache
def get_num_children(num_steps_left):
    n = 0

    num_steps_left -= 9
    if num_steps_left > 0:
        n += 1 + get_num_children(num_steps_left)

    c = cycle("1234567")
    num_steps_left -= 1
    while num_steps_left > 0:
        if next(c) == "7":
            n += 1 + get_num_children(num_steps_left)
        num_steps_left -= 1

    return n


def num_species(stages, num_steps):
    num_children = 0
    for steps_left in range(num_steps, 1, -1):
        stages = list(map(lambda n: (n - 1) % 7, stages))
        num_zeros = len(list(filter(lambda n: n == 0, stages)))
        num_children += num_zeros * (1 + get_num_children(steps_left - 1))
    return len(stages) + num_children


with open("input.txt", "r") as f:
    stages = list(map(int, f.readline().split(",")))

    print("part 1:", num_species(stages, 80))
    print("part 2:", num_species(stages, 256))
