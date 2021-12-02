use std::fs;

fn read_file(file_name: &str) -> Vec<usize> {
    let input = fs::read_to_string(&file_name).unwrap();
    input.lines().map(|x| x.parse().unwrap()).collect()
}

fn num_increased(depths: &[usize]) -> usize {
    depths.windows(2).filter(|pair| pair[1] > pair[0]).count()
}

fn num_increased_sliding(depths: &[usize]) -> usize {
    let sums: Vec<_> = depths.windows(3).map(|t| t[0] + t[1] + t[2]).collect();
    num_increased(&sums)
}

fn main() {
    let depths = read_file("example.txt");
    println!("example: {}", num_increased(&depths));

    let depths = read_file("input.txt");
    println!("part 1: {}", num_increased(&depths));
    println!("part 2: {}", num_increased_sliding(&depths));
}
