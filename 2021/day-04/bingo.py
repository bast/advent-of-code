from dataclasses import dataclass, field


@dataclass
class Board:
    number_to_position: dict[int, (int, int)] = field(default_factory=dict)
    drawn_positions: set[(int, int)] = field(default_factory=set)
    has_won: bool = False


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


def sum_unmarked(board: Board) -> int:
    numbers = []
    for number, position in board.number_to_position.items():
        if not position in board.drawn_positions:
            numbers.append(number)
    return sum(numbers)


def board_wins(board: Board) -> bool:
    for i in range(5):
        if all([(i, j) in board.drawn_positions for j in range(5)]):
            return True
        if all([(j, i) in board.drawn_positions for j in range(5)]):
            return True
    return False


def compute_scores(sequence, boards) -> list[int]:
    scores = []
    for n in sequence:
        for board in boards:
            if not board.has_won:
                if n in board.number_to_position:
                    i, j = board.number_to_position[n]
                    board.drawn_positions.add((i, j))
                    if board_wins(board):
                        scores.append(n * sum_unmarked(board))
                        board.has_won = True
    return scores


if __name__ == "__main__":
    file_name = "input.txt"

    sequence = read_sequence(file_name)
    boards = read_boards(file_name)

    scores = compute_scores(sequence, boards)

    print("part 1:", scores[0])  # first to win
    print("part 2:", scores[-1])  # last to win
