import sys

sys.path.append("../..")

from read import read_regex_and_parse


def equal(a: int, b: int) -> bool:
    return a == b


def greater_than(a: int, b: int) -> bool:
    return a > b


def fewer_than(a: int, b: int) -> bool:
    return a < b


def aunt_matches(ticker_tape, things) -> bool:
    for thing, count in things.items():
        count_tape, fun = ticker_tape[thing]
        if not fun(count, count_tape):
            return False
    return True


def find_aunt(aunts, ticker_tape) -> int:
    for i, things in enumerate(aunts):
        if aunt_matches(ticker_tape, things):
            return i + 1


aunts = []
for a_name, a_count, b_name, b_count, c_name, c_count in read_regex_and_parse(
    "input.txt",
    r"Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)",
    (str, int, str, int, str, int),
):
    d = {}
    d[a_name] = a_count
    d[b_name] = b_count
    d[c_name] = c_count
    aunts.append(d)


ticker_tape = {
    "children": (3, equal),
    "cats": (7, equal),
    "samoyeds": (2, equal),
    "pomeranians": (3, equal),
    "akitas": (0, equal),
    "vizslas": (0, equal),
    "goldfish": (5, equal),
    "trees": (3, equal),
    "cars": (2, equal),
    "perfumes": (1, equal),
}

print(f"part 1: {find_aunt(aunts, ticker_tape)}")


ticker_tape = {
    "children": (3, equal),
    "cats": (7, greater_than),
    "samoyeds": (2, equal),
    "pomeranians": (3, fewer_than),
    "akitas": (0, equal),
    "vizslas": (0, equal),
    "goldfish": (5, fewer_than),
    "trees": (3, greater_than),
    "cars": (2, equal),
    "perfumes": (1, equal),
}

print(f"part 2: {find_aunt(aunts, ticker_tape)}")
