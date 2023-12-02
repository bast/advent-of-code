from collections import deque


def steal_presents_part_1(elf, circle):
    next_elf = circle[elf]
    next_next_elf = circle[next_elf]
    circle[elf] = next_next_elf
    del circle[next_elf]
    return circle


def part_1(num_elves):
    circle = {k + 1: v + 1 for k, v in zip(range(num_elves), range(1, num_elves))}
    circle[num_elves] = 1
    elf = 1
    while len(circle) > 1:
        circle = steal_presents_part_1(elf, circle)
        elf = circle[elf]
    return list(circle.keys())[0]


def part_2(num_elves):
    stack1 = deque()
    stack2 = deque()
    for i in range(1, num_elves + 1):
        if i < (num_elves // 2) + 1:
            stack1.append(i)
        else:
            stack2.appendleft(i)

    while stack1 and stack2:
        if len(stack1) > len(stack2):
            stack1.pop()
        else:
            stack2.pop()

        stack2.appendleft(stack1.popleft())
        stack1.append(stack2.pop())
    return stack1[0] or stack2[0]


num_elves = 3012210
print("part 1:", part_1(num_elves))
print("part 2:", part_2(num_elves))
