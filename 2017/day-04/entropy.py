def passphrase_is_valid1(line):
    words = line.split()
    return len(words) == len(set(words))


def passphrase_is_valid2(line):
    words = line.split()
    words = list(map(lambda w: "".join(sorted(w)), words))
    return len(words) == len(set(words))


lines = open("input.txt", "r").read().splitlines()

print("part 1:", sum(map(passphrase_is_valid1, lines)))
print("part 2:", sum(map(passphrase_is_valid2, lines)))
