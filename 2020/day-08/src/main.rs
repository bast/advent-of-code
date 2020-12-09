use std::collections::HashSet;
use std::fs;

#[derive(Clone, Copy, PartialEq, Debug)]
enum Operation {
    Nop,
    Acc,
    Jmp,
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let (operations, arguments) = parse_input(&input);

    let (accumulator, _) = run_instructions(&operations, &arguments);

    println!("accumulator value (part 1): {}", accumulator);

    let places_to_check: Vec<_> = operations
        .iter()
        .enumerate()
        .filter(|x| *x.1 == Operation::Nop || *x.1 == Operation::Jmp)
        .map(|x| x.0)
        .collect();

    for &position in places_to_check.iter() {
        let operations_flipped = adjust_operations(&operations, position);
        let (accumulator, completed) = run_instructions(&operations_flipped, &arguments);
        if completed {
            println!("accumulator value (part 2): {}", accumulator);
            break;
        }
    }
}

fn adjust_operations(operations: &[Operation], position: usize) -> Vec<Operation> {
    let mut operations_adjusted = operations.to_vec();
    match operations[position] {
        Operation::Nop => operations_adjusted[position] = Operation::Jmp,
        Operation::Jmp => operations_adjusted[position] = Operation::Nop,
        _ => panic!("unexpected input"),
    }
    operations_adjusted
}

fn run_instructions(operations: &[Operation], arguments: &[i32]) -> (i32, bool) {
    let mut visited: HashSet<i32> = HashSet::new();

    let mut position: i32 = 0;
    let mut accumulator = 0;

    loop {
        if position == operations.len() as i32 {
            break;
        }

        if visited.contains(&position) {
            return (accumulator, false);
        } else {
            visited.insert(position);
        }

        match operations[position as usize] {
            Operation::Acc => {
                accumulator += arguments[position as usize];
                position += 1;
            }
            Operation::Jmp => {
                position += arguments[position as usize];
            }
            _ => position += 1,
        }
    }

    (accumulator, true)
}

fn parse_input(input: &str) -> (Vec<Operation>, Vec<i32>) {
    let mut operations = Vec::new();
    let mut arguments = Vec::new();

    for line in input.lines() {
        let operation = match &line[..3] {
            "nop" => Operation::Nop,
            "acc" => Operation::Acc,
            "jmp" => Operation::Jmp,
            _ => panic!("unexpected input"),
        };
        operations.push(operation);
        arguments.push(line[4..].parse::<i32>().unwrap());
    }

    (operations, arguments)
}
