from itertools import cycle


def find_repeating(numbers: list[int]) -> int:
    visited = set()
    i = 0
    for n in cycle(numbers):
        i += n
        if i in visited:
            return i
        else:
            visited.add(i)


numbers = list(map(int, open("input.txt", "r").read().splitlines()))

print("part 1:", sum(numbers))
print("part 2:", find_repeating(numbers))
