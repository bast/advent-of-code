import sys

sys.path.append("../..")

from gol import read_board, update_board, print_board


def biodiversity_rating(board) -> int:
    rating = 0
    i = 1
    for row in range(board.num_rows):
        for col in range(board.num_cols):
            if board.values[(row, col)] == 1:
                rating += i
            i *= 2
    return rating


def neighbors(position):
    row, col = position
    return [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
    ]


def update_function(value, neighbor_values):
    s = sum(neighbor_values)
    if value == 1:
        if s == 1:
            return 1
        else:
            return 0
    else:
        if s == 1 or s == 2:
            return 1
        else:
            return 0


def part1(board):
    ratings = set()
    while True:
        board = update_board(board, neighbors, update_function)
        rating = biodiversity_rating(board)
        if rating in ratings:
            return rating
        else:
            ratings.add(rating)


board = read_board("input.txt")
print_board(board)

print("part 1:", part1(board))
