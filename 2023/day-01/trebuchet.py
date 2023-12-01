def calibration_value(line, mapping):
    l = []
    for k, v in mapping.items():
        p = line.find(k)
        if p != -1:
            l.append((p, v))
        p = line.rfind(k)
        if p != -1:
            l.append((p, v))
    l.sort()
    (_, first), (_, last) = l[0], l[-1]
    return 10 * first + last


lines = open("input.txt", "r").read().splitlines()

mapping = {str(i): i for i in range(1, 10)}

print("part 1:", sum(map(lambda l: calibration_value(l, mapping), lines)))

mapping.update(
    {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
)

print("part 2:", sum(map(lambda l: calibration_value(l, mapping), lines)))
