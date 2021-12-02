use std::fs;

fn parse_line(line: &str) -> (String, usize) {
    let words: Vec<&str> = line.split_whitespace().collect();
    let s = words[0].to_string();
    let n: usize = words[1].parse().unwrap();
    (s, n)
}

fn read_input(file_name: &str) -> Vec<(String, usize)> {
    let input = fs::read_to_string(file_name).unwrap();
    input.lines().map(|line| parse_line(line)).collect()
}

fn main() {
    let instructions = read_input("input.txt");

    let (mut x, mut y) = (0, 0);
    for (instruction, n) in &instructions {
        match &instruction[..] {
            "forward" => x += n,
            "down" => y += n,
            "up" => y -= n,
            _ => panic!("unexpected input"),
        }
    }
    println!("part 1: {}", x * y);

    let (mut x, mut y, mut aim) = (0, 0, 0);
    for (instruction, n) in &instructions {
        match &instruction[..] {
            "forward" => {
                x += n;
                y += n * aim;
            }
            "down" => aim += n,
            "up" => aim -= n,
            _ => panic!("unexpected input"),
        }
    }
    println!("part 2: {}", x * y);
}
