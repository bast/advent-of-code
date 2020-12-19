use std::collections::HashSet;
use std::fs;

#[derive(PartialEq, Eq, Hash, Copy, Clone, Debug)]
struct Position {
    x: i32,
    y: i32,
    z: i32,
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let mut active_cells = read_input(&input);

    for _ in 0..6 {
        active_cells = timestep(&active_cells);
    }

    println!("number of active cells (part 1): {}", active_cells.len());
}

fn timestep(active_cells: &HashSet<Position>) -> HashSet<Position> {
    let mut new_cells = HashSet::new();

    // If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains
    // active. Otherwise, the cube becomes inactive.
    for &cell in active_cells {
        let n = num_active_neighbors(&cell, &active_cells);
        if n == 2 || n == 3 {
            new_cells.insert(cell);
        }
    }

    // If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
    // Otherwise, the cube remains inactive.
    for &cell in inactive_neighbors(&active_cells).iter() {
        if num_active_neighbors(&cell, &active_cells) == 3 {
            new_cells.insert(cell);
        }
    }

    new_cells
}

fn inactive_neighbors(active_cells: &HashSet<Position>) -> Vec<Position> {
    let mut set = HashSet::new();

    for cell in active_cells {
        for &neighbor in neighbors(&cell)
            .iter()
            .filter(|&x| !active_cells.contains(x))
        {
            set.insert(neighbor);
        }
    }

    set.into_iter().collect()
}

fn num_active_neighbors(position: &Position, active_cells: &HashSet<Position>) -> usize {
    neighbors(&position)
        .iter()
        .filter(|&x| active_cells.contains(x))
        .count()
}

fn neighbors(position: &Position) -> Vec<Position> {
    let mut positions = Vec::new();

    for x in &[position.x - 1, position.x, position.x + 1] {
        for y in &[position.y - 1, position.y, position.y + 1] {
            for z in &[position.z - 1, position.z, position.z + 1] {
                if (x, y, z) != (&position.x, &position.y, &position.z) {
                    positions.push(Position {
                        x: *x,
                        y: *y,
                        z: *z,
                    });
                }
            }
        }
    }

    positions
}

fn read_input(input: &str) -> HashSet<Position> {
    let mut active_cells = HashSet::new();

    for (x, line) in input.lines().enumerate() {
        for (y, c) in line.chars().enumerate() {
            if c == '#' {
                active_cells.insert(Position {
                    x: x as i32,
                    y: y as i32,
                    z: 0,
                });
            }
        }
    }

    active_cells
}
