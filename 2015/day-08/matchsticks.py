def replaced_length(line: str) -> int:
    s = f"{line[1:-1]}"
    s = s.replace(r"\\", "_")
    s = s.replace(r"\"", "_")
    return len(s) - 3 * s.count(r"\x")


def encoded_length(line: str) -> int:
    return len(line) + line.count(r'"') + line.count("\\") + 2


lines = open("input.txt", "r").read().splitlines()

print("part 1:", sum(map(lambda l: len(l) - replaced_length(l), lines)))
print("part 2:", sum(map(lambda l: encoded_length(l) - len(l), lines)))
