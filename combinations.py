def find_combinations(containers, target, allow_reuse):
    valid_combinations = []
    combination = []
    visited = set()
    _find_recursive(
        valid_combinations, containers, combination, target, 0, visited, allow_reuse
    )
    return valid_combinations


def _find_recursive(
    valid_combinations,
    containers,
    combination,
    target,
    current_index,
    visited,
    allow_reuse,
):
    if target == 0:
        valid_combinations.append(list(combination))
        return
    for i, container in enumerate(containers):
        if i >= current_index:
            if allow_reuse or (i not in visited):
                if (target - container) >= 0:
                    # add container
                    combination.append(container)
                    if not allow_reuse:
                        visited.add(i)
                    # recurse
                    _find_recursive(
                        valid_combinations,
                        containers,
                        combination,
                        target - container,
                        i,
                        visited,
                        allow_reuse,
                    )
                    # backtrack
                    combination.remove(container)
                    if not allow_reuse:
                        visited.remove(i)


def test_find_combinations_with_reuse():
    assert find_combinations(
        containers=[20, 15, 10, 5], target=25, allow_reuse=True
    ) == [[20, 5], [15, 10], [15, 5, 5], [10, 10, 5], [10, 5, 5, 5], [5, 5, 5, 5, 5]]


def test_find_combinations_without_reuse():
    assert find_combinations(
        containers=[20, 15, 10, 5, 5], target=25, allow_reuse=False
    ) == [[20, 5], [20, 5], [15, 10], [15, 5, 5]]
