import hashlib
import re
import sys
from collections import defaultdict
from heapq import heappush, heappop

sys.path.append("../..")

from read import read_regex_and_parse


def get_hash(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def split_into_elements(molecule: str) -> list[str]:
    return re.findall(r"[A-Z][a-z]*", molecule)


def part1(molecule, replacements) -> int:
    hashes = set()
    elements = split_into_elements(molecule)
    for i, element in enumerate(elements):
        for replacement in replacements[element]:
            new_molecule = list(elements)
            new_molecule[i] = replacement
            hashes.add(get_hash("".join(new_molecule)))
    return len(hashes)


def replacements_one_at_a_time(
    string: str, substring: str, replace_by: str
) -> list[str]:
    l = []
    for m in re.finditer(substring, string):
        l.append(string[: m.start()] + replace_by + string[m.end() :])
    return l


def part2(molecule, replacements_back, basic_elements) -> int:
    """
    Replace molecules "backwards" in a greedy way: Always take the shortest
    intermediate as the next molecule to process and put new intermediates back
    into the priority queue where the priority is the length of the molecule.
    This does not guarantee to always find the smallest number of steps but it
    works here for this example.
    """
    queue = []
    heappush(queue, (len(molecule), (molecule, 0)))  # 0 steps
    while True:
        _, (molecule, num_steps) = heappop(queue)
        for k, v in replacements_back.items():
            if k in molecule:
                for new_molecule in replacements_one_at_a_time(molecule, k, v):
                    if new_molecule in basic_elements:
                        return num_steps + 2
                    else:
                        heappush(
                            queue, (len(new_molecule), (new_molecule, num_steps + 1))
                        )


molecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

replacements = defaultdict(list)
replacements_back = {}
basic_elements = set()
for a, b in read_regex_and_parse("input.txt", r"(\w+) => (\w+)", (str, str)):
    if a == "e":
        basic_elements.add(b)
    else:
        replacements[a].append(b)
        replacements_back[b] = a

print("part 1:", part1(molecule, replacements))
print("part 2:", part2(molecule, replacements_back, basic_elements))
