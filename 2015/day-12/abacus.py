import re
import json


def sum_numbers(s):
    numbers = map(int, re.findall(r"([-]*[0-9]+)", s))
    return sum(numbers)


def sum_json(element):
    if type(element) is int:
        return element
    if type(element) is list:
        return sum(map(sum_json, element))
    if type(element) is dict:
        if "red" in element.values():
            return 0
        return sum(map(sum_json, element.values()))
    else:
        return 0


text = open("input.txt", "r").read()

print("part 1:", sum_numbers(text))
print("part 2:", sum_json(json.loads(text)))
