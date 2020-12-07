use std::collections::HashMap;
use std::fs;

type Color = String;
type Map = HashMap<Color, Vec<(usize, Color)>>;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let (map_parents, map_children) = create_maps(&input);

    let mut parents: Vec<Color> = follow(1, "shiny gold", &map_parents)
        .iter()
        .map(|x| x.1.clone())
        .collect();
    parents.sort();
    parents.dedup();
    println!("result from part 1: {}", parents.len());

    let children: Vec<usize> = follow(1, "shiny gold", &map_children)
        .iter()
        .map(|x| x.0)
        .collect();
    let sum: usize = children.iter().sum();
    println!("result from part 2: {}", sum);
}

fn follow(multiply: usize, color: &str, map: &Map) -> Vec<(usize, Color)> {
    let mut results = Vec::new();
    let key = color.to_string();
    if map.contains_key(&key) {
        for value in map.get(&key).unwrap().iter() {
            let (k, v) = value.clone();
            results.push((multiply * k, v));
            results.extend(follow(multiply * k, &value.1, &map));
        }
    }
    results
}

fn create_maps(input: &str) -> (Map, Map) {
    let mut map_parents = HashMap::new();
    let mut map_children = HashMap::new();
    for line in input.lines() {
        let (color_parent, bags) = parse_line(line);
        for (how_many, color_child) in bags.iter() {
            map_parents
                .entry(color_child.clone())
                .or_insert(Vec::new())
                .push((1, color_parent.clone()));
            map_children
                .entry(color_parent.clone())
                .or_insert(Vec::new())
                .push((*how_many, color_child.clone()));
        }
    }
    (map_parents, map_children)
}

fn parse_line(input: &str) -> (Color, Vec<(usize, Color)>) {
    let mut before_after = input.split(" contain ");

    let first_part = before_after.next().unwrap_or("");
    let second_part = before_after.next().unwrap_or("");

    let color = first_part
        .split_whitespace()
        .take(2)
        .collect::<Vec<&str>>()
        .join(" ");

    let mut bags = Vec::new();
    for chunk in second_part.split(", ") {
        let mut words = chunk.split_whitespace();
        let how_many = words.next().unwrap().parse().unwrap_or(0);
        if how_many > 0 {
            let color_contains = words.take(2).collect::<Vec<&str>>().join(" ");
            bags.push((how_many, color_contains));
        }
    }

    (color, bags)
}
