use regex::Regex;
use std::cmp;
use std::fs;

#[derive(Debug, Clone)]
struct Star {
    x: isize,
    y: isize,
    v_x: isize,
    v_y: isize,
}

fn parse_position_and_velocity(line: &str) -> Star {
    let re = Regex::new(r"position=<\s*(-*\d+),\s\s*(-*\d+)> velocity=<\s*(-*\d+),\s\s*(-*\d+)>$")
        .unwrap();
    let caps = re.captures(line).unwrap();
    let x = caps.get(1).unwrap().as_str().parse().unwrap();
    let y = caps.get(2).unwrap().as_str().parse().unwrap();
    let v_x = caps.get(3).unwrap().as_str().parse().unwrap();
    let v_y = caps.get(4).unwrap().as_str().parse().unwrap();
    Star { x, y, v_x, v_y }
}

fn move_star(star_initial: &Star, time_arrow: isize) -> Star {
    Star {
        x: star_initial.x + time_arrow * star_initial.v_x,
        y: star_initial.y + time_arrow * star_initial.v_y,
        v_x: star_initial.v_x,
        v_y: star_initial.v_y,
    }
}

fn bbox(stars: &[Star]) -> (isize, isize, isize, isize) {
    let mut x_min = std::isize::MAX;
    let mut x_max = -x_min;
    let mut y_min = std::isize::MAX;
    let mut y_max = -y_min;

    for star in stars.iter() {
        x_min = cmp::min(x_min, star.x);
        x_max = cmp::max(x_max, star.x);
        y_min = cmp::min(y_min, star.y);
        y_max = cmp::max(y_max, star.y);
    }

    (x_min, x_max, y_min, y_max)
}

fn print_stars(stars: &[Star]) {
    let (x_min, x_max, y_min, y_max) = bbox(&stars);

    let x_len = (x_max - x_min) as usize + 1;
    let y_len = (y_max - y_min) as usize + 1;

    let mut message: Vec<Vec<char>> = vec![vec![' '; x_len]; y_len];
    for star in stars.iter() {
        message[(star.y - y_min) as usize][(star.x - x_min) as usize] = '*';
    }

    for row_chars in message.iter() {
        let row: String = row_chars.iter().collect();
        println!("{}", row);
    }
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let mut stars: Vec<_> = input
        .lines()
        .map(|x| parse_position_and_velocity(x))
        .collect();

    let mut num_iterations = 0;
    let mut surface = std::isize::MAX;
    loop {
        stars = stars.iter_mut().map(|x| move_star(x, 1)).collect();

        let (x_min, x_max, y_min, y_max) = bbox(&stars);
        let new_surface = (x_max - x_min).abs() * (y_max - y_min).abs();

        if new_surface < surface {
            surface = new_surface;
            num_iterations += 1;
        } else {
            // we went one step too far, move one step back
            stars = stars.iter_mut().map(|x| move_star(x, -1)).collect();
            break;
        }
    }

    print_stars(&stars);

    println!("reached after {} iterations", num_iterations);
}
