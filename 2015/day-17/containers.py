import sys
from collections import Counter

sys.path.append("../..")

from combinations import find_combinations


containers = [
    33,
    14,
    18,
    20,
    45,
    35,
    16,
    35,
    1,
    13,
    18,
    13,
    50,
    44,
    48,
    6,
    24,
    41,
    30,
    42,
]

target = 150

combinations = find_combinations(containers, target, allow_reuse=False)
print(f"part 1: {len(combinations)}")

counter = Counter(map(len, combinations))
print(f"part 2: {counter}")
