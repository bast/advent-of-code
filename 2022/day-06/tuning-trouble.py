from more_itertools import windowed


def get_index(s, n):
    for i, t in enumerate(windowed(s, n)):
        if len(set(t)) == n:
            return i + n


s = open("input.txt", "r").read()

print("part 1:", get_index(s, 4))
print("part 2:", get_index(s, 14))
