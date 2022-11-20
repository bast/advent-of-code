import sys

sys.path.append("../..")

from read import read_regex_and_parse


usages = []
availabilities = []
for _x, _y, used, avail in read_regex_and_parse(
    "input.txt",
    r"/dev/grid/node-x(\d+)-y(\d+)\s+\w+\s+(\d+)T\s+(\d+)T\s+\w+",
    (int, int, int, int),
):
    usages.append(used)
    availabilities.append(avail)


# the only node where the avail was larger than minimum size had avail 91
n = len(list(filter(lambda n: n < 92, usages)))
print("part 1:", n - 1)  # subtracting the node with 0
