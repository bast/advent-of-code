import string


def react(polymer):
    while True:
        n = len(polymer)
        for a, b in zip(string.ascii_lowercase, string.ascii_uppercase):
            polymer = polymer.replace(a + b, "")
            polymer = polymer.replace(b + a, "")
        if len(polymer) == n:
            return polymer


def shortest(polymer):
    lengths = []
    for c in string.ascii_lowercase:
        remaining_polymer = polymer.replace(c, "").replace(c.upper(), "")
        lengths.append(len(react(remaining_polymer)))
    return min(lengths)


polymer = open("input.txt", "r").read().strip()

print("part 1:", len(react(polymer)))
print("part 2:", shortest(polymer))
