from collections import defaultdict


def read_input(file_name, num_x, num_y):
    lines = open(file_name, "r").read().splitlines()
    risks = {}
    k = 0
    for icol in range(num_x):
        for line in lines:
            for jcol in range(num_y):
                for c in line:
                    risks[k] = (int(c) + icol + jcol - 1) % 9 + 1
                    k += 1
    return risks


def precompute_neighbors(side_length):
    neighbors = defaultdict(list)
    k = 0
    for y in range(side_length):
        for x in range(side_length):
            for d in [-1, +1]:
                if 0 <= x + d < side_length:
                    neighbors[k].append(k + d)
            for d in [-1, +1]:
                if 0 <= y + d < side_length:
                    neighbors[k].append(k + d * side_length)
            k += 1
    return neighbors


def shortest_path(risks, neighbors):
    distance = defaultdict(int)
    nodes_to_visit = set(range(1, len(risks)))
    current_node = 0
    while len(nodes_to_visit) > 0:
        for neighbor in neighbors[current_node]:
            n = distance[current_node] + risks[neighbor]
            if distance[neighbor] == 0 or distance[neighbor] > n:
                distance[neighbor] = n
                nodes_to_visit.add(neighbor)
        current_node = nodes_to_visit.pop()
    return distance[len(risks) - 1]


for (title, num_x, num_y) in [("part 1:", 1, 1), ("part 2:", 5, 5)]:
    risks = read_input("input.txt", num_x, num_y)
    side_length = int(len(risks) ** 0.5)
    neighbors = precompute_neighbors(side_length)
    print(title, shortest_path(risks, neighbors))
