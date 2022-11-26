def num_jumps(offsets, part2):
    n = 0
    current_position = 0
    while True:
        try:
            new_position = current_position + offsets[current_position]
            if part2 and offsets[current_position] > 2:
                offsets[current_position] -= 1
            else:
                offsets[current_position] += 1
            current_position = new_position
            n += 1
        except IndexError:
            return n


offsets = list(map(int, open("input.txt", "r").read().splitlines()))
print("part 1:", num_jumps(list(offsets), part2=False))
print("part 2:", num_jumps(list(offsets), part2=True))
