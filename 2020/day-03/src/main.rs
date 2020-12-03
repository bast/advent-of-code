use std::fs;

fn position_is_tree(line: &str, position: usize) -> bool {
    let position_modulo = position % line.len();
    let symbol = line.chars().nth(position_modulo).unwrap();
    symbol == '#'
}

fn num_encounters(contents: &str, down: usize, right: usize) -> usize {
    let mut num_moves = 0;
    let mut num_encounters = 0;

    for (i, line) in contents.lines().enumerate() {
        if (i % down) == 0 {
            let x_position = num_moves * right;
            if position_is_tree(line, x_position) {
                num_encounters += 1
            }
            num_moves += 1;
        }
    }

    num_encounters
}

fn main() {
    let contents = fs::read_to_string("input.txt").unwrap();

    let num_1_1 = num_encounters(&contents, 1, 1);
    let num_1_3 = num_encounters(&contents, 1, 3);
    let num_1_5 = num_encounters(&contents, 1, 5);
    let num_1_7 = num_encounters(&contents, 1, 7);
    let num_2_1 = num_encounters(&contents, 2, 1);

    println!("number of encounters in part 1: {}", num_1_3);

    let result = num_1_1 * num_1_3 * num_1_5 * num_1_7 * num_2_1;

    println!("result from part 2: {}", result);
}
