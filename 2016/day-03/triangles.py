from more_itertools import chunked


def is_valid(t) -> bool:
    a, b, c = t
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


lines = open("input.txt", "r").read().splitlines()

tuples = map(lambda l: tuple(map(int, l.split())), lines)
print("part 1:", len(list(filter(is_valid, tuples))))

n = 0
for chunk in chunked(lines, 3):
    a1, a2, a3 = tuple(map(int, chunk[0].split()))
    b1, b2, b3 = tuple(map(int, chunk[1].split()))
    c1, c2, c3 = tuple(map(int, chunk[2].split()))
    if is_valid((a1, b1, c1)):
        n += 1
    if is_valid((a2, b2, c2)):
        n += 1
    if is_valid((a3, b3, c3)):
        n += 1

print("part 2:", n)
