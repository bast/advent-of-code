def process_line(line, registers) -> int:
    instruction, arg, *jump = line.split()
    offset = 1
    match instruction:
        case "hlf":
            registers[arg] //= 2
        case "tpl":
            registers[arg] *= 3
        case "inc":
            registers[arg] += 1
        case "jmp":
            offset = int(arg)
        case "jie":
            if registers[arg] % 2 == 0:
                offset = int(jump[0])
        case "jio":
            if registers[arg] == 1:
                offset = int(jump[0])
    return offset


def run_program(instructions, registers):
    position = 0
    while True:
        try:
            position += process_line(instructions[position], registers)
        except:
            return registers


instructions = open("input.txt", "r").read().splitlines()
instructions = list(map(lambda s: s.replace(",", ""), instructions))


print("part 1:", run_program(instructions, {"a": 0, "b": 0}))
print("part 2:", run_program(instructions, {"a": 1, "b": 0}))
