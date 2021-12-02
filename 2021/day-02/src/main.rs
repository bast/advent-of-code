use std::fs;

fn read_instructions(file_name: &str) -> Vec<(String, i32)> {
    let input = fs::read_to_string(file_name).unwrap();

    let mut v = Vec::new();

    for line in input.lines() {
        let words: Vec<&str> = line.split_whitespace().collect();
        let instruction = words[0].to_string();
        let n: i32 = words[1].parse().unwrap();
        v.push((instruction, n));
    }

    v
}

fn main() {
    let instructions = read_instructions("input.txt");

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
