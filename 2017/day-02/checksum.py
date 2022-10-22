def order(a, b):
    if a <= b:
        return a, b
    else:
        return b, a


def find_divisor(row):
    for a in row:
        for b in row:
            if a != b:
                c, d = order(a, b)
                if d % c == 0:
                    return d // c


rows = []
with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        rows.append(list(map(int, line.split())))


checksum = sum(map(lambda r: max(r) - min(r), rows))
print(f"part 1: {checksum}")

checksum = sum(map(find_divisor, rows))
print(f"part 2: {checksum}")
