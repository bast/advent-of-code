from collections import defaultdict


def parent_directory(path):
    *rest, _, _ = tuple(path.split("/"))
    return "/".join(rest) + "/"


def all_parents(path):
    parents = []
    while path != "/":
        path = parent_directory(path)
        parents.append(path)
    return parents


def read_sizes(file_name):
    sizes = defaultdict(int)
    pwd = ""
    for line in open(file_name, "r").read().splitlines():
        a, b, *c = tuple(line.split())
        match (a, b, c):
            case ("dir", _, _):
                pass
            case ("$", "ls", _):
                pass
            case ("$", "cd", arg):
                if arg == [".."]:
                    pwd = parent_directory(pwd)
                else:
                    pwd += arg[0]
                    if not pwd.endswith("/"):
                        pwd += "/"
            case (n, _, _):
                size = int(n)
                sizes[pwd] += size
                for parent in all_parents(pwd):
                    sizes[parent] += size
    return sizes


sizes = read_sizes("input.txt")

print("part 1:", sum(filter(lambda n: n <= 100000, sizes.values())))

target = 30000000 - (70000000 - max(sizes.values()))

print("part 2:", min(filter(lambda n: n >= target, sizes.values())))
