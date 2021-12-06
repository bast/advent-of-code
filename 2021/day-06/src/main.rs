use std::fs;

fn evolve(stages: &[usize], num_steps: usize) -> usize {
    let mut time_to_hatch = vec![0; 9];

    for &stage in stages {
        time_to_hatch[stage] += 1;
    }

    for _ in 0..num_steps {
        time_to_hatch.rotate_left(1);
        let number_new_fish = time_to_hatch[8];
        time_to_hatch[6] += number_new_fish;
    }

    time_to_hatch.iter().sum()
}

fn main() {
    let stages = read_input("input.txt");

    println!("part 1: {}", evolve(&stages, 80));
    println!("part 2: {}", evolve(&stages, 256));
}

fn read_input(file_name: &str) -> Vec<usize> {
    let input = fs::read_to_string(file_name).unwrap();
    input
        .trim()
        .split(',')
        .map(|c| c.parse().unwrap())
        .collect()
}
