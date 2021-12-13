from collections import defaultdict


def walk(graph, current_node, destination, num_visits, is_valid_move, path):
    if current_node in num_visits:
        num_visits[current_node] += 1
    path.append(current_node)

    successful_paths = []
    if current_node == destination:
        successful_paths.append(list(path))
    else:
        for next_node in graph[current_node]:
            if is_valid_move(next_node, num_visits):
                successful_paths += walk(
                    graph, next_node, destination, num_visits, is_valid_move, path
                )

    if current_node in num_visits:
        num_visits[current_node] -= 1
    path.pop()
    return successful_paths


def read_input(file_name):
    d = defaultdict(list)
    for line in open(file_name).read().splitlines():
        a, b = line.split("-")
        d[a].append(b)
        d[b].append(a)
    return d


def is_valid_move1(next_node, d):
    if next_node not in d:
        return True
    return d[next_node] < 1


def is_valid_move2(next_node, d):
    if next_node not in d:
        return True
    if next_node in ["start", "end"]:
        return d[next_node] < 1
    if d[next_node] == 2:
        return False
    if 2 in d.values():
        return d[next_node] < 1
    return True


if __name__ == "__main__":
    graph = read_input("input.txt")

    num_visits = {k: 0 for k in graph.keys() if k.islower()}
    successful_paths = walk(graph, "start", "end", num_visits, is_valid_move1, path=[])
    print("part 1:", len(successful_paths))

    num_visits = {k: 0 for k in graph.keys() if k.islower()}
    successful_paths = walk(graph, "start", "end", num_visits, is_valid_move2, path=[])
    print("part 2:", len(successful_paths))
