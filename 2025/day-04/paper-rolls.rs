#!/usr/bin/env rust-script

use std::collections::HashSet;
use std::fs;

fn neighbors_sum(grid: &HashSet<(isize, isize)>, y: isize, x: isize) -> usize {
    let offsets = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ];

    offsets
        .iter()
        .filter(|&&(dy, dx)| grid.contains(&(y + dy, x + dx)))
        .count()
}

fn accessible_positions(positions: &HashSet<(isize, isize)>) -> HashSet<(isize, isize)> {
    positions
        .iter()
        .filter(|&&(y, x)| neighbors_sum(positions, y, x) < 4)
        .cloned()
        .collect()
}

fn main() {
    let grid = fs::read_to_string("input.txt").expect("Failed to read input file");

    let mut positions: HashSet<(isize, isize)> = HashSet::new();
    for (y, line) in grid.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            if c == '@' {
                positions.insert((y as isize, x as isize));
            }
        }
    }

    let mut accessible = accessible_positions(&positions);
    println!("part 1: {}", accessible.len());

    let mut num_accessible = accessible.len();

    while !accessible.is_empty() {
        positions.retain(|p| !accessible.contains(p));
        accessible = accessible_positions(&positions);
        num_accessible += accessible.len();
    }

    println!("part 2: {}", num_accessible);
}
