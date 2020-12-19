use regex::Regex;
use std::collections::{HashMap, HashSet};
use std::fs;
use std::iter::FromIterator;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let (valid_seats, nearby_tickets) = parse1(&input);

    let invalid_numbers: Vec<_> = nearby_tickets
        .iter()
        .filter(|&x| !valid_seats.contains(x))
        .copied()
        .collect();

    let error_rate: usize = invalid_numbers.iter().sum();

    println!("ticket scanning error rate: {}", error_rate);

    let (ranges, departure_rows) = parse_ranges(&input);
    let columns = parse2(&input, &invalid_numbers);
    let your_ticket = parse_your_ticket(&input);

    let map = map_ranges_to_columns(&ranges, &columns);

    let mut result = 1;
    for row in departure_rows {
        let i = map.get(&row).unwrap();
        result *= your_ticket[*i];
    }
    println!("result from part 2: {}", result);
}

fn map_ranges_to_columns(
    ranges: &[HashSet<usize>],
    columns: &[Vec<usize>],
) -> HashMap<usize, usize> {
    let mut matching_pairs = Vec::new();
    for (i, range) in ranges.iter().enumerate() {
        let mut matching_columns = Vec::new();
        for (j, column) in columns.iter().enumerate() {
            if range_matches_column(&range, &column) {
                matching_columns.push(j);
            }
        }
        matching_pairs.push((i, matching_columns));
    }
    matching_pairs.sort_by_key(|k| k.1.len());

    let mut map = HashMap::new();

    let num_rows = matching_pairs.len();
    for i in 0..num_rows {
        let only_number = matching_pairs[i].1[0];
        map.insert(matching_pairs[i].0, only_number);
        for j in (i + 1)..num_rows {
            matching_pairs[j].1.retain(|&x| x != only_number);
        }
    }

    map
}

fn range_matches_column(range: &HashSet<usize>, column: &[usize]) -> bool {
    let column_as_set: HashSet<usize> = HashSet::from_iter(column.iter().cloned());
    column_as_set.is_subset(&range)
}

fn parse2(input: &str, invalid_numbers: &[usize]) -> Vec<Vec<usize>> {
    let mut columns = Vec::new();

    let chunks: Vec<&str> = input.split("nearby tickets:\n").collect();
    let lines: Vec<&str> = chunks[1].lines().collect();
    for _ in lines[0].split(',') {
        columns.push(Vec::new());
    }

    for line in lines.iter() {
        let mut numbers = Vec::new();
        let mut valid_batch = true;
        for number in line.split(',') {
            let n: usize = number.parse().unwrap();
            if invalid_numbers.contains(&n) {
                valid_batch = false;
                break;
            }
            numbers.push(n);
        }
        if valid_batch {
            for (i, number) in numbers.iter().enumerate() {
                columns[i].push(*number);
            }
        }
    }

    columns
}

fn parse_your_ticket(input: &str) -> Vec<usize> {
    let mut numbers = Vec::new();

    let lines: Vec<&str> = input.lines().collect();
    for (i, line) in lines.iter().enumerate() {
        if i > 0 && lines[i - 1].contains("your ticket") {
            for number in line.split(',') {
                numbers.push(number.parse().unwrap());
            }
        }
    }

    numbers
}

fn parse_ranges(input: &str) -> (Vec<HashSet<usize>>, Vec<usize>) {
    let mut ranges = Vec::new();
    let mut departure_rows = Vec::new();

    let mut i = 0;
    for line in input.lines() {
        if line.contains(": ") {
            if line.contains("departure") {
                departure_rows.push(i);
            }
            i += 1;
            let mut valid_seats = HashSet::new();
            for number in parse_range(&line) {
                valid_seats.insert(number);
            }
            ranges.push(valid_seats);
        }
    }

    (ranges, departure_rows)
}

fn parse1(input: &str) -> (HashSet<usize>, Vec<usize>) {
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
    let re = Regex::new(r"^\w+\s*\w*: (\d+)-(\d+) or (\d+)-(\d+)$").unwrap();
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
