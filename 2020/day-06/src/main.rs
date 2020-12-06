use std::collections::{HashMap, HashSet};
use std::fs;
use std::iter::FromIterator;

fn chop_input(input: &str) -> Vec<&str> {
    // blocks are separated by one empty line
    input.split("\n\n").collect()
}

fn num_unique_characters(input: &str) -> usize {
    let characters: Vec<char> = input.replace("\n", "").chars().collect();
    let set: HashSet<_> = HashSet::from_iter(characters.iter().cloned());
    set.len()
}

fn num_answers_policy2(input: &str) -> usize {
    let characters: Vec<char> = input.replace("\n", "").chars().collect();

    let mut num_groups = input.matches('\n').count();
    // the last entry can carry an extra newline
    if !input.ends_with('\n') {
        num_groups += 1;
    }

    let mut frequencies: HashMap<char, usize> = HashMap::new();
    for &character in characters.iter() {
        *frequencies.entry(character).or_insert(0) += 1;
    }

    frequencies
        .into_iter()
        .filter(|&(_, v)| v == num_groups)
        .count()
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let blocks = chop_input(&input);

    println!(
        "number of answers (part 1): {}",
        blocks
            .iter()
            .map(|x| num_unique_characters(x))
            .sum::<usize>()
    );

    println!(
        "number of answers (part 2): {}",
        blocks.iter().map(|x| num_answers_policy2(x)).sum::<usize>()
    );
}
