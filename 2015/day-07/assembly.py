import operator
import re


def read_instructions(lines):
    instructions = {}
    for line in lines:
        m = (
            re.match(r"(\w+) -> (\w+)", line)
            or re.match(r"(\w+) (\w+) (\w+) -> (\w+)", line)
            or re.match(r"(\w+) (\w+) -> (\w+)", line)
        ).groups()

        instructions[m[-1]] = m[:-1]
    return instructions


def int_or_evaluate(instructions, s, values):
    try:
        return int(s)
    except:
        return evaluate(instructions, s, values)


def evaluate(instructions, value, values):
    if not value in values:
        command = instructions[value]
        match len(command):
            case 1:
                values[value] = int_or_evaluate(instructions, command[0], values)
            case 2:
                _not, x = command
                values[value] = ~(int_or_evaluate(instructions, x, values)) & 0xFFFF
            case 3:
                a, op, b = command
                match op:
                    case "AND":
                        values[value] = operator.and_(
                            int_or_evaluate(instructions, a, values),
                            int_or_evaluate(instructions, b, values),
                        )
                    case "OR":
                        values[value] = operator.or_(
                            int_or_evaluate(instructions, a, values),
                            int_or_evaluate(instructions, b, values),
                        )
                    case "LSHIFT":
                        values[value] = operator.lshift(
                            int_or_evaluate(instructions, a, values),
                            int_or_evaluate(instructions, b, values),
                        )
                    case "RSHIFT":
                        values[value] = operator.rshift(
                            int_or_evaluate(instructions, a, values),
                            int_or_evaluate(instructions, b, values),
                        )

    return values[value]


lines = open("input.txt", "r").read().splitlines()

instructions = read_instructions(lines)
result = evaluate(instructions, "a", values={})
print(f"part 1: {result}")

new_lines = []
for line in lines:
    if line.endswith("-> b"):
        new_lines.append(f"{result} -> b")
    else:
        new_lines.append(line)

instructions = read_instructions(new_lines)
result = evaluate(instructions, "a", values={})
print(f"part 2: {result}")
