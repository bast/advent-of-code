from collections import Counter


def part2(text: str) -> int:
    floor = 0
    for i, c in enumerate(text):
        if c == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i + 1


text = open("input.txt", "r").read()

c = Counter(text)
print("part 1:", c["("] - c[")"])

print("part 2:", part2(text))
