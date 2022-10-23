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


def read_positions(file_name, row_major):
    positions = []
    with open(file_name, "r") as f:
        for row, line in enumerate(f.read().splitlines()):
            for col, c in enumerate(line):
                if c == "#":
                    if row_major:
                        positions.append((row, col))
                    else:
                        positions.append((col, row))
    return positions


def read_block_columns(file_name):
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
        columns = []
        for column in range(len(lines[0])):
            columns.append([line[column] for line in lines])
        return columns


def read_block_dimensions(file_name):
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
        num_rows = len(lines)
        num_cols = len(lines[0])
        return num_rows, num_cols
