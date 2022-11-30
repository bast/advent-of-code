import math


def compare(p1, p2, v1, v2):
    if p1 < p2:
        v1 += 1
        v2 -= 1
    if p1 > p2:
        v2 += 1
        v1 -= 1
    return v1, v2


def step(pos, vel):
    p1, p2, p3, p4 = pos
    v1, v2, v3, v4 = vel

    # apply gravity
    v1, v2 = compare(p1, p2, v1, v2)
    v1, v3 = compare(p1, p3, v1, v3)
    v1, v4 = compare(p1, p4, v1, v4)
    v2, v3 = compare(p2, p3, v2, v3)
    v2, v4 = compare(p2, p4, v2, v4)
    v3, v4 = compare(p3, p4, v3, v4)

    # apply velocity
    p1 += v1
    p2 += v2
    p3 += v3
    p4 += v4

    return (p1, p2, p3, p4), (v1, v2, v3, v4)


def energy(px, py, pz, vx, vy, vz):
    e = 0
    for i in range(4):
        pot = abs(px[i]) + abs(py[i]) + abs(pz[i])
        kin = abs(vx[i]) + abs(vy[i]) + abs(vz[i])
        e += pot * kin
    return e


def energy_after_num_steps(px, py, pz, vx, vy, vz, num_steps) -> int:
    for _ in range(num_steps):
        px, vx = step(px, vx)
        py, vy = step(py, vy)
        pz, vz = step(pz, vz)
    return energy(px, py, pz, vx, vy, vz)


def period(pos, vel) -> int:
    s = set()
    i = 0
    while (pos, vel) not in s:
        s.add((pos, vel))
        pos, vel = step(pos, vel)
        i += 1
    return i


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


px = (-6, 12, 9, -1)
py = (2, -14, 5, -4)
pz = (-9, -4, -6, 9)

vx = (0, 0, 0, 0)
vy = (0, 0, 0, 0)
vz = (0, 0, 0, 0)

result = energy_after_num_steps(px, py, pz, vx, vy, vz, 1000)
print("part 1:", result)

pa = period(px, vx)
pb = period(py, vy)
pc = period(pz, vz)
print("part 2:", lcm(pa, lcm(pb, pc)))
