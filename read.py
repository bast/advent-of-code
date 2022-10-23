import re


def read_split_and_parse(file_name, character, fun):
    with open(file_name, "r") as f:
        return list(map(fun, f.read().split(character)))


def read_regex_and_parse(file_name, regex, fun):
    """
    Example: read_and_parse("input.txt", r"(\d+) -> (\d+)", (float, int))
    """
    pattern = re.compile(regex)
    result = []
    with open(file_name, "r") as f:
        for line in f.read().splitlines():
            try:
                words = pattern.search(line).groups()
                if len(words) == 1:
                    result.append(fun(words[0]))
                else:
                    result.append(tuple(map(lambda t: t[0](t[1]), zip(fun, words))))
            except AttributeError:
                pass
    return result


def read_positions(file_name):
    positions = []
    with open(file_name, "r") as f:
        for row, line in enumerate(f.read().splitlines()):
            for col, c in enumerate(line):
                if c == "#":
                    positions.append((col, row))
    return positions
