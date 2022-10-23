from collections import defaultdict
from dataclasses import dataclass

from read import read_positions, read_block_dimensions


@dataclass
class Board:
    num_rows: int
    num_cols: int
    values: defaultdict(int)


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


def update_board(board, update_function):
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


def sum_values(board):
    return sum(board.values.values())


def read_board(file_name):
    values = defaultdict(int)
    for (row, col) in read_positions(file_name, row_major=True):
        values[(row, col)] = 1

    num_rows, num_cols = read_block_dimensions(file_name)

    return Board(num_rows, num_cols, values)
