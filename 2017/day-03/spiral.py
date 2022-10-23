def lower_bound_sequence():
    n = 1
    i = 0
    while True:
        yield n
        i += 1
        if i > 3:
            n += 1
            i = 0


def upper_bound_sequence():
    n = 1
    i = 0
    while True:
        yield n
        i += 1
        if n % 2 != 0 or i > 2:
            n += 1
            i = 0


def ul_sequence():
    u = upper_bound_sequence()
    l = lower_bound_sequence()
    while True:
        yield next(u)
        yield next(l)


def spiral_sequence():
    s = ul_sequence()
    _ = next(s)
    _ = next(s)
    target = next(s)
    n = 1
    increment = 1
    while True:
        yield n
        n += increment
        if n == target:
            target = next(s)
            increment *= -1


s = spiral_sequence()
num_steps = 368078 - 1
for _ in range(num_steps):
    n = next(s)

print(f"part 1: {n}")
