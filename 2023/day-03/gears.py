import re


def find_numbers(line):
    return [(int(m.group()), m.start(), m.end() - 1) for m in re.finditer(r"\d+", line)]


def symbol_positions(line, predicate):
    positions = []
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if predicate(c):
                positions.append((row, col))
    return positions


def aura(row, start, end):
    l = []
    l.append((row, start - 1))
    l.append((row, end + 1))
    for i in range(start - 1, end + 2):
        l.append((row - 1, i))
        l.append((row + 1, i))
    return l


def aura_touches_symbol(row, start, end, symbols):
    for position in aura(row, start, end):
        if position in symbols:
            return True
    return False


lines = open("input.txt", "r").read().splitlines()

symbols = symbol_positions(lines, lambda c: not c.isdigit() and c != ".")
gears = {p: [] for p in symbol_positions(lines, lambda c: c == "*" and c != ".")}

result1 = 0
for row, line in enumerate(lines):
    for number, start, end in find_numbers(line):
        if aura_touches_symbol(row, start, end, symbols):
            result1 += number
        for position in aura(row, start, end):
            if position in gears.keys():
                gears[position].append(number)
print("part 1:", result1)

result2 = 0
for _, numbers in gears.items():
    if len(numbers) == 2:
        result2 += numbers[0] * numbers[1]
print("part 2:", result2)
