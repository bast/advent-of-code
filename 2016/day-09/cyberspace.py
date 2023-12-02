from functools import lru_cache


@lru_cache(maxsize=None)
def count(s, recursive):
    length = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            j = s.find(")", i)
            n, m = map(int, s[i + 1 : j].split("x"))
            new_s = s[j + 1 : j + 1 + n] * m
            i = j + 1 + n
            if recursive:
                length += count(new_s, recursive)
            else:
                length += len(new_s)
        else:
            i += 1
            length += 1
    return length


def test_count():
    assert count("ADVENT", recursive=False) == 6
    assert count("A(1x5)BC", recursive=False) == 7
    assert count("(3x3)XYZ", recursive=False) == 9
    assert count("A(2x2)BCD(2x2)EFG", recursive=False) == 11
    assert count("(6x1)(1x3)A", recursive=False) == 6
    assert count("X(8x2)(3x3)ABCY", recursive=False) == 18


def test_count_recursive():
    assert count("(3x3)XYZ", recursive=True) == 9
    assert count("X(8x2)(3x3)ABCY", recursive=True) == 20
    assert count("(27x12)(20x12)(13x14)(7x10)(1x12)A", recursive=True) == 241920
    assert (
        count(
            "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", recursive=True
        )
        == 445
    )


s = open("input.txt").read().strip()

print("part 1:", count(s, recursive=False))
print("part 2:", count(s, recursive=True))
