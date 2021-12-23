from collections import defaultdict


def read_input(file_name):
    data = defaultdict(list)
    i = -1
    for line in open(file_name, "r").read().splitlines():
        if "scanner" in line:
            i += 1
        if "," in line:
            (x, y, z) = tuple(map(int, line.split(",")))
            data[i].append((x, y, z))
    return data


def distance(x1, y1, z1, x2, y2, z2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    # multiplying and converting to integer just to be able to form a set and
    # have enough digits
    return int(d * 1000.0)  # arbitrary units but we need enough digits


def num_unique_beacons(file_name):
    data = read_input(file_name)

    # the distance to two closest neighbor beacons
    # is taken as "signature" of that beacon
    signatures = set()

    for sensor in data.keys():
        for (x1, y1, z1) in data[sensor]:
            distances = sorted(
                [distance(x1, y1, z1, x2, y2, z2) for (x2, y2, z2) in data[sensor]]
            )
            # we are only interested in distances to two closest beacons
            _, b, c, *_ = distances
            signatures.add((b, c))

    return len(signatures)


print("example 1:", num_unique_beacons("example.txt"))
print("part 1:", num_unique_beacons("input.txt"))
