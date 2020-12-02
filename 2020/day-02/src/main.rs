use regex::Regex;
use std::fs;

struct Record {
    i: usize,
    j: usize,
    character: char,
    password: String,
}

fn read_data(file_name: &str) -> Vec<Record> {
    let error_message = format!("something went wrong reading file {}", file_name);
    let contents = fs::read_to_string(file_name).expect(&error_message);

    let re = Regex::new(r"^(\d+)-(\d+) (\w): (\w+)$").unwrap();
    let mut records = Vec::new();

    for line in contents.lines() {
        let caps = re.captures(line).unwrap();

        let i = caps.get(1).unwrap().as_str().parse().unwrap();
        let j = caps.get(2).unwrap().as_str().parse().unwrap();
        let character = caps.get(3).unwrap().as_str().parse().unwrap();
        let password = caps.get(4).unwrap().as_str().parse().unwrap();

        records.push(Record {
            i,
            j,
            character,
            password,
        });
    }

    records
}

fn is_valid_policy1(record: &Record) -> bool {
    let count = record.password.matches(record.character).count();
    (record.i <= count) && (count <= record.j)
}

fn is_valid_policy2(record: &Record) -> bool {
    let ith = record.password.chars().nth(record.i - 1).unwrap();
    let jth = record.password.chars().nth(record.j - 1).unwrap();
    (record.character == ith) ^ (record.character == jth)
}

fn main() {
    let records = read_data("input.txt");

    println!(
        "number of valid records (policy 1): {}",
        records.iter().filter(|x| is_valid_policy1(x)).count()
    );

    println!(
        "number of valid records (policy 2): {}",
        records.iter().filter(|x| is_valid_policy2(x)).count()
    );
}
