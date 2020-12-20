use std::collections::{HashMap, HashSet};
use std::fs;

// A       B
//  +-----+
//  |     |
//  |     |
//  +-----+
// D       C
struct Tile {
    id: i32,
    // data: Vec<Vec<char>>,
    ab: String,
    bc: String,
    cd: String,
    da: String,
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let tiles = read_tiles(&input);

    let mut product: i64 = 1;
    for id in corner_ids(&tiles) {
        product *= id as i64;
    }
    println!("result from part 1: {}", product);
}

fn corner_ids(tiles: &[Tile]) -> Vec<i32> {
    // let mut map_side_to_tile: HashMap<String, Vec<(i32, (i32, i32))>> = HashMap::new();
    let mut map_side_to_tile: HashMap<String, HashSet<i32>> = HashMap::new();

    // here we check the tiles for common sides we also flip by x and y
    // flipping by x and y corresponds to rotation so we don't do that
    for tile in tiles {
        map_side_to_tile
            .entry(tile.ab.clone())
            .or_insert(HashSet::new())
            .insert(tile.id);
        map_side_to_tile
            .entry(tile.bc.clone())
            .or_insert(HashSet::new())
            .insert(tile.id);
        map_side_to_tile
            .entry(tile.cd.clone())
            .or_insert(HashSet::new())
            .insert(tile.id);
        map_side_to_tile
            .entry(tile.da.clone())
            .or_insert(HashSet::new())
            .insert(tile.id);

        // flip by x
        map_side_to_tile
            .entry(reverse(&tile.ab))
            .or_insert(HashSet::new())
            .insert(tile.id);
        map_side_to_tile
            .entry(reverse(&tile.da))
            .or_insert(HashSet::new())
            .insert(tile.id);
        map_side_to_tile
            .entry(reverse(&tile.cd))
            .or_insert(HashSet::new())
            .insert(tile.id);
        map_side_to_tile
            .entry(reverse(&tile.bc))
            .or_insert(HashSet::new())
            .insert(tile.id);

        // flip by y
        map_side_to_tile
            .entry(reverse(&tile.cd))
            .or_insert(HashSet::new())
            .insert(tile.id);
        map_side_to_tile
            .entry(reverse(&tile.bc))
            .or_insert(HashSet::new())
            .insert(tile.id);
        map_side_to_tile
            .entry(reverse(&tile.ab))
            .or_insert(HashSet::new())
            .insert(tile.id);
        map_side_to_tile
            .entry(reverse(&tile.da))
            .or_insert(HashSet::new())
            .insert(tile.id);
    }

    let mut map_tile_to_neighbors: HashMap<i32, HashSet<i32>> = HashMap::new();

    for key in map_side_to_tile.keys() {
        let neighbors = map_side_to_tile.get(key).unwrap().clone();
        if neighbors.len() > 1 {
            let all_neighbors = neighbors.clone();
            for id in neighbors {
                let mut other_neighbors = all_neighbors.clone();
                other_neighbors.retain(|&x| x != id);
                for other_neighbor in other_neighbors {
                    map_tile_to_neighbors
                        .entry(id)
                        .or_insert(HashSet::new())
                        .insert(other_neighbor);
                }
            }
        }
    }

    let mut ids = Vec::new();
    for key in map_tile_to_neighbors.keys() {
        if map_tile_to_neighbors.get(key).unwrap().len() == 2 {
            ids.push(*key);
        }
    }

    ids
}

fn reverse(s: &String) -> String {
    s.chars().rev().collect()
}

fn read_tiles(input: &str) -> Vec<Tile> {
    let mut tiles = Vec::new();

    let tile_size = 10;

    for chunk in input.split("\n\n") {
        let lines: Vec<&str> = chunk.lines().collect();
        let id: i32 = lines[0][5..9].parse().unwrap();

        let mut data: Vec<Vec<char>> = Vec::new();
        let mut ad_chars: Vec<char> = Vec::new();
        let mut bc_chars: Vec<char> = Vec::new();
        for i in 0..tile_size {
            data.push(lines[i + 1].chars().collect());
            ad_chars.push(lines[i + 1][0..1].parse().unwrap());
            bc_chars.push(lines[i + 1][(tile_size - 1)..tile_size].parse().unwrap());
        }

        let ab: String = data[0].iter().collect();
        let bc: String = bc_chars.iter().collect();
        let cd: String = data[tile_size - 1].iter().rev().collect();
        let da: String = ad_chars.iter().rev().collect();

        tiles.push(Tile { id, ab, bc, cd, da });
    }

    tiles
}
