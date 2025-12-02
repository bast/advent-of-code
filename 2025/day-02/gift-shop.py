def chunks_repeat(digits: list[int], num_chunks: int) -> bool:
    n = len(digits) // num_chunks
    pattern = digits[:n]
    for i in range(0, len(digits), n):
        if digits[i : i + n] != pattern:
            return False
    return True


def is_invalid(number: int, max_num_chunks: int) -> bool:
    digits = list(map(int, str(number)))

    max_num_chunks = min(max_num_chunks, len(digits))
    for num_chunks in range(2, max_num_chunks + 1):
        if chunks_repeat(digits, num_chunks):
            return True
    return False


if __name__ == "__main__":
    ranges = open("input.txt").read().strip().split(",")

    numbers = []
    for number_range in ranges:
        start, end = map(int, number_range.split("-"))
        for number in range(start, end + 1):
            numbers.append(number)

    largest_number = max(numbers)
    max_num_digits = len(str(largest_number))

    print("part 1:", sum(filter(lambda num: is_invalid(num, 2), numbers)))
    print("part 2:", sum(filter(lambda num: is_invalid(num, max_num_digits), numbers)))
