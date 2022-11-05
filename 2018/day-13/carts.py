from itertools import cycle
from dataclasses import dataclass


def direction_generator():
    for direction in cycle([turn_left, straight, turn_right]):
        yield direction


@dataclass
class Cart:
    direction: (int, int)
    next_direction: direction_generator()


def read_input(file_name):
    d = {}
    with open(file_name, "r") as f:
        for row, line in enumerate(f.read().splitlines()):
            for col, c in enumerate(line):
                d[(row, col)] = c
    return d


def find_carts(track):
    carts = {}
    new_track = dict(track)
    for k, v in track.items():
        match v:
            case ">":
                carts[k] = Cart((0, 1), direction_generator())
                new_track[k] = "-"
            case "<":
                carts[k] = Cart((0, -1), direction_generator())
                new_track[k] = "-"
            case "^":
                carts[k] = Cart((-1, 0), direction_generator())
                new_track[k] = "|"
            case "v":
                carts[k] = Cart((1, 0), direction_generator())
                new_track[k] = "|"
            case "_":
                new_track[k] = v
    return carts, new_track


def turn_left(t):
    return (-t[1], t[0])


def turn_right(t):
    return (t[1], -t[0])


def straight(t):
    return t


def turn_at_curve(curve, t):
    if curve == "/":
        if t == (0, 1):  # >
            return (-1, 0)
        if t == (0, -1):  # <
            return (1, 0)
        if t == (-1, 0):  # ^
            return (0, 1)
        if t == (1, 0):  # v
            return (0, -1)
    if curve == "\\":
        if t == (0, 1):  # >
            return (1, 0)
        if t == (0, -1):  # <
            return (-1, 0)
        if t == (-1, 0):  # ^
            return (0, -1)
        if t == (1, 0):  # v
            return (0, 1)


def first_collision(carts, track):
    while True:
        new_carts = {}
        for position, cart in sorted(carts.items()):
            x, y = position
            dx, dy = cart.direction
            new_position = (x + dx, y + dy)
            element = track[new_position]
            if element in ["/", "\\"]:
                cart.direction = turn_at_curve(element, cart.direction)
            if element == "+":
                cart.direction = next(cart.next_direction)(cart.direction)
            if new_position in new_carts:
                return new_position
            if not new_position in new_carts:
                new_carts[new_position] = cart
        carts = new_carts


def last_cart_standing(carts, track):
    while True:
        new_carts = {}
        for position, cart in sorted(carts.items()):
            x, y = position
            dx, dy = cart.direction
            new_position = (x + dx, y + dy)
            if new_position in new_carts:
                del new_carts[new_position]
            else:
                element = track[new_position]
                if element in ["/", "\\"]:
                    cart.direction = turn_at_curve(element, cart.direction)
                if element == "+":
                    cart.direction = next(cart.next_direction)(cart.direction)
                new_carts[new_position] = cart
        carts = new_carts
        if len(carts.keys()) == 1:
            return list(carts.keys())[0]


track = read_input("input.txt")
carts, track = find_carts(track)
x, y = first_collision(carts, track)
print(f"part 1: {y},{x}")

track = read_input("input.txt")
carts, track = find_carts(track)
x, y = last_cart_standing(carts, track)
print(f"part 2: {y},{x}")
