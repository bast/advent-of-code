from collections import Counter


def contains_repeating(s, n):
    return n in Counter(s).values()


def string_without_char(s, n):
    return s[:n] + s[n + 1 :]


def find_common(lines):
    for n in range(len(lines[0])):
        new_lines = map(lambda s: string_without_char(s, n), lines)
        c = {v: k for k, v in Counter(new_lines).items()}
        if 2 in c:
            return c[2]


lines = open("input.txt", "r").read().splitlines()

n = len(list(filter(lambda s: contains_repeating(s, 2), lines)))
m = len(list(filter(lambda s: contains_repeating(s, 3), lines)))

print("part 1:", n * m)
print("part 2:", find_common(lines))
