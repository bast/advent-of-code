use std::fs;

fn main() {
    let input = read_input("input.txt");

    let min_position = *input.iter().min().unwrap();
    let max_position = *input.iter().max().unwrap();
    let positions: Vec<i32> = (min_position..=max_position).collect();

    let compute_fuel1 = |p: i32| -> i32 { input.iter().map(|x| (x - p).abs()).sum() };
    let compute_fuel2 = |p: i32| -> i32 { input.iter().map(|x| gauss_sum((x - p).abs())).sum() };

    println!(
        "part 1: {}",
        positions.iter().map(|&p| compute_fuel1(p)).min().unwrap()
    );

    println!(
        "part 2: {}",
        positions.iter().map(|&p| compute_fuel2(p)).min().unwrap()
    );
}

fn gauss_sum(n: i32) -> i32 {
    (n * (n + 1)) / 2
}

fn read_input(file_name: &str) -> Vec<i32> {
    let input = fs::read_to_string(file_name).unwrap();
    input
        .trim()
        .split(',')
        .map(|c| c.parse().unwrap())
        .collect()
}
