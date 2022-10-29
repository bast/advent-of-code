from itertools import combinations


def quantum_entanglement(packages, num_groups, num_in_first_group):
    target = sum(packages) // num_groups
    results = []
    for combination in combinations(range(len(packages)), num_in_first_group):
        s = 0
        p = 1
        for i in combination:
            s += packages[i]
            p *= packages[i]
        if s == target:
            results.append(p)
    return results


packages = [
    1,
    3,
    5,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
]

# has to be even and the smallest even number where the sum matches is 6
results = quantum_entanglement(packages, 3, 6)
print("part 1:", sorted(results)[0])

# smallest odd number is 5
results = quantum_entanglement(packages, 4, 5)
print("part 2:", sorted(results)[0])
