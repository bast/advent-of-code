import sys

sys.path.append("../..")

from gol import read_board, update_board


def neighbors(position):
    row, col = position
    return [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]


def update_function(value, neighbor_values):
    s = sum(neighbor_values)
    if value == 1:
        if s == 2 or s == 3:
            return 1
        else:
            return 0
    else:
        if s == 3:
            return 1
        else:
            return 0


def tweak_corner_lights(board):
    board.values[(0, 0)] = 1
    board.values[(board.num_rows - 1, 0)] = 1
    board.values[(0, board.num_cols - 1)] = 1
    board.values[(board.num_rows - 1, board.num_cols - 1)] = 1
    return board


num_steps = 100

board = read_board("input.txt")
for _ in range(num_steps):
    board = update_board(board, neighbors, update_function)

print(f"part 1: {sum(board.values.values())}")

board = read_board("input.txt")
board = tweak_corner_lights(board)
for _ in range(num_steps):
    board = update_board(board, neighbors, update_function)
    board = tweak_corner_lights(board)

print(f"part 2: {sum(board.values.values())}")
