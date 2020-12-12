use std::collections::HashMap;
use std::fs;

struct Seatmap {
    map: HashMap<(i32, i32), bool>,
    map_backup: HashMap<(i32, i32), bool>,
}

impl Seatmap {
    fn new(input: &str) -> Seatmap {
        let mut map = HashMap::new();
        for (i, line) in input.lines().enumerate() {
            for (j, character) in line.chars().enumerate() {
                if character == 'L' {
                    map.insert((i as i32, j as i32), true);
                }
            }
        }
        Seatmap {
            map: map.clone(),
            map_backup: map,
        }
    }

    fn backup(&mut self) {
        self.map_backup = self.map.clone();
    }

    fn update_occupation(&mut self, tolerance: i32, max_distance: i32) {
        for &(i, j) in self.map_backup.keys() {
            let occupation = match *self.map_backup.get(&(i, j)).unwrap() {
                false => self.num_neighbors(i, j, max_distance) == 0,
                true => self.num_neighbors(i, j, max_distance) < tolerance,
            };
            self.map.insert((i, j), occupation);
        }
    }

    fn is_unchanged(&self) -> bool {
        self.map == self.map_backup
    }

    fn num_neighbors(&self, i: i32, j: i32, max_distance: i32) -> i32 {
        let mut n = 0;
        for &(x, y) in &[
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ] {
            for d in 1..=max_distance {
                if self.map_backup.contains_key(&(i + d * x, j + d * y)) {
                    if *self.map_backup.get(&(i + d * x, j + d * y)).unwrap() {
                        n += 1;
                    }
                    break;
                }
            }
        }
        n
    }

    fn num_occupied_seats(&self) -> usize {
        self.map
            .keys()
            .filter(|&k| *self.map.get(&(k)).unwrap())
            .count()
    }
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let mut seatmap = Seatmap::new(&input);
    let num_seats = find_equilibrium(&mut seatmap, 4, 1);
    println!("number of occupied seats (part 1): {}", num_seats);

    let mut seatmap = Seatmap::new(&input);
    let num_seats = find_equilibrium(&mut seatmap, 5, 100);
    println!("number of occupied seats (part 2): {}", num_seats);
}

fn find_equilibrium(seatmap: &mut Seatmap, tolerance: i32, max_distance: i32) -> usize {
    let mut num_occupied;
    loop {
        seatmap.backup();
        seatmap.update_occupation(tolerance, max_distance);
        num_occupied = seatmap.num_occupied_seats();
        println!("iterating ... current number: {}", num_occupied);
        if seatmap.is_unchanged() {
            break;
        }
    }
    num_occupied
}
