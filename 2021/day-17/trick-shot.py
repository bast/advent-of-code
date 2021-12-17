def gravity(vx, vy):
    return (vx, vy - 1)


def drag(vx, vy):
    if vx > 0:
        return (vx - 1, vy)
    if vx < 0:
        return (vx + 1, vy)
    return (vx, vy)


def positions(vx, vy):
    (x, y) = (0, 0)
    while True:
        x += vx
        y += vy
        (vx, vy) = drag(vx, vy)
        (vx, vy) = gravity(vx, vy)
        yield (x, y)


def shoot(vx, vy, target):
    (tx_min, tx_max, ty_min, ty_max) = target
    p = positions(vx, vy)
    y_max = 0
    while True:
        (x, y) = next(p)
        if y < ty_min:
            break
        y_max = max(y_max, y)
        if tx_min <= x <= tx_max and ty_min <= y <= ty_max:
            return True, y_max
    return False, y_max


def find_all_shots(tx_min, tx_max, ty_min, ty_max):
    target = (tx_min, tx_max, ty_min, ty_max)
    highest = 0
    count = 0
    for vx in range(tx_max + 1):
        for vy in range(ty_min, 100):  # 100 is a lazy guess
            hits_target, y_max = shoot(vx, vy, target)
            if hits_target:
                count += 1
                highest = max(highest, y_max)
    return highest, count


highest, count = find_all_shots(20, 30, -10, -5)
print(f"example part 1: {highest}, example part 2: {count}")

highest, count = find_all_shots(241, 273, -97, -63)
print(f"part 1: {highest}, part 2: {count}")
