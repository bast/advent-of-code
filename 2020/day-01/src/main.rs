use std::collections::HashMap;
use std::fs;

fn read_data(file_name: &str) -> Vec<i32> {
    let contents = fs::read_to_string(file_name).unwrap();
    contents.lines().map(|s| s.parse().unwrap()).collect()
}

fn convert_to_map(vectors: &Vec<Vec<i32>>) -> HashMap<i32, Vec<i32>> {
    let mut map = HashMap::new();

    for numbers in vectors.iter() {
        map.insert(numbers.iter().sum(), numbers.clone());
    }

    map
}

fn find_and_multiply(sum: i32, numbers: &Vec<i32>, vectors: &Vec<Vec<i32>>) -> Option<i32> {
    let map = convert_to_map(&vectors);

    for number in numbers.iter() {
        let difference = sum - number;
        if map.contains_key(&difference) {
            let product: i32 = map.get(&difference).unwrap().iter().product();
            return Some(number * product);
        }
    }

    None
}

fn main() {
    let numbers = read_data("input.txt");

    let mut singles = Vec::new();
    let mut pairs = Vec::new();

    for i in 0..numbers.len() {
        singles.push(vec![numbers[i]]);
        for j in 0..i {
            pairs.push(vec![numbers[i], numbers[j]]);
        }
    }

    match find_and_multiply(2020, &numbers, &singles) {
        Some(x) => println!("result for step 1: {}", x),
        None => println!("nothing found"),
    }

    match find_and_multiply(2020, &numbers, &pairs) {
        Some(x) => println!("result for step 2: {}", x),
        None => println!("nothing found"),
    }
}
