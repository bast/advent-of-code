from itertools import permutations


def num_digits_part1(line):
    before, after = line.split(" | ")
    return len(list(filter(lambda w: len(w) in [2, 4, 3, 7], after.split())))


def translate_word(word, d):
    return "".join(sorted([d[c] for c in word]))


def permutation_is_valid(permutation, words, segments_to_digit):
    d = {k: v for (k, v) in zip(permutation, "abcdefg")}
    for word in words:
        if translate_word(word, d) not in segments_to_digit:
            return False
    return True


def find_valid_permutation(words, segments_to_digit):
    for permutation in permutations("abcdefg"):
        if permutation_is_valid(permutation, words, segments_to_digit):
            return permutation


def value_part2(line):
    before, after = line.split(" | ")
    valid_permutation = find_valid_permutation(before.split(), segments_to_digit)
    d = {k: v for (k, v) in zip(valid_permutation, "abcdefg")}
    digits = map(lambda w: segments_to_digit[translate_word(w, d)], after.split())
    return int("".join(digits))


segments_to_digit = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

print("part 1:", sum(map(num_digits_part1, lines)))
print("part 2:", sum(map(value_part2, lines)))
