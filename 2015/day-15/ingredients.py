from more_itertools import flatten
from collections import defaultdict


def partitions(total, num_parts):
    assert num_parts > 1
    l = []
    if num_parts == 2:
        for i in range(total + 1):
            l.append((i, total - i))
    else:
        for i in range(total + 1):
            for p in partitions(total - i, num_parts - 1):
                l.append(tuple(flatten([[i], p])))
    return l


def test_partitions():
    assert partitions(5, 2) == [(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]
    assert partitions(5, 3) == [
        (0, 0, 5),
        (0, 1, 4),
        (0, 2, 3),
        (0, 3, 2),
        (0, 4, 1),
        (0, 5, 0),
        (1, 0, 4),
        (1, 1, 3),
        (1, 2, 2),
        (1, 3, 1),
        (1, 4, 0),
        (2, 0, 3),
        (2, 1, 2),
        (2, 2, 1),
        (2, 3, 0),
        (3, 0, 2),
        (3, 1, 1),
        (3, 2, 0),
        (4, 0, 1),
        (4, 1, 0),
        (5, 0, 0),
    ]


def total_score(scores, partitioning, num_calories) -> int:
    sums = defaultdict(int)
    for i, name in enumerate(scores.keys()):
        p = partitioning[i]
        for k, v in scores[name].items():
            sums[k] += v * p
    for k, v in sums.items():
        sums[k] = max(0, v)
    result = sums["capacity"] * sums["durability"] * sums["flavor"] * sums["texture"]
    if num_calories:
        if sums["calories"] != num_calories:
            result = 0
    return result


scores = {}
scores["Sugar"] = {
    "capacity": 3,
    "durability": 0,
    "flavor": 0,
    "texture": -3,
    "calories": 2,
}
scores["Sprinkles"] = {
    "capacity": -3,
    "durability": 3,
    "flavor": 0,
    "texture": 0,
    "calories": 9,
}
scores["Candy"] = {
    "capacity": -1,
    "durability": 0,
    "flavor": 4,
    "texture": 0,
    "calories": 1,
}
scores["Chocolate"] = {
    "capacity": 0,
    "durability": 0,
    "flavor": -2,
    "texture": 2,
    "calories": 8,
}


if __name__ == "__main__":
    result = max(
        map(lambda p: total_score(scores, p, num_calories=None), partitions(100, 4))
    )
    print(f"part 1: {result}")

    result = max(
        map(lambda p: total_score(scores, p, num_calories=500), partitions(100, 4))
    )
    print(f"part 2: {result}")
