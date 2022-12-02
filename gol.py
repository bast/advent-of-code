from collections import defaultdict
from dataclasses import dataclass

from read import read_positions, read_block_dimensions


@dataclass
class Board:
    num_rows: int
    num_cols: int
    values: defaultdict(int)


def update_board(board, neighbors, update_function):
    new_board = Board(
        num_rows=board.num_rows, num_cols=board.num_cols, values=defaultdict(int)
    )
    for row in range(board.num_rows):
        for col in range(board.num_cols):
            position = (row, col)
            value = board.values[position]
            neighbor_values = map(lambda p: board.values[p], neighbors(position))
            new_board.values[position] = update_function(value, neighbor_values)
    return new_board


def read_board(file_name):
    values = defaultdict(int)
    for (row, col) in read_positions(file_name, row_major=True):
        values[(row, col)] = 1

    num_rows, num_cols = read_block_dimensions(file_name)

    return Board(num_rows, num_cols, values)


def print_board(board):
    print()
    for row in range(board.num_rows):
        s = ""
        for col in range(board.num_cols):
            if board.values[(row, col)] == 1:
                s += "#"
            else:
                s += "."
        print(s)
