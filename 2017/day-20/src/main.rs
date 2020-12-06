use indicatif::ProgressIterator;
use regex::Regex;
use std::collections::HashMap;
use std::fs;

#[derive(Debug, Clone)]
struct Particle {
    x: isize,
    y: isize,
    z: isize,
    vx: isize,
    vy: isize,
    vz: isize,
    ax: isize,
    ay: isize,
    az: isize,
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let num_iterations = 100_000;

    let mut particles: Vec<_> = input.lines().map(parse).collect();

    for _ in (0..num_iterations).progress() {
        particles = particles.iter_mut().map(|x| move_particle(x)).collect();
    }

    let mut distances: Vec<(usize, usize)> = Vec::new();
    for (i, particle) in particles.iter().enumerate() {
        distances.push((manhattan_distance(&particle), i));
    }

    distances.sort_unstable();

    println!(
        "part 1: particle with index {} stays closest",
        distances.first().unwrap().1
    );

    let mut particles: Vec<_> = input.lines().map(parse).collect();

    for _ in (0..num_iterations).progress() {
        particles = particles.iter_mut().map(|x| move_particle(x)).collect();
        particles = remove_colliding(&particles);
    }

    println!("part 2: number of surviving particles: {}", particles.len());
}

fn remove_colliding(particles: &[Particle]) -> Vec<Particle> {
    let mut frequencies: HashMap<(isize, isize, isize), usize> = HashMap::new();
    for particle in particles.iter() {
        *frequencies
            .entry((particle.x, particle.y, particle.z))
            .or_insert(0) += 1;
    }

    let mut surviving_particles = Vec::new();
    for particle in particles.iter() {
        if *frequencies
            .get(&(particle.x, particle.y, particle.z))
            .unwrap()
            < 2
        {
            surviving_particles.push(particle.clone());
        }
    }

    surviving_particles
}

fn parse_chunk(input: &str) -> (isize, isize, isize) {
    let re = Regex::new(r".<(-*\d+),(-*\d+),(-*\d+)>$").unwrap();
    let caps = re.captures(input).unwrap();

    let x = caps.get(1).unwrap().as_str().parse().unwrap();
    let y = caps.get(2).unwrap().as_str().parse().unwrap();
    let z = caps.get(3).unwrap().as_str().parse().unwrap();

    (x, y, z)
}

fn manhattan_distance(particle: &Particle) -> usize {
    (particle.x.abs() + particle.y.abs() + particle.z.abs()) as usize
}

fn parse(input: &str) -> Particle {
    let chunks: Vec<&str> = input.split(", ").collect();

    let (x, y, z) = parse_chunk(chunks[0]);
    let (vx, vy, vz) = parse_chunk(chunks[1]);
    let (ax, ay, az) = parse_chunk(chunks[2]);

    Particle {
        x,
        y,
        z,
        vx,
        vy,
        vz,
        ax,
        ay,
        az,
    }
}

fn move_particle(particle_initial: &Particle) -> Particle {
    let ax = particle_initial.ax;
    let ay = particle_initial.ay;
    let az = particle_initial.az;

    let vx = particle_initial.vx + ax;
    let vy = particle_initial.vy + ay;
    let vz = particle_initial.vz + az;

    let x = particle_initial.x + vx;
    let y = particle_initial.y + vy;
    let z = particle_initial.z + vz;

    Particle {
        x,
        y,
        z,
        vx,
        vy,
        vz,
        ax,
        ay,
        az,
    }
}
