import sys

sys.path.append("../..")

from read import read_regex_and_parse


crates = {
    1: ["T", "P", "Z", "C", "S", "L", "Q", "N"],
    2: ["L", "P", "T", "V", "H", "C", "G"],
    3: ["D", "C", "Z", "F"],
    4: ["G", "W", "T", "D", "L", "M", "V", "C"],
    5: ["P", "W", "C"],
    6: ["P", "F", "J", "D", "C", "T", "S", "Z"],
    7: ["V", "W", "G", "B", "D"],
    8: ["N", "J", "S", "Q", "H", "W"],
    9: ["R", "C", "Q", "F", "S", "L", "V"],
}

instructions = read_regex_and_parse(
    "input.txt", r"move (\d+) from (\d+) to (\d+)", (int, int, int)
)

for n, a, b in instructions:
    for _ in range(n):
        crates[b].append(crates[a].pop())

print("part 1:", "".join(v[-1] for v in crates.values()))

# run instructions backwards to reset the input
for n, b, a in reversed(instructions):
    for _ in range(n):
        crates[b].append(crates[a].pop())

for n, a, b in instructions:
    docks = []
    for _ in range(n):
        docks.append(crates[a].pop())
    for _ in range(n):
        crates[b].append(docks.pop())

print("part 2:", "".join(v[-1] for v in crates.values()))
