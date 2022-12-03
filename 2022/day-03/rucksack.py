import string
from more_itertools import chunked


def common_character(chunks) -> str:
    first, *other = tuple(chunks)
    s = set(first)
    for chunk in other:
        s = s.intersection(set(chunk))
    return s.pop()


def split_line(line: str) -> (str, str):
    n = len(line) // 2
    return line[:n], line[n:]


priority = {}
for i, c in enumerate(string.ascii_lowercase + string.ascii_uppercase):
    priority[c] = i + 1

lines = open("input.txt", "r").read().splitlines()

characters = map(common_character, map(split_line, lines))
print("part 1:", sum(map(lambda c: priority[c], characters)))

characters = map(common_character, chunked(lines, 3))
print("part 2:", sum(map(lambda c: priority[c], characters)))
