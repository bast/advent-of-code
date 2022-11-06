def move(position, instructions, pad):
    row, col = position
    for instruction in instructions:
        match instruction:
            case "U":
                new_position = (row - 1, col)
            case "D":
                new_position = (row + 1, col)
            case "L":
                new_position = (row, col - 1)
            case "R":
                new_position = (row, col + 1)
        if new_position in pad:
            row, col = new_position
    return (row, col)


def get_code(lines, pad, start_position):
    position = start_position
    code = ""
    for line in lines:
        position = move(position, line, pad)
        code += pad[position]
    return code


pad1 = {
    (0, 0): "1",
    (0, 1): "2",
    (0, 2): "3",
    (1, 0): "4",
    (1, 1): "5",
    (1, 2): "6",
    (2, 0): "7",
    (2, 1): "8",
    (2, 2): "9",
}

pad2 = {
    (0, 2): "1",
    (1, 1): "2",
    (1, 2): "3",
    (1, 3): "4",
    (2, 0): "5",
    (2, 1): "6",
    (2, 2): "7",
    (2, 3): "8",
    (2, 4): "9",
    (3, 1): "A",
    (3, 2): "B",
    (3, 3): "C",
    (4, 2): "D",
}

lines = open("input.txt", "r").read().splitlines()

print("part 1:", get_code(lines, pad1, (1, 1)))
print("part 2:", get_code(lines, pad2, (2, 0)))
