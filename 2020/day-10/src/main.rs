use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let mut numbers: Vec<i32> = input.lines().map(|x| x.parse().unwrap()).collect();

    numbers.sort_unstable();

    // should try to re-express this as a fold
    let mut num_1 = 1;
    let mut num_3 = 1;
    for batch in numbers.windows(2) {
        match batch[1] - batch[0] {
            1 => num_1 += 1,
            3 => num_3 += 1,
            _ => (),
        }
    }

    println!("part 1: {}", num_1 * num_3);
}
