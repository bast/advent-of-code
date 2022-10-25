def diagonal_indices() -> int:
    n = 0
    while True:
        for i in range(n + 1, 0, -1):
            yield (i, n - i + 2)
        n += 1


def next_number(n: int) -> int:
    m = n * 252533
    return m % 33554393


indices = diagonal_indices()
_ = next(indices)

n = 20151125
i, j = 2981, 3075

while True:
    n = next_number(n)
    if next(indices) == (i, j):
        print(n)
        break
