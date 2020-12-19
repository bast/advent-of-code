use std::collections::HashSet;
use std::fs;

type Position = Vec<i32>;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    println!("number of active cells (part 1): {}", driver(&input, 6, 3));
    println!("number of active cells (part 2): {}", driver(&input, 6, 4));
}

fn driver(input: &str, num_steps: usize, num_dimensions: usize) -> usize {
    let mut active_cells = read_input(&input, num_dimensions);

    for _ in 0..num_steps {
        active_cells = timestep(&active_cells, num_dimensions);
    }

    active_cells.len()
}

fn timestep(active_cells: &HashSet<Position>, num_dimensions: usize) -> HashSet<Position> {
    let mut new_cells = HashSet::new();

    // If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains
    // active. Otherwise, the cube becomes inactive.
    for cell in active_cells {
        let n = num_active_neighbors(&cell, &active_cells, num_dimensions);
        if n == 2 || n == 3 {
            new_cells.insert(cell.clone());
        }
    }

    // If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
    // Otherwise, the cube remains inactive.
    for cell in inactive_neighbors(&active_cells, num_dimensions).iter() {
        if num_active_neighbors(&cell, &active_cells, num_dimensions) == 3 {
            new_cells.insert(cell.clone());
        }
    }

    new_cells
}

fn inactive_neighbors(active_cells: &HashSet<Position>, num_dimensions: usize) -> Vec<Position> {
    let mut set = HashSet::new();

    for cell in active_cells {
        for neighbor in neighbors(&cell, num_dimensions)
            .iter()
            .filter(|&x| !active_cells.contains(x))
        {
            set.insert(neighbor.clone());
        }
    }

    set.into_iter().collect()
}

fn num_active_neighbors(
    position: &Position,
    active_cells: &HashSet<Position>,
    num_dimensions: usize,
) -> usize {
    neighbors(&position, num_dimensions)
        .iter()
        .filter(|&x| active_cells.contains(x))
        .count()
}

fn neighbors(position: &Position, num_dimensions: usize) -> Vec<Position> {
    let mut positions = Vec::new();

    for displacement in displacements(num_dimensions) {
        positions.push(
            position
                .iter()
                .zip(displacement)
                .map(|(a, b)| a + b)
                .collect(),
        );
    }

    positions
}

fn displacements(num_dimensions: usize) -> Vec<Position> {
    let mut coordinates = add_coordinate(&vec![]);

    for _ in 1..num_dimensions {
        let mut new_coordinates: Vec<Position> = Vec::new();
        for coordinate in coordinates {
            for new_coordinate in add_coordinate(&coordinate) {
                new_coordinates.push(new_coordinate);
            }
        }
        coordinates = new_coordinates.clone();
    }

    // we need to remove 0, 0, ...  because this would not be a displacement
    let null_vector: Vec<i32> = vec![0; num_dimensions];
    let index = coordinates.iter().position(|x| x == &null_vector).unwrap();
    coordinates.remove(index);

    coordinates
}

// ugly, might beautify later, maybe
fn add_coordinate(displacements: &Position) -> Vec<Position> {
    let mut new_coordinates = Vec::new();

    let mut new_vector = displacements.to_owned();
    new_vector.push(-1);
    new_coordinates.push(new_vector);

    let mut new_vector = displacements.to_owned();
    new_vector.push(0);
    new_coordinates.push(new_vector);

    let mut new_vector = displacements.to_owned();
    new_vector.push(1);
    new_coordinates.push(new_vector);

    new_coordinates
}

fn read_input(input: &str, num_dimensions: usize) -> HashSet<Position> {
    let mut active_cells = HashSet::new();

    for (x, line) in input.lines().enumerate() {
        for (y, c) in line.chars().enumerate() {
            if c == '#' {
                let mut v = vec![0; num_dimensions];
                v[0] = x as i32;
                v[1] = y as i32;
                active_cells.insert(v);
            }
        }
    }

    active_cells
}
