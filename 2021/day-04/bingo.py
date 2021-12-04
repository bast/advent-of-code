from dataclasses import dataclass, field
from collections import defaultdict


@dataclass
class Board:
    number_to_position: dict[int, (int, int)] = field(default_factory=dict)
    position_is_drawn: dict[(int, int), bool] = field(
        default_factory=lambda: defaultdict(bool)
    )


def read_sequence(file_name: str) -> list[int]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
        return list(map(int, lines[0].split(",")))


def read_boards(file_name: str) -> list[Board]:
    boards = []
    with open(file_name, "r") as f:
        next(f)
        while True:
            try:
                next(f)
                board = Board()
                for i in range(5):
                    for j, number in enumerate(map(int, next(f).split())):
                        board.number_to_position[number] = (i, j)
                boards.append(board)
            except StopIteration:
                return boards


def get_unmarked_numbers(board: Board) -> list[int]:
    numbers = []
    for number, position in board.number_to_position.items():
        if not board.position_is_drawn[position]:
            numbers.append(number)
    return numbers


def board_wins(board: Board) -> bool:
    for i in range(5):
        if all([board.position_is_drawn[(i, j)] for j in range(5)]):
            return True
        if all([board.position_is_drawn[(j, i)] for j in range(5)]):
            return True
    return False


def compute_scores(sequence, boards) -> list[int]:
    boards_left = list(range(len(boards)))
    scores = []
    for n in sequence:
        for m, board in enumerate(boards):
            if m in boards_left:
                if n in board.number_to_position:
                    i, j = board.number_to_position[n]
                    board.position_is_drawn[(i, j)] = True
                    if board_wins(board):
                        scores.append(n * sum(get_unmarked_numbers(board)))
                        boards_left.remove(m)
                        if len(boards_left) == 0:
                            return scores


if __name__ == "__main__":
    file_name = "input.txt"

    sequence = read_sequence(file_name)
    boards = read_boards(file_name)

    scores = compute_scores(sequence, boards)

    print("part 1:", scores[0])  # first to win
    print("part 2:", scores[-1])  # last to win
