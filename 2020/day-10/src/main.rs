use std::collections::HashMap;
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let mut numbers: Vec<i32> = input.lines().map(|x| x.parse().unwrap()).collect();

    numbers.sort_unstable();

    // should try to re-express this as a fold
    let mut num_1 = 1;
    let mut num_3 = 1;
    for batch in numbers.windows(2) {
        match batch[1] - batch[0] {
            1 => num_1 += 1,
            3 => num_3 += 1,
            _ => (),
        }
    }

    println!("part 1: {}", num_1 * num_3);

    let mut map: HashMap<i32, i64> = HashMap::new();

    map.insert(0, 1);
    for number in &numbers {
        let mut num_connections = 0;
        for reachable in &[number - 1, number - 2, number - 3] {
            if map.contains_key(reachable) {
                num_connections += map.get(&reachable).unwrap();
            }
            map.insert(*number, num_connections);
        }
    }

    let result = map.get(numbers.iter().last().unwrap()).unwrap();
    println!("part 2: {}", result);
}
