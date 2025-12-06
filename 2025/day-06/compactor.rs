#!/usr/bin/env rust-script

use std::fs::read_to_string;

type Problem = Vec<usize>;

fn read_data(filename: &str) -> (Vec<Problem>, Vec<Problem>, Vec<char>) {
    let mut lines: Vec<String> = read_to_string(filename)
        .expect("failed to read file")
        .lines()
        .filter(|l| !l.trim().is_empty())
        .map(String::from)
        .collect();

    let operations: Vec<char> = lines
        .pop()
        .unwrap()
        .chars()
        .filter(|c| !c.is_whitespace())
        .collect();

    // to solve part 2, transpose the block of text (without the operations line)
    // and then we will parse the transposed text
    let lines_transposed = transpose_block_of_text(lines.clone());

    let numbers: Vec<Problem> = lines
        .into_iter()
        .map(|l| l.split_whitespace().map(|n| n.parse().unwrap()).collect())
        .collect();

    // transpose
    let problems1 = (0..numbers[0].len())
        .map(|i| numbers.iter().map(|row| row[i]).collect())
        .collect();

    let problems2: Vec<Vec<usize>> = lines_transposed
        .split(|line| line.trim().is_empty())
        .filter(|chunk| !chunk.is_empty())
        .map(|chunk| {
            chunk
                .iter()
                .map(|line| line.trim().parse::<usize>().unwrap())
                .collect()
        })
        .collect();

    (problems1, problems2, operations)
}

fn transpose_block_of_text(rows: Vec<String>) -> Vec<String> {
    let chars: Vec<Vec<char>> = rows.into_iter().map(|s| s.chars().collect()).collect();
    let width = chars[0].len();

    (0..width)
        .map(|i| chars.iter().map(|row| row[i]).collect())
        .collect()
}

fn get_total(problems: &[Vec<usize>], operations: &[char]) -> usize {
    problems
        .iter()
        .zip(operations.iter())
        .map(|(list, op)| match op {
            '+' => list.iter().sum::<usize>(),
            '*' => list.iter().product::<usize>(),
            _ => panic!("Unknown operation"),
        })
        .sum()
}

fn main() {
    let (problems1, problems2, operations) = read_data("input.txt");
    println!("part 1: {}", get_total(&problems1, &operations));
    println!("part 2: {}", get_total(&problems2, &operations));
}
