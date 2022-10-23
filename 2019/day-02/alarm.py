import sys
from more_itertools import grouper

sys.path.append("../..")

from read import read_split_and_parse


def intcode(series, noun, verb):
    series[1] = noun
    series[2] = verb
    for (i, j, k, l) in grouper(range(len(series)), 4):
        opcode = series[i]
        if opcode == 99:
            return series[0]
        a = series[series[j]]
        b = series[series[k]]
        if opcode == 1:
            series[series[l]] = a + b
        else:
            series[series[l]] = a * b


def find_pair(series, target):
    for noun in range(100):
        for verb in range(100):
            if intcode(series[:], noun, verb) == target:
                return noun, verb


series = read_split_and_parse("input.txt", ",", int)
print(f"part 1: {intcode(series[:], 12, 2)}")

noun, verb = find_pair(series, 19690720)
print(f"part 2: {100 * noun + verb}")
