import re
from minizinc import Instance, Model, Solver


def parse_puzzle(path: str) -> list[dict]:
    results = []

    for line in open(path, "r").read().splitlines():
        line = line.strip()

        match_positions = re.search(r"\[([.#]+)\]", line)
        positions = [1 if c == "#" else 0 for c in match_positions.group(1)]

        match_buttons = re.findall(r"\(([\d,]+)\)", line)
        buttons = []
        for combination in match_buttons:
            buttons.append([int(x) for x in combination.split(",")])

        match_values = re.search(r"\{([\d,]+)\}", line)
        values = [int(x) for x in match_values.group(1).split(",")]

        results.append({"positions": positions, "buttons": buttons, "values": values})

    return results


def minizinc_model(buttons: list[list[int]], target: list[int], operation: str) -> str:
    num_positions = len(target)
    num_buttons = len(buttons)

    # button[b][i] = 1 if button b flips position i
    matrix = []
    for btn in buttons:
        row = [1 if i in btn else 0 for i in range(num_positions)]
        matrix.extend(row)

    matrix_str = ", ".join(str(v) for v in matrix)

    target_str = ", ".join(str(v) for v in target)

    if operation == "xor":
        extra_operation = "mod 2"
        value_range = "0..1"
    elif operation == "sum":
        extra_operation = ""
        value_range = "0..max(target)"
    else:
        raise ValueError(f"unknown operation: {operation}")

    model = f"""
int: num_positions = {num_positions};
int: num_buttons = {num_buttons};

array[1..num_buttons, 1..num_positions] of int: button =
  array2d(1..num_buttons, 1..num_positions,
    [
      {matrix_str}
    ]
  );

array[1..num_positions] of int: target = [{target_str}];

array[1..num_buttons] of var {value_range}: x;

constraint
  forall(i in 1..num_positions)(
      sum(b in 1..num_buttons)( button[b,i] * x[b] ) {extra_operation} = target[i]
  );

solve minimize sum(b in 1..num_buttons)(x[b]);
"""

    return model


# example: min_number_of_button_presses([[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]], [0, 1, 1, 0], operation="xor")
def min_number_of_button_presses(
    buttons: list[list[int]], target: list[int], operation: str
) -> int:
    model = Model()
    model.add_string(minizinc_model(buttons, target, operation))
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode, model)
    result = instance.solve(all_solutions=False)
    return sum(result["x"])


if __name__ == "__main__":
    lines = parse_puzzle("input.txt")

    result1 = 0
    result2 = 0
    for i, line in enumerate(lines):
        print(f"processing line {i + 1}/{len(lines)}")

        result1 += min_number_of_button_presses(
            line["buttons"], line["positions"], operation="xor"
        )
        result2 += min_number_of_button_presses(
            line["buttons"], line["values"], operation="sum"
        )

    print("part 1:", result1)
    print("part 2:", result2)
