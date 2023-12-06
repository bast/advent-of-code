from functools import reduce


def num_winning(t, d):
    n = 0
    for i in range(t):
        speed, seconds = (i, t - i)
        distance = speed * seconds
        if distance > d:
            n += 1
    return n


records1 = [(34, 204), (90, 1713), (89, 1210), (86, 1780)]
records2 = [(34908986, 204171312101780)]


for part, records in [(1, records1), (2, records2)]:
    numbers = list(map(lambda x: num_winning(x[0], x[1]), records))
    print(f"part {part}:", reduce(lambda x, y: x * y, numbers))
