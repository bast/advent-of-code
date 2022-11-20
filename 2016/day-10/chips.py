import sys
from collections import defaultdict

sys.path.append("../..")

from read import read_regex_and_parse


def read_data():
    values = defaultdict(list)
    for value, recipient in read_regex_and_parse(
        "input.txt",
        r"value (\d+) goes to (.*)",
        (int, str),
    ):
        values[recipient].append(value)

    rules = {}
    for bot, low, high in read_regex_and_parse(
        "input.txt",
        r"(.*) gives low to (.*) and high to (.*)",
        (str, str, str),
    ):
        rules[bot] = (low, high)

    return values, rules


def ordered(l):
    return tuple(sorted(l))


def trade_chips(values, rules):
    new_values = defaultdict(list)
    for k, v in values.items():
        if len(v) == 2 and "bot" in k:
            l, h = ordered(v)
            l_recipient, h_recipient = rules[k]
            new_values[l_recipient].append(l)
            new_values[h_recipient].append(h)
        else:
            new_values[k].append(v[0])
    return new_values


def find_bot(values, rules, comparison):
    while True:
        for k, v in values.items():
            if sorted(v) == comparison:
                return k
        values = trade_chips(values, rules)


values, rules = read_data()

comparison = [17, 61]
bot = find_bot(values, rules, comparison)
print("part 1:", bot)

values, rules = read_data()
for _ in range(1000):  # lazy, there is a more elegant way
    values = trade_chips(values, rules)
print("part 2:", values["output 0"][0] * values["output 1"][0] * values["output 2"][0])
