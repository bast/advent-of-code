use std::fs;

fn binary_to_decimal(input: &str) -> usize {
    usize::from_str_radix(input, 2).unwrap()
}

fn boarding_pass_id(input: &str) -> usize {
    let binary = &input
        .replace("B", "1")
        .replace("F", "0")
        .replace("R", "1")
        .replace("L", "0");
    binary_to_decimal(binary)
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let boarding_passes: Vec<&str> = input.lines().collect();

    let mut ids: Vec<_> = boarding_passes
        .iter()
        .map(|x| boarding_pass_id(x))
        .collect();
    ids.sort();

    let first = ids.first().unwrap();
    let last = ids.last().unwrap();

    println!("highest ID: {}", last);

    let mut counter: usize = *first;
    for &id in ids.iter() {
        if counter != id {
            println!("missing seat: {}", counter);
            break;
        }
        counter += 1;
    }
}
