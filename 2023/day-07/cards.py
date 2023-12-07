from collections import Counter
from functools import cmp_to_key


def hand_value(hand):
    c = Counter(hand)
    distribution = sorted(c.values(), reverse=True)
    match distribution:
        case [1, 1, 1, 1, 1]:
            return 0
        case [2, 1, 1, 1]:
            return 1
        case [2, 2, 1]:
            return 2
        case [3, 1, 1]:
            return 3
        case [3, 2]:
            return 4
        case [4, 1]:
            return 5
        case [5]:
            return 6


def hand_value_part2(hand):
    _cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    best_count = hand_value(hand)
    if "J" in hand:
        for card in _cards:
            hypothetical_count = hand_value(hand.replace("J", card))
            best_count = max(best_count, hypothetical_count)
    return best_count


def compare_similar(hand1, hand2, values):
    for c1, c2 in zip(hand1, hand2):
        if values[c1] > values[c2]:
            return -1
        if values[c1] < values[c2]:
            return 1


def provide_compare_function(values, value_function):
    def _compare(hand1, hand2):
        if value_function(hand1) > value_function(hand2):
            return -1
        if value_function(hand1) < value_function(hand2):
            return 1
        return compare_similar(hand1, hand2, values)

    return _compare


def solve_part(hands, bid, part, cards, value_function):
    values = {c: i for i, c in enumerate(cards)}
    ordered_hands = reversed(
        sorted(hands, key=cmp_to_key(provide_compare_function(values, hand_value)))
    )

    n = 0
    for i, card in enumerate(ordered_hands):
        n += (i + 1) * int(bid[card])
    print(f"part {part}:", n)


bid = {}
for line in open("input.txt", "r").read().splitlines():
    h, b = tuple(line.split())
    bid[h] = b
hands = bid.keys()


cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
solve_part(hands, bid, 1, cards, hand_value)

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
solve_part(hands, bid, 2, cards, hand_value_part2)
