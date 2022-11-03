from itertools import cycle

numbers = list(map(int, open("input.txt", "r").read().splitlines()))

print("part 1:", sum(numbers))

visited = set()
i = 0
for n in cycle(numbers):
    i += n
    if i in visited:
        break
    else:
        visited.add(i)

print("part 2:", i)
