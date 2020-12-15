use std::collections::HashMap;

fn main() {
    let input = vec![17, 1, 3, 16, 19, 0];

    println!("result part 1: {}", find_number_spoken(&input, 2020));
    println!("result part 2: {}", find_number_spoken(&input, 30000000));
}

fn find_number_spoken(input: &[usize], num_turns: usize) -> usize {
    let mut number_to_last_turn: HashMap<usize, usize> = HashMap::new();

    let mut number_spoken = 0;
    let mut turn = 1;

    for &number in input {
        number_spoken = save_number_get_next(number, turn, &mut number_to_last_turn);
        turn += 1;
    }

    loop {
        if turn == num_turns {
            break;
        }
        number_spoken = save_number_get_next(number_spoken, turn, &mut number_to_last_turn);
        turn += 1;
    }

    number_spoken
}

fn save_number_get_next(number: usize, turn: usize, map: &mut HashMap<usize, usize>) -> usize {
    let since_last = if map.contains_key(&number) {
        turn - map.get(&number).unwrap()
    } else {
        0
    };

    map.insert(number, turn);

    since_last
}
