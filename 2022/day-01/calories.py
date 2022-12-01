def calories_sum(chunk: str) -> int:
    numbers = map(int, chunk.splitlines())
    return sum(numbers)


chunks = open("input.txt", "r").read().split("\n\n")

calories = list(map(calories_sum, chunks))
print("part 1:", max(calories))

calories = sorted(calories)
print("part 2:", calories.pop() + calories.pop() + calories.pop())
