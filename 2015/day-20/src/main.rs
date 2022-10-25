use std::collections::HashSet;

use rayon::prelude::*;

fn score(n: usize) -> (usize, usize) {
    let mut result1 = 0;
    let mut result2 = 0;
    for factor in factors_noddy(n) {
        result1 += factor * 10;
        if n / factor < 51 {
            result2 += factor * 11;
        }
    }
    (result1, result2)
}

fn factors_noddy(n: usize) -> HashSet<usize> {
    let mut set = HashSet::new();
    for i in 2..=n / 2 {
        if n % i == 0 {
            set.insert(i);
        }
    }
    set.insert(1);
    set.insert(n);
    set
}

fn main() {
    let target = 34000000;

    let house_numbers: Vec<usize> = (1..1000000).collect();
    let scores: Vec<(usize, usize)> = house_numbers.par_iter().map(|&n| score(n)).collect();

    for (i, (n, _)) in scores.iter().enumerate() {
        if n > &target {
            println!("part 1: {}", i + 1);
            break;
        }
    }

    for (i, (_, n)) in scores.iter().enumerate() {
        if n > &target {
            println!("part 2: {}", i + 1);
            break;
        }
    }
}
