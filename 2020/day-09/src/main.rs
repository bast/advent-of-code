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

    let problem_number = numbers[bad_position];
    println!("problem number in part 1: {}", problem_number);

    println!(
        "encryption weakness (part 2): {}",
        encryption_weakness(&numbers, problem_number).unwrap()
    );
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

// could be done with a fold ... another day
fn encryption_weakness(numbers: &[i64], invalid_number: i64) -> Option<i64> {
    for i in 0..numbers.len() {
        let mut set = Vec::new();
        for &number in numbers.iter().skip(i + 1) {
            set.push(number);
            let sum = set.iter().sum::<i64>();
            if sum == invalid_number {
                return Some(set.iter().min().unwrap() + set.iter().max().unwrap());
            }
            if sum > invalid_number {
                break;
            }
        }
    }

    None
}
