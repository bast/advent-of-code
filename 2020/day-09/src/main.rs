use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let numbers: Vec<i64> = input.lines().map(|x| x.parse().unwrap()).collect();

    let batch_size = 25;

    let bad_position = batch_size
        + numbers
            .windows(batch_size + 1)
            .map(check_batch)
            .position(|x| !x)
            .unwrap();
    println!("problem number in part 1: {}", numbers[bad_position]);
}

fn check_batch(batch: &[i64]) -> bool {
    for i in 0..(batch.len() - 1) {
        for j in 0..(batch.len() - 1) {
            if batch[i] + batch[j] == batch[batch.len() - 1] {
                return true;
            }
        }
    }
    false
}
