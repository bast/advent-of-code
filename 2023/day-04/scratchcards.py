import re
from collections import defaultdict


def extract_all_numbers(line):
    numbers = list(map(int, re.findall(r"\d+", line)))
    game_number = numbers[0]
    winning_numbers = numbers[1:11]
    my_numbers = numbers[11:]
    return game_number, winning_numbers, my_numbers


def num_winning(line):
    game_number, winning_numbers, my_numbers = extract_all_numbers(line)
    points = set(winning_numbers) & set(my_numbers)
    return game_number, len(points)


def sum_cards(card, d):
    if card not in d:
        return 0
    else:
        return sum([1 + sum_cards(c, d) for c in d[card]])


lines = open("input.txt").read().splitlines()


d = defaultdict(list)
result1 = 0
for line in lines:
    game, n = num_winning(line)
    if n > 0:
        result1 += 2 ** (n - 1)
    for i in range(game + 1, game + n + 1):
        d[game].append(i)

print("part 1:", result1)


result2 = 0
for i in range(1, len(lines) + 1):
    result2 += 1 + sum_cards(i, d)

print("part 2:", result2)
