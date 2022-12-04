import sys

sys.path.append("../..")

from read import read_regex_and_parse


def one_range_covers_the_other(a, b, c, d) -> bool:
    return (a <= c <= d <= b) or (c <= a <= b <= d)


def ranges_overlap(a, b, c, d) -> bool:
    return (
        one_range_covers_the_other(a, b, c, d)
        or (a <= c <= b)
        or (a <= d <= b)
        or (c <= a <= d)
        or (c <= b <= d)
    )


n1 = 0
n2 = 0
for a, b, c, d in read_regex_and_parse(
    "input.txt", r"(\d+)-(\d+),(\d+)-(\d+)", (int, int, int, int)
):
    if one_range_covers_the_other(a, b, c, d):
        n1 += 1
    if ranges_overlap(a, b, c, d):
        n2 += 1

print("part 1:", n1)
print("part 2:", n2)
