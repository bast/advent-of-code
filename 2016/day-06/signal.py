import sys
from collections import Counter


sys.path.append("../..")

from read import read_block_columns


def most_common(column):
    character, _ = Counter(column).most_common(1)[0]
    return character


def least_common(column):
    c = Counter(column)
    sorted_list = sorted(c.items(), key=lambda t: t[1], reverse=True)
    character, _ = sorted_list.pop()
    return character


columns = read_block_columns("input.txt")

print(f"part 1: {''.join(map(most_common, columns))}")
print(f"part 2: {''.join(map(least_common, columns))}")
