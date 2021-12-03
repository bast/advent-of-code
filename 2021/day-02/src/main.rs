use recap::Recap;
use serde::Deserialize;
use std::fs;

#[derive(Debug, Deserialize, Recap)]
#[recap(regex = r"(?x)
        (?P<direction>\w+)
        \s+
        (?P<n>\d+)
        $")]
struct Command {
    direction: String,
    n: usize,
}

fn read_input(file_name: &str) -> Vec<Command> {
    let input = fs::read_to_string(file_name).unwrap();
    input.lines().map(|line| line.parse().unwrap()).collect()
}

fn main() {
    let commands = read_input("input.txt");

    let (mut x, mut y) = (0, 0);
    for command in &commands {
        match &command.direction[..] {
            "forward" => x += command.n,
            "down" => y += command.n,
            "up" => y -= command.n,
            _ => panic!("unexpected input"),
        }
    }
    println!("part 1: {}", x * y);

    let (mut x, mut y, mut aim) = (0, 0, 0);
    for command in &commands {
        match &command.direction[..] {
            "forward" => {
                x += command.n;
                y += command.n * aim;
            }
            "down" => aim += command.n,
            "up" => aim -= command.n,
            _ => panic!("unexpected input"),
        }
    }
    println!("part 2: {}", x * y);
}
