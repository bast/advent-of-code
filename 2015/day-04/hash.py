import hashlib


def find_answer(puzzle_input, starts_with):
    i = 1
    while True:
        s = puzzle_input + str(i)
        digest = hashlib.md5(s.encode("utf-8")).hexdigest()
        if digest.startswith(starts_with):
            return i
        i += 1


print("part 1:", find_answer("iwrupvqb", "00000"))
print("part 2:", find_answer("iwrupvqb", "000000"))
