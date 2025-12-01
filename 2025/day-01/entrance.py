def parse_line(line: str) -> int:
    direction, num_steps = line[0], int(line[1:])
    if direction == "R":
        return num_steps
    else:
        return -num_steps


lines = open("input.txt").read().splitlines()

position = 50
num_clicks1 = 0
num_clicks2 = 0


for line in lines:
    step = parse_line(line)
    new_position = (position + step) % 100

    num_clicks2 += abs(int((position + step) / 100))
    if new_position == 0:
        num_clicks1 += 1

    if step < 0 and abs(step) >= position and position != 0:
        num_clicks2 += 1

    position = new_position


print("part 1:", num_clicks1)
print("part 2:", num_clicks2)
