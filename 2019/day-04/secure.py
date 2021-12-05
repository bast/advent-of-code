from collections import Counter


def number_is_nondecreasing(n: int) -> bool:
    digits = list(map(int, [c for c in str(n)]))
    for (i, j) in zip(digits, digits[1:]):
        if j < i:
            return False
    return True


def number_is_valid1(n: int) -> bool:
    counts = Counter(str(n))
    return any([v > 1 for (_, v) in counts.items()])


def number_is_valid2(n: int) -> bool:
    counts = Counter(str(n))
    return any([v == 2 for (_, v) in counts.items()])


numbers = range(234208, 765869 + 1)
nondecreasing_numbers = list(filter(number_is_nondecreasing, numbers))

print("part 1:", len(list(filter(number_is_valid1, nondecreasing_numbers))))
print("part 2:", len(list(filter(number_is_valid2, nondecreasing_numbers))))
