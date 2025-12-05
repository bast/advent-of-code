#!/usr/bin/env rust-script

//! ```cargo
//! [package]
//! edition = "2024"
//! ```

use std::fs;

#[derive(Debug, Clone, Copy)]
struct Range {
    start: usize,
    end: usize,
}

impl Range {
    fn len(&self) -> usize {
        self.end - self.start + 1
    }

    fn contains(&self, ingredient: usize) -> bool {
        self.start <= ingredient && ingredient <= self.end
    }
}

fn merge_ranges(mut ranges: Vec<Range>) -> Vec<Range> {
    ranges.sort_by_key(|r| r.start);

    ranges.into_iter().fold(Vec::new(), |mut acc, r| {
        if let Some(last) = acc.last_mut()
            && r.start <= last.end
        {
            last.end = last.end.max(r.end);
            return acc;
        }
        acc.push(r);
        acc
    })
}

fn ingeredients_in_ranges(ingredients: &[usize], ranges: &[Range]) -> Vec<usize> {
    ingredients
        .iter()
        .copied()
        .filter(|&ingredient| ranges.iter().any(|range| range.contains(ingredient)))
        .collect()
}

fn main() -> std::io::Result<()> {
    let data = fs::read_to_string("input.txt")?;

    let mut ranges = Vec::new();
    let mut ingredients = Vec::new();
    for line in data.lines().filter(|l| !l.is_empty()) {
        if let Some((a, b)) = line.split_once('-') {
            ranges.push(Range {
                start: a.parse().unwrap(),
                end: b.parse().unwrap(),
            });
        } else {
            ingredients.push(line.parse().unwrap());
        }
    }

    let merged_ranges = merge_ranges(ranges);

    let fresh_ingredients = ingeredients_in_ranges(&ingredients, &merged_ranges);
    println!("part 1: {:?}", fresh_ingredients.len());

    let num_all_fresh_ingredients: usize = merged_ranges.iter().map(|r| r.len()).sum();
    println!("part 2: {:?}", num_all_fresh_ingredients);

    Ok(())
}
