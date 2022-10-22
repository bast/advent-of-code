def result(sequence, shift):
    n = len(sequence)
    result = 0
    for i, a in enumerate(sequence):
        if a == sequence[(i + shift) % n]:
            result += a
    return result


text = open("input.txt", "r").read().strip()
sequence = list(map(int, text))

print(f"part 1: {result(sequence, 1)}")
print(f"part 2: {result(sequence, len(sequence) // 2)}")
