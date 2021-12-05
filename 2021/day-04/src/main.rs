use std::collections::{HashMap, HashSet};
use std::fs;

#[derive(Debug, Clone)]
struct Board {
    number_to_position: HashMap<usize, (usize, usize)>,
    drawn_positions: HashSet<(usize, usize)>,
    has_won: bool,
}

fn main() {
    let (sequence, boards) = read_input("input.txt");

    let scores = compute_scores(&sequence, &boards);

    println!("part 1: {}", scores[0]); // first to win
    println!("part 2: {}", scores[scores.len() - 1]); // last to win
}

fn sum_unmarked(board: &Board) -> usize {
    let mut numbers = Vec::new();
    for (number, position) in &board.number_to_position {
        if !board.drawn_positions.contains(position) {
            numbers.push(*number);
        }
    }
    numbers.iter().sum()
}

fn board_wins(board: &Board) -> bool {
    'rows: for i in 0..5 {
        for j in 0..5 {
            if !board.drawn_positions.contains(&(i, j)) {
                continue 'rows;
            }
        }
        return true;
    }

    'cols: for i in 0..5 {
        for j in 0..5 {
            if !board.drawn_positions.contains(&(j, i)) {
                continue 'cols;
            }
        }
        return true;
    }

    false
}

fn compute_scores(sequence: &[usize], boards: &[Board]) -> Vec<usize> {
    let mut boards_mutable = boards.to_owned();
    let mut scores = Vec::new();
    for n in sequence {
        for board in &mut boards_mutable {
            if !board.has_won && board.number_to_position.contains_key(n) {
                let (i, j) = board.number_to_position.get(n).unwrap();
                board.drawn_positions.insert((*i, *j));
                if board_wins(board) {
                    scores.push(n * sum_unmarked(board));
                    board.has_won = true;
                }
            }
        }
    }
    scores
}

fn read_input(file_name: &str) -> (Vec<usize>, Vec<Board>) {
    let input = fs::read_to_string(file_name).unwrap();
    let mut lines = input.lines();

    let sequence = lines
        .next()
        .unwrap()
        .split(',')
        .map(|c| c.parse().unwrap())
        .collect();

    let mut boards = Vec::new();

    loop {
        let line = lines.next();
        if line.is_none() {
            break;
        }

        let mut number_to_position = HashMap::new();
        let drawn_positions = HashSet::new();

        for i in 0..5 {
            let numbers: Vec<usize> = lines
                .next()
                .unwrap()
                .split_whitespace()
                .map(|c| c.parse().unwrap())
                .collect();
            for (j, number) in numbers.iter().enumerate() {
                number_to_position.insert(*number, (i, j));
            }
        }

        let has_won = false;

        boards.push(Board {
            number_to_position,
            drawn_positions,
            has_won,
        });
    }

    (sequence, boards)
}
