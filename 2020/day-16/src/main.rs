use regex::Regex;
use std::collections::HashSet;
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let (valid_seats, nearby_tickets) = parse(&input);

    let invalid_numbers: Vec<_> = nearby_tickets
        .iter()
        .filter(|&x| !valid_seats.contains(x))
        .copied()
        .collect();

    let error_rate: usize = invalid_numbers.iter().sum();

    println!("ticket scanning error rate: {}", error_rate);
}

fn parse(input: &str) -> (HashSet<usize>, Vec<usize>) {
    let re = Regex::new(r"^\w+: (\d+)-(\d+) or (\d+)-(\d+)$").unwrap();

    let mut valid_seats = HashSet::new();
    for line in input.lines() {
        if re.is_match(line) {
            for number in parse_range(&line) {
                valid_seats.insert(number);
            }
        }
    }

    let mut nearby_tickets = Vec::new();
    let chunks: Vec<&str> = input.split("nearby tickets:\n").collect();
    for number in chunks[1].replace("\n", ",").split(',') {
        if number != "" {
            nearby_tickets.push(number.parse().unwrap());
        }
    }

    (valid_seats, nearby_tickets)
}

fn parse_range(input: &str) -> Vec<usize> {
    let re = Regex::new(r"^\w+: (\d+)-(\d+) or (\d+)-(\d+)$").unwrap();
    let caps = re.captures(input).unwrap();

    let from1: usize = caps.get(1).unwrap().as_str().parse().unwrap();
    let to1: usize = caps.get(2).unwrap().as_str().parse().unwrap();
    let from2: usize = caps.get(3).unwrap().as_str().parse().unwrap();
    let to2: usize = caps.get(4).unwrap().as_str().parse().unwrap();

    [
        (from1..=to1).collect::<Vec<usize>>(),
        (from2..=to2).collect::<Vec<usize>>(),
    ]
    .concat()
}
