import sys

sys.path.append("../..")

from read import read_regex_and_parse


elements = set(read_regex_and_parse("input.txt", r"^(\w+).*", str))

linked_to_elements = set()
for line in read_regex_and_parse("input.txt", r".* -> (.*)$", str):
    for word in line.split(", "):
        linked_to_elements.add(word)

print("part 1:", elements.difference(linked_to_elements))
