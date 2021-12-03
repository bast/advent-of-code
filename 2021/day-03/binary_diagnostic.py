from collections import Counter


def get_column(lines, n):
    return map(lambda line: line[n], lines)


def binary_to_decimal(b):
    s = "".join(map(str, b))
    return int(s, 2)


def find_bit(lines, position, default):
    c = Counter(get_column(lines, position))
    a = c.most_common()
    if a[0][1] == a[1][1]:
        # in this case 0 and 1 are equally common
        return default
    else:
        # xor of default to determine whether we want most common or least
        # common
        return a[default ^ 1][0]


def find_rating(lines, default):
    position = -1
    while len(lines) > 1:
        position += 1
        b = find_bit(lines, position, default)
        lines = list(filter(lambda l: l[position] == b, lines))
    return lines[0]


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        for line in f.read().splitlines():
            lines.append(list(map(int, list(line))))

    gamma_rate = [find_bit(lines, p, 1) for p in range(len(lines[0]))]
    epsilon_rate = [(c ^ 1) for c in gamma_rate]

    print("part 1:", binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate))

    oxygen_rating = find_rating(lines, 1)
    co2_rating = find_rating(lines, 0)

    print("part 2:", binary_to_decimal(oxygen_rating) * binary_to_decimal(co2_rating))
