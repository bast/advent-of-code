def get_stack(line):
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    stack = []
    for c in line:
        if c in pairs:
            if pairs[c] != stack.pop():
                return points[c], []
        else:
            stack.append(c)
    return 0, stack


def unwind_stack(stack):
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    score = 0
    for c in reversed(stack):
        score *= 5
        score += points[c]
    return score


lines = open("input.txt").read().splitlines()

results = map(get_stack, lines)
scores1, stacks = zip(*results)

print("part 1:", sum(scores1))

scores2 = list(filter(lambda s: s > 0, map(unwind_stack, stacks)))

print("part 2:", sorted(scores2)[len(scores2) // 2])
