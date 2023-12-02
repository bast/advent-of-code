from collections import defaultdict


def parse_line(line):
    first, rest = line.split(": ")
    game = int(first.split()[1])
    sets = []
    for part in rest.split("; "):
        l = []
        for chunk in part.split(", "):
            n, color = chunk.split()
            l.append((color, int(n)))
        sets.append(l)
    return game, sets


def game_is_valid(sets):
    d_max = {"red": 12, "green": 13, "blue": 14}
    for s in sets:
        for (color, n) in s:
            if n > d_max[color]:
                return False
    return True


def power(sets):
    d = defaultdict(int)
    for s in sets:
        for (color, n) in s:
            d[color] = max(d[color], n)
    return d["red"] * d["green"] * d["blue"]


lines = open("input.txt").read().splitlines()


result1 = 0
result2 = 0
for line in lines:
    game, sets = parse_line(line)
    if game_is_valid(sets):
        result1 += game
    result2 += power(sets)


print("part 1:", result1)
print("part 2:", result2)
