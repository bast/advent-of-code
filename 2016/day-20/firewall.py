import sys

sys.path.append("../..")

from read import read_regex_and_parse


def range_containing_number(n, ranges):
    for lower, upper in ranges:
        if lower <= n <= upper:
            return (lower, upper)
    return None


def add_tuple(t, ranges):
    lower, upper = t
    lower_range = range_containing_number(lower, ranges)
    upper_range = range_containing_number(upper, ranges)
    match (lower_range, upper_range):
        case ((a, b), None):
            ranges.remove((a, b))
            ranges.add((a, upper))
        case (None, (c, d)):
            ranges.remove((c, d))
            ranges.add((lower, d))
        case ((a, b), (c, d)):
            ranges.remove((a, b))
            if (c, d) in ranges:
                ranges.remove((c, d))
            ranges.add((a, d))
        case (None, None):
            ranges.add((lower, upper))


def range_len(t):
    return t[1] - t[0] + 1


tuples = read_regex_and_parse("input.txt", r"(\d+)-(\d+)", (int, int))
tuples = sorted(tuples, key=range_len, reverse=True)

ranges = set()
for t in tuples:
    add_tuple(t, ranges)

for _, upper in sorted(list(ranges)):
    if range_containing_number(upper + 1, ranges) is None:
        print("part 1:", upper + 1)
        break

print("part 2:", 1 + 4294967295 - sum(map(range_len, ranges)))
