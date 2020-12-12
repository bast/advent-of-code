use std::collections::HashMap;
use std::fs;

#[derive(Clone, Copy, Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let instructions = parse(&input);

    println!("manhattan distance (part 1): {}", distance1(&instructions));
    println!("manhattan distance (part 2): {}", distance2(&instructions));
}

fn distance1(instructions: &[(char, i32)]) -> i32 {
    let mut boat_orientation = 'E';
    let mut moves: HashMap<char, i32> = HashMap::new();

    for &(direction, n) in instructions {
        match direction {
            'N' | 'E' | 'S' | 'W' => *moves.entry(direction).or_insert(0) += n,
            'F' => *moves.entry(boat_orientation).or_insert(0) += n,
            'L' | 'R' => boat_orientation = turn_in_place(&boat_orientation, &direction, n),
            _ => panic!("unexpected input"),
        }
    }

    let num_n = moves.get(&'N').unwrap_or(&0);
    let num_e = moves.get(&'E').unwrap_or(&0);
    let num_s = moves.get(&'S').unwrap_or(&0);
    let num_w = moves.get(&'W').unwrap_or(&0);

    (num_n - num_s).abs() + (num_e - num_w).abs()
}

fn distance2(instructions: &[(char, i32)]) -> i32 {
    let mut ship = Point { x: 0, y: 0 };
    let mut waypoint_relative = Point { x: 10, y: 1 };

    for &(direction, n) in instructions {
        match direction {
            'N' => waypoint_relative.y += n,
            'S' => waypoint_relative.y -= n,
            'E' => waypoint_relative.x += n,
            'W' => waypoint_relative.x -= n,
            'L' | 'R' => {
                waypoint_relative = rotate_around_origin(&waypoint_relative, &direction, n)
            }
            'F' => {
                ship.x += n * waypoint_relative.x;
                ship.y += n * waypoint_relative.y;
            }
            _ => panic!("unexpected input"),
        }
    }

    ship.x.abs() + ship.y.abs()
}

fn rotate_around_origin(point: &Point, turn_direction: &char, degrees: i32) -> Point {
    let mut new_point = *point;

    let sign = match turn_direction {
        'L' => Point { x: -1, y: 1 },
        'R' => Point { x: 1, y: -1 },
        _ => panic!("unexpected input"),
    };

    let num_turns = degrees / 90;
    for _ in 0..num_turns {
        let x = new_point.x;
        let y = new_point.y;
        new_point.x = sign.x * y;
        new_point.y = sign.y * x;
    }

    new_point
}

fn turn_in_place(direction: &char, turn_direction: &char, degrees: i32) -> char {
    let directions: Vec<char> = vec!['N', 'E', 'S', 'W'];

    let num_turns = match turn_direction {
        'R' => degrees / 90,
        'L' => -degrees / 90,
        _ => panic!("unexpected input"),
    };

    let index_initial = directions.iter().position(|x| x == direction).unwrap() as i32;

    let mut index_final = (index_initial + num_turns) % 4;
    if index_final < 0 {
        index_final += 4;
    }

    directions[index_final as usize]
}

fn parse(input: &str) -> Vec<(char, i32)> {
    let mut instructions = Vec::new();
    for line in input.lines() {
        let c = &line[..1];
        let n = &line[1..];
        instructions.push((c.parse().unwrap(), n.parse().unwrap()));
    }
    instructions
}
