from more_itertools import windowed


def read_input(file_name, padding):
    rules = {}
    for line in open(file_name, "r").read().splitlines():
        if "initial" in line:
            state = line.split()[-1]
        if "=>" in line:
            left, right = line.split(" => ")
            rules[left] = right

    state = "." * padding + state + "." * padding
    return state, rules


def step(state, rules):
    new_state = list("." * len(state))
    for i, chars in enumerate(windowed(state, 5)):
        pattern = "".join(chars)
        if pattern in rules:
            new_state[i + 2] = rules[pattern]
    return "".join(new_state)


def sum_numbers(state, padding):
    result = 0
    for i, c in enumerate(state):
        if c == "#":
            result += i - padding
    return result


def let_grow(state, rules, padding, num_generations):
    # n_last = sum_numbers(state, padding)
    for i in range(num_generations):
        state = step(state, rules)
        n = sum_numbers(state, padding)
        # print(i, n - n_last)
        # n_last = n
    return n


padding = 300
state, rules = read_input("input.txt", padding)

print("part 1:", let_grow(state, rules, padding, num_generations=20))

num_generations = 50000000000
n = let_grow(state, rules, padding, num_generations=108)

print("part 2:", n + (num_generations - 108) * 65)
