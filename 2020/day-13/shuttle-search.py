import sys

sys.path.append("../..")

from crt import chinese_remainder


def minutes_to_wait(t, bus_number) -> int:
    multiple = bus_number * (t // bus_number)
    if multiple < t:
        return multiple + bus_number - t
    return 0


def part1(t, line):
    bus_numbers = []
    for item in line.split(","):
        if item != "x":
            bus_numbers.append(int(item))
    waiting_times = map(lambda b: minutes_to_wait(t, b), bus_numbers)
    w, b = sorted(zip(waiting_times, bus_numbers))[0]
    return w * b


def part2(line):
    moduli = line.split(",")
    residues = reversed(range(1, len(moduli) + 1))

    n = []
    a = []
    for m, r in zip(moduli, residues):
        if m != "x":
            n.append(int(m))
            a.append(r)

    return chinese_remainder(n, a) - len(moduli)


t = 1000390
line = "13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17"

print("part 1:", part1(t, line))
print("part 2:", part2(line))
