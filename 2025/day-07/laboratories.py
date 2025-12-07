from collections import defaultdict


def num_splits(lines):
    beams = set()
    result = 0

    for line in lines:
        for i, char in enumerate(line):
            if char == "S":
                beams.add(i)
            elif char == "^" and i in beams:
                beams.remove(i)
                beams.update({i - 1, i + 1})
                result += 1

    return result


def num_timelines(lines):
    num_timelines_at_position = defaultdict(int)

    for line in lines:
        for i, char in enumerate(line):
            if char == "S":
                num_timelines_at_position[i] = 1
            elif char == "^":
                n = num_timelines_at_position.pop(i, 0)
                if n:
                    num_timelines_at_position[i - 1] += n
                    num_timelines_at_position[i + 1] += n

    return sum(num_timelines_at_position.values())


if __name__ == "__main__":
    lines = open("input.txt", "r").read().splitlines()

    print("part 1:", num_splits(lines))
    print("part 2:", num_timelines(lines))
