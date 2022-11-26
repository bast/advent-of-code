from functools import reduce


# adapted after https://rosettacode.org/wiki/Chinese_remainder_theorem
def chinese_remainder(n, a):
    s = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * modular_multiplicative_inverse(p, n_i) * p
    return s % prod


# adapted after https://rosettacode.org/wiki/Chinese_remainder_theorem
def modular_multiplicative_inverse(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def test_chinese_remainder():
    n = [3, 5, 7]
    a = [2, 3, 2]
    assert chinese_remainder(n, a) == 23
