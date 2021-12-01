use std::fs;

fn read_file(file_name: &str) -> Vec<i32> {
    let input = fs::read_to_string(&file_name).unwrap();
    input.lines().map(|x| x.parse().unwrap()).collect()
}

fn num_increased(depths: &[i32]) -> usize {
    let mut n = 0;
    for pair in depths.windows(2) {
        if pair[1] > pair[0] {
            n += 1;
        }
    }
    n
}

fn num_increased_sliding(depths: &[i32]) -> usize {
    let sums: Vec<_> = depths.windows(3).map(|t| t[0] + t[1] + t[2]).collect();
    num_increased(&sums)
}

fn main() {
    let depths = read_file("example.txt");
    println!("example: {}", num_increased(&depths));

    let depths = read_file("input.txt");
    println!("part 1: {}", num_increased(&depths));

    let depths = read_file("input.txt");
    println!("part 2: {}", num_increased_sliding(&depths));
}
